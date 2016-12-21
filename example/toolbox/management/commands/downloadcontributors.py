import os
import csv
import time
import agate
import calculate
from github import Github
from pprint import pprint
from datetime import datetime
from csvkit import CSVKitDictWriter
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
        # Set the output directory
        self.data_dir = os.path.join(
            settings.BASE_DIR,
            'network-analysis'
        )
        os.path.exists(self.data_dir) or os.mkdir(self.data_dir)
        # Get our GitHub repos
        # self.gh = Github(os.getenv('GITHUB_TOKEN'))
        self.gh = Github(
            client_id=settings.SOCIAL_AUTH_GITHUB_ORG_KEY,
            client_secret=settings.SOCIAL_AUTH_GITHUB_ORG_SECRET
        )
        self.org = self.gh.get_organization("california-civic-data-coalition")
        self.repo_list = self.org.get_repos()

    def handle(self, *args, **kwargs):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **kwargs)
        self.set_options()
        self.header("Analyzing contributors")

        self.headers = [
            'repo',
            'login',
            'name',
            'email',
            'company',
            'location',
            'bio',
            'avatar_url',
            'contributions'
        ]
        self.outfile_path = os.path.join(
            self.data_dir,
            'contributors.csv'
        )
        self.outfile = CSVKitDictWriter(
            open(self.outfile_path, 'wb'),
            fieldnames=self.headers
        )
        self.outfile.writeheader()

        for repo in self.repo_list:
            repo_name = repo.name
            self.log(" - Sifting through %s" % repo_name)
            contributor_list = repo.get_contributors()
            for contrib in contributor_list:
                d = dict(
                    repo=repo_name,
                    login=contrib.login,
                    name=contrib.name,
                    email=contrib.email,
                    company=contrib.company,
                    location=contrib.location,
                    bio=contrib.bio,
                    avatar_url=contrib.avatar_url,
                    contributions=contrib.contributions
                )
                pprint(d)
                self.outfile.writerow(d)
                time.sleep(2)
