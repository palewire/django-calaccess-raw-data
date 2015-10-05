import os
import time
import calculate
from github import Github
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(CalAccessCommand):
    help = 'Analyze how many model lack a UNIQUE_KEY definition'

    def handle(self, *args, **kwargs):
        """
        Make it happen.
        """
        # Loop through all the models and find any fields without docs
        missing_list = []
        model_count = 0
        for m in get_model_list():
            model_count += 1
            if m.UNIQUE_KEY is None:
                self.log("Missing: %s.%s" % (
                        m().klass_group,
                        m().klass_name,
                    )
                )
                missing_list.append(m)

        # If everything is done, declare victory
        missing_count = len(missing_list)
        if not missing_count:
            self.success("All %s models have a UNIQUE_KEY!" % missing_count)
            return False

        # If not, loop through the missing and create issues
        self.failure(
            "%s/%s (%d%%) of models lack a UNIQUE_KEY" % (
                intcomma(missing_count),
                model_count,
                calculate.percentage(missing_count, model_count)
            )
        )
