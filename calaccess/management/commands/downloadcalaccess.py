import os
import requests
from hurry.filesize import size
from django.conf import settings
from django.utils.six.moves import input
from dateutil.parser import parse as dateparse
from django.template.defaultfilters import date as dateformat
from django.core.management.base import BaseCommand, CommandError
from django.contrib.humanize.templatetags.humanize import naturaltime


PROMPT = """
The CalAccess snapshot was last updated %s at %s, %s.

It is %s in size.

Do you want to download the file to %s

Type 'yes' to do it, or 'no' to back out: """


class Command(BaseCommand):
    help = 'Download the latest snapshot of the CalAccess database'

    def set_options(self, *args, **kwargs):
        self.url = 'http://campaignfinance.cdn.sos.ca.gov/dbwebexport.zip'
        self.data_dir = settings.CALACCESS_DOWNLOAD_DIR
        self.zip_path = os.path.join(self.data_dir, 'calaccess.zip')
        self.metadata = self.get_metadata()
        self.prompt = PROMPT % (
            dateformat(self.metadata['last-modified'], 'N j, Y'),
            dateformat(self.metadata['last-modified'], 'P'),
            naturaltime(self.metadata['last-modified']),
            self.metadata['content-length'],
            self.data_dir,
        )

    def handle(self, *args, **options):
        self.set_options(*args, **options)
        confirm = input(self.prompt)
        if confirm != 'yes':
            raise CommandError("Download cancelled.")
        else:
            self.download()

    def download(self):
        """
        Download the ZIP file in pieces.
        """
        print "Downloading ZIP file"
        r = requests.get(self.url, stream=True)
        with open(self.zip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()

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
