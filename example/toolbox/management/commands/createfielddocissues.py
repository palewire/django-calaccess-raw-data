import os
import calculate
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(CalAccessCommand):
    help = 'Create GitHub issues for model fields without documentation'

    def handle(self, *args, **kwargs):
        self.header(
            "Creating GitHub issues for model fields without documentation"
        )
        field_count = 0
        missing_list = []
        for m in get_model_list():
            field_list = m().get_field_list()
            field_count += len(field_list)
            for f in field_list:
                if not self.has_docs(f):
                    missing_list.append((m().klass_name, f))
        if missing_list:
            missing_count = len(missing_list)
            self.log(
                "- %s/%s (%d%%) of fields lack documentation" % (
                    intcomma(missing_count),
                    intcomma(field_count),
                    calculate.percentage(missing_count, field_count)
                )
            )

    def has_docs(self, field):
        if field.help_text:
            return True
        if not field.__dict__['verbose_name']:
            return True
        return False