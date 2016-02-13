Database tables
===============

The {{ model_count }} tab-delimited database exports published by California's Secretary of State and loaded by this Django application.

.. warning::

    Most definitions below are drawn from the spotty and incomplete `official documentation <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/officialdocumentation.html>`_ verbatim. As we continue our research, we plan to improve the descriptions.

    For the time being, to be absolutely certain about what each table and field contains, you should compare the electronic data back to the original paper records published by the state.

The categories for these tables are based on what's found in the `ReadMe <_http://django-calaccess-raw-data.californiacivicdata.org/en/latest/officialdocumentation.html#readme-zip>`_ file for the .ZIP database export file and the `mapping <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/officialdocumentation.html#mapcalformat2fields>`_ of .CAL format to database fields. However, in cases where this official documentation was incomplete or inconsistent, we've either listed the table under whichever category is most obviously relevant or listed it under "Other".


{% for group, model_list in group_list %}
{{ group|capfirst }} tables
---------------------------

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
            <th class="head">Unique key</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    {% for field in object.get_field_list %}
    {% if field.name != "id" %}
        <tr>
            <td>{{ field.name }}</td>
            <td>{{ field.description }}</td>
            <td>{% if field.is_unique_key %}Yes{% else %}No{% endif %}</td>
            <td>{{ field.definition|capfirst }}</td>
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

While the following tables are described in the documentation, but the downloaded raw data files are empty.

.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Group</th>
            <th class="head">File Name</th>
        </tr>
    </thead>
    <tbody valign="top">
    {% for object in empty_files %}
        <tr>
            <td>{{ object.klass_group }}</td>
            <td>{{ object.klass_name }}</td>
        </tr>
    {% endfor %}
    </tbody>
    </table>
    </div>