import os
import time
import calculate
from github import Github
from datetime import datetime
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(CalAccessCommand):
    help = 'Analyze GitHub contributors across our repositories'

    def set_options(self, *args, **kwargs):
        """
        Hook up with the GitHub API
        """
        self.gh = Github(os.getenv('GITHUB_TOKEN'))
        self.org = self.gh.get_organization("california-civic-data-coalition")
        self.repo_list = [
            self.org.get_repo("django-calaccess-raw-data"),
            self.org.get_repo("django-calaccess-campaign-browser"),
        ]

    def handle(self, *args, **kwargs):
        """
        Make it happen.
        """
        self.set_options()
        self.header("Analyzing Code Rush contributors")

        author_list = []
        for repo in self.repo_list:
            self.log(" - Sifting through %s" % repo.name)
            for contrib in repo.get_contributors():
                if contrib.name not in author_list:
                    self.log("  - Adding %s" % contrib.name)
                    author_list.append(contrib.name)
                time.sleep(0.5)
        self.log("- Contributors: %s" % len(author_list))
