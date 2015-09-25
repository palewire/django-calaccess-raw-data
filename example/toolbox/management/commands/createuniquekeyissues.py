import os
import time
import calculate
from github import Github
from django.conf import settings
from calaccess_raw import get_model_list
from calaccess_raw.management.commands import CalAccessCommand
from django.contrib.humanize.templatetags.humanize import intcomma


class Command(CalAccessCommand):
    help = "Creating GitHub issues for model models without a UNIQUE_KEY"

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
        self.milestone = self.repo.get_milestone(4)

    def handle(self, *args, **kwargs):
        """
        Make it happen.
        """
        self.set_options()
        self.header(
            "Creating GitHub issues for model models without a UNIQUE_KEY"
        )

        # Loop through all the models and find any fields without docs
        missing_list = []
        model_count = 0
        for m in get_model_list():
            model_count += 1
            if not m.UNIQUE_KEY:
                self.log("Missing: %s.%s" % (
                        m().klass_group,
                        m().klass_name,
                    )
                )
                missing_list.append(m)

        # If everything is done, declare victory
        missing_count = len(missing_list)
        if not missing_count:
            self.success("All %s models have a UNIQUE_KEY!" % missing_count)
            return False

        # If not, loop through the missing and create issues
        self.log(
            "- %s/%s (%d%%) of fields lack a UNIQUE_KEY" % (
                intcomma(missing_count),
                intcomma(model_count),
                calculate.percentage(missing_count, model_count)
            )
        )
        for model in missing_list[1:]:
            self.create_issue(model)

    def create_issue(self, model):
        """
        Create a GitHub issue for the provided model and field.
        """
        title = TITLE_TEMPLATE % model().klass_name

        body = BODY_TEMPLATE % (
               model().klass_name,
               model().klass_group,
               model().klass_group,
        )
        self.log("-- Creating issue for %s" % model().klass_name)
        self.repo.create_issue(
            title,
            body=body,
            labels=self.labels,
            milestone=self.milestone
        )
        time.sleep(2.5)

TITLE_TEMPLATE = """
Add UNIQUE_KEY to the ``%s`` database model
""".replace("\n", "")

BODY_TEMPLATE = """
## Your mission

Add a ``UNIQUE_KEY`` setting to the ``%s`` database model.

## Here's how

**Step 1**: Claim this ticket by leaving a comment below. Tell everyone you're ON IT!

**Step 2**: In a separate tab, open up the <a href="http://www.documentcloud.org/documents/1308002-cal-access-about.html#document/p100">official state documentation</a> and find the page that defines this table. They are listed there in alphabetical order.

![The docs](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1440367001.08.png)

**Step 3**: Find the "PK_" row in the index list included with the table's definition that spells out the list of "column codes" that make up the unique key for each row. If it lacks that documentation. Note that in the ticket and close it now.

![The definition](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1442811831.94.png)

**Step 4**: Return to this tab.

**Step 5**: Open up the file that contains this model. It should be in <a href="https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/calaccess_raw/models/%s.py">calaccess_raw.models.%s.py</a>.

**Step 6**: Hit the little pencil button in the upper-right corner of the code box to begin editing the file.

![Edit](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1440367320.67.png)

**Step 7**: Find this model in the file. (Clicking into the box and searching with CTRL-F can help you here.) Once you find it, we expect the model to lack a ``UNIQUE_KEY`` attribute indented just under the documentation.

```python
class WhateverYourModel(CalAccessBaseModel):
    '''
    There will be some documentation here but don't touch it.
    '''
    field1 = models.CharField(blah='blah')
```
**Step 8**: Add this model's ``UNIQUE_KEY`` list of column codes, to our field definition by inserting it under the documentation. That should look something like this:

```python
class WhateverYourModel(CalAccessBaseModel):
    '''
    There will be some documentation here but don't touch it.
    '''
    UNIQUE_KEY = ['FIELD1', 'FIELD2', 'FIELD3']
    field1 = models.CharField(blah='blah')
```

**Step 9**: Scroll down below the code box and describe the change you've made in the commit message. Press the button below.

**Step 10**:  Review your changes and create a pull request submitting them to the core team for inclusion.

That's it! Mission accomplished!
"""
