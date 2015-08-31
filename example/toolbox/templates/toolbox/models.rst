Models
======

A crosswalk between the tables published by California's Secretary of State and the models in this Django application.
{% for group, model_list in group_list %}
{{ group|capfirst }}
-------
{% for object in model_list %}
{{ object.klass_name }}
~~~~~~~~~~~~~~~~~~~~~~~

{{ object.doc.strip|safe }}

**Source**: `{{ object.get_tsv_name }} <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

**Fields**

.. raw:: html

    <table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
    {% for field in object.get_field_list %}
        <tr>
            <td>{{ field.name }}</td>
            <td>{{ field.get_internal_type }}</td>
            <td>{{ field.help_text|safe }}</td>
        </tr>
    {% endfor %}
    </tbody>
    </table>
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
