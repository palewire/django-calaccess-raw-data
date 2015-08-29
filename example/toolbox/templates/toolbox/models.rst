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


        `{{ object.get_tsv_name }} <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

  

**Fields**

<table>
	<thead>
			<tr>
				<th>Field Name</th>
				<th>Field verbHelp</th>
				<th>Field Help</th>

			</tr>

		</thead>	
{% for field in object.get_field_list %}
		
		<tbody>
			<tr>
       <td>  {{ field.name }}</td>
       	
       	

            <td>{% if field.verbose_name %}*{{ field.verbose_name|capfirst }}* {% endif %}</td>
	    
	    	<td>{% if field.help_text %}{{ field.help_text|safe }}{% endif %}</td>
</tr>

        {% endfor %}
        	</tbody>

</table>




{% endfor %}

{% endfor %}



Empty files

-----------

+------------------------------+--------------------------+
|
Source TSV                   | Django model             |
+==============================+==========================+
| FILER_TYPE_PERIODS_CD        |                          |
+------------------------------+--------------------------+
| LOBBYIST_EMPLOYER_HISTORY_CD |                          |
+------------------------------+--------------------------+
| LOBBYIST_FIRM_HISTORY_CD     |                          |
+------------------------------+--------------------------+
