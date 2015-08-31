Database tables
===============

The {{ model_count }} tab-delimited database exports published by California's Secretary of State and loaded by this Django application.

{% for group, model_list in group_list %}
{{ group|capfirst }}
-------
{% for object in model_list %}
{{ object.klass_name }}
~~~~~~~~~~~~~~~~~~~~~~~

{{ object.doc.strip|safe }}

**Source:** `{{ object.get_tsv_name }} <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

**Fields:**

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Name</th>
            <th class="head">Type</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    {% for field in object.get_field_list %}
    {% if field.name != "id" %}
        <tr>
            <td>{{ field.name }}</td>
            <td>{{ field.get_internal_type }}</td>
            <td>{{ field.help_text|safe }}</td>
        </tr>
    {% endif %}
    {% endfor %}
    </tbody>
    </table>
    </div>
{% endfor %}
{% endfor %}

Empty files
-----------

+------------------------------+
|Source TSV                    |
+==============================+
| FILER_TYPE_PERIODS_CD        |
+------------------------------+
| LOBBYIST_EMPLOYER_HISTORY_CD |
+------------------------------+
| LOBBYIST_FIRM_HISTORY_CD     |
+------------------------------+
