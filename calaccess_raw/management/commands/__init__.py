from django.utils.termcolors import colorize
from django.core.management.base import BaseCommand


class CalAccessCommand(BaseCommand):

    def handle(self, *args, **options):
        self.verbosity = int(options.get("verbosity"))
        self.no_color = options.get("no_color")

    def header(self, string):
        if not self.no_color:
            string = colorize(string, fg="cyan", opts=("bold",))
        self.stdout.write(string)

    def log(self, string):
        if not self.no_color:
            string = colorize("%s" % string, fg="white")
        self.stdout.write(string)

    def success(self, string):
        if not self.no_color:
            string = colorize(string, fg="green")
        self.stdout.write(string)

    def failure(self, string):
        if not self.no_color:
            string = colorize(string, fg="red")
        self.stdout.write(string)
