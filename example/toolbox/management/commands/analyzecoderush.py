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
    help = 'Analyze GitHub commits during one of our code sprints'

    def set_options(self, *args, **kwargs):
        """
        Hook up with the GitHub API.
        """
        self.gh = Github(os.getenv('GITHUB_TOKEN'))
        self.org = self.gh.get_organization("california-civic-data-coalition")
        self.repo_list = [
            self.org.get_repo("django-calaccess-raw-data"),
        ]
        self.start = datetime(2016, 3, 9, 0, 0, 0)
        self.end = datetime(2016, 3, 15, 0, 0, 0)

    def handle(self, *args, **kwargs):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **kwargs)
        self.set_options()
        self.header("Analyzing Code Rush commits")

        for repo in self.repo_list:
            self.log(repo.name)
            commit_count = 0
            addition_count = 0
            author_list = []
            for commit in repo.get_commits(since=self.start):
                commit_count += 1
                #addition_count += commit.stats.additions
                if commit.author not in author_list:
                    author_list.append(commit.author)
                time.sleep(0.1)
            self.log("- Authors: %s" % len(author_list))
            self.log("- Commits: %s" % commit_count)
            #self.log("- Additions: %s" % addition_count)
