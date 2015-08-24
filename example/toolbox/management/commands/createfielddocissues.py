import os
import time
import calculate
from github import Github
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(CalAccessCommand):
    help = 'Create GitHub issues for model fields without documentation'

    def set_options(self, *args, **kwargs):
        """
        Hook up with the GitHub API and prepare to create issues.
        """
        self.gh = Github(os.getenv('GITHUB_TOKEN'))
        self.org = self.gh.get_organization("california-civic-data-coalition")
        self.repo = self.org.get_repo("django-calaccess-raw-data")
        self.labels = [
            self.repo.get_label("small"),
            self.repo.get_label("documentation"),
            self.repo.get_label("enhancement"),
        ]
        self.milestone = self.repo.get_milestone(3)

    def handle(self, *args, **kwargs):
        """
        Make it happen.
        """
        self.set_options()
        self.header(
            "Creating GitHub issues for model fields without documentation"
        )

        # Loop through all the models and find any fields without docs
        field_count = 0
        missing_list = []
        for m in get_model_list():
            field_list = m().get_field_list()
            field_count += len(field_list)
            for f in field_list:
                if not self.has_docs(f):
                    missing_list.append((m, f))

        # If everything is done, declare victory
        if not missing_list:
            self.success("All %s fields documented!" % field_count)
            return False

        # If not, loop through the missing and create issues
        missing_count = len(missing_list)
        self.log(
            "- %s/%s (%d%%) of fields lack documentation" % (
                intcomma(missing_count),
                intcomma(field_count),
                calculate.percentage(missing_count, field_count)
            )
        )
        for model, field in missing_list[611:]:
            # For now we are excluding the 'other' model module to
            # avoid overkill
            if model().klass_group != 'other':
                self.create_issue(model, field)

    def has_docs(self, field):
        """
        Test if a Django field has some kind of documentation already.

        Returns True or False
        """
        if field.name == 'id':
            return True
        if field.help_text:
            return True
        if field.__dict__['_verbose_name']:
            return True
        return False

    def create_issue(self, model, field):
        """
        Create a GitHub issue for the provided model and field.
        """
        title = TITLE_TEMPLATE % (field.name, model().klass_name)

        body = BODY_TEMPLATE % (
               field.name,
               model().klass_name,
               model().klass_group,
               model().klass_group,
        )
        self.log("-- Creating issue for %s.%s" % (
                model().klass_name,
                field.name
            )
        )
        self.repo.create_issue(
            title,
            body=body,
            labels=self.labels,
            milestone=self.milestone
        )
        time.sleep(2.5)

TITLE_TEMPLATE = """
Add documentation for the ``%s`` field on the ``%s`` database model
""".replace("\n", "")

BODY_TEMPLATE = """
## Your mission

Add documentation for the ``%s`` field on the ``%s`` database model.

## Here's how

**Step 1**: Claim this ticket by leaving a comment below. Tell everyone you're ON IT!

**Step 2**: Open up the file that contains this model. It should be in <a href="https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/calaccess_raw/models/%s.py">calaccess_raw.models.%s.py</a>.

**Step 3**: Hit the little pencil button in the upper-right corner of the code box to begin editing the file.

![Edit](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1440367320.67.png)

**Step 4**: Find this model and field in the file. (Clicking into the box and searching with CTRL-F can help you here.) Once you find it, we expect the field to lack the ``help_text`` field typically used in Django to explain what a field contains.

```python
effect_dt = fields.DateField(
    null=True,
    db_column="EFFECT_DT"
)
```

**Step 5**: In a separate tab, open up the <a href="Quilmes">official state documentation</a> and find the page that defines all the fields in this model.

![The docs](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1440367001.08.png)

**Step 6**: Find the row in that table's definition table that spells out what this field contains. If it lacks documentation. Note that in the ticket and close it now.

![The definition](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1440367068.59.png)

**Step 7**: Return to the GitHub tab.

**Step 8**: Add the state's label explaining what's in the field, to our field definition by inserting it a ``help_text`` argument. That should look something like this:

```python
effect_dt = fields.DateField(
    null=True,
    db_column="EFFECT_DT",
    # Add a help_text argument like the one here, but put your string in instead.
    help_text="The other values in record were effective as of this date"
)
```

**Step 9**: Scroll down below the code box and describe the change you've made in the commit message. Press the button below.

![Commit](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1440367511.66.png)

**Step 10**:  Review your changes and create a pull request submitting them to the core team for inclusion.

![Pull request](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1440368058.52.png)

That's it! Mission accomplished!
"""
