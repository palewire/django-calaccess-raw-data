import os
import time
from github import Github
from django.db import models
from calaccess_raw import get_model_list
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    help = 'Create GitHub issues for fields missing verbose and/or help text'

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "--dry-run",
            action="store_true",
            dest="dry_run",
            default=False,
            help="Print text of issues without sending to Github"
        )

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)
        """
        Connect to Github using token stored in environment, loop over model fields, and \
        create an issue for any choice field missing 
        """
        self.dry_run = options["dry_run"]
        # set up connect to Github account
        self.gh = Github(os.getenv('GITHUB_TOKEN'))
        self.org = self.gh.get_organization("california-civic-data-coalition")
        self.repo = self.org.get_repo("django-calaccess-raw-data")
        self.labels = [
            self.repo.get_label("small"),
            self.repo.get_label("documentation"),
            self.repo.get_label("enhancement"),
        ]
        self.header(
            "Creating GitHub issues for model choice fields"
        )

        model_list = sorted(
            get_model_list(),
            key=lambda x: (x().klass_group, x().klass_name)
        )

        models_to_fix = []

        for m in model_list:
            fields_to_fix = {}

            for f in m._meta.fields:
                if f.name == 'id':
                    continue
                # test for verbose name
                if not f.__dict__['_verbose_name']:
                    fields_to_fix[f] = {'no_verbose': True, 'no_help': False}
                elif len(f.__dict__['_verbose_name']) == 0:
                    fields_to_fix[f] = {'no_verbose': True, 'no_help': False}
                
                # test for help text
                if len(f.help_text) == 0:
                    try:
                        fields_to_fix[f]['no_help'] = True
                    except KeyError:
                        fields_to_fix[f] = {'no_verbose': False, 'no_help': True}
            
            if len(fields_to_fix) > 0:
                fs = []
                for k, v in fields_to_fix.items():
                    fs.append((k, v))

                models_to_fix.append(
                    (m, tuple(fs))
                )

        for model, fields in models_to_fix:

            context = dict(
                model_name=model.__name__,
                model_docs=model().DOCUMENTCLOUD_PAGES,
                file_name=model.__module__.split('.')[-1] + '.py',
                fields=fields,
            )

            title = "Add verbose and/or help text fields on {model_name} (in \
{file_name})".format(**context)

            body = render_to_string(
                'toolbox/createverboseandhelptextissues.md',
                context,
            )

            self.log("-- Creating issue for {model_name}".format(**context))
            if self.dry_run:
                print '=========================='
                print title
                print '--------------------------'
                print body
                print '=========================='
            else:
                self.repo.create_issue(
                    title,
                    body=body,
                    labels=self.labels,
                )
                time.sleep(2.5)

