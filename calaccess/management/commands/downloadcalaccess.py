import requests
from hurry.filesize import size
from dateutil.parser import parse as dateparse
from django.template.defaultfilters import date as dateformat
from django.core.management.base import BaseCommand, CommandError
from django.contrib.humanize.templatetags.humanize import naturaltime


class Command(BaseCommand):
    help = 'Download the latest snapshot of the CalAccess database'
    url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'

    def handle(self, *args, **options):
        self.metadata = self.get_metadata()
        print "- Last updated %s at %s, %s" % (
            dateformat(self.metadata['last-modified'], 'N j, Y'),
            dateformat(self.metadata['last-modified'], 'P'),
            naturaltime(self.metadata['last-modified']),
        )
        print "- %s in size" % self.metadata['content-length']

    def get_metadata(self):
        """
        Returns basic metadata about the current CalAccess snapshot,
        like its size and the last time it was updated, while stopping
        of short of actually downloading it.
        """
        request = requests.head(self.url)
        return {
            'content-length': size(int(request.headers['content-length'])),
            'last-modified': dateparse(request.headers['last-modified'])
        }
