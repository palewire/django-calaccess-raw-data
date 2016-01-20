from django.utils.termcolors import colorize
from django.core.management.base import BaseCommand


class CalAccessCommand(BaseCommand):

    def add_arguments(self, parser):
            # allow any CalAccessCommand to be performed on other apps
            parser.add_argument(
                "-a",
                "--app-name",
                dest="app_name",
                default="calaccess_raw",
                help="Name of Django app where model will be imported from"
            )

    def header(self, string):
        self.stdout.write(
            colorize(string, fg="cyan", opts=("bold",))
        )

    def log(self, string):
        self.stdout.write(
            colorize("%s" % string, fg="white")
        )

    def success(self, string):
        self.stdout.write(
            colorize(string, fg="green")
        )

    def failure(self, string):
        self.stdout.write(
            colorize(string, fg="red")
        )
