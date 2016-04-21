This issue is part of our on-going efforts to thoroughly document the raw data from CAL-ACCESS.

As such, our goal is to ensure that every field in the database be a `verbose_text` that is more intelligble than its header in the raw file. In many cases, this is just a matter of filling in the missing letters of words in the field names. For example, a field named `acct_opendt` would have `verbose_name='account opened datetime'`.

Another of our goals in this documenting effort is for every field to have an accurate and descriptive `help_text`. This would include additional explanations about this field, usually discovered in the official documentation. Here are the locations in the official docs where we've previously found descriptions about this table (there may still be others to find):
{% for doc in model_docs %}
* [{{ doc.title }}, p. {{ doc.start_page }}{% if doc.end_page %}-{{ doc.end_page }}{% endif %}]({{ doc.canonical_url }})
{% endfor %}

Note that in some cases, a field's `verbose_text` and the `help_text` might be exactly the same. Regardless, both should be assigned.

The following fields on {{ model_name }} (in [{{ file_name }}](https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/calaccess_raw/models/{{ file_name }})) are missing either `verbose_text` or `help_text` attribute (or both):
{% for field, issues in fields %}
- [ ] {{ field.name }} is missing{% if issues.no_verbose and issues.no_help %} both `verbose_text` and `help_text`{% elif issues.no_verbose %} `verbose_text`{% elif issues.no_help %} `help_text`{% endif %}
{% endfor %}

And thanks for helping out!