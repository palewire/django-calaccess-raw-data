#!/usr/bin/env python
# -*- coding: utf-8 -*-
import agate
from django.db.models import Count
from calaccess_raw.management.commands import CalAccessCommand
from calaccess_raw import get_model_list


class Command(CalAccessCommand):
    help = "Discovers choice field values in the database \
that aren't defined in the choices attr"

    def add_arguments(self, parser):
        """
        Adds custom arguments specific to this command.
        """
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            "-a",
            "--app-name",
            dest="app_name",
            default="calaccess_raw",
            help="Name of Django app with models into which data will "
                 "be imported (if other not calaccess_raw)"
        )

    def handle(self, *args, **options):
        super(Command, self).handle(*args, **options)

        model_list = sorted(
            get_model_list(),
            key=lambda x: (x().klass_group, x().klass_name)
        )

        results = []

        for m in model_list:
            if self.verbosity > 1:
                self.log(
                    " Verifying {0}.{1} fields".format(
                        m().klass_group,
                        m.__name__,
                    )
                )
            for f in m._meta.fields:
                if f.choices:
                    for value, count in m.objects.order_by().values_list(
                        f.name,
                    ).annotate(Count(f.name)):
                        if (
                            value not in [x[0] for x in f.choices] and
                            value != '' and
                            value is not None
                        ):
                            if self.verbosity > 2:
                                self.failure(
                                    "  Undefined value for {0}: {1} ({2} occurrences)".format(
                                        f.name,
                                        value,
                                        count
                                    )
                                )
                            results.append((
                                m().klass_group,
                                m.__name__,
                                f.name,
                                value,
                                count,
                            ))

        if len(results) > 0:
            self.failure("{} undefined choice field values".format(len(results)))

            table = agate.Table(
                results,
                ['group', 'model', 'field', 'undefined_value', 'occurrences']
            )
            table.print_table(max_rows=None, max_column_width=50)
        else:
            self.success("No undefined choice field values")
