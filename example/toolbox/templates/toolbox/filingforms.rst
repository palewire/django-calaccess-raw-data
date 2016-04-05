Filing Forms
============

The data in CAL-ACCESS originates from forms filed by public office candidates, campaign committees, lobbyists and lobbyist employers. Those forms are describe below.

You can find more information about these filing forms and their instructions in the `Forms <http://www.fppc.ca.gov/forms.html>`_ section of the California Fair Political Practices Commission (FPPC) website and in the `Campaign Finance <http://www.sos.ca.gov/campaign-lobbying/campaign-disclosure-and-requirements>`_ and `Lobbying Activities <http://www.sos.ca.gov/campaign-lobbying/lobbying-disclosure-requirements>`_ sections of the California Secretary of State's website. 

{% for group, form_list in group_list %}
{{ group|title }} Forms
--------------------------

{% for form in form_list %}
{{ form.id }}
~~~~~~~~~~~~~

{{ form.description|safe }}
{% if form.get_models|length > 0 %}
Tables
^^^^^^
Data collected via {{ form.id }} filings are written to the following tables:
{% for model in form.get_models %}
* `{{ model.klass_name }} </models.html#{{ model.klass_name|lower }}>`_
{% endfor %}
{% endif %}

{% if not form.documentcloud %}
*No PDF available.*
{% else %}


.. raw:: html

    <div style="margin-bottom:35px;" id="DV-viewer-{{ form.documentcloud.id }}" class="DV-container"></div>
    <script src="//s3.amazonaws.com/s3.documentcloud.org/viewer/loader.js"></script>
    <script>
      DV.load("//www.documentcloud.org/documents/{{ form.documentcloud.id }}.js", {
      container: "#DV-viewer-{{ form.documentcloud.id }}",
      width: 680,
      height: 850,
      sidebar: false,
      zoom: 550
      });
    </script>
      <noscript>
      <a href={{ form.documentcloud.pdf_url }}>{{ form.documentcloud.title }} (PDF)</a>
      <br />
      <a href={{ form.documentcloud.text_url }}>{{ form.documentcloud.title }} (Text)</a>
    </noscript>

{% endif %}
{% endfor %}
{% endfor %}