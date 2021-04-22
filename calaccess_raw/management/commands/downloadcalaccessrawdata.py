#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Download the latest CAL-ACCESS database ZIP.
"""
# Files
import os
import shutil
import requests
from hurry.filesize import size

# Strings
from django.template.loader import render_to_string
from django.contrib.humanize.templatetags.humanize import naturaltime

# Time
from datetime import datetime
from django.utils import timezone

# Django stuff
from django.conf import settings
from django.core.files import File
from calaccess_raw.models.tracking import RawDataVersion

# Commands
from clint.textui import progress
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand

# Logging
import logging
logger = logging.getLogger(__name__)


class Command(CalAccessCommand):
    """
    Download the latest CAL-ACCESS database ZIP.
    """
    help = "Download the latest CAL-ACCESS database ZIP"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--noinput",
            action="store_true",
            dest="noinput",
            default=False,
            help="Download the ZIP archive without asking permission"
        )
        parser.add_argument(
            "--force-restart",
            "--restart",
            action="store_true",
            dest="restart",
            default=False,
            help="Force re-start (overrides auto-resume)."
        )

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        super(Command, self).handle(*args, **options)

        self.download_metadata = self.get_download_metadata()
        logger.debug('Server: %s <-- (from HEAD)' % self.download_metadata['server'])
        logger.debug('ETag: %s <-- (from HEAD)' % self.download_metadata['etag'])
        logger.debug('Last-Modified: %s <-- (from HEAD)' % self.download_metadata['last-modified'])
        logger.debug('Content-Length %s <-- (from HEAD)' % self.download_metadata['content-length'])

        self.last_modified_from_head = self.parse_imf_datetime_str(self.download_metadata['last-modified'])

        # get or create the RawDataVersion
        self.version, created = self.get_or_create_version(
            self.download_metadata['content-length'],
            self.last_modified_from_head,
        )

        # if not called from command-line, assume called by update command
        if not self._called_from_command_line:
            # get the version that the update command is working on
            try:
                last_update_started = RawDataVersion.objects.filter(
                    update_start_datetime__isnull=False
                ).latest('update_start_datetime')
            except RawDataVersion.DoesNotExist:
                pass
            else:
                # confirm that update and download commands are working with same version
                if self.version != last_update_started:
                    raise CommandError(
                        'Version available to download ({0}) does not match version '
                        'of update ({1}).'.format(
                            self.version,
                            last_update_started.release_datetime,
                        )
                    )

        # log if a new version was found
        if created:
            logger.info('New CAL-ACCESS version available.')

        # if download is stalled, zip file is there, and user did not invoke restart
        if (
            self.version.download_stalled
            and os.path.exists(self.zip_path)
            and not options['restart']
        ):
            # enable resuming
            self.resume = True
            # set current size to partially downloaded zip
            self.local_file_size = os.path.getsize(self.zip_path)
            # set the datetime of last download to last modified date of zip file
            timestamp = os.path.getmtime(self.zip_path)
            self.local_file_datetime = datetime.fromtimestamp(
                timestamp,
                timezone.utc
            )
        else:
            self.resume = False
            self.local_file_size = 0
            self.local_file_datetime = None

        if not options['noinput']:
            # get downloaded versions
            downloaded_versions = RawDataVersion.objects.filter(
                download_finish_datetime__isnull=False
            )
            # if there are any
            if downloaded_versions:
                # get the last version downloaded datetime
                last_download_datetime = downloaded_versions.latest(
                    'download_finish_datetime'
                ).download_finish_datetime
                since_last_download = naturaltime(last_download_datetime)
            else:
                last_download_datetime = None

            # setting up the prompt
            prompt_context = dict(
                latest_version=self.version,
                resume=self.resume,
                local_file_size=size(self.local_file_size),
                local_file_datetime=self.local_file_datetime,
                download_dir=self.data_dir,
                since_previous_download=since_last_download,
            )

            prompt = render_to_string(
                'calaccess_raw/downloadcalaccessrawdata.txt',
                prompt_context,
            )

            # if the user doesn't confirm initially
            if not self.confirm_proceed(prompt):
                # but the user can resume
                if self.resume:
                    # prompt to restart
                    confirm_restart = self.confirm_proceed(
                        'Do you want re-start your update?\n'
                    )
                    # if user confirms restart, do not resume
                    if confirm_restart:
                        self.resume = False
                    else:
                        # if the user doesn't confirm restart, cancel
                        raise CommandError("Download cancelled")
                # if the user doesn't confirm initial and can't resume
                elif not self.resume:
                    # cancel
                    raise CommandError("Download cancelled")

        # if not resuming, store the download start time
        if not self.resume:
            self.version.download_start_datetime = timezone.now()
        # either way, reset the finish time
        self.version.download_finish_datetime = None
        # save here in case the command doesn't finish
        self.version.save()

        # check if local zip file is already completely downloaded before trying
        if self.local_file_size < self.version.expected_size:
            self.download()

        logger.debug('Download zip size: %s bytes' % os.path.getsize(self.zip_path))
        # log warning if downloaded zip size is not same as expected size
        if self.version.expected_size != os.path.getsize(self.zip_path):
            raise CommandError(
                'Expected {0} byte zip, but downloaded {1} byte zip.'.format(
                    self.version.expected_size,
                    os.path.getsize(self.zip_path)
                )
            )

        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            self.archive()

        # store download finish time
        self.version.download_finish_datetime = timezone.now()
        # and save the RawDataVersion
        self.version.save()

    def download(self):
        """
        Download the ZIP file in pieces.
        """
        if self.verbosity:
            if self.resume:
                self.header(
                    "Resuming download of {:%m-%d-%Y %H:%M:%S} ZIP".format(
                        self.version.release_datetime
                    )
                )
            else:
                self.header(
                    "Downloading {:%m-%d-%Y %H:%M:%S} ZIP".format(
                        self.version.release_datetime
                    )
                )

        # Prep
        expected_size = self.version.expected_size
        headers = dict()

        if self.resume:
            headers['Range'] = 'bytes=%d-' % self.local_file_size
            expected_size = expected_size - self.local_file_size
        else:
            # flush previous download
            if os.path.exists(self.download_dir):
                shutil.rmtree(self.download_dir)
            os.mkdir(self.download_dir)

        # Stream the download
        chunk_size = 1024
        resp = requests.get(self.url, stream=True, headers=headers)
        logger.debug(
            'Response status {0.status_code} ({0.reason}) from GET request.'.format(resp)
        )
        if not resp.ok:
            resp.raise_for_status()

        logger.debug('Server: %s <--  (from GET)' % resp.headers['server'])
        logger.debug('ETag: %s <-- (from GET)' % resp.headers['etag'])
        logger.debug('Last-Modified: %s <--  (from GET)' % resp.headers['last-modified'])
        logger.debug('Content-Length: %s <-- (from GET)' % resp.headers['content-length'])

        # Calculate absolute value of diff between last-modifed in HEAD and GET
        last_modified_from_request = self.parse_imf_datetime_str(
            resp.headers['last-modified']
        )
        last_modified_diff = abs(
            self.last_modified_from_head - last_modified_from_request
        )
        # Quit if diff greater than five minutes
        if last_modified_diff.total_seconds() > 300:
            raise CommandError(
                "Last-modified of HEAD and GET are more than five minutes apart."
            )

        # in Python 2, need to convert this to long int
        try:
            divisor = long(chunk_size + 1)
        except NameError:
            # no long() in Python 3, all ints are long ints
            divisor = chunk_size + 1

        n_iters = float(expected_size) / divisor

        with open(self.zip_path, 'ab') as fp:
            for chunk in progress.bar(resp.iter_content(chunk_size=chunk_size), expected_size=n_iters):
                fp.write(chunk)
                fp.flush()

    def archive(self):
        """
        Save a copy of the download zip file and each file inside.
        """
        if self.verbosity:
            self.log(" Archiving {}".format(os.path.basename(self.zip_path)))
        # Remove previous zip file
        self.version.download_zip_archive.delete()
        # Store the actual download zip file size
        self.version.download_zip_size = os.path.getsize(self.zip_path)
        # Open up the zipped file so we can wrap it in the Django File obj
        zipped_file = open(self.zip_path, 'rb')
        # Save the zip on the raw data version
        self.version.download_zip_archive.save(
            self.url.split('/')[-1],
            File(zipped_file)
        )
        zipped_file.close()
