#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Download the latest CAL-ACCESS database ZIP.
"""
from __future__ import unicode_literals
import os
import logging
import requests
from datetime import datetime
from hurry.filesize import size
from clint.textui import progress
from django.conf import settings
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.core.files import File
from django.utils.timezone import utc, now
from calaccess_raw import get_download_directory
from django.template.loader import render_to_string
from django.core.management.base import CommandError
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw.models.tracking import RawDataVersion
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

        # get the dir where data goes from app settings
        self.data_dir = get_download_directory()
        # if data_dir doesn't exist, create it
        os.path.exists(self.data_dir) or os.makedirs(self.data_dir)

        # downloaded zip file will go in data_dir
        self.zip_path = os.path.join(self.data_dir, self.url.split('/')[-1])

        self.download_metadata = self.get_download_metadata()
        logger.debug('Server: %s <-- (from HEAD)' % self.download_metadata['server'])
        logger.debug('ETag: %s <-- (from HEAD)' % self.download_metadata['etag'])
        logger.debug(
            'Last-Modified: %s <-- (from HEAD)' % self.download_metadata['last-modified']
        )
        logger.debug(
            'Content-Length %s <-- (from HEAD)' % self.download_metadata['content-length']
        )

        # get or create the RawDataVersion
        self.version, created = RawDataVersion.objects.get_or_create(
            release_datetime=self.download_metadata['last-modified'],
            expected_size=self.download_metadata['content-length'],
        )

        # if not called from command-line, assume called by update command
        if not self._called_from_command_line:
            # get the version that the update command is working on
            last_update_started = RawDataVersion.objects.filter(
                update_start_datetime__isnull=False
            ).latest('update_start_datetime')
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
            self.version.download_stalled and
            os.path.exists(self.zip_path) and
            not options['restart']
        ):
            # enable resuming
            self.resume = True
            # set current size to partially downloaded zip
            self.local_file_size = os.path.getsize(self.zip_path)
            # set the datetime of last download to last modified date of zip file
            timestamp = os.path.getmtime(self.zip_path)
            self.local_file_datetime = datetime.fromtimestamp(timestamp, utc)
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
            self.version.download_start_datetime = now()
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
                'Expected {0} byte zip, but download {1} byte zip.'.format(
                    self.version.expected_size,
                    os.path.getsize(self.zip_path)
                )
            )

        if getattr(settings, 'CALACCESS_STORE_ARCHIVE', False):
            self.archive()

        # store download finish time
        self.version.download_finish_datetime = now()
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
        if os.path.exists(self.zip_path):
            if self.resume:
                headers['Range'] = 'bytes=%d-' % self.local_file_size
                expected_size = expected_size - self.local_file_size
            else:
                os.remove(self.zip_path)

        # Stream the download
        chunk_size = 1024
        req = requests.get(self.url, stream=True, headers=headers)

        logger.debug('Server: %s <--  (from GET)' % req.headers['server'])
        logger.debug('ETag: %s <-- (from GET)' % req.headers['etag'])
        logger.debug('Last-Modified: %s <--  (from GET)' % req.headers['last-modified'])
        logger.debug('Content-Length: %s <-- (from GET)' % req.headers['content-length'])

        if self.download_metadata['etag'] != req.headers['etag']:
            raise CommandError("ETags in HEAD and GET requests don't match.")

        # in Python 2, need to convert this to long int
        try:
            divisor = long(chunk_size + 1)
        except NameError:
            # no long() in Python 3, all ints are long ints
            divisor = chunk_size + 1

        n_iters = float(expected_size) / divisor

        with open(self.zip_path, 'ab') as fp:
            for chunk in progress.bar(req.iter_content(chunk_size=chunk_size),
                                      expected_size=n_iters):
                fp.write(chunk)
                fp.flush()

    def archive(self):
        """
        Save a copy of the download zip file and each file inside.
        """
        if self.verbosity:
            self.log(" Archiving {0}".format(os.path.basename(self.zip_path)))
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
