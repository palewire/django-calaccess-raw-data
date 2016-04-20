Filing Forms
============

The data in CAL-ACCESS originates from forms filed by public office candidates, campaign committees, lobbyists and lobbyist employers. These filing forms are outlined below.

Much of the documents and descriptions included here were gathered from the `Forms <http://www.fppc.ca.gov/forms.html>`_ section of the California Fair Political Practices Commission (FPPC) website, where you can find even more detailed filing instructions and requirements.

Similar documentation and background info can also be found in the `Campaign Finance <http://www.sos.ca.gov/campaign-lobbying/campaign-disclosure-and-requirements>`_ and `Lobbying Activities <http://www.sos.ca.gov/campaign-lobbying/lobbying-disclosure-requirements>`_ sections of the California Secretary of State's website.

.. warning::

    The sections and page numbers noted below match those of the current sample forms provided by the FPPC, but not necessarily any of the actual forms submitted by filers. This is a result of filings that include multiple pages for a given schedule as well as changes to the layout of forms over the years.

    You can view a PDF of any form submitted by a filer by pointing your browser at http://cal-access.ss.ca.gov/PDFGen/pdfgen.prg?filingid=2028957&amendid=0. Note that in the query string parameters, *2028957* and *0* should be exchanged for the filling id and amendment id of the desired filling.


{% for group, form_list in group_list %}
{{ group|title }} Forms
--------------------------

{% for form in form_list %}
{{ form.type_and_num|safe }}
~~~~~~~~~~~~~

{{ form.title|safe }}

{{ form.description|safe }}
{% if form.sections|length > 0 %}
Sections
^^^^^^^^
{% for section in form.sections %}
* {{ section.title|safe }} {% if section.documentcloud.start_page %}(`p. {{ section.documentcloud.start_page }}{% if section.documentcloud.end_page %}-{{ section.documentcloud.end_page }}{% endif%} <{{ section.documentcloud.canonical_url }}>`_){% endif %}

{% endfor %}
{% endif %}

{% if not form.documentcloud_id %}
*No PDF available.*
{% else %}
Example Form
^^^^^^^^^^^^


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

{% if form.get_models|length > 0 %}
Database Tables
^^^^^^^^^^^^^^^
Data collected via {{ form.type_and_num|safe }} filings are written to the following tables:
{% for model in form.get_models %}
* `{{ model.klass_name }} <models.html#{{ model.klass_name|slugify }}>`_
{% endfor %}
{% endif %}

{% endfor %}
{% endfor %}