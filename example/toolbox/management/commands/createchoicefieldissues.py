import os
import time
from github import Github
from django.db import models
from calaccess_raw import get_model_list
from django.template.loader import render_to_string
from calaccess_raw.management.commands import CalAccessCommand


class Command(CalAccessCommand):
    help = 'Create GitHub issues for model choice fields'

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

        choice_field_strs = [
            '_cd',
            '_code',
            'type',
            'status',
            '_lvl',
            'reportname',
            'form_id',
        ]
        excluded_fields = [
            'LookupCodesCd.code_type',
            'S497Cd.sup_off_cd',
        ]

        model_list = sorted(
            get_model_list(),
            key=lambda x: (x().klass_group, x().klass_name)
        )

        for m in model_list:
            for f in m._meta.fields:
                if (
                    any(x in f.name for x in choice_field_strs) and
                    f.name != 'memo_code' and
                    f.__class__ is not models.ForeignKey and
                    '{}.{}'.format(m().klass_name, f.name) not in excluded_fields
                ):
                    # make an issue for every choice field missing docs
                    # includes those that are also missing choices
                    if not f.documentcloud_pages:
                        self.create_issue(f)

    def create_issue(self, field):
        """
        Create a GitHub issue for the provided field.
        """
        context = dict(
            field=field,
            model_name=field.model.__name__,
            field_class=field.__class__.__name__,
            db_table=field.model._meta.fields[1].model._meta.db_table,
            has_choices=bool(field.choices),
            has_docs=bool(field.documentcloud_pages),
            file_name=field.model.__module__.split('.')[-1] + '.py',
        )
        title = " to {model}.{field} (in {file_name})".format(
            model=field.model.__name__,
            field=field.name,
            file_name=context['file_name']
        )

        if not field.choices and not field.documentcloud_pages:
            title = 'Add choices and documentcloud_pages' + title
        elif not field.documentcloud_pages:
            title = 'Add documentcloud_pages' + title

        body = render_to_string(
            'toolbox/createchoicefieldissue.md',
            context,
        )

        self.log("-- Creating issue for %s.%s" % (
                field.model.__name__,
                field.name
            )
        )
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
