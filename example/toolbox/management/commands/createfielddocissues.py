import os
import time
import calculate
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(CalAccessCommand):
    help = 'Create GitHub issues for model fields without documentation'

    def handle(self, *args, **kwargs):
        self.header(
            "Creating GitHub issues for model fields without documentation"
        )
        field_count = 0
        missing_list = []
        for m in get_model_list():
            field_list = m().get_field_list()
            field_count += len(field_list)
            for f in field_list:
                if not self.has_docs(f):
                    missing_list.append((m, f))
        if missing_list:
            missing_count = len(missing_list)
            self.log(
                "- %s/%s (%d%%) of fields lack documentation" % (
                    intcomma(missing_count),
                    intcomma(field_count),
                    calculate.percentage(missing_count, field_count)
                )
            )
            for model, field in missing_list:
                if model().klass_group != 'other':
                    self.create_issue(model, field)

    def create_issue(self, model, field):
        headline = """
Add documentation for the ``%s`` field on the ``%s`` database model.
""" % (field.name, model().klass_name)
        text = """
Add documentation for the ``%s`` field on the ``%s`` database model.

**Step 1**: Claim this ticket by leaving a comment below. Tell everyone you're ON IT!

**Step 2**: Open up the file that contains this model. It should be in
<a href="https://github.com/california-civic-data-coalition/django-calaccess-raw-data/
master/calaccess_raw/models/%s.py">calaccess_raw.models.%s.py</a>.

**Step 3**: Hit the little pencil button in the upper-right corner of the code box to
begin editing the file.

**Step 4**: Find this model and field in the file. We expect it to lack the ``help_text``
field typically used in Django to explain what a field contains.

```python
effect_dt = fields.DateField(
    null=True,
    db_column="EFFECT_DT"
)
```

**Step 5**: In a separate tab, open up the <a href="">official state documentation</a>
and find the page that defines all the fields in this model.

**Step 6**: Find the row in that table's definition table that spells out what
this field contains. It it lacks documentation. Note that in the ticket and close it now.

**Step 7**: Return to the GitHub tab.

**Step 8**: Add the state's label explaining what's in the field,
to our field definition by inserting it a ``help_text`` argument. That should
look something like this:

```python
effect_dt = fields.DateField(
    null=True,
    db_column="EFFECT_DT",
    # Add a help_text argument like the one here, but put your string in instead.
    help_text="The other values in record were effective as of this date"
)
```

**Step 9**: Scroll down below the code box and describe the change you've made in
the committe message. Press the button below.

**Step 10**:  Review your changes and create a pull request submitting them to
the core team for inclusion.
""" % (
       field.name,
       model().klass_name,
       model().klass_group,
       model().klass_group,
)
        tags = "small, documentation"
        milestone = "california code rush 2"
        print headline

        time.sleep(1)

    def has_docs(self, field):
        if field.name == 'id':
            return True
        if field.help_text:
            return True
        if field.__dict__['_verbose_name']:
            return True
        return False
