Models
======

A crosswalk between the tables published by California's Secretary of State
and the models in this Django application.

Filings
-------
{% for object in model_list %}
{{ object.klass_name }}
~~~~~~~~~~~~~~~~~~~~~~~
{{ object.doc }}

.. py:class:: {{ object.klass_name }}

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
