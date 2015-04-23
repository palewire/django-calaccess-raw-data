Models
======

A crosswalk between the tables published by California's Secretary of State
and the models in this Django application.

{% for group, model_list in group_list %}
{{ group|capfirst }}
-------
{% for object in model_list %}
{{ object.klass_name }}
~~~~~~~~~~~~~~~~~~~~~~~
{{ object.doc.strip }}

.. py:class:: {{ object.klass_name }}

    **Source data**

        .. py:attribute:: {{ object.get_tsv_name }}

    **Fields**

        {% for field in object.get_field_list %}
        .. py:attribute:: {{ field.name }}

            {% if field.verbose_name %}*{{ field.verbose_name|capfirst }}* {% endif %}{% if field.help_text %}{{ field.help_text|safe }}{% endif %}
        {% endfor %}

{% endfor %}
{% endfor %}

Empty files
-----------

+------------------------------+--------------------------+
| Source TSV                   | Django model             |
+==============================+==========================+
| FILER_TYPE_PERIODS_CD        |                          |
+------------------------------+--------------------------+
| LOBBYIST_EMPLOYER_HISTORY_CD |                          |
+------------------------------+--------------------------+
| LOBBYIST_FIRM_HISTORY_CD     |                          |
+------------------------------+--------------------------+
