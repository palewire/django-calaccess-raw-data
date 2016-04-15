## Overview
{% if not has_choices and not has_docs %}
Add choices and documentcloud_pages to the **{{ field.name }}** field on **{{ model_name }}** the database model.
{% elif not has_docs %}
Add documentcloud_pages to the **{{ field.name }}** field on **{{ model_name }}** the database model.
{% endif %}
Basically, we think **{{ field.name }}** should be defined as a "choice field" (in Django parlance), which just means it's a field with a defined list of valid values and an intelligible definition for each value. 

Our goal is for every potential choice field to include references to locations in the [official documentation](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/officialdocumentation.html) where the field's valid values and their meanings are described AND to have those choices included in the field's definition.

And we need your help!

## What to do

**Step 1**: Claim this ticket by adding yourself as an **Assignee** (to the right)

**Step 2**: Find where in the [official documentation](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/officialdocumentation.html) {{ field.name }}'s list of valid values is defined. 

The best place to look first is in the .CAL layout documents: [.CAL Format version 2.01](http://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p1) and [.CAL Format version 1.05.02](http://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02.html#document/p1). These are documents that describe the layout of the .CAL file format, which is the required electronic format of any filings ingested by the CAL-ACCESS system (more on that [here](http://django-calaccess-raw-data.californiacivicdata.org/en/latest/officialdocumentation.html#cal-file-format) if you are interested).

You can start by opening the document and just searching for "{{ field.name }}". For example, if you were assigned to tackle the stmt_type field on the CvrCampaignDisclosureCd model, you would be looking for something like this::

![Docs](https://dl.dropboxusercontent.com/s/jue8oa2btod3i0v/stmt_type.png?dl=0)

But note that the same column might appear on multiple tables, and the list of valid values may vary depending on the table. We want to be sure to find the list of valid values for the {{ field.name }} on the {{ model_name }} model.

Another good place to look is in the [MapCalFormat2Fields](http://www.documentcloud.org/documents/2711616-MapCalFormat2Fields.html#document/p1) document, which describes how .CAL format fields are mapped to CAL-ACCESS database table columns. Note the _Valid_V_ column on the far right.

**Step 3**: Copy the DocumentCloud ID and the page number(s) where {{ field.name }}'s list of valid values is defined.

The DocumentCloud ID can be found the in the URL that points to the document. For example, the url to the .CAL Format version 2.01 doc is `http://www.documentcloud.org/documents/2712034-Cal-Format-201.html#document/p1`, and the id is `2712034-Cal-Format-201`. 

And the start page we want to grab is the DocumentCloud page number, not the page number printed on the .PDF. If the list of valid values spans multiple pages, then grab the page where the list ends as well.

**Step 4**: Find where {{ field.name }} is defined in {{ file_name }} in the [/calaccess_raw/models/{{ file_name }}](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/calaccess_raw/models/{{ file_name }}) file underneath the {{ model_name }} class.

Since the model files are rather long, take care to be sure you find the where {{ field.name }} is defined for the {{ model_name }} model. It should look something like this:
```python
    class {{ model_name }}(CalAccessBaseModel):
        # ...
        # several lines of code later...
        # ...
        {{ field.name }} = fields.{{ field_class }}(
            max_length={{ field.max_length }},
            db_column='{{ field.db_column }}',
            blank={{ field.blank }},
            verbose_name='{{ field.verbose_name }}',
            help_text='{{ field.help_text }}',
        )
```
**Step 5**: Add the document references

Say you found the list of valid values listed in three places. You would list them in the `documentcloud_pages` attribute like this:
```python
    class {{ model_name }}(CalAccessBaseModel):
        # ...
        # several lines of code later...
        # ...
        {{ field.name }} = fields.{{ field_class }}(
            max_length={{ field.max_length }},
            db_column='{{ field.db_column }}',
            blank={{ field.blank }},
            verbose_name='{{ field.verbose_name }}',
            help_text='{{ field.help_text }}',
            documentcloud_pages=[
                DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=10),
                DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=19),
                DocumentCloud(id='2712034-Cal-Format-201', start_page=24, end_page=25),
            ]
        )
```
Note: You only need to specify the `end_page` if the list spans multiple pages.
**Step 6**: Update the {{ field.name}}'s `help_text` (if necessary)

It might be missing or it might be an empty string or it might not be consistent with what you see in the documentation. Note: The entire help_text string needs to be enclosed in single- or double-quotes like this:
```python
    help_text='This is the help text',
```

If the help text is really long (80+ characters), then it needs to span multiple lines like this:
```python
    help_text='This is the help text...blah...blah...blah...blah...blah...blah...\ 
...blah...blah...blah',
```
{% if not has_choices and not has_docs %}
**Step 7**: Define the choices

The normal Django pattern is to define choices within the model class as a tuple which contains a bunch of two item tuples. The first item of each inner tuple is the valid database column value, and the second item is the definition. It should look something like this:

```python
    {{ field.name|upper }}_CHOICES = (
        ('AAA', 'Some definition of AAA'),
        ('BBB', 'Some definition of BBB'),
        ('CCC', 'Some definition of CCC'),
        # ...and more..
    )
```

Then we assign this tuple of tuples to {{ field.names }}'s choice argument with a single line: `choices={{ field.name|upper }}_CHOICES`.

When finished, it should all look something like this:

```python
    class {{ model_name }}(CalAccessBaseModel):
        # ...
        # several lines of code later...
        # ...
        {{ field.name|upper }}_CHOICES = (
            ('AAA', 'Some definition of AAA'),
            ('BBB', 'Some definition of BBB'),
            ('CCC', 'Some definition of CCC'),
            # ...and more..
        )
        {{ field.name }} = fields.{{ field_class }}(
            choices={{ field.name|upper }}_CHOICES,
            max_length={{ field.max_length }},
            db_column='{{ field.db_column }}',
            blank={{ field.blank }},
            verbose_name='{{ field.verbose_name }}',
            help_text='{{ field.help_text }}',
            documentcloud_pages=[
                DocumentCloud(id='2711616-MapCalFormat2Fields', start_page=10),
                DocumentCloud(id='2712033-Cal-Format-1-05-02', start_page=19),
                DocumentCloud(id='2712034-Cal-Format-201', start_page=24, end_page=25),
            ]
        )
```
So some of these choice fields show up on multiple tables (the various `office_cd` fields are a good example), and of course it's rather redundant to repeat these values and their definitions over and over. In some these cases, we've consolidated these valid values into one place: [calaccess_raw/annotations/choices.py](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/calaccess_raw/annotations/choices.py).

So then instead of listing out all the choices in the tuple of tuples, we can do this:
```python
    OFFICE_CD_CHOICES = get_sorted_choices(choices.OFFICE_CODES)
    office_cd = fields.CharField(
        choices=OFFICE_CD_CHOICES,
        # ...other stuff...
    )

```

If you think the field your looking at is a candidate for this sort of consolidation, let's have a conversation about it. Just post a comment below.
{% endif %}
**If you can,** check the {{ field.name }}'s defined choices against the actual values in {{ field.name }}'s database column.

This will require you to install the app and run the `updatecalaccessrawdata` command. Then you can get the distinct column values with a `GROUP BY` query like this:
```sql
    SELECT {{ field.db_column }}, COUNT(*)
    FROM {{ db_table }}
    GROUP BY 1
    ORDER BY 1;
```
It's likely that you'll find undocumented values in database column, some of which are variants of the valid values. You can note these by repeating the same definition for each variant like this:
```python
    OFFICE_CD_CHOICES = (
        ('GOV', 'Governor'),
        ('gov', 'Governor'),
        ('GUV', 'Governor'),
        # ...
    ),
```
If you're dealing with a set of choices that's been consolidated into [calaccess_raw/annotations/choices.py](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/calaccess_raw/annotations/choices.py), you can map the different variants to the same definition using the key of the choices dict like this:

```python
    OFFICE_CD_CHOICES = (
        ('gov', look_ups.OFFICE_CODES['GOV']),
        ('GUV', look_ups.OFFICE_CODES['GOV']),
        # ...
    ),
```
If you're not able to check the database column values for whatever reason, don't sweat it. We'll deal with it in a later issue.

**Wrap up**: Review your changes and create a pull request 

![Pull request](https://dl.dropboxusercontent.com/u/3640647/ScreenCloud/1440368058.52.png)

That's it!

**PS**: If any of this feels confusing, or if it doesn't seem to match up with what you are seeing, or if you have any suggestions about another approach, don't hesitate to speak up. You can post a comment below, or hit up the #california-civic-data channel on the News Nerdery Slack.
