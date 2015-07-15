"""
Custom field overrides that allow for cleaning and transforming the data
when it is bulk loaded into the database with PostgreSQL's COPY command via
django-postgres-copy.
"""
from django.db.models import fields


class CharField(fields.CharField):
    copy_type = "text"
    copy_template = """
    CASE
        WHEN "%(name)s" IS NULL
            THEN ''
        ELSE TRIM("%(name)s")
    END
    """


class DateField(fields.DateField):
    copy_type = "text"
    copy_template = """
    CASE
        WHEN "%(name)s" IS NOT NULL AND TRIM("%(name)s") != ''
            THEN to_date(substring("%(name)s" from 1 for 10), 'MM/DD/YYYY')
        ELSE null
    END
    """


class DateTimeField(fields.DateTimeField):
    copy_type = "text"
    copy_template = """
    CASE
        WHEN "%(name)s" IS NOT NULL AND TRIM("%(name)s") != ''
            THEN to_timestamp("%(name)s", 'MM/DD/YYYY HH12:MI:SS AM')
        ELSE null
    END
    """


class DecimalField(fields.DecimalField):
    copy_type = "text"
    copy_template = """
    CASE
        WHEN "%(name)s" = ''
            THEN 0.0
        WHEN "%(name)s" IS NULL
            THEN 0.0
        WHEN "%(name)s" IS NOT NULL
            THEN "%(name)s"::numeric
    END
    """


class FloatField(fields.FloatField):
    copy_type = "text"
    copy_template = """
    CASE
        WHEN TRIM("%(name)s") = ''
            THEN 0.0
        WHEN TRIM("%(name)s") IS NULL
            THEN 0.0
        WHEN TRIM("%(name)s") IS NOT NULL
            THEN "%(name)s"::double precision
    END
    """


class IntegerField(fields.IntegerField):
    copy_type = "text"
    copy_template = """
    CASE
        WHEN TRIM("%(name)s") = ''
            THEN NULL
        WHEN "%(name)s" = '          '
            THEN NULL
        WHEN "%(name)s" = '         '
            THEN NULL
        WHEN "%(name)s" = 'Y'
            THEN 1
        WHEN "%(name)s" = 'y'
            THEN 1
        WHEN "%(name)s" = 'X'
            THEN 1
        WHEN "%(name)s" = 'x'
            THEN 1
        WHEN "%(name)s" = 'N'
            THEN 0
        WHEN "%(name)s" = 'n'
            THEN 0
        WHEN "%(name)s" IS NOT NULL
            THEN "%(name)s"::int
        ELSE NULL
    END"""
