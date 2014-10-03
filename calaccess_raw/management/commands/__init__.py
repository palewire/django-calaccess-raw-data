from django.utils.termcolors import colorize
from django.core.management.base import BaseCommand


class CalAccessCommand(BaseCommand):

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
