Database tables
===============

The 80 tab-delimited database exports published by California's Secretary of State and loaded by this Django application.

.. warning::

    Most definitions below are drawn from the spotty and incomplete `official documentation <officialdocumentation.html>`_ verbatim. As we continue our research, we plan to improve the descriptions.

    For the time being, to be absolutely certain about what each table and field contains, you should compare the electronic data back to the original paper records published by the state.

The categories for these tables are based on what's found in the `ReadMe <officialdocumentation.html#readme-zip>`_ file for the .ZIP database export file and the `mapping <officialdocumentation.html#mapcalformat2fields>`_ of .CAL format to database fields. However, in cases where this official documentation was incomplete or inconsistent, we've either listed the table under whichever category is most obviously relevant or listed it under "Other".


Campaign tables
---------------------------


Cvr2CampaignDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Record used to carry additional names (e.g., Assistant Treasurers for the
campaign disclosure forms below.

**Sample:** `CVR2_CAMPAIGN_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_CAMPAIGN_DISCLOSURE_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p41-thumbnail.gif'></a><p>p. 41</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p42-thumbnail.gif'></a><p>p. 42</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p43-thumbnail.gif'></a><p>p. 43</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p32-thumbnail.gif'></a><p>p. 32</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p33-thumbnail.gif'></a><p>p. 33</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p34-thumbnail.gif'></a><p>p. 34</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p35-thumbnail.gif'></a><p>p. 35</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p31-thumbnail.gif'></a><p>p. 31</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p32-thumbnail.gif'></a><p>p. 32</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p33-thumbnail.gif'></a><p>p. 33</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p34-thumbnail.gif'></a><p>p. 34</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/23.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p23-thumbnail.gif'></a><p>p. 23</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p24-thumbnail.gif'></a><p>p. 24</p></div></div>




Filing Forms
^^^^^^^^^^^^
Cvr2CampaignDisclosureCd contains data collected from the following filing forms, form parts and schedules:



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity): Part 1, Committee Information



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 3, Committee Information



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement): Cover Page - Part 2



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report): Part 5, Filing Officers




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Commitee identification number, when the entity is a committee</td>
        </tr>
    
    
    
        <tr>
            <td>control_yn</td>
            <td>Integer</td>
            <td>No</td>
            <td>Controlled Committee (yes/no) checkbox. Legal values are &quot;Y&quot; or &quot;N&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code used to identify the type of entity being described with in the record.</td>
        </tr>
    
    
    
        <tr>
            <td>enty_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Entity city</td>
        </tr>
    
    
    
        <tr>
            <td>enty_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Entity email address</td>
        </tr>
    
    
    
        <tr>
            <td>enty_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity fax number</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity name, or last name if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity prefix or title, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity phone number</td>
        </tr>
    
    
    
        <tr>
            <td>enty_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Entity state</td>
        </tr>
    
    
    
        <tr>
            <td>enty_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity ZIP code</td>
        </tr>
    
    
    
        <tr>
            <td>f460_part</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Part of 460 cover page coded on ths cvr2 record</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer&#39;s mailing city</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer&#39;s mailing state</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s mailing ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>title</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Official title of filing officer. Applies to the form 465.</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p32-thumbnail.gif'></a><p>p. 32</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p32-thumbnail.gif'></a><p>p. 32</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/23.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p23-thumbnail.gif'></a><p>p. 23</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p24-thumbnail.gif'></a><p>p. 24</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ATR</td>
            <td>Assistant treasurer</td>
        </tr>
    
        <tr>
            <td>BNM</td>
            <td>Ballot measure&#39;s name/title</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled committee</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>POF</td>
            <td>Principal officer</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>Proponent</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>FIL</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PEX</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>RDP</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*f460_part*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p32-thumbnail.gif'></a><p>p. 32</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p32-thumbnail.gif'></a><p>p. 32</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p24-thumbnail.gif'></a><p>p. 24</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>3</td>
            <td>Part 3: Committee Information</td>
        </tr>
    
        <tr>
            <td>4a</td>
            <td>Part 4a: Officeholder or Candidate Controlled Committee</td>
        </tr>
    
        <tr>
            <td>4A</td>
            <td>Part 4a: Officeholder or Candidate Controlled Committee</td>
        </tr>
    
        <tr>
            <td>4b</td>
            <td>Part 4b: Related Committees Not Included in this Statement</td>
        </tr>
    
        <tr>
            <td>4B</td>
            <td>Part 4b: Related Committees Not Included in this Statement</td>
        </tr>
    
        <tr>
            <td>5a</td>
            <td>Part 5a: Officeholder or Candidate Controlled Committee</td>
        </tr>
    
        <tr>
            <td>5A</td>
            <td>Part 5a: Officeholder or Candidate Controlled Committee</td>
        </tr>
    
        <tr>
            <td>5b</td>
            <td>Part 5b: Related Committees Not Included in this Statement</td>
        </tr>
    
        <tr>
            <td>5B</td>
            <td>Part 5b: Related Committees Not Included in this Statement</td>
        </tr>
    
        <tr>
            <td>6</td>
            <td>Part 6: Primarily Formed Committee</td>
        </tr>
    
        <tr>
            <td>6a</td>
            <td>Part 6a: Name of Ballot Measure</td>
        </tr>
    
        <tr>
            <td>6A</td>
            <td>Part 6a: Name of Ballot Measure</td>
        </tr>
    
        <tr>
            <td>6b</td>
            <td>Part 6b: Name of Officeholder, Candidate, or Proponent</td>
        </tr>
    
        <tr>
            <td>6B</td>
            <td>Part 6b: Name of Officeholder, Candidate, or Proponent</td>
        </tr>
    
        <tr>
            <td>7</td>
            <td>Part 7: Primarily Formed Committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p31-thumbnail.gif'></a><p>p. 31</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/23.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p23-thumbnail.gif'></a><p>p. 23</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F425</td>
            <td>Form 425 (Semi-Annual Statement of no Activity): Part 1, Committee Information</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 3, Committee Information</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Cover Page - Part 2</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465 (Supplemental Independent Expenditure Report): Part 5, Filing Officers</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p35-thumbnail.gif'></a><p>p. 35</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p33-thumbnail.gif'></a><p>p. 33</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p24-thumbnail.gif'></a><p>p. 24</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>sen</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>SD</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>se</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>LBC</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CA</td>
            <td>Statewide</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p35-thumbnail.gif'></a><p>p. 35</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p34-thumbnail.gif'></a><p>p. 34</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p24-thumbnail.gif'></a><p>p. 24</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>s</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>T</td>
            <td>HELD</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Errata-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712032/pages/Cal-Errata-201-p2-thumbnail.gif'></a><p>p. 2</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ST</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>PAC</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p41-thumbnail.gif'></a><p>p. 41</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p32-thumbnail.gif'></a><p>p. 32</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p31-thumbnail.gif'></a><p>p. 31</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/23.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p23-thumbnail.gif'></a><p>p. 23</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR2</td>
            <td>Cover, Page 2</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sup_opp_cd*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p41-thumbnail.gif'></a><p>p. 41</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p35-thumbnail.gif'></a><p>p. 35</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>OPPOSITION</td>
        </tr>
    
        <tr>
            <td>s</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>o</td>
            <td>OPPOSITION</td>
        </tr>
    
    </tbody>
    </table>
    </div>




Cvr2SoCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Additional names and committees information included on the second page
of a statement of organization creation form filed
by a slate-mailer organization or recipient committee.

**Sample:** `CVR2_SO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_SO_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p45-thumbnail.gif'></a><p>p. 45</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p46-thumbnail.gif'></a><p>p. 46</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p38-thumbnail.gif'></a><p>p. 38</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p39-thumbnail.gif'></a><p>p. 39</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p40-thumbnail.gif'></a><p>p. 40</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p62-thumbnail.gif'></a><p>p. 62</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p63-thumbnail.gif'></a><p>p. 63</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p64-thumbnail.gif'></a><p>p. 64</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/48.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p48-thumbnail.gif'></a><p>p. 48</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p49-thumbnail.gif'></a><p>p. 49</p></div></div>




Filing Forms
^^^^^^^^^^^^
Cvr2SoCd contains data collected from the following filing forms, form parts and schedules:



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization)): Part 3, Individuals Who Authorize Contents Of Slate Mailers



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee): Part 4, Type of Committee




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Type of record. This column will always contain &quot;CVR2&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Form type of the filing the record is included in. This must equal the form_type of the parent filing&#39;s cover (CVR) record.</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record.</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity&#39;s business name or last name if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity&#39;s first name if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity&#39;s name prefix or title if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity&#39;s name suffix if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>item_cd</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Section of the Statement of Organization this itemization relates to. See CAL document for the definition of legal values for this column.</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>State portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zipcode portion of the entity&#39;s mailing address</td>
        </tr>
    
    
    
        <tr>
            <td>day_phone</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity&#39;s daytime phone number</td>
        </tr>
    
    
    
        <tr>
            <td>fax_phone</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Entity&#39;s fax number</td>
        </tr>
    
    
    
        <tr>
            <td>email_adr</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Email address. Not contained in current forms.</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Entity&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ind_group</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Industry group/affiliation description</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description used if the office sought code (OFFICE_CD) equals other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Office jurisdiction code. See CAL document for a list of legal values.</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description provided if the         jurisdiction code (JURIS_CD) equals other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Office district number for Senate, Assembly, and Board of Equalization districts.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office sought/held code. Legal values are &quot;S&quot; for sought and &quot;H&quot; for held</td>
        </tr>
    
    
    
        <tr>
            <td>non_pty_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Non-partisan check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td>party_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of party (if partisan)</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>year_elect</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Year of election</td>
        </tr>
    
    
    
        <tr>
            <td>pof_title</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Position/title of the principal officer</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p46-thumbnail.gif'></a><p>p. 46</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p38-thumbnail.gif'></a><p>p. 38</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p58-thumbnail.gif'></a><p>p. 58</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p45-thumbnail.gif'></a><p>p. 45</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR2</td>
            <td>Cover Page; Additional Names &amp; Addresses</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p38-thumbnail.gif'></a><p>p. 38</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p58-thumbnail.gif'></a><p>p. 58</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p59-thumbnail.gif'></a><p>p. 59</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p45-thumbnail.gif'></a><p>p. 45</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p46-thumbnail.gif'></a><p>p. 46</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F400</td>
            <td>Form 400 (Statement of Organization (Slate Mailer Organization)): Part 3, Individuals Who Authorize Contents Of Slate Mailers</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410 (Statement of Organization Recipient Committee): Part 4, Type of Committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p38-thumbnail.gif'></a><p>p. 38</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p62-thumbnail.gif'></a><p>p. 62</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/48.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p48-thumbnail.gif'></a><p>p. 48</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ATH</td>
            <td>Authorizing individual</td>
        </tr>
    
        <tr>
            <td>ATR</td>
            <td>Assistant treasurer</td>
        </tr>
    
        <tr>
            <td>BNM</td>
            <td>Ballot measure&#39;s name/title</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled committee</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>POF</td>
            <td>Principal officer</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>Proponent</td>
        </tr>
    
        <tr>
            <td>SPO</td>
            <td>Sponsor</td>
        </tr>
    
        <tr>
            <td>BMN</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*item_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p62-thumbnail.gif'></a><p>p. 62</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/48.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p48-thumbnail.gif'></a><p>p. 48</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ATR</td>
            <td>Assistant Treasurer (F410)</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled Committee (F410)</td>
        </tr>
    
        <tr>
            <td>P5B</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PFC</td>
            <td>Primarily Formed Committee Item (F410)</td>
        </tr>
    
        <tr>
            <td>Pfc</td>
            <td>Primarily Formed Committee Item (F410)</td>
        </tr>
    
        <tr>
            <td>POF</td>
            <td>Principal Officer (F400, F410</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>Proponent</td>
        </tr>
    
        <tr>
            <td>SMA</td>
            <td>Slate Mailer Authorizer (F400)</td>
        </tr>
    
        <tr>
            <td>SPO</td>
            <td>Sponsored Committee Itemization (F410)</td>
        </tr>
    
        <tr>
            <td>n/a</td>
            <td>Not Applicable</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CST</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Errata-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712032/pages/Cal-Errata-201-p2-thumbnail.gif'></a><p>p. 2</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
        <tr>
            <td>Asm</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>LEG</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>OF</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>REP</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>05</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>PAC</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p39-thumbnail.gif'></a><p>p. 39</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p63-thumbnail.gif'></a><p>p. 63</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p49-thumbnail.gif'></a><p>p. 49</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>FED</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>JR</td>
            <td>N/A</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p46-thumbnail.gif'></a><p>p. 46</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p39-thumbnail.gif'></a><p>p. 39</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p63-thumbnail.gif'></a><p>p. 63</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p49-thumbnail.gif'></a><p>p. 49</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sup_opp_cd*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p46-thumbnail.gif'></a><p>p. 46</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p40-thumbnail.gif'></a><p>p. 40</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p64-thumbnail.gif'></a><p>p. 64</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p49-thumbnail.gif'></a><p>p. 49</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>O</td>
            <td>OPPOSITION</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SUPPORT</td>
        </tr>
    
    </tbody>
    </table>
    </div>




Cvr3VerificationInfoCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page verification information from campaign disclosure forms

**Sample:** `CVR3_VERIFICATION_INFO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR3_VERIFICATION_INFO_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p46-thumbnail.gif'></a><p>p. 46</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p47-thumbnail.gif'></a><p>p. 47</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p41-thumbnail.gif'></a><p>p. 41</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p42-thumbnail.gif'></a><p>p. 42</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p34-thumbnail.gif'></a><p>p. 34</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p64-thumbnail.gif'></a><p>p. 64</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/25.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p25-thumbnail.gif'></a><p>p. 25</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/50.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p50-thumbnail.gif'></a><p>p. 50</p></div></div>




Filing Forms
^^^^^^^^^^^^
Cvr3VerificationInfoCd contains data collected from the following filing forms, form parts and schedules:



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization)): Part 5, Verification



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement): Cover Page



* `Form 402 <filingforms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization)): Verification



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee): Part 3, Verification



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity): Part 3, Verification



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 4, Verification



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement): Cover Page



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement): Part 4, Verification



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report): Part 6, Verification



* `Form 511 <filingforms.html#form-511>`_ (Paid Spokesperson Report)



* `Form 900 <filingforms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR3</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code</td>
        </tr>
    
    
    
        <tr>
            <td>sig_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date when signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_loc</td>
            <td>String (up to 39)</td>
            <td>No</td>
            <td>City and state where signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_naml</td>
            <td>String (up to 56)</td>
            <td>No</td>
            <td>Last name of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Title of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_nams</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Suffix of the signer</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p34-thumbnail.gif'></a><p>p. 34</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p64-thumbnail.gif'></a><p>p. 64</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/25.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p25-thumbnail.gif'></a><p>p. 25</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/50.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p50-thumbnail.gif'></a><p>p. 50</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR3</td>
            <td>Cover Page 3, Verification Information</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p64-thumbnail.gif'></a><p>p. 64</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/50.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p50-thumbnail.gif'></a><p>p. 50</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F400</td>
            <td>Form 400 (Statement of Organization (Slate Mailer Organization)): Part 5, Verification</td>
        </tr>
    
        <tr>
            <td>F401</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Cover Page</td>
        </tr>
    
        <tr>
            <td>F402</td>
            <td>Form 402 (Statement of Termination (Slate Mailer Organization)): Verification</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410 (Statement of Organization Recipient Committee): Part 3, Verification</td>
        </tr>
    
        <tr>
            <td>F425</td>
            <td>Form 425 (Semi-Annual Statement of no Activity): Part 3, Verification</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 4, Verification</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Cover Page</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 4, Verification</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465 (Supplemental Independent Expenditure Report): Part 6, Verification</td>
        </tr>
    
        <tr>
            <td>F511</td>
            <td>Form 511: Paid Spokesperson Report</td>
        </tr>
    
        <tr>
            <td>F900</td>
            <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p34-thumbnail.gif'></a><p>p. 34</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/25.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p25-thumbnail.gif'></a><p>p. 25</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ATR</td>
            <td>Assistant treasurer</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>Treasurer</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>Proponent</td>
        </tr>
    
        <tr>
            <td>SPO</td>
            <td>Sponsor</td>
        </tr>
    
        <tr>
            <td>atr</td>
            <td>Treasurer</td>
        </tr>
    
        <tr>
            <td>tre</td>
            <td>Assistant treasurer</td>
        </tr>
    
        <tr>
            <td>cao</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>MDI</td>
            <td>Major Donor/Ind Expenditure</td>
        </tr>
    
        <tr>
            <td>POF</td>
            <td>Principal officer</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>BBB</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MAI</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>




CvrCampaignDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page information from campaign disclosure forms. This data comes from
the electronic filing. The data contained herein is "as filed" by the entity
making the filing.

**Sample:** `CVR_CAMPAIGN_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_CAMPAIGN_DISCLOSURE_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/25.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p25-thumbnail.gif'></a><p>p. 25</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/26.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p26-thumbnail.gif'></a><p>p. 26</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/27.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p27-thumbnail.gif'></a><p>p. 27</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p28-thumbnail.gif'></a><p>p. 28</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p29-thumbnail.gif'></a><p>p. 29</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p6-thumbnail.gif'></a><p>p. 6</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/14.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p14-thumbnail.gif'></a><p>p. 14</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p22-thumbnail.gif'></a><p>p. 22</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/23.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p23-thumbnail.gif'></a><p>p. 23</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p24-thumbnail.gif'></a><p>p. 24</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/25.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p25-thumbnail.gif'></a><p>p. 25</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/26.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p26-thumbnail.gif'></a><p>p. 26</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/27.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p27-thumbnail.gif'></a><p>p. 27</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p28-thumbnail.gif'></a><p>p. 28</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p30-thumbnail.gif'></a><p>p. 30</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p18-thumbnail.gif'></a><p>p. 18</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p19-thumbnail.gif'></a><p>p. 19</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p20-thumbnail.gif'></a><p>p. 20</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p21-thumbnail.gif'></a><p>p. 21</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




Filing Forms
^^^^^^^^^^^^
CvrCampaignDisclosureCd contains data collected from the following filing forms, form parts and schedules:



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement): Cover Page



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity): Part 1, Committee Information



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Type of Recipient Committee



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement): Cover Page



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)

    * Part 1, Name and Address of Filer

    * Part 2, Nature and Interests of Filer




* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)

    * Part 1, Committee/Filer Information

    * Part 2, Name of Candidate or Measure Supported or Opposed




* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report): Part 1, List Only One Candidate or Ballot Measure



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 511 <filingforms.html#form-511>`_ (Paid Spokesperson Report)



* `Form 900 <filingforms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amendexp_1</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 1</td>
        </tr>
    
    
    
        <tr>
            <td>amendexp_2</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 2</td>
        </tr>
    
    
    
        <tr>
            <td>amendexp_3</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amendment explanation line 3</td>
        </tr>
    
    
    
        <tr>
            <td>assoc_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Association Interests info included check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td>assoc_int</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Description of association interests</td>
        </tr>
    
    
    
        <tr>
            <td>bal_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>.CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td>brdbase_yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Broad Base Committee (yes/no) check box. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td>bus_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employer/business address city</td>
        </tr>
    
    
    
        <tr>
            <td>bus_inter</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Employer/business interest description</td>
        </tr>
    
    
    
        <tr>
            <td>bus_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of employer/business. Applies to the form 461.</td>
        </tr>
    
    
    
        <tr>
            <td>bus_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employer/business address state</td>
        </tr>
    
    
    
        <tr>
            <td>bus_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer/business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>busact_cb</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Business activity info included check-box. Valid values are &#39;X&#39; and null</td>
        </tr>
    
    
    
        <tr>
            <td>busactvity</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Business activity description</td>
        </tr>
    
    
    
        <tr>
            <td>cand_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/officeholder city</td>
        </tr>
    
    
    
        <tr>
            <td>cand_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/officeholder email. This field is not contained on the forms.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder fax. This field is not contained on the forms.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>.CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name. Applies to forms 460, 465, and 496.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>cand_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder phone</td>
        </tr>
    
    
    
        <tr>
            <td>cand_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>cand_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>cmtte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee ID (Filer_id) of recipient Committee who&#39;s campaign statement is attached. This field applies to the form 401.</td>
        </tr>
    
    
    
        <tr>
            <td>cmtte_type</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Type of Recipient Committee. Applies to the 450/460.</td>
        </tr>
    
    
    
        <tr>
            <td>control_yn</td>
            <td>Integer</td>
            <td>No</td>
            <td>Controlled Committee (yes/no) check box. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>elect_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the General Election</td>
        </tr>
    
    
    
        <tr>
            <td>emplbus_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Employer/Business Info included check-box. Legal values are &#39;X&#39; or null. Applies to the Form 461.</td>
        </tr>
    
    
    
        <tr>
            <td>employer</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer. This field is most likely unused.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>The entity type of the filer. These codes vary by form type.</td>
        </tr>
    
    
    
        <tr>
            <td>file_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Filer&#39;s email address</td>
        </tr>
    
    
    
        <tr>
            <td>filer_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>filer_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer&#39;s fax</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer&#39;s first name, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>The committee&#39;s or organization&#39;s name or if an individual the filer&#39;s last name.</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s suffix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s title or prefix, if an individual</td>
        </tr>
    
    
    
        <tr>
            <td>filer_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer phone number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer state</td>
        </tr>
    
    
    
        <tr>
            <td>filer_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction description if the field JURIS_CD is set to city (CIT), county (CTY), local (LOC), or other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td>late_rptno</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Identifying Report Number used to distinguish multiple reports filed during the same filing period. For example, this field allows for multiple form 497s to be filed on the same day.</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer mailing address state</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer mailing address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>occupation</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation. This field is most likely unused.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description if the field OFFICE_CD is set to other (OTH)</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>other_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other entity interests info included check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td>other_int</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Other entity interests description</td>
        </tr>
    
    
    
        <tr>
            <td>primfrm_yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Primarily Formed Committee (yes/no) checkbox. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number, as reported by the filer Report Number 000 represents an original filing. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>reportname</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement type. Legal values are 450, 460, and 461.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_att_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Committee Report Attached check-box. Legal values are &#39;X&#39; or null. This field applies to the form 401.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report was filed, according to the filer</td>
        </tr>
    
    
    
        <tr>
            <td>rptfromdt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement - Period from date.</td>
        </tr>
    
    
    
        <tr>
            <td>rptthrudt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement - Period through date.</td>
        </tr>
    
    
    
        <tr>
            <td>selfemp_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self employed check-box. CAL format to db tables doc says: &quot;Not Used-AMS KDE&quot;</td>
        </tr>
    
    
    
        <tr>
            <td>sponsor_yn</td>
            <td>Integer</td>
            <td>No</td>
            <td>Sponsored Committee (yes/no) checkbox. Legal values are &#39;Y&#39; or &#39;N&#39;.</td>
        </tr>
    
    
    
        <tr>
            <td>stmt_type</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address.</td>
        </tr>
    
    
    
        <tr>
            <td>tres_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s email</td>
        </tr>
    
    
    
        <tr>
            <td>tres_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s fax number</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s ZIP Code</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*cmtte_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p10-thumbnail.gif'></a><p>p. 10</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p24-thumbnail.gif'></a><p>p. 24</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p19-thumbnail.gif'></a><p>p. 19</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>C</td>
            <td>Candidate or officeholder controlled committee</td>
        </tr>
    
        <tr>
            <td>P</td>
            <td>Candidate or officeholder primarily formed committee</td>
        </tr>
    
        <tr>
            <td>B</td>
            <td>Ballot-measure committee</td>
        </tr>
    
        <tr>
            <td>G</td>
            <td>General-purpose committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p6-thumbnail.gif'></a><p>p. 6</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p22-thumbnail.gif'></a><p>p. 22</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>BMC</td>
            <td>Ballot measure committee</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>MDI</td>
            <td>Major Donor/Ind Expenditure</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PTY</td>
            <td>Political Party</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SCC</td>
            <td>Small Contributor Committee</td>
        </tr>
    
        <tr>
            <td>SMO</td>
            <td>Slate-mailer organization</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p22-thumbnail.gif'></a><p>p. 22</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F401</td>
            <td>Form 401: Slate Mailer Organization Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F425</td>
            <td>Form 425: Semi-Annual Statement of no Activity</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>F498</td>
            <td>Form 498: Slate Mailer Late Payment Report</td>
        </tr>
    
        <tr>
            <td>F511</td>
            <td>Form 511: Paid Spokesperson Report</td>
        </tr>
    
        <tr>
            <td>F900</td>
            <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p13-thumbnail.gif'></a><p>p. 13</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p28-thumbnail.gif'></a><p>p. 28</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p21-thumbnail.gif'></a><p>p. 21</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>sen</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>Gov</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>46</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>55</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>APP</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SD</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>OC</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>AD</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>CA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p28-thumbnail.gif'></a><p>p. 28</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p21-thumbnail.gif'></a><p>p. 21</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>s</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>h</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>UNKNOWN</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
        <tr>
            <td>Gov</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>Sen</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>LEG</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>REP</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>Mem</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>PAC</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/25.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p25-thumbnail.gif'></a><p>p. 25</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p6-thumbnail.gif'></a><p>p. 6</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p22-thumbnail.gif'></a><p>p. 22</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR</td>
            <td>Cover Page</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*reportname*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p19-thumbnail.gif'></a><p>p. 19</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/26.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p26-thumbnail.gif'></a><p>p. 26</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/15.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p15-thumbnail.gif'></a><p>p. 15</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p20-thumbnail.gif'></a><p>p. 20</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*stmt_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p7-thumbnail.gif'></a><p>p. 7</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/23.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p23-thumbnail.gif'></a><p>p. 23</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>PE</td>
            <td>Pre-Election (F450, F460)</td>
        </tr>
    
        <tr>
            <td>QT</td>
            <td>Quarterly Stmt (F450,F460)</td>
        </tr>
    
        <tr>
            <td>SA</td>
            <td>Semi-annual (F450, F460)</td>
        </tr>
    
        <tr>
            <td>SE</td>
            <td>Supplemental Pre-elect (F450, F460, F495)</td>
        </tr>
    
        <tr>
            <td>SY</td>
            <td>Special Odd-Yr. Campaign (F450, F460)</td>
        </tr>
    
        <tr>
            <td>S1</td>
            <td>Semi-Annual (Jan1-Jun30) (F425)</td>
        </tr>
    
        <tr>
            <td>S2</td>
            <td>Semi-Annual (Jul1-Dec31) (F425)</td>
        </tr>
    
        <tr>
            <td>TS</td>
            <td>Termination Statement (F450, F460)</td>
        </tr>
    
        <tr>
            <td>pe</td>
            <td>Pre-Election (F450, F460)</td>
        </tr>
    
        <tr>
            <td>qt</td>
            <td>Quarterly Stmt (F450,F460)</td>
        </tr>
    
        <tr>
            <td>sa</td>
            <td>Semi-annual (F450, F460)</td>
        </tr>
    
        <tr>
            <td>se</td>
            <td>Supplemental Pre-elect (F450, F460, F495)</td>
        </tr>
    
        <tr>
            <td>sy</td>
            <td>Special Odd-Yr. Campaign (F450, F460)</td>
        </tr>
    
        <tr>
            <td>ts</td>
            <td>Termination Statement (F450, F460)</td>
        </tr>
    
        <tr>
            <td>**</td>
            <td>Amendment</td>
        </tr>
    
        <tr>
            <td>1</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>2</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MD</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>NA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PR</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>QS</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>x</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>YE</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sup_opp_cd*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p28-thumbnail.gif'></a><p>p. 28</p></div></div>


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/14.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p14-thumbnail.gif'></a><p>p. 14</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p28-thumbnail.gif'></a><p>p. 28</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p21-thumbnail.gif'></a><p>p. 21</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>OPPOSITION</td>
        </tr>
    
        <tr>
            <td>s</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>o</td>
            <td>OPPOSITION</td>
        </tr>
    
    </tbody>
    </table>
    </div>




CvrF470Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page layout for Officeholder and Candidate Short and Supplement Forms
(Form 470)

**Sample:** `CVR_F470_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_F470_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p30-thumbnail.gif'></a><p>p. 30</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p31-thumbnail.gif'></a><p>p. 31</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p32-thumbnail.gif'></a><p>p. 32</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/15.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p15-thumbnail.gif'></a><p>p. 15</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p16-thumbnail.gif'></a><p>p. 16</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p30-thumbnail.gif'></a><p>p. 30</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




Filing Forms
^^^^^^^^^^^^
CvrF470Cd contains data collected from the following filing forms, form parts and schedules:



* `Form 470 <filingforms.html#form-470>`_ (Officeholder and Candidate Campaign Statement, Short Form)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment Identification number. A number of 0 is an original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_adr1</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>First line of the filer&#39;s street address.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_adr2</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Second line of the filer&#39;s street address. </td>
        </tr>
    
    
    
        <tr>
            <td>cand_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s City.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s EMail address. Not required by the form.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s FAX Phone Number. Not required by the form.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/Officeholder&#39;s phone number.</td>
        </tr>
    
    
    
        <tr>
            <td>cand_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer&#39;s State</td>
        </tr>
    
    
    
        <tr>
            <td>cand_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s zipcode</td>
        </tr>
    
    
    
        <tr>
            <td>date_1000</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date contributions totaling $1,000 or more. (For the 470-S)</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>elect_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the general election. Required for filings in even years.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>The filer&#39;s entity code. The value of this column will always be Candidate/Office Holder (CAO) for this table.</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer&#39;s First Name(s) - required for individuals</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer&#39;s Last Name/Committee name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer&#39;s Name Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>The filer&#39;s prefix or title that preceeds their name if they are an individual.</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Type of Filing or Formset. The value of this column will always be equal to F470.</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office Jurisdiction Code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description text reqired if the jurisdiction code (Juris_cd) is equal to CIT, CTY, LOC, or OTH.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office Sought/Held code. Legal values are &quot;S&quot; for sought and &quot;H&quot; for held.</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description used if the office code is other (OTH).</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Code that identifies the office being sought. See the CAL document for a list of valid codes.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 3)</td>
            <td>Yes</td>
            <td>Type of CAL record. This column will always contain CVR.</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number; 000 Original; 001-999 Amended as reported in the filing.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed as reported by the filer.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F470</td>
            <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p30-thumbnail.gif'></a><p>p. 30</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR</td>
            <td>Cover Page</td>
        </tr>
    
    </tbody>
    </table>
    </div>




CvrSoCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page for a statement of organization creation or termination
form filed by a slate-mailer organization or recipient committee.

**Sample:** `CVR_SO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_SO_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p39-thumbnail.gif'></a><p>p. 39</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p40-thumbnail.gif'></a><p>p. 40</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p41-thumbnail.gif'></a><p>p. 41</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p28-thumbnail.gif'></a><p>p. 28</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p29-thumbnail.gif'></a><p>p. 29</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p30-thumbnail.gif'></a><p>p. 30</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p31-thumbnail.gif'></a><p>p. 31</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p59-thumbnail.gif'></a><p>p. 59</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/60.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p60-thumbnail.gif'></a><p>p. 60</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p61-thumbnail.gif'></a><p>p. 61</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p46-thumbnail.gif'></a><p>p. 46</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p47-thumbnail.gif'></a><p>p. 47</p></div></div>




Filing Forms
^^^^^^^^^^^^
CvrSoCd contains data collected from the following filing forms, form parts and schedules:



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))

    * Part 1, Slate Mailer Organization Information

    * Part 2, Treasurer And Other Principal Officers

    * Part 4, Is This Organization A "Committee" Pursuant To Government Code Section 82013?




* `Form 402 <filingforms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization)): Cover Page



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee)

    * Part 1, Committee Information

    * Part 2, Treasurer and Other Principal Officers

    * Part 4, Type of Committee





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>acct_opendt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date Account Opened</td>
        </tr>
    
    
    
        <tr>
            <td>actvty_lvl</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Organization&#39;s level of activity</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>bank_adr1</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Street 1 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_adr2</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>Street 2 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_nam</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Phone of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>bank_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP+4 of Financial Institution</td>
        </tr>
    
    
    
        <tr>
            <td>brdbase_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Broad Based Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Optional Committee EMAIL address</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Optional Committee FAX number</td>
        </tr>
    
    
    
        <tr>
            <td>com82013id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>ID of 82013 Committee (if Com82013Nm is a RCP cmtte)</td>
        </tr>
    
    
    
        <tr>
            <td>com82013nm</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of 82013 Committee (F400; when Com82013YN=Y)</td>
        </tr>
    
    
    
        <tr>
            <td>com82013yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Is this SMO a 82013 &quot;Committee&quot;? (Yes/No) (F400)</td>
        </tr>
    
    
    
        <tr>
            <td>control_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Controlled Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>county_act</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>County where Active (F410)</td>
        </tr>
    
    
    
        <tr>
            <td>county_res</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>County of Domicile, Residence, or Location</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Filer. Values: SMO - Slate Mailer Organization (F400,402) [COM|RCP] - Recipient Committee (F410)</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer name title</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>genpurp_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>General Purpose Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>gpc_descr</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Brief description of Activity of GPC</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - City</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - State</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Mailing Address of Filing Committee - ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td>phone</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Phone Number of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td>primfc_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Primarily Formed Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>qualfy_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date qualified as an organization</td>
        </tr>
    
    
    
        <tr>
            <td>qual_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Qualified Committee check-box (Req. if SMO)</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number - Values: 000 - Original Report 001 thru 999 - Amended Rpt #1-#999</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed</td>
        </tr>
    
    
    
        <tr>
            <td>smcont_qualdt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date Small Contributor Committee Qualified</td>
        </tr>
    
    
    
        <tr>
            <td>sponsor_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Sponsored Committee Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State of Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    
        <tr>
            <td>surplusdsp</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Disposition of Surplus Funds</td>
        </tr>
    
    
    
        <tr>
            <td>term_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Termination Effective Date (Req. if F402)</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s name title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Treasurer&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer&#39;s street</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP+4 for Org / Committee / Candidate or Office holder</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*actvty_lvl*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p30-thumbnail.gif'></a><p>p. 30</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/60.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p60-thumbnail.gif'></a><p>p. 60</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p47-thumbnail.gif'></a><p>p. 47</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CI</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CO</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>ST</td>
            <td>State</td>
        </tr>
    
        <tr>
            <td>St</td>
            <td>State</td>
        </tr>
    
        <tr>
            <td>st</td>
            <td>State</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p59-thumbnail.gif'></a><p>p. 59</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p46-thumbnail.gif'></a><p>p. 46</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>BMC</td>
            <td>Ballot measure committee</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled committee</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SMO</td>
            <td>Slate-mailer organization</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p59-thumbnail.gif'></a><p>p. 59</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p46-thumbnail.gif'></a><p>p. 46</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F400</td>
            <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F402</td>
            <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410: Statement of Organization Recipient Committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p28-thumbnail.gif'></a><p>p. 28</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p59-thumbnail.gif'></a><p>p. 59</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p46-thumbnail.gif'></a><p>p. 46</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR</td>
            <td>Cover Page for Stmt of Organization / Slate Mailer Org, Stmt of Termination / Slate Mailer Org or Stmt of Organization / Recipient Committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>




DebtCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Form 460 (Recipient Committee Campaign Statement) Schedule (F) Accrued
Expenses (Unpaid Bills) records

**Sample:** `DEBT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/DEBT_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p47-thumbnail.gif'></a><p>p. 47</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/48.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p48-thumbnail.gif'></a><p>p. 48</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p49-thumbnail.gif'></a><p>p. 49</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p45-thumbnail.gif'></a><p>p. 45</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p46-thumbnail.gif'></a><p>p. 46</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p33-thumbnail.gif'></a><p>p. 33</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p34-thumbnail.gif'></a><p>p. 34</p></div></div>




Filing Forms
^^^^^^^^^^^^
DebtCd contains data collected from the following filing forms, form parts and schedules:



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amt_incur</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount incurred this period</td>
        </tr>
    
    
    
        <tr>
            <td>amt_paid</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount paid this period.</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to a transaction identifier of a parent record.</td>
        </tr>
    
    
    
        <tr>
            <td>beg_bal</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding balance at beginning of period</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>end_bal</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding balance at close of this period</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code describing the payee</td>
        </tr>
    
    
    
        <tr>
            <td>expn_code</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Expense Code</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number of the parent filing</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 1)</td>
            <td>Yes</td>
            <td>Schedule Name/ID: (F - Sched F / Accrued Expenses)</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Record line item number</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record.</td>
        </tr>
    
    
    
        <tr>
            <td>payee_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>First line of the payee&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s first name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s business name or last name if the payee is an individual.</td>
        </tr>
    
    
    
        <tr>
            <td>payee_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s name suffix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Payee&#39;s prefix or title if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>payee_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record type value: DEBT</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Transaction identifier - permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td>xref_match</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. /&quot;X/&quot; indicates this condition is true</td>
        </tr>
    
    
    
        <tr>
            <td>xref_schnm</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Schedule C.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p45-thumbnail.gif'></a><p>p. 45</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p33-thumbnail.gif'></a><p>p. 33</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>BNM</td>
            <td>Ballot measure&#39;s name/title</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PTY</td>
            <td>Political Party</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SCC</td>
            <td>Small Contributor Committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*expn_code*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/14.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p14-thumbnail.gif'></a><p>p. 14</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p11-thumbnail.gif'></a><p>p. 11</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CMP</td>
            <td>campaign paraphernalia/miscellaneous</td>
        </tr>
    
        <tr>
            <td>CNS</td>
            <td>campaign consultants</td>
        </tr>
    
        <tr>
            <td>CTB</td>
            <td>contribution (if nonmonetary, explain)*</td>
        </tr>
    
        <tr>
            <td>CVC</td>
            <td>civic donations</td>
        </tr>
    
        <tr>
            <td>FIL</td>
            <td>candidate filing/ballot feeds</td>
        </tr>
    
        <tr>
            <td>FND</td>
            <td>fundraising events</td>
        </tr>
    
        <tr>
            <td>IKD</td>
            <td>In-kind contribution (nonmonetary)</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>independent expenditure supporting/opposing others (explain)*</td>
        </tr>
    
        <tr>
            <td>LEG</td>
            <td>legal defense</td>
        </tr>
    
        <tr>
            <td>LIT</td>
            <td>campaign literature and mailings</td>
        </tr>
    
        <tr>
            <td>LON</td>
            <td>loan</td>
        </tr>
    
        <tr>
            <td>MBR</td>
            <td>member communications</td>
        </tr>
    
        <tr>
            <td>MON</td>
            <td>monetary contribution</td>
        </tr>
    
        <tr>
            <td>MTG</td>
            <td>meetings and appearances</td>
        </tr>
    
        <tr>
            <td>OFC</td>
            <td>office expenses</td>
        </tr>
    
        <tr>
            <td>PET</td>
            <td>petition circulating</td>
        </tr>
    
        <tr>
            <td>PHO</td>
            <td>phone banks</td>
        </tr>
    
        <tr>
            <td>POL</td>
            <td>polling and survey research</td>
        </tr>
    
        <tr>
            <td>POS</td>
            <td>postage, delivery and messenger services</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>professional services (legal, accounting)</td>
        </tr>
    
        <tr>
            <td>PRT</td>
            <td>print ads</td>
        </tr>
    
        <tr>
            <td>RAD</td>
            <td>radio airtime and production costs</td>
        </tr>
    
        <tr>
            <td>RFD</td>
            <td>returned contributions</td>
        </tr>
    
        <tr>
            <td>SAL</td>
            <td>campaign workers salaries</td>
        </tr>
    
        <tr>
            <td>TEL</td>
            <td>T.V. or cable airtime and production costs</td>
        </tr>
    
        <tr>
            <td>TRC</td>
            <td>candidate travel, lodging and meals (explain)</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>staff/spouse travel, lodging and meals (explain)</td>
        </tr>
    
        <tr>
            <td>TSF</td>
            <td>transfer between committees of the same candidate/sponsor</td>
        </tr>
    
        <tr>
            <td>VOT</td>
            <td>voter registration</td>
        </tr>
    
        <tr>
            <td>WEB</td>
            <td>information technology costs (internet, e-mail)</td>
        </tr>
    
        <tr>
            <td>Fnd</td>
            <td>fundraising events</td>
        </tr>
    
        <tr>
            <td>ofc</td>
            <td>office expenses</td>
        </tr>
    
        <tr>
            <td>*</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>AIR</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>BUS</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>C</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CAM</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CC</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>&#39;CN&#39;</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CSN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>DEP</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>EVE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FED</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>fns</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>G</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>GGG</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>HOT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>L</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>LDF</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MEE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>N</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>P</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PEN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SPE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>STA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>T</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TAX</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TRA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>V</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>X</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p45-thumbnail.gif'></a><p>p. 45</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p33-thumbnail.gif'></a><p>p. 33</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p45-thumbnail.gif'></a><p>p. 45</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p46-thumbnail.gif'></a><p>p. 46</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p33-thumbnail.gif'></a><p>p. 33</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p34-thumbnail.gif'></a><p>p. 34</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>DEBT</td>
            <td>DEBT</td>
        </tr>
    
    </tbody>
    </table>
    </div>




ExpnCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Campaign expenditures from a variety of forms

**Sample:** `EXPN_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/EXPN_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p53-thumbnail.gif'></a><p>p. 53</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p54-thumbnail.gif'></a><p>p. 54</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/55.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p55-thumbnail.gif'></a><p>p. 55</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p56-thumbnail.gif'></a><p>p. 56</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p45-thumbnail.gif'></a><p>p. 45</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/46.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p46-thumbnail.gif'></a><p>p. 46</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p47-thumbnail.gif'></a><p>p. 47</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/48.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p48-thumbnail.gif'></a><p>p. 48</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p42-thumbnail.gif'></a><p>p. 42</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p43-thumbnail.gif'></a><p>p. 43</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p44-thumbnail.gif'></a><p>p. 44</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p31-thumbnail.gif'></a><p>p. 31</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p32-thumbnail.gif'></a><p>p. 32</p></div></div>




Filing Forms
^^^^^^^^^^^^
ExpnCd contains data collected from the following filing forms, form parts and schedules:



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees

    * Schedule E, Payments Made

    * Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)




* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement): Part 5, Contributions (Including Loans, Forgiveness of Loans, and LoanGuarantees) and Expenditures Made



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report): Part 3, Independent Expenditures Made



* `Form 900 <filingforms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>agent_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td>agent_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Last name (Sched G)</td>
        </tr>
    
    
    
        <tr>
            <td>agent_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>agent_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent of Ind. Contractor&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of Payment</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to a Tran_ID of a &#39;parent&#39; record</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot Measure Name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot Number or Letter</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate&#39;s Last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee ID (If [COM|RCP] &amp; no ID#, Treas info Req.)</td>
        </tr>
    
    
    
        <tr>
            <td>cum_oth</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative / &#39;Other&#39; (No Cumulative on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td>cum_ytd</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative / Year-to-date amount         (No Cumulative on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office District Number (Req. if Juris_Cd=[SEN|ASM|BOE]</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing payee</td>
        </tr>
    
    
    
        <tr>
            <td>expn_chkno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Check Number (Optional)</td>
        </tr>
    
    
    
        <tr>
            <td>expn_code</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>CTB &amp; IND need explanation &amp; listing on Sched D TRC &amp; TRS require explanation</td>
        </tr>
    
    
    
        <tr>
            <td>expn_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of Expenditure (Note: Date not on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 6)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>g_from_e_f</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Back Reference from Sched G to Sched &#39;E&#39; or &#39;F&#39;?</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office Jurisdiction Code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction Description         (Req. if Juris_Cd=[CIT|CTY|LOC|OTH]</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo Amount? (Date/Amount are informational only)</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Sought Description (Req. if Office_Cd=OTH)</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>payee_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee City</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s First name</td>
        </tr>
    
    
    
        <tr>
            <td>payee_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s Last name</td>
        </tr>
    
    
    
        <tr>
            <td>payee_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>payee_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State code</td>
        </tr>
    
    
    
        <tr>
            <td>payee_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zip+4</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: EXPN</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer City</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer&#39;s First name (Req if [COM|RCP] &amp; no ID#)</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer&#39;s Last name (Req if [COM|RCP] &amp; no ID#)</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer State</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td>xref_match</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>X = Related item on other Sched has same Tran_ID</td>
        </tr>
    
    
    
        <tr>
            <td>xref_schnm</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related item is included on Sched &#39;C&#39; or &#39;H2&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p42-thumbnail.gif'></a><p>p. 42</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p31-thumbnail.gif'></a><p>p. 31</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PTY</td>
            <td>Political Party</td>
        </tr>
    
        <tr>
            <td>SCC</td>
            <td>Small Contributor Committee</td>
        </tr>
    
        <tr>
            <td>BNM</td>
            <td>Ballot measure&#39;s name/title</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>MBR</td>
            <td>Member of Associaton</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PTH</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>RFD</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*expn_code*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/14.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p14-thumbnail.gif'></a><p>p. 14</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p11-thumbnail.gif'></a><p>p. 11</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CMP</td>
            <td>campaign paraphernalia/miscellaneous</td>
        </tr>
    
        <tr>
            <td>CNS</td>
            <td>campaign consultants</td>
        </tr>
    
        <tr>
            <td>CTB</td>
            <td>contribution (if nonmonetary, explain)*</td>
        </tr>
    
        <tr>
            <td>CVC</td>
            <td>civic donations</td>
        </tr>
    
        <tr>
            <td>FIL</td>
            <td>candidate filing/ballot feeds</td>
        </tr>
    
        <tr>
            <td>FND</td>
            <td>fundraising events</td>
        </tr>
    
        <tr>
            <td>IKD</td>
            <td>In-kind contribution (nonmonetary)</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>independent expenditure supporting/opposing others (explain)*</td>
        </tr>
    
        <tr>
            <td>LEG</td>
            <td>legal defense</td>
        </tr>
    
        <tr>
            <td>LIT</td>
            <td>campaign literature and mailings</td>
        </tr>
    
        <tr>
            <td>LON</td>
            <td>loan</td>
        </tr>
    
        <tr>
            <td>MBR</td>
            <td>member communications</td>
        </tr>
    
        <tr>
            <td>MON</td>
            <td>monetary contribution</td>
        </tr>
    
        <tr>
            <td>MTG</td>
            <td>meetings and appearances</td>
        </tr>
    
        <tr>
            <td>OFC</td>
            <td>office expenses</td>
        </tr>
    
        <tr>
            <td>PET</td>
            <td>petition circulating</td>
        </tr>
    
        <tr>
            <td>PHO</td>
            <td>phone banks</td>
        </tr>
    
        <tr>
            <td>POL</td>
            <td>polling and survey research</td>
        </tr>
    
        <tr>
            <td>POS</td>
            <td>postage, delivery and messenger services</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>professional services (legal, accounting)</td>
        </tr>
    
        <tr>
            <td>PRT</td>
            <td>print ads</td>
        </tr>
    
        <tr>
            <td>RAD</td>
            <td>radio airtime and production costs</td>
        </tr>
    
        <tr>
            <td>RFD</td>
            <td>returned contributions</td>
        </tr>
    
        <tr>
            <td>SAL</td>
            <td>campaign workers salaries</td>
        </tr>
    
        <tr>
            <td>TEL</td>
            <td>T.V. or cable airtime and production costs</td>
        </tr>
    
        <tr>
            <td>TRC</td>
            <td>candidate travel, lodging and meals (explain)</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>staff/spouse travel, lodging and meals (explain)</td>
        </tr>
    
        <tr>
            <td>TSF</td>
            <td>transfer between committees of the same candidate/sponsor</td>
        </tr>
    
        <tr>
            <td>VOT</td>
            <td>voter registration</td>
        </tr>
    
        <tr>
            <td>WEB</td>
            <td>information technology costs (internet, e-mail)</td>
        </tr>
    
        <tr>
            <td>ctb</td>
            <td>contribution (if nonmonetary, explain)*</td>
        </tr>
    
        <tr>
            <td>ikd</td>
            <td>In-kind contribution (nonmonetary)</td>
        </tr>
    
        <tr>
            <td>Mon</td>
            <td>monetary contribution</td>
        </tr>
    
        <tr>
            <td>ofc</td>
            <td>office expenses</td>
        </tr>
    
        <tr>
            <td>OFc</td>
            <td>office expenses</td>
        </tr>
    
        <tr>
            <td>Ofc</td>
            <td>office expenses</td>
        </tr>
    
        <tr>
            <td></td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>*</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>001</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>011</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>200</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>401</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>ADV</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>ANN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>APR</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>AUG</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>AUT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Ban</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>BAN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>BOO</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>BOX</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>C</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CC</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CHE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CIV</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CNT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>COP</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CRE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CSN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>,CT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>.CT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CTN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CVD</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>DEC</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Dem</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>DIN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Don</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>DON</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Ear</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>EIM</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>EMP</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FAX</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FDN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FED</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FEE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FIN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Fun</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FUN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>G</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>GEN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>GGG</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>GOT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>IEs</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>IN-</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Ina</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>INK</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>ITE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>JAN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>JUL</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>JUN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>KIC</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>L</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>LEV</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Lit</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>LN#</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>LOG</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>M</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MAI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Mar</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MAR</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MED</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MEE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MGT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Mis</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MRB</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>NGP</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>NON</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>NOT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>NOV</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>OCT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>.OF</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>OPE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>P</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Pac</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PAI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PAR</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PAY</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PEN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PMT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>.PO</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Pos</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PRE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PRI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PRP</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>R</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>.Re</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>.RE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>REF</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>REI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>RFP</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S-A</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Sal</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S C</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S.C</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SCU</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SEE</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SEP</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S.M.</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SOF</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SWI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>T</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TAX</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TB</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TB,</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TIC</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Tor</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TRA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TRF</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>TRV</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>UN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>UTI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>V</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>VEN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>-VO</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>VOI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>VOY</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>WI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>x</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>X</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S-6</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S.M</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S-4</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SA:</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>100</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>RFN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>REN</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>003</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>S-1</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>08</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p42-thumbnail.gif'></a><p>p. 42</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p31-thumbnail.gif'></a><p>p. 31</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F450P5</td>
            <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
        </tr>
    
        <tr>
            <td>D</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees</td>
        </tr>
    
        <tr>
            <td>E</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule E, Payments Made</td>
        </tr>
    
        <tr>
            <td>G</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)</td>
        </tr>
    
        <tr>
            <td>F461P5</td>
            <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 5, Contributions (Including Loans, Forgiveness of Loans, and LoanGuarantees) and Expenditures Made</td>
        </tr>
    
        <tr>
            <td>F465P3</td>
            <td>Form 465 (Supplemental Independent Expenditure Report): Part 3, Independent Expenditures Made</td>
        </tr>
    
        <tr>
            <td>F900</td>
            <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p44-thumbnail.gif'></a><p>p. 44</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p32-thumbnail.gif'></a><p>p. 32</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>Cit</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>sen</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>Sen</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>stw</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>APP</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>12</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>4</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>8</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>27</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>93</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>98</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>CLB</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Boa</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>Sta</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>STA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CA</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p44-thumbnail.gif'></a><p>p. 44</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p32-thumbnail.gif'></a><p>p. 32</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>s</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>h</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>A</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>a</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>8</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>UNKNOWN</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Errata-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712032/pages/Cal-Errata-201-p2-thumbnail.gif'></a><p>p. 2</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
        <tr>
            <td>Cou</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>sen</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>AtT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>May</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>Sen</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>asm</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>gov</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>Gov</td>
            <td>Governor</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p42-thumbnail.gif'></a><p>p. 42</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/31.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p31-thumbnail.gif'></a><p>p. 31</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>EXPN</td>
            <td>Expense</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sup_opp_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p44-thumbnail.gif'></a><p>p. 44</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p32-thumbnail.gif'></a><p>p. 32</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>O</td>
            <td>OPPOSITION</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>s</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>o</td>
            <td>OPPOSITION</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>N</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>X</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>Y</td>
            <td>UNKNOWN</td>
        </tr>
    
    </tbody>
    </table>
    </div>




F495P2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Form 495 Supplemental Pre-Election Campaign Statement (attachment to
Recipient Committee Campaign Statements (Forms 450 and 460).

**Sample:** `F495P2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F495P2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p56-thumbnail.gif'></a><p>p. 56</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p57-thumbnail.gif'></a><p>p. 57</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p49-thumbnail.gif'></a><p>p. 49</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p35-thumbnail.gif'></a><p>p. 35</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/26.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p26-thumbnail.gif'></a><p>p. 26</p></div></div>




Filing Forms
^^^^^^^^^^^^
F495P2Cd contains data collected from the following filing forms, form parts and schedules:



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type Value: F495</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form to which the Form 495 is attached (must equal Form_Type in CVR record)</td>
        </tr>
    
    
    
        <tr>
            <td>elect_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of the General Election This date will be the same as on the filing&#39;s cover (CVR) record.</td>
        </tr>
    
    
    
        <tr>
            <td>electjuris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of the election</td>
        </tr>
    
    
    
        <tr>
            <td>contribamt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Contribution amount (For the period of 6 months prior to 17 days before the election)</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p35-thumbnail.gif'></a><p>p. 35</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/26.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p26-thumbnail.gif'></a><p>p. 26</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F495</td>
            <td>F495</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p35-thumbnail.gif'></a><p>p. 35</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/26.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p26-thumbnail.gif'></a><p>p. 26</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
    </tbody>
    </table>
    </div>




F501502Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Candidate intention statement (Forms 501 and 502)

**Sample:** `F501_502_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F501_502_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p57-thumbnail.gif'></a><p>p. 57</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p58-thumbnail.gif'></a><p>p. 58</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p59-thumbnail.gif'></a><p>p. 59</p></div></div>




Filing Forms
^^^^^^^^^^^^
F501502Cd contains data collected from the following filing forms, form parts and schedules:



* `Form 501 <filingforms.html#form-501>`_ (Candidate Intention Statement)



* `Form 502 <filingforms.html#form-502>`_ (Campaign Bank Account Statement)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>committee_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Report Number; 000 Original; 001-999 Amended</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report is filed</td>
        </tr>
    
    
    
        <tr>
            <td>stmt_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    
        <tr>
            <td>elect_date</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Date of election</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officerholder last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officerholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>can_namm</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder middle name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Candidate/officerholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td>moniker_pos</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Location of the candidate/officeholder&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>moniker</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>cand_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Candidate/officerholder city</td>
        </tr>
    
    
    
        <tr>
            <td>cand_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Candidate/officeholder state</td>
        </tr>
    
    
    
        <tr>
            <td>cand_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder zip +4</td>
        </tr>
    
    
    
        <tr>
            <td>cand_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officeholder phone number</td>
        </tr>
    
    
    
        <tr>
            <td>cand_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Candidate/officerholder fax</td>
        </tr>
    
    
    
        <tr>
            <td>cand_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Candidate/officeholder email address</td>
        </tr>
    
    
    
        <tr>
            <td>fin_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Financial institution&#39;s business name</td>
        </tr>
    
    
    
        <tr>
            <td>fin_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s first name.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s title.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_nams</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s suffix.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Financial institution&#39;s city.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Financial institution&#39;s state.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Financial institution&#39;s zip code.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Financial institution&#39;s phone number.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Financial institution&#39;s FAX Number.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Financial institution&#39;s e-mail address.</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 80)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>agency_nam</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agency name</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>party</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Political party</td>
        </tr>
    
    
    
        <tr>
            <td>yr_of_elec</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year of election</td>
        </tr>
    
    
    
        <tr>
            <td>elec_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Election type</td>
        </tr>
    
    
    
        <tr>
            <td>execute_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Execution date</td>
        </tr>
    
    
    
        <tr>
            <td>can_sig</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate signature</td>
        </tr>
    
    
    
        <tr>
            <td>account_no</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Account number</td>
        </tr>
    
    
    
        <tr>
            <td>acct_op_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Account open date</td>
        </tr>
    
    
    
        <tr>
            <td>party_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Party code</td>
        </tr>
    
    
    
        <tr>
            <td>district_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>accept_limit_yn</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>did_exceed_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>cntrb_prsnl_fnds_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p58-thumbnail.gif'></a><p>p. 58</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR</td>
            <td>CVR</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p58-thumbnail.gif'></a><p>p. 58</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F501</td>
            <td>Form 501: Candidate Intention Statement</td>
        </tr>
    
        <tr>
            <td>F502</td>
            <td>Form 502: Campaign Bank Account Statement</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ATH</td>
            <td>Authorizing individual</td>
        </tr>
    
        <tr>
            <td>ATR</td>
            <td>Assistant treasurer</td>
        </tr>
    
        <tr>
            <td>BMC</td>
            <td>Ballot measure committee</td>
        </tr>
    
        <tr>
            <td>BNM</td>
            <td>Ballot measure&#39;s name/title</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>MDI</td>
            <td>Major Donor/Ind Expenditure</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>POF</td>
            <td>Principal officer</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>Proponent</td>
        </tr>
    
        <tr>
            <td>PTY</td>
            <td>Political Party</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SCC</td>
            <td>Small Contributor Committee</td>
        </tr>
    
        <tr>
            <td>SMO</td>
            <td>Slate-mailer organization</td>
        </tr>
    
        <tr>
            <td>SPO</td>
            <td>Sponsor</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>Treasurer</td>
        </tr>
    
        <tr>
            <td>8</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*stmt_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p6-thumbnail.gif'></a><p>p. 6</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>10001</td>
            <td>ORIGINAL/INITIAL</td>
        </tr>
    
        <tr>
            <td>10002</td>
            <td>AMENDMENT</td>
        </tr>
    
        <tr>
            <td>10003</td>
            <td>TERMINATION</td>
        </tr>
    
        <tr>
            <td>10004</td>
            <td>REDESIGNATE THE ACCOUNT FOR FUTURE ELECTION TO THE SAME OFFICE</td>
        </tr>
    
        <tr>
            <td>10005</td>
            <td>LOG</td>
        </tr>
    
        <tr>
            <td>10006</td>
            <td>LOG/AMENDMENT</td>
        </tr>
    
        <tr>
            <td>10007</td>
            <td>AS FILED BY COMMITTEE</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p20-thumbnail.gif'></a><p>p. 20</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p21-thumbnail.gif'></a><p>p. 21</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>30001</td>
            <td>PRESIDENT</td>
        </tr>
    
        <tr>
            <td>30002</td>
            <td>GOVERNOR</td>
        </tr>
    
        <tr>
            <td>30003</td>
            <td>LIEUTENANT GOVERNOR</td>
        </tr>
    
        <tr>
            <td>30004</td>
            <td>SECRETARY OF STATE</td>
        </tr>
    
        <tr>
            <td>30005</td>
            <td>CONTROLLER</td>
        </tr>
    
        <tr>
            <td>30006</td>
            <td>TREASURER</td>
        </tr>
    
        <tr>
            <td>30007</td>
            <td>ATTORNEY GENERAL</td>
        </tr>
    
        <tr>
            <td>30008</td>
            <td>SUPERINTENDENT OF PUBLIC INSTRUCTION</td>
        </tr>
    
        <tr>
            <td>30009</td>
            <td>MEMBER BOARD OF EQUALIZATION</td>
        </tr>
    
        <tr>
            <td>30010</td>
            <td>OXNARD HARBOR COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30011</td>
            <td>CITY CONTROLLER</td>
        </tr>
    
        <tr>
            <td>30012</td>
            <td>STATE SENATE</td>
        </tr>
    
        <tr>
            <td>30013</td>
            <td>ASSEMBLY</td>
        </tr>
    
        <tr>
            <td>30014</td>
            <td>INSURANCE COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30015</td>
            <td>JUDGE</td>
        </tr>
    
        <tr>
            <td>30016</td>
            <td>BOARD MEMBER</td>
        </tr>
    
        <tr>
            <td>30017</td>
            <td>TAX COLLECTOR</td>
        </tr>
    
        <tr>
            <td>30018</td>
            <td>TRUSTEE</td>
        </tr>
    
        <tr>
            <td>30019</td>
            <td>SUPERVISOR</td>
        </tr>
    
        <tr>
            <td>30020</td>
            <td>SHERIFF</td>
        </tr>
    
        <tr>
            <td>30021</td>
            <td>CORONER</td>
        </tr>
    
        <tr>
            <td>30022</td>
            <td>MARSHALL</td>
        </tr>
    
        <tr>
            <td>30023</td>
            <td>CITY CLERK</td>
        </tr>
    
        <tr>
            <td>30024</td>
            <td>SCHOOL BOARD</td>
        </tr>
    
        <tr>
            <td>30025</td>
            <td>HARBOR COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30026</td>
            <td>DISTRICT ATTORNEY</td>
        </tr>
    
        <tr>
            <td>30027</td>
            <td>COUNTY CLERK</td>
        </tr>
    
        <tr>
            <td>30028</td>
            <td>AUDITOR</td>
        </tr>
    
        <tr>
            <td>30029</td>
            <td>MAYOR</td>
        </tr>
    
        <tr>
            <td>30030</td>
            <td>CITY ATTORNEY</td>
        </tr>
    
        <tr>
            <td>30031</td>
            <td>DEMOCRATIC COUNTY CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30032</td>
            <td>TOWN COUNCIL</td>
        </tr>
    
        <tr>
            <td>30033</td>
            <td>ASSESSOR</td>
        </tr>
    
        <tr>
            <td>30034</td>
            <td>CITY TREASURER</td>
        </tr>
    
        <tr>
            <td>30035</td>
            <td>CITY COUNCIL</td>
        </tr>
    
        <tr>
            <td>30036</td>
            <td>COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30037</td>
            <td>REPUBLICAN COUNTY CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30038</td>
            <td>DIRECTOR</td>
        </tr>
    
        <tr>
            <td>30039</td>
            <td>DIRECTOR OF ZONE 7</td>
        </tr>
    
        <tr>
            <td>30040</td>
            <td>COMMUNITY COLLEGE BOARD</td>
        </tr>
    
        <tr>
            <td>30041</td>
            <td>POLICE CHIEF</td>
        </tr>
    
        <tr>
            <td>30042</td>
            <td>CHIEF OF POLICE</td>
        </tr>
    
        <tr>
            <td>30043</td>
            <td>CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30044</td>
            <td>BOARD OF EDUCATION</td>
        </tr>
    
        <tr>
            <td>30045</td>
            <td>BOARD OF DIRECTORS</td>
        </tr>
    
        <tr>
            <td>30046</td>
            <td>COLLEGE BOARD</td>
        </tr>
    
        <tr>
            <td>30047</td>
            <td>BART BOARD DIRECTOR</td>
        </tr>
    
        <tr>
            <td>30048</td>
            <td>BOARD OF TRUSTEES</td>
        </tr>
    
        <tr>
            <td>30049</td>
            <td>IRRIGATION</td>
        </tr>
    
        <tr>
            <td>30050</td>
            <td>WATER BOARD</td>
        </tr>
    
        <tr>
            <td>30051</td>
            <td>COMMUNITY PLANNING GROUP</td>
        </tr>
    
        <tr>
            <td>30052</td>
            <td>BOARD OF SUPERVISORS</td>
        </tr>
    
        <tr>
            <td>30053</td>
            <td>SUPERIOR COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>30054</td>
            <td>DISTRICT ATTORNEY/PUBLIC DEFENDER</td>
        </tr>
    
        <tr>
            <td>30055</td>
            <td>MEASURE</td>
        </tr>
    
        <tr>
            <td>30056</td>
            <td>CITY PROSECUTOR</td>
        </tr>
    
        <tr>
            <td>30057</td>
            <td>SUPREME COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>30058</td>
            <td>PUBLIC EMPLOYEES RETIREMENT BOARD</td>
        </tr>
    
        <tr>
            <td>30059</td>
            <td>APPELLATE COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>50001</td>
            <td>Ag</td>
        </tr>
    
        <tr>
            <td>50002</td>
            <td>Assembly</td>
        </tr>
    
        <tr>
            <td>50003</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>50004</td>
            <td>Assessor/Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50005</td>
            <td>Assessor/County Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50006</td>
            <td>Assessor/Recorder</td>
        </tr>
    
        <tr>
            <td>50007</td>
            <td>Associate Justice</td>
        </tr>
    
        <tr>
            <td>50008</td>
            <td>Auditor</td>
        </tr>
    
        <tr>
            <td>50009</td>
            <td>Auditor/Controller</td>
        </tr>
    
        <tr>
            <td>50010</td>
            <td>Auditor/Controller/Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50011</td>
            <td>Auditor/Controller/Recorder</td>
        </tr>
    
        <tr>
            <td>50012</td>
            <td>Auditor/Controller/Treasurer/Tax Collector</td>
        </tr>
    
        <tr>
            <td>50013</td>
            <td>Auditor/Recorder</td>
        </tr>
    
        <tr>
            <td>50014</td>
            <td>Board Member</td>
        </tr>
    
        <tr>
            <td>50015</td>
            <td>Board Of Director</td>
        </tr>
    
        <tr>
            <td>50016</td>
            <td>Board Of Supervisor</td>
        </tr>
    
        <tr>
            <td>50017</td>
            <td>Boe</td>
        </tr>
    
        <tr>
            <td>50018</td>
            <td>Chief Justice</td>
        </tr>
    
        <tr>
            <td>50019</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>50020</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>50021</td>
            <td>City Auditor</td>
        </tr>
    
        <tr>
            <td>50022</td>
            <td>City Clerk</td>
        </tr>
    
        <tr>
            <td>50023</td>
            <td>City Council</td>
        </tr>
    
        <tr>
            <td>50024</td>
            <td>City Of Los Angeles</td>
        </tr>
    
        <tr>
            <td>50025</td>
            <td>City Of South El Monte</td>
        </tr>
    
        <tr>
            <td>50026</td>
            <td>City Prosecutor</td>
        </tr>
    
        <tr>
            <td>50027</td>
            <td>City Treasurer</td>
        </tr>
    
        <tr>
            <td>50028</td>
            <td>Clerk/Auditor</td>
        </tr>
    
        <tr>
            <td>50029</td>
            <td>Clerk/Record/Public Admin</td>
        </tr>
    
        <tr>
            <td>50030</td>
            <td>Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50031</td>
            <td>Clerk/Recorder/Registar</td>
        </tr>
    
        <tr>
            <td>50032</td>
            <td>Clerk/Recorder/Registrar</td>
        </tr>
    
        <tr>
            <td>50033</td>
            <td>Commissioner</td>
        </tr>
    
        <tr>
            <td>50034</td>
            <td>Controller</td>
        </tr>
    
        <tr>
            <td>50035</td>
            <td>Costa Mesa</td>
        </tr>
    
        <tr>
            <td>50036</td>
            <td>Council Member</td>
        </tr>
    
        <tr>
            <td>50037</td>
            <td>County Clerk</td>
        </tr>
    
        <tr>
            <td>50038</td>
            <td>County Clerk/Auditor</td>
        </tr>
    
        <tr>
            <td>50039</td>
            <td>County Clerk/Auditor/Controller</td>
        </tr>
    
        <tr>
            <td>50040</td>
            <td>County Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50041</td>
            <td>County Clerk/Recorder/Assessor</td>
        </tr>
    
        <tr>
            <td>50042</td>
            <td>County Clerk/Recorder/Public Admin</td>
        </tr>
    
        <tr>
            <td>50043</td>
            <td>Democratic County Central Committee</td>
        </tr>
    
        <tr>
            <td>50044</td>
            <td>Director</td>
        </tr>
    
        <tr>
            <td>50045</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>50046</td>
            <td>District Attorney/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50047</td>
            <td>Gccc</td>
        </tr>
    
        <tr>
            <td>50048</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>50049</td>
            <td>Harbor Commissioner</td>
        </tr>
    
        <tr>
            <td>50050</td>
            <td>Ic</td>
        </tr>
    
        <tr>
            <td>50051</td>
            <td>Irrigation Dist</td>
        </tr>
    
        <tr>
            <td>50052</td>
            <td>Judge</td>
        </tr>
    
        <tr>
            <td>50053</td>
            <td>Justice</td>
        </tr>
    
        <tr>
            <td>50054</td>
            <td>Legislature</td>
        </tr>
    
        <tr>
            <td>50055</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>50056</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>50057</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>50058</td>
            <td>Placentia</td>
        </tr>
    
        <tr>
            <td>50059</td>
            <td>Public Administrator</td>
        </tr>
    
        <tr>
            <td>50060</td>
            <td>Public Administrator/Guardian</td>
        </tr>
    
        <tr>
            <td>50061</td>
            <td>Rent Stabilization Board</td>
        </tr>
    
        <tr>
            <td>50062</td>
            <td>Republican Central Committee</td>
        </tr>
    
        <tr>
            <td>50063</td>
            <td>San Francisco Dccc</td>
        </tr>
    
        <tr>
            <td>50064</td>
            <td>Sanger</td>
        </tr>
    
        <tr>
            <td>50065</td>
            <td>School Board</td>
        </tr>
    
        <tr>
            <td>50066</td>
            <td>Secretary Of State</td>
        </tr>
    
        <tr>
            <td>50067</td>
            <td>Senator</td>
        </tr>
    
        <tr>
            <td>50068</td>
            <td>Sheriff</td>
        </tr>
    
        <tr>
            <td>50069</td>
            <td>Sheriff/Coroner</td>
        </tr>
    
        <tr>
            <td>50070</td>
            <td>Sheriff/Coroner/Marshall</td>
        </tr>
    
        <tr>
            <td>50071</td>
            <td>Sheriff/Coroner/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50072</td>
            <td>Solana Beach</td>
        </tr>
    
        <tr>
            <td>50073</td>
            <td>Superintendent</td>
        </tr>
    
        <tr>
            <td>50074</td>
            <td>Supervisor</td>
        </tr>
    
        <tr>
            <td>50075</td>
            <td>Supt Of Schools</td>
        </tr>
    
        <tr>
            <td>50076</td>
            <td>Tax Collector</td>
        </tr>
    
        <tr>
            <td>50077</td>
            <td>Town Council</td>
        </tr>
    
        <tr>
            <td>50078</td>
            <td>Treasurer</td>
        </tr>
    
        <tr>
            <td>50079</td>
            <td>Treasurer/Tax Collector</td>
        </tr>
    
        <tr>
            <td>50080</td>
            <td>Treasurer/Tax Collector/Clerk</td>
        </tr>
    
        <tr>
            <td>50081</td>
            <td>Treasurer/Tax Collector/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50082</td>
            <td>Treasurer/Tax Collector/Public Administrator/County Clerk</td>
        </tr>
    
        <tr>
            <td>50083</td>
            <td>Treasurer/Tax Collector/Recorder</td>
        </tr>
    
        <tr>
            <td>50084</td>
            <td>Trustee</td>
        </tr>
    
        <tr>
            <td>50085</td>
            <td>Weed Recreation Board Member</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p19-thumbnail.gif'></a><p>p. 19</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p20-thumbnail.gif'></a><p>p. 20</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40501</td>
            <td>LOCAL</td>
        </tr>
    
        <tr>
            <td>40502</td>
            <td>STATE</td>
        </tr>
    
        <tr>
            <td>40503</td>
            <td>COUNTY</td>
        </tr>
    
        <tr>
            <td>40504</td>
            <td>MULTI-COUNTY</td>
        </tr>
    
        <tr>
            <td>40505</td>
            <td>CITY</td>
        </tr>
    
        <tr>
            <td>40507</td>
            <td>SUPERIOR COURT JUDGE</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*elec_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/3.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p3-thumbnail.gif'></a><p>p. 3</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>3001</td>
            <td>GENERAL</td>
        </tr>
    
        <tr>
            <td>3002</td>
            <td>PRIMARY</td>
        </tr>
    
        <tr>
            <td>3003</td>
            <td>RECALL</td>
        </tr>
    
        <tr>
            <td>3004</td>
            <td>SPECIAL ELECTION</td>
        </tr>
    
        <tr>
            <td>3005</td>
            <td>OFFICEHOLDER</td>
        </tr>
    
        <tr>
            <td>3006</td>
            <td>SPECIAL RUNOFF</td>
        </tr>
    
        <tr>
            <td>3007</td>
            <td>UNKNOWN</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*party_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p11-thumbnail.gif'></a><p>p. 11</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>16001</td>
            <td>DEMOCRATIC</td>
        </tr>
    
        <tr>
            <td>16002</td>
            <td>REPUBLICAN</td>
        </tr>
    
        <tr>
            <td>16003</td>
            <td>GREEN PARTY</td>
        </tr>
    
        <tr>
            <td>16004</td>
            <td>REFORM PARTY</td>
        </tr>
    
        <tr>
            <td>16005</td>
            <td>AMERICAN INDEPENDENT PARTY</td>
        </tr>
    
        <tr>
            <td>16006</td>
            <td>PEACE AND FREEDOM</td>
        </tr>
    
        <tr>
            <td>16007</td>
            <td>INDEPENDENT</td>
        </tr>
    
        <tr>
            <td>16008</td>
            <td>LIBERTARIAN</td>
        </tr>
    
        <tr>
            <td>16009</td>
            <td>NON PARTISAN</td>
        </tr>
    
        <tr>
            <td>16010</td>
            <td>NATURAL LAW</td>
        </tr>
    
        <tr>
            <td>16011</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>16012</td>
            <td>NO PARTY PREFERENCE</td>
        </tr>
    
        <tr>
            <td>16013</td>
            <td>AMERICANS ELECT</td>
        </tr>
    
        <tr>
            <td>16014</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>16020</td>
            <td>PEACE AND FREEDOM</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*district_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p13-thumbnail.gif'></a><p>p. 13</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>17001</td>
            <td>01</td>
        </tr>
    
        <tr>
            <td>17002</td>
            <td>13</td>
        </tr>
    
        <tr>
            <td>17003</td>
            <td>24</td>
        </tr>
    
        <tr>
            <td>17004</td>
            <td>35</td>
        </tr>
    
        <tr>
            <td>17005</td>
            <td>46</td>
        </tr>
    
        <tr>
            <td>17006</td>
            <td>57</td>
        </tr>
    
        <tr>
            <td>17007</td>
            <td>68</td>
        </tr>
    
        <tr>
            <td>17008</td>
            <td>79</td>
        </tr>
    
        <tr>
            <td>17009</td>
            <td>02</td>
        </tr>
    
        <tr>
            <td>17010</td>
            <td>05</td>
        </tr>
    
        <tr>
            <td>17011</td>
            <td>04</td>
        </tr>
    
        <tr>
            <td>17013</td>
            <td>06</td>
        </tr>
    
        <tr>
            <td>17014</td>
            <td>07</td>
        </tr>
    
        <tr>
            <td>17015</td>
            <td>08</td>
        </tr>
    
        <tr>
            <td>17016</td>
            <td>19</td>
        </tr>
    
        <tr>
            <td>17017</td>
            <td>10</td>
        </tr>
    
        <tr>
            <td>17018</td>
            <td>11</td>
        </tr>
    
        <tr>
            <td>17019</td>
            <td>12</td>
        </tr>
    
        <tr>
            <td>17020</td>
            <td>14</td>
        </tr>
    
        <tr>
            <td>17021</td>
            <td>15</td>
        </tr>
    
        <tr>
            <td>17022</td>
            <td>16</td>
        </tr>
    
        <tr>
            <td>17023</td>
            <td>17</td>
        </tr>
    
        <tr>
            <td>17024</td>
            <td>18</td>
        </tr>
    
        <tr>
            <td>17026</td>
            <td>20</td>
        </tr>
    
        <tr>
            <td>17027</td>
            <td>21</td>
        </tr>
    
        <tr>
            <td>17028</td>
            <td>22</td>
        </tr>
    
        <tr>
            <td>17029</td>
            <td>23</td>
        </tr>
    
        <tr>
            <td>17030</td>
            <td>25</td>
        </tr>
    
        <tr>
            <td>17031</td>
            <td>26</td>
        </tr>
    
        <tr>
            <td>17032</td>
            <td>27</td>
        </tr>
    
        <tr>
            <td>17033</td>
            <td>28</td>
        </tr>
    
        <tr>
            <td>17034</td>
            <td>29</td>
        </tr>
    
        <tr>
            <td>17035</td>
            <td>30</td>
        </tr>
    
        <tr>
            <td>17036</td>
            <td>31</td>
        </tr>
    
        <tr>
            <td>17037</td>
            <td>32</td>
        </tr>
    
        <tr>
            <td>17038</td>
            <td>33</td>
        </tr>
    
        <tr>
            <td>17039</td>
            <td>34</td>
        </tr>
    
        <tr>
            <td>17040</td>
            <td>36</td>
        </tr>
    
        <tr>
            <td>17041</td>
            <td>37</td>
        </tr>
    
        <tr>
            <td>17042</td>
            <td>38</td>
        </tr>
    
        <tr>
            <td>17043</td>
            <td>39</td>
        </tr>
    
        <tr>
            <td>17044</td>
            <td>40</td>
        </tr>
    
        <tr>
            <td>17045</td>
            <td>41</td>
        </tr>
    
        <tr>
            <td>17046</td>
            <td>42</td>
        </tr>
    
        <tr>
            <td>17047</td>
            <td>43</td>
        </tr>
    
        <tr>
            <td>17048</td>
            <td>44</td>
        </tr>
    
        <tr>
            <td>17049</td>
            <td>45</td>
        </tr>
    
        <tr>
            <td>17050</td>
            <td>47</td>
        </tr>
    
        <tr>
            <td>17051</td>
            <td>48</td>
        </tr>
    
        <tr>
            <td>17052</td>
            <td>49</td>
        </tr>
    
        <tr>
            <td>17053</td>
            <td>50</td>
        </tr>
    
        <tr>
            <td>17054</td>
            <td>51</td>
        </tr>
    
        <tr>
            <td>17055</td>
            <td>52</td>
        </tr>
    
        <tr>
            <td>17056</td>
            <td>53</td>
        </tr>
    
        <tr>
            <td>17057</td>
            <td>54</td>
        </tr>
    
        <tr>
            <td>17058</td>
            <td>55</td>
        </tr>
    
        <tr>
            <td>17059</td>
            <td>56</td>
        </tr>
    
        <tr>
            <td>17060</td>
            <td>03</td>
        </tr>
    
        <tr>
            <td>17061</td>
            <td>59</td>
        </tr>
    
        <tr>
            <td>17062</td>
            <td>60</td>
        </tr>
    
        <tr>
            <td>17063</td>
            <td>61</td>
        </tr>
    
        <tr>
            <td>17064</td>
            <td>62</td>
        </tr>
    
        <tr>
            <td>17065</td>
            <td>63</td>
        </tr>
    
        <tr>
            <td>17066</td>
            <td>64</td>
        </tr>
    
        <tr>
            <td>17067</td>
            <td>65</td>
        </tr>
    
        <tr>
            <td>17068</td>
            <td>66</td>
        </tr>
    
        <tr>
            <td>17069</td>
            <td>67</td>
        </tr>
    
        <tr>
            <td>17070</td>
            <td>69</td>
        </tr>
    
        <tr>
            <td>17071</td>
            <td>70</td>
        </tr>
    
        <tr>
            <td>17072</td>
            <td>71</td>
        </tr>
    
        <tr>
            <td>17073</td>
            <td>72</td>
        </tr>
    
        <tr>
            <td>17074</td>
            <td>73</td>
        </tr>
    
        <tr>
            <td>17075</td>
            <td>74</td>
        </tr>
    
        <tr>
            <td>17076</td>
            <td>75</td>
        </tr>
    
        <tr>
            <td>17077</td>
            <td>76</td>
        </tr>
    
        <tr>
            <td>17078</td>
            <td>77</td>
        </tr>
    
        <tr>
            <td>17079</td>
            <td>78</td>
        </tr>
    
        <tr>
            <td>17080</td>
            <td>80</td>
        </tr>
    
        <tr>
            <td>17081</td>
            <td>09</td>
        </tr>
    
        <tr>
            <td>17090</td>
            <td>58</td>
        </tr>
    
        <tr>
            <td>17012</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17082</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17025</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LoanCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Loans received and made

**Sample:** `LOAN_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOAN_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p87-thumbnail.gif'></a><p>p. 87</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p88-thumbnail.gif'></a><p>p. 88</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/89.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p89-thumbnail.gif'></a><p>p. 89</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p90-thumbnail.gif'></a><p>p. 90</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/60.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p60-thumbnail.gif'></a><p>p. 60</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p61-thumbnail.gif'></a><p>p. 61</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p62-thumbnail.gif'></a><p>p. 62</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p63-thumbnail.gif'></a><p>p. 63</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p47-thumbnail.gif'></a><p>p. 47</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/48.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p48-thumbnail.gif'></a><p>p. 48</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p49-thumbnail.gif'></a><p>p. 49</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/50.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p50-thumbnail.gif'></a><p>p. 50</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p35-thumbnail.gif'></a><p>p. 35</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/36.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p36-thumbnail.gif'></a><p>p. 36</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p37-thumbnail.gif'></a><p>p. 37</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p38-thumbnail.gif'></a><p>p. 38</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p39-thumbnail.gif'></a><p>p. 39</p></div></div>




Filing Forms
^^^^^^^^^^^^
LoanCd contains data collected from the following filing forms, form parts and schedules:



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule B - Part 1, Loans Received

    * Schedule B - Part 2, Loan Guarantors

    * Schedule B - Part 3, Outstanding Bal

    * Schedule H, Loans Made to Others

    * Schedule H - Part 1, Loans Made

    * Schedule H- Part 2, Repayments Rcvd

    * Schedule H - Part 3, Outstanding Loans





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to transaction identifier of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code describing the lender</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 2)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>intr_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Intermediary&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>intr_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Intermediary&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>intr_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>intr_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>intr_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>intr_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Intermediary&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>intr_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>lndr_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Lender&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>lndr_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Lender&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>lndr_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>lndr_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt1</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Repaid or forgiven amount; Original loan amount. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt2</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Outstanding Principal; unpaid balance. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt3</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Interest Paid; Unpaid interest; Interest received. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt4</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative Amount/Other. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt5</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt6</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt7</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>loan_amt8</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>loan_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Lender&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>loan_date1</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the loan was made or recieved. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_date2</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date repaid/forgiven; date loan due. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Loan employer. Applies to the Form 460 Schedule B Part 1.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_occ</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Loan occupation. Applies to the Form 460 Schedule B Part 1.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_rate</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Interest Rate. The content of this column varies based on the schedule/part that the record applies to. See the CAL document for a description of the value of this field.</td>
        </tr>
    
    
    
        <tr>
            <td>loan_self</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self-employed checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>loan_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Lender&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>loan_type</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Type of loan</td>
        </tr>
    
    
    
        <tr>
            <td>loan_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Lender&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LOAN</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>xref_match</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. &quot;X&quot; indicates this condition is true.</td>
        </tr>
    
    
    
        <tr>
            <td>xref_schnm</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Form 460 Schedule &#39;A&#39; or &#39;E&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p47-thumbnail.gif'></a><p>p. 47</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p35-thumbnail.gif'></a><p>p. 35</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PTY</td>
            <td>Political Party</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SCC</td>
            <td>Small Contributor Committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p47-thumbnail.gif'></a><p>p. 47</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p35-thumbnail.gif'></a><p>p. 35</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>B1</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 1, Loans Received</td>
        </tr>
    
        <tr>
            <td>B2</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 2, Loan Guarantors</td>
        </tr>
    
        <tr>
            <td>B3</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 3, Outstanding Bal</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H, Loans Made to Others</td>
        </tr>
    
        <tr>
            <td>H1</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H - Part 1, Loans Made</td>
        </tr>
    
        <tr>
            <td>H2</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H- Part 2, Repayments Rcvd</td>
        </tr>
    
        <tr>
            <td>H3</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H - Part 3, Outstanding Loans</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*loan_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p47-thumbnail.gif'></a><p>p. 47</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p35-thumbnail.gif'></a><p>p. 35</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>H2T</td>
            <td>Third party payment</td>
        </tr>
    
        <tr>
            <td>H2F</td>
            <td>Forgiven</td>
        </tr>
    
        <tr>
            <td>H2R</td>
            <td>Repay</td>
        </tr>
    
        <tr>
            <td>B2T</td>
            <td>Third party payment</td>
        </tr>
    
        <tr>
            <td>B2F</td>
            <td>Forgiven</td>
        </tr>
    
        <tr>
            <td>B2R</td>
            <td>Repay</td>
        </tr>
    
        <tr>
            <td>B1G</td>
            <td>Guarantor</td>
        </tr>
    
        <tr>
            <td>B1L</td>
            <td>Lender</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/47.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p47-thumbnail.gif'></a><p>p. 47</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p35-thumbnail.gif'></a><p>p. 35</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>LOAN</td>
            <td>LOAN</td>
        </tr>
    
    </tbody>
    </table>
    </div>




RcptCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Receipts schedules for Slate Mailer Organization and Recipient Committee
Campaign Statements (Forms 401 and 460).

**Sample:** `RCPT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/RCPT_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/118.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p118-thumbnail.gif'></a><p>p. 118</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/119.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p119-thumbnail.gif'></a><p>p. 119</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/120.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p120-thumbnail.gif'></a><p>p. 120</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/121.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p121-thumbnail.gif'></a><p>p. 121</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p71-thumbnail.gif'></a><p>p. 71</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p72-thumbnail.gif'></a><p>p. 72</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/73.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p73-thumbnail.gif'></a><p>p. 73</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p74-thumbnail.gif'></a><p>p. 74</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p75-thumbnail.gif'></a><p>p. 75</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p37-thumbnail.gif'></a><p>p. 37</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p38-thumbnail.gif'></a><p>p. 38</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p39-thumbnail.gif'></a><p>p. 39</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p40-thumbnail.gif'></a><p>p. 40</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p41-thumbnail.gif'></a><p>p. 41</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p29-thumbnail.gif'></a><p>p. 29</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p30-thumbnail.gif'></a><p>p. 30</p></div></div>




Filing Forms
^^^^^^^^^^^^
RcptCd contains data collected from the following filing forms, form parts and schedules:



* `Electronic Form 530 <filingforms.html#electronic-form-530>`_ (Electronic Issue Advocacy Report)



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule A, Monetary Contributions Received

    * Schedule A-1, Contributions Transferred to Special Election Commitee

    * Schedule C, Non-Monetary Contributions Received

    * Schedule I, miscellanous increases to cash




* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report): Part 3, Contributions > $100 Received



* `Form 900 <filingforms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount Received (Monetary, Inkkind, Promise)</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back Reference to a transaction identifier of a parent record</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s first name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name suffix. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s name prefix or title. Used on the Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee Identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Contributor&#39;s City</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_dscr</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Description of goods/services received</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Contributor&#39;s First Name</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Contributor&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_occ</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_self</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self Employed Check-box</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Contributor&#39;s State</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor&#39;s ZIP+4</td>
        </tr>
    
    
    
        <tr>
            <td>cum_oth</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative Other (Sched A, A-1)</td>
        </tr>
    
    
    
        <tr>
            <td>cum_ytd</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative year to date amount (Form 460 Schedule A and Form 401 Schedule A, A-1)</td>
        </tr>
    
    
    
        <tr>
            <td>date_thru</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items received</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office District Number (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the contributor</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>int_rate</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>intr_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Intermediary&#39;s City</td>
        </tr>
    
    
    
        <tr>
            <td>intr_cmteid</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>intr_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s Employer</td>
        </tr>
    
    
    
        <tr>
            <td>intr_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Intermediary&#39;s First Name</td>
        </tr>
    
    
    
        <tr>
            <td>intr_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Intermediary&#39;s Last Name</td>
        </tr>
    
    
    
        <tr>
            <td>intr_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s Suffix</td>
        </tr>
    
    
    
        <tr>
            <td>intr_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s Prefix or Title</td>
        </tr>
    
    
    
        <tr>
            <td>intr_occ</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Intermediary&#39;s Occupation</td>
        </tr>
    
    
    
        <tr>
            <td>intr_self</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Intermediary&#39;s self employed check box</td>
        </tr>
    
    
    
        <tr>
            <td>intr_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Intermediary&#39;s state</td>
        </tr>
    
    
    
        <tr>
            <td>intr_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Intermediary&#39;s zip code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code. See the CAL document for the list of legal values. Used on Form 401 Schedule A</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Jurisdiction Description (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag (Date/Amount are informational only)</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office Sought Description (used on F401A)</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>rcpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date item received</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tran_type</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Transaction Type</td>
        </tr>
    
    
    
        <tr>
            <td>tres_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City portion of the treasurer or responsible officer&#39;s street address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>tres_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>tres_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Treasurer or responsible officer&#39;s prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>tres_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td>tres_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Zip code portion of the treasurer or responsible officer&#39;s address</td>
        </tr>
    
    
    
        <tr>
            <td>xref_match</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Related item on other schedule has same transaction identifier. &#39;X&#39; indicates this condition is true</td>
        </tr>
    
    
    
        <tr>
            <td>xref_schnm</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Related record is included on Sched &#39;B2&#39; or &#39;F&#39;</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p37-thumbnail.gif'></a><p>p. 37</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p29-thumbnail.gif'></a><p>p. 29</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>PTY</td>
            <td>Political Party</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SCC</td>
            <td>Small Contributor Committee</td>
        </tr>
    
        <tr>
            <td>Com</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>BNM</td>
            <td>Ballot measure&#39;s name/title</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PTH</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>RFD</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>MBR</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p37-thumbnail.gif'></a><p>p. 37</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p29-thumbnail.gif'></a><p>p. 29</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>E530</td>
            <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
        </tr>
    
        <tr>
            <td>F900</td>
            <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
        </tr>
    
        <tr>
            <td>F401A</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
        </tr>
    
        <tr>
            <td>A</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
        </tr>
    
        <tr>
            <td>A-1</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule A-1, Contributions Transferred to Special Election Commitee</td>
        </tr>
    
        <tr>
            <td>C</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
        </tr>
    
        <tr>
            <td>I</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule I, miscellanous increases to cash</td>
        </tr>
    
        <tr>
            <td>F496P3</td>
            <td>Form 496 (Late Independent Expenditure Report): Part 3, Contributions &gt; $100 Received</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p40-thumbnail.gif'></a><p>p. 40</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p30-thumbnail.gif'></a><p>p. 30</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>CLB</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>CO</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SAC</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>SF</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>OR</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>AL</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>4</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CA</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p75-thumbnail.gif'></a><p>p. 75</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p40-thumbnail.gif'></a><p>p. 40</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p30-thumbnail.gif'></a><p>p. 30</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Errata-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712032/pages/Cal-Errata-201-p2-thumbnail.gif'></a><p>p. 2</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
        <tr>
            <td>asm</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>gov</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>OTh</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>oth</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>csu</td>
            <td>County Supervisor</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p29-thumbnail.gif'></a><p>p. 29</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p37-thumbnail.gif'></a><p>p. 37</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>E530</td>
            <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
        </tr>
    
        <tr>
            <td>RCPT</td>
            <td>Receipt</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sup_opp_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p40-thumbnail.gif'></a><p>p. 40</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p30-thumbnail.gif'></a><p>p. 30</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>OPPOSITION</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*tran_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p72-thumbnail.gif'></a><p>p. 72</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p38-thumbnail.gif'></a><p>p. 38</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p29-thumbnail.gif'></a><p>p. 29</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F</td>
            <td>Forgiven Loan</td>
        </tr>
    
        <tr>
            <td>I</td>
            <td>Intermediary</td>
        </tr>
    
        <tr>
            <td>R</td>
            <td>Returned (Negative Amount?)</td>
        </tr>
    
        <tr>
            <td>T</td>
            <td>Third Party Repayment</td>
        </tr>
    
        <tr>
            <td>X</td>
            <td>Transfer</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>I</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>M</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>N</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>R</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>T</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>




S401Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table contains Form 401 (Slate Mailer Organization) payment and other
disclosure schedules (F401B, F401B-1, F401C, F401D) information. Does not
include Form 401, Schedule A (Payments Received).

**Sample:** `S401_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S401_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/123.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p123-thumbnail.gif'></a><p>p. 123</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/124.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p124-thumbnail.gif'></a><p>p. 124</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p76-thumbnail.gif'></a><p>p. 76</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p77-thumbnail.gif'></a><p>p. 77</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p78-thumbnail.gif'></a><p>p. 78</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/51.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p51-thumbnail.gif'></a><p>p. 51</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/52.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p52-thumbnail.gif'></a><p>p. 52</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p39-thumbnail.gif'></a><p>p. 39</p></div></div>




Filing Forms
^^^^^^^^^^^^
S401Cd contains data collected from the following filing forms, form parts and schedules:



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)

    * Schedule B, Payments Made

    * Schedule B-1, Payments Made by Agent or Independent Contractor

    * Schedule C, Persons Receiving $1,000 or More

    * Schedule D, Candidates and Measures Not Listed on Schedule A





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>No</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S401</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>agent_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>agent_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>agent_namt</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>agent_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Agent or independent contractor&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>payee_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee&#39;s business name or last name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee&#39;s first name if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s title or prefix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee&#39;s suffix if the payee is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>payee_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee&#39;s city address</td>
        </tr>
    
    
    
        <tr>
            <td>payee_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee state address</td>
        </tr>
    
    
    
        <tr>
            <td>payee_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount (Sched F401B, 401B-1, 401C)</td>
        </tr>
    
    
    
        <tr>
            <td>aggregate</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Aggregate year-to-date amount (Sched 401C)</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in the TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to transaction identifier of parent record</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/51.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p51-thumbnail.gif'></a><p>p. 51</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p39-thumbnail.gif'></a><p>p. 39</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S401</td>
            <td>S401</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/51.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p51-thumbnail.gif'></a><p>p. 51</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p39-thumbnail.gif'></a><p>p. 39</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F401B</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
        </tr>
    
        <tr>
            <td>F401B-1</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
        </tr>
    
        <tr>
            <td>F401C</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule C, Persons Receiving $1,000 or More</td>
        </tr>
    
        <tr>
            <td>F401D</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule D, Candidates and Measures Not Listed on Schedule A</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Errata-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712032/pages/Cal-Errata-201-p2-thumbnail.gif'></a><p>p. 2</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
        <tr>
            <td>asm</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ltg</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>OTh</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>att</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>oth</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>tre</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>con</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>boe</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>sos</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>sup</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p77-thumbnail.gif'></a><p>p. 77</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/52.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p52-thumbnail.gif'></a><p>p. 52</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p39-thumbnail.gif'></a><p>p. 39</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/52.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p52-thumbnail.gif'></a><p>p. 52</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p39-thumbnail.gif'></a><p>p. 39</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sup_opp_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/52.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p52-thumbnail.gif'></a><p>p. 52</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p39-thumbnail.gif'></a><p>p. 39</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>OPPOSITION</td>
        </tr>
    
    </tbody>
    </table>
    </div>




S496Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Form 496 Late Independent Expenditures

**Sample:** `S496_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S496_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/124.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p124-thumbnail.gif'></a><p>p. 124</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/125.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p125-thumbnail.gif'></a><p>p. 125</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p53-thumbnail.gif'></a><p>p. 53</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p40-thumbnail.gif'></a><p>p. 40</p></div></div>




Filing Forms
^^^^^^^^^^^^
S496Cd contains data collected from the following filing forms, form parts and schedules:



* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S496</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Expenditure amount</td>
        </tr>
    
    
    
        <tr>
            <td>exp_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Expenditure dates</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>date_thru</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items paid</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p53-thumbnail.gif'></a><p>p. 53</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p40-thumbnail.gif'></a><p>p. 40</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S496</td>
            <td>S496</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p53-thumbnail.gif'></a><p>p. 53</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/40.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p40-thumbnail.gif'></a><p>p. 40</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
    </tbody>
    </table>
    </div>




S497Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Form 497: Late Contributions Received/Made

**Sample:** `S497_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S497_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/125.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p125-thumbnail.gif'></a><p>p. 125</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/126.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p126-thumbnail.gif'></a><p>p. 126</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/127.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p127-thumbnail.gif'></a><p>p. 127</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p80-thumbnail.gif'></a><p>p. 80</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/81.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p81-thumbnail.gif'></a><p>p. 81</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p54-thumbnail.gif'></a><p>p. 54</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/55.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p55-thumbnail.gif'></a><p>p. 55</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p41-thumbnail.gif'></a><p>p. 41</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p42-thumbnail.gif'></a><p>p. 42</p></div></div>




Filing Forms
^^^^^^^^^^^^
S497Cd contains data collected from the following filing forms, form parts and schedules:



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)

    * Part 1, Contribution(s) Received

    * Part 2, Contribution(s) Made





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S497</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 6)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Name title or prefix of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Name suffix of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>City address of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>State address of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>enty_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code of Contributor/Recipient</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer of Contributor (populated for some Recipients as well)</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_occ</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Occupation of Contributor (populated for some Recipients as well)</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_self</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Contributor self-employed checkbox. &quot;X&quot; indicates the contributor is self-employed.</td>
        </tr>
    
    
    
        <tr>
            <td>elec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of election</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date item received/made</td>
        </tr>
    
    
    
        <tr>
            <td>date_thru</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>End of date range for items received</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount received/made</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Jurisdiction code describing the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Ballot measure jurisdiction</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in TEXT code</td>
        </tr>
    
    
    
        <tr>
            <td>bal_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>cand_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>sup_off_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p54-thumbnail.gif'></a><p>p. 54</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p41-thumbnail.gif'></a><p>p. 41</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S497</td>
            <td>S497</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p54-thumbnail.gif'></a><p>p. 54</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p41-thumbnail.gif'></a><p>p. 41</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F497P1</td>
            <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
        </tr>
    
        <tr>
            <td>F497P2</td>
            <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p54-thumbnail.gif'></a><p>p. 54</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/41.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p41-thumbnail.gif'></a><p>p. 41</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>BNM</td>
            <td>Ballot measure&#39;s name/title</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled committee</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>com</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PTY</td>
            <td>Political Party</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SCC</td>
            <td>Small Contributor Committee</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Errata-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712032/pages/Cal-Errata-201-p2-thumbnail.gif'></a><p>p. 2</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
        <tr>
            <td>asm</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>sen</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>Asm</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>May</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>ASm</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>oth</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>csu</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>Oth</td>
            <td>Other</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/55.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p55-thumbnail.gif'></a><p>p. 55</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p42-thumbnail.gif'></a><p>p. 42</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>asm</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>sen</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>cit</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>CLB</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>IRV</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>Fon</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>JRS</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>CO</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>Riv</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>SNE</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>83</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FED</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>CA</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>JR</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/55.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p55-thumbnail.gif'></a><p>p. 55</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/42.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p42-thumbnail.gif'></a><p>p. 42</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>s</td>
            <td>SOUGHT</td>
        </tr>
    
        <tr>
            <td>h</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>T</td>
            <td>UNKNOWN</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sup_opp_cd*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p82-thumbnail.gif'></a><p>p. 82</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>O</td>
            <td>OPPOSITION</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SUPPORT</td>
        </tr>
    
    </tbody>
    </table>
    </div>




S498Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Form 498: Slate Mailer Late Independent Expenditures Made

**Sample:** `S498_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/S498_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/127.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p127-thumbnail.gif'></a><p>p. 127</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/128.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p128-thumbnail.gif'></a><p>p. 128</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/129.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p129-thumbnail.gif'></a><p>p. 129</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/83.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p83-thumbnail.gif'></a><p>p. 83</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/84.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p84-thumbnail.gif'></a><p>p. 84</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/85.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p85-thumbnail.gif'></a><p>p. 85</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p56-thumbnail.gif'></a><p>p. 56</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p57-thumbnail.gif'></a><p>p. 57</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p43-thumbnail.gif'></a><p>p. 43</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p44-thumbnail.gif'></a><p>p. 44</p></div></div>




Filing Forms
^^^^^^^^^^^^
S498Cd contains data collected from the following filing forms, form parts and schedules:



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)

    * Part A, Late Payments Attributed To

    * Part R, Late Payments Received From





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: S498</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>payor_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payor&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>payor_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payor&#39;s first name.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s Prefix or title.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s suffix.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payor&#39;s city.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payor&#39;s State.</td>
        </tr>
    
    
    
        <tr>
            <td>payor_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payor&#39;s zip code</td>
        </tr>
    
    
    
        <tr>
            <td>date_rcvd</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date received</td>
        </tr>
    
    
    
        <tr>
            <td>amt_rcvd</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Candidate/officerholder last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Candidate/officerholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officerholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officerholder suffix</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Description of office sought</td>
        </tr>
    
    
    
        <tr>
            <td>juris_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office jurisdiction code</td>
        </tr>
    
    
    
        <tr>
            <td>juris_dscr</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Office jurisdiction description</td>
        </tr>
    
    
    
        <tr>
            <td>dist_no</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>District number for the office being sought. Populated for Senate, Assembly, or Board of Equalization races.</td>
        </tr>
    
    
    
        <tr>
            <td>off_s_h_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>bal_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Ballot measure name</td>
        </tr>
    
    
    
        <tr>
            <td>bal_num</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Ballot measure number or letter.</td>
        </tr>
    
    
    
        <tr>
            <td>bal_juris</td>
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Jurisdiction of ballot measure</td>
        </tr>
    
    
    
        <tr>
            <td>sup_opp_cd</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Support or opposition code</td>
        </tr>
    
    
    
        <tr>
            <td>amt_attrib</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount attributed (only if Form_type = &#39;F498-A&#39;)</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flat</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference text contained in TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>employer</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>occupation</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>selfemp_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self-employed checkbox</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p56-thumbnail.gif'></a><p>p. 56</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p43-thumbnail.gif'></a><p>p. 43</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S498</td>
            <td>S498</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p56-thumbnail.gif'></a><p>p. 56</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p43-thumbnail.gif'></a><p>p. 43</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F498-A</td>
            <td>Form 498 (Slate Mailer Late Payment Report): Part A, Late Payments Attributed To</td>
        </tr>
    
        <tr>
            <td>F498-R</td>
            <td>Form 498 (Slate Mailer Late Payment Report): Part R, Late Payments Received From</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p56-thumbnail.gif'></a><p>p. 56</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p43-thumbnail.gif'></a><p>p. 43</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


*Cal-Errata-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712032-Cal-Errata-201/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712032/pages/Cal-Errata-201-p2-thumbnail.gif'></a><p>p. 2</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p12-thumbnail.gif'></a><p>p. 12</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p10-thumbnail.gif'></a><p>p. 10</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>APP</td>
            <td>State Appellate Court Justice</td>
        </tr>
    
        <tr>
            <td>ASM</td>
            <td>State Assembly Person</td>
        </tr>
    
        <tr>
            <td>ASR</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>ATT</td>
            <td>Attorney General</td>
        </tr>
    
        <tr>
            <td>BED</td>
            <td>Board of Education</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization Member</td>
        </tr>
    
        <tr>
            <td>BSU</td>
            <td>Board of Supervisors</td>
        </tr>
    
        <tr>
            <td>CAT</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>CCB</td>
            <td>Community College Board</td>
        </tr>
    
        <tr>
            <td>CCM</td>
            <td>City Council Member</td>
        </tr>
    
        <tr>
            <td>CON</td>
            <td>State Controller</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County Counsel</td>
        </tr>
    
        <tr>
            <td>CSU</td>
            <td>County Supervisor</td>
        </tr>
    
        <tr>
            <td>CTR</td>
            <td>Local Controller</td>
        </tr>
    
        <tr>
            <td>DAT</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>INS</td>
            <td>Insurance Commissioner</td>
        </tr>
    
        <tr>
            <td>LTG</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>MAY</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PDR</td>
            <td>Public Defender</td>
        </tr>
    
        <tr>
            <td>PER</td>
            <td>Public Employees Retirement System</td>
        </tr>
    
        <tr>
            <td>PLN</td>
            <td>Planning Commissioner</td>
        </tr>
    
        <tr>
            <td>SCJ</td>
            <td>Superior Court Judge</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>State Senator</td>
        </tr>
    
        <tr>
            <td>SHC</td>
            <td>Sheriff-Coroner</td>
        </tr>
    
        <tr>
            <td>SOS</td>
            <td>Secretary of State</td>
        </tr>
    
        <tr>
            <td>SPM</td>
            <td>Supreme Court Justice</td>
        </tr>
    
        <tr>
            <td>SUP</td>
            <td>Superintendent of Public Instruction</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>State Treasurer</td>
        </tr>
    
        <tr>
            <td>TRS</td>
            <td>Local Treasurer</td>
        </tr>
    
        <tr>
            <td>gov</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>oth</td>
            <td>Other</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*juris_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p57-thumbnail.gif'></a><p>p. 57</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p43-thumbnail.gif'></a><p>p. 43</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ASM</td>
            <td>Assembly District</td>
        </tr>
    
        <tr>
            <td>BOE</td>
            <td>Board of Equalization District</td>
        </tr>
    
        <tr>
            <td>CIT</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>CTY</td>
            <td>County</td>
        </tr>
    
        <tr>
            <td>LOC</td>
            <td>Local</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>SEN</td>
            <td>Senate District</td>
        </tr>
    
        <tr>
            <td>STW</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Statewide</td>
        </tr>
    
        <tr>
            <td>COU</td>
            <td>County</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*off_s_h_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p57-thumbnail.gif'></a><p>p. 57</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p44-thumbnail.gif'></a><p>p. 44</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>H</td>
            <td>HELD</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SOUGHT</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sup_opp_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p57-thumbnail.gif'></a><p>p. 57</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p43-thumbnail.gif'></a><p>p. 43</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>O</td>
            <td>OPPOSITION</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SUPPORT</td>
        </tr>
    
    </tbody>
    </table>
    </div>





Common tables
---------------------------


CvrE530Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table method is undocumented.

**Sample:** `CVR_E530_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_E530_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/29.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p29-thumbnail.gif'></a><p>p. 29</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/30.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p30-thumbnail.gif'></a><p>p. 30</p></div></div>




Filing Forms
^^^^^^^^^^^^
CvrE530Cd contains data collected from the following filing forms, form parts and schedules:



* `Electronic Form 530 <filingforms.html#electronic-form-530>`_ (Electronic Issue Advocacy Report)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filer_city</td>
            <td>String (up to 16)</td>
            <td>No</td>
            <td>Filer city</td>
        </tr>
    
    
    
        <tr>
            <td>filer_st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>filer_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>occupation</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>employer</td>
            <td>String (up to 13)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>cand_naml</td>
            <td>String (up to 46)</td>
            <td>No</td>
            <td>Candidate last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 21)</td>
            <td>No</td>
            <td>Candidate first name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Candidate title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Candidate suffix</td>
        </tr>
    
    
    
        <tr>
            <td>district_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>pmnt_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>pmnt_amount</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_literature</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_printads</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_radio</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_tv</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_it</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_billboards</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>type_other</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>other_desc</td>
            <td>String (up to 49)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR</td>
            <td>CVR</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>E530</td>
            <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p11-thumbnail.gif'></a><p>p. 11</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p9-thumbnail.gif'></a><p>p. 9</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ATH</td>
            <td>Authorizing individual</td>
        </tr>
    
        <tr>
            <td>ATR</td>
            <td>Assistant treasurer</td>
        </tr>
    
        <tr>
            <td>BMC</td>
            <td>Ballot measure committee</td>
        </tr>
    
        <tr>
            <td>BNM</td>
            <td>Ballot measure&#39;s name/title</td>
        </tr>
    
        <tr>
            <td>CAO</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled committee</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>MDI</td>
            <td>Major Donor/Ind Expenditure</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>POF</td>
            <td>Principal officer</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>Proponent</td>
        </tr>
    
        <tr>
            <td>PTY</td>
            <td>Political Party</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SCC</td>
            <td>Small Contributor Committee</td>
        </tr>
    
        <tr>
            <td>SMO</td>
            <td>Slate-mailer organization</td>
        </tr>
    
        <tr>
            <td>SPO</td>
            <td>Sponsor</td>
        </tr>
    
        <tr>
            <td>TRE</td>
            <td>Treasurer</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*office_cd*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>30001</td>
            <td>PRESIDENT</td>
        </tr>
    
        <tr>
            <td>30002</td>
            <td>GOVERNOR</td>
        </tr>
    
        <tr>
            <td>30003</td>
            <td>LIEUTENANT GOVERNOR</td>
        </tr>
    
        <tr>
            <td>30004</td>
            <td>SECRETARY OF STATE</td>
        </tr>
    
        <tr>
            <td>30005</td>
            <td>CONTROLLER</td>
        </tr>
    
        <tr>
            <td>30006</td>
            <td>TREASURER</td>
        </tr>
    
        <tr>
            <td>30007</td>
            <td>ATTORNEY GENERAL</td>
        </tr>
    
        <tr>
            <td>30008</td>
            <td>SUPERINTENDENT OF PUBLIC INSTRUCTION</td>
        </tr>
    
        <tr>
            <td>30009</td>
            <td>MEMBER BOARD OF EQUALIZATION</td>
        </tr>
    
        <tr>
            <td>30010</td>
            <td>OXNARD HARBOR COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30011</td>
            <td>CITY CONTROLLER</td>
        </tr>
    
        <tr>
            <td>30012</td>
            <td>STATE SENATE</td>
        </tr>
    
        <tr>
            <td>30013</td>
            <td>ASSEMBLY</td>
        </tr>
    
        <tr>
            <td>30014</td>
            <td>INSURANCE COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30015</td>
            <td>JUDGE</td>
        </tr>
    
        <tr>
            <td>30016</td>
            <td>BOARD MEMBER</td>
        </tr>
    
        <tr>
            <td>30017</td>
            <td>TAX COLLECTOR</td>
        </tr>
    
        <tr>
            <td>30018</td>
            <td>TRUSTEE</td>
        </tr>
    
        <tr>
            <td>30019</td>
            <td>SUPERVISOR</td>
        </tr>
    
        <tr>
            <td>30020</td>
            <td>SHERIFF</td>
        </tr>
    
        <tr>
            <td>30021</td>
            <td>CORONER</td>
        </tr>
    
        <tr>
            <td>30022</td>
            <td>MARSHALL</td>
        </tr>
    
        <tr>
            <td>30023</td>
            <td>CITY CLERK</td>
        </tr>
    
        <tr>
            <td>30024</td>
            <td>SCHOOL BOARD</td>
        </tr>
    
        <tr>
            <td>30025</td>
            <td>HARBOR COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30026</td>
            <td>DISTRICT ATTORNEY</td>
        </tr>
    
        <tr>
            <td>30027</td>
            <td>COUNTY CLERK</td>
        </tr>
    
        <tr>
            <td>30028</td>
            <td>AUDITOR</td>
        </tr>
    
        <tr>
            <td>30029</td>
            <td>MAYOR</td>
        </tr>
    
        <tr>
            <td>30030</td>
            <td>CITY ATTORNEY</td>
        </tr>
    
        <tr>
            <td>30031</td>
            <td>DEMOCRATIC COUNTY CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30032</td>
            <td>TOWN COUNCIL</td>
        </tr>
    
        <tr>
            <td>30033</td>
            <td>ASSESSOR</td>
        </tr>
    
        <tr>
            <td>30034</td>
            <td>CITY TREASURER</td>
        </tr>
    
        <tr>
            <td>30035</td>
            <td>CITY COUNCIL</td>
        </tr>
    
        <tr>
            <td>30036</td>
            <td>COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30037</td>
            <td>REPUBLICAN COUNTY CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30038</td>
            <td>DIRECTOR</td>
        </tr>
    
        <tr>
            <td>30039</td>
            <td>DIRECTOR OF ZONE 7</td>
        </tr>
    
        <tr>
            <td>30040</td>
            <td>COMMUNITY COLLEGE BOARD</td>
        </tr>
    
        <tr>
            <td>30041</td>
            <td>POLICE CHIEF</td>
        </tr>
    
        <tr>
            <td>30042</td>
            <td>CHIEF OF POLICE</td>
        </tr>
    
        <tr>
            <td>30043</td>
            <td>CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30044</td>
            <td>BOARD OF EDUCATION</td>
        </tr>
    
        <tr>
            <td>30045</td>
            <td>BOARD OF DIRECTORS</td>
        </tr>
    
        <tr>
            <td>30046</td>
            <td>COLLEGE BOARD</td>
        </tr>
    
        <tr>
            <td>30047</td>
            <td>BART BOARD DIRECTOR</td>
        </tr>
    
        <tr>
            <td>30048</td>
            <td>BOARD OF TRUSTEES</td>
        </tr>
    
        <tr>
            <td>30049</td>
            <td>IRRIGATION</td>
        </tr>
    
        <tr>
            <td>30050</td>
            <td>WATER BOARD</td>
        </tr>
    
        <tr>
            <td>30051</td>
            <td>COMMUNITY PLANNING GROUP</td>
        </tr>
    
        <tr>
            <td>30052</td>
            <td>BOARD OF SUPERVISORS</td>
        </tr>
    
        <tr>
            <td>30053</td>
            <td>SUPERIOR COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>30054</td>
            <td>DISTRICT ATTORNEY/PUBLIC DEFENDER</td>
        </tr>
    
        <tr>
            <td>30055</td>
            <td>MEASURE</td>
        </tr>
    
        <tr>
            <td>30056</td>
            <td>CITY PROSECUTOR</td>
        </tr>
    
        <tr>
            <td>30057</td>
            <td>SUPREME COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>30058</td>
            <td>PUBLIC EMPLOYEES RETIREMENT BOARD</td>
        </tr>
    
        <tr>
            <td>30059</td>
            <td>APPELLATE COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>50001</td>
            <td>Ag</td>
        </tr>
    
        <tr>
            <td>50002</td>
            <td>Assembly</td>
        </tr>
    
        <tr>
            <td>50003</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>50004</td>
            <td>Assessor/Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50005</td>
            <td>Assessor/County Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50006</td>
            <td>Assessor/Recorder</td>
        </tr>
    
        <tr>
            <td>50007</td>
            <td>Associate Justice</td>
        </tr>
    
        <tr>
            <td>50008</td>
            <td>Auditor</td>
        </tr>
    
        <tr>
            <td>50009</td>
            <td>Auditor/Controller</td>
        </tr>
    
        <tr>
            <td>50010</td>
            <td>Auditor/Controller/Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50011</td>
            <td>Auditor/Controller/Recorder</td>
        </tr>
    
        <tr>
            <td>50012</td>
            <td>Auditor/Controller/Treasurer/Tax Collector</td>
        </tr>
    
        <tr>
            <td>50013</td>
            <td>Auditor/Recorder</td>
        </tr>
    
        <tr>
            <td>50014</td>
            <td>Board Member</td>
        </tr>
    
        <tr>
            <td>50015</td>
            <td>Board Of Director</td>
        </tr>
    
        <tr>
            <td>50016</td>
            <td>Board Of Supervisor</td>
        </tr>
    
        <tr>
            <td>50017</td>
            <td>Boe</td>
        </tr>
    
        <tr>
            <td>50018</td>
            <td>Chief Justice</td>
        </tr>
    
        <tr>
            <td>50019</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>50020</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>50021</td>
            <td>City Auditor</td>
        </tr>
    
        <tr>
            <td>50022</td>
            <td>City Clerk</td>
        </tr>
    
        <tr>
            <td>50023</td>
            <td>City Council</td>
        </tr>
    
        <tr>
            <td>50024</td>
            <td>City Of Los Angeles</td>
        </tr>
    
        <tr>
            <td>50025</td>
            <td>City Of South El Monte</td>
        </tr>
    
        <tr>
            <td>50026</td>
            <td>City Prosecutor</td>
        </tr>
    
        <tr>
            <td>50027</td>
            <td>City Treasurer</td>
        </tr>
    
        <tr>
            <td>50028</td>
            <td>Clerk/Auditor</td>
        </tr>
    
        <tr>
            <td>50029</td>
            <td>Clerk/Record/Public Admin</td>
        </tr>
    
        <tr>
            <td>50030</td>
            <td>Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50031</td>
            <td>Clerk/Recorder/Registar</td>
        </tr>
    
        <tr>
            <td>50032</td>
            <td>Clerk/Recorder/Registrar</td>
        </tr>
    
        <tr>
            <td>50033</td>
            <td>Commissioner</td>
        </tr>
    
        <tr>
            <td>50034</td>
            <td>Controller</td>
        </tr>
    
        <tr>
            <td>50035</td>
            <td>Costa Mesa</td>
        </tr>
    
        <tr>
            <td>50036</td>
            <td>Council Member</td>
        </tr>
    
        <tr>
            <td>50037</td>
            <td>County Clerk</td>
        </tr>
    
        <tr>
            <td>50038</td>
            <td>County Clerk/Auditor</td>
        </tr>
    
        <tr>
            <td>50039</td>
            <td>County Clerk/Auditor/Controller</td>
        </tr>
    
        <tr>
            <td>50040</td>
            <td>County Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50041</td>
            <td>County Clerk/Recorder/Assessor</td>
        </tr>
    
        <tr>
            <td>50042</td>
            <td>County Clerk/Recorder/Public Admin</td>
        </tr>
    
        <tr>
            <td>50043</td>
            <td>Democratic County Central Committee</td>
        </tr>
    
        <tr>
            <td>50044</td>
            <td>Director</td>
        </tr>
    
        <tr>
            <td>50045</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>50046</td>
            <td>District Attorney/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50047</td>
            <td>Gccc</td>
        </tr>
    
        <tr>
            <td>50048</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>50049</td>
            <td>Harbor Commissioner</td>
        </tr>
    
        <tr>
            <td>50050</td>
            <td>Ic</td>
        </tr>
    
        <tr>
            <td>50051</td>
            <td>Irrigation Dist</td>
        </tr>
    
        <tr>
            <td>50052</td>
            <td>Judge</td>
        </tr>
    
        <tr>
            <td>50053</td>
            <td>Justice</td>
        </tr>
    
        <tr>
            <td>50054</td>
            <td>Legislature</td>
        </tr>
    
        <tr>
            <td>50055</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>50056</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>50057</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>50058</td>
            <td>Placentia</td>
        </tr>
    
        <tr>
            <td>50059</td>
            <td>Public Administrator</td>
        </tr>
    
        <tr>
            <td>50060</td>
            <td>Public Administrator/Guardian</td>
        </tr>
    
        <tr>
            <td>50061</td>
            <td>Rent Stabilization Board</td>
        </tr>
    
        <tr>
            <td>50062</td>
            <td>Republican Central Committee</td>
        </tr>
    
        <tr>
            <td>50063</td>
            <td>San Francisco Dccc</td>
        </tr>
    
        <tr>
            <td>50064</td>
            <td>Sanger</td>
        </tr>
    
        <tr>
            <td>50065</td>
            <td>School Board</td>
        </tr>
    
        <tr>
            <td>50066</td>
            <td>Secretary Of State</td>
        </tr>
    
        <tr>
            <td>50067</td>
            <td>Senator</td>
        </tr>
    
        <tr>
            <td>50068</td>
            <td>Sheriff</td>
        </tr>
    
        <tr>
            <td>50069</td>
            <td>Sheriff/Coroner</td>
        </tr>
    
        <tr>
            <td>50070</td>
            <td>Sheriff/Coroner/Marshall</td>
        </tr>
    
        <tr>
            <td>50071</td>
            <td>Sheriff/Coroner/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50072</td>
            <td>Solana Beach</td>
        </tr>
    
        <tr>
            <td>50073</td>
            <td>Superintendent</td>
        </tr>
    
        <tr>
            <td>50074</td>
            <td>Supervisor</td>
        </tr>
    
        <tr>
            <td>50075</td>
            <td>Supt Of Schools</td>
        </tr>
    
        <tr>
            <td>50076</td>
            <td>Tax Collector</td>
        </tr>
    
        <tr>
            <td>50077</td>
            <td>Town Council</td>
        </tr>
    
        <tr>
            <td>50078</td>
            <td>Treasurer</td>
        </tr>
    
        <tr>
            <td>50079</td>
            <td>Treasurer/Tax Collector</td>
        </tr>
    
        <tr>
            <td>50080</td>
            <td>Treasurer/Tax Collector/Clerk</td>
        </tr>
    
        <tr>
            <td>50081</td>
            <td>Treasurer/Tax Collector/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50082</td>
            <td>Treasurer/Tax Collector/Public Administrator/County Clerk</td>
        </tr>
    
        <tr>
            <td>50083</td>
            <td>Treasurer/Tax Collector/Recorder</td>
        </tr>
    
        <tr>
            <td>50084</td>
            <td>Trustee</td>
        </tr>
    
        <tr>
            <td>50085</td>
            <td>Weed Recreation Board Member</td>
        </tr>
    
    </tbody>
    </table>
    </div>




FilerFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Key table that links filers to their paper, key data entry, legacy,
and electronic filings. This table is used as an index to locate
filing information.

**Sample:** `FILER_FILINGS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_FILINGS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p64-thumbnail.gif'></a><p>p. 64</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p65-thumbnail.gif'></a><p>p. 65</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p66-thumbnail.gif'></a><p>p. 66</p></div></div>




Filing Forms
^^^^^^^^^^^^
FilerFilingsCd contains data collected from the following filing forms, form parts and schedules:



* `Electronic Form 530 <filingforms.html#electronic-form-530>`_ (Electronic Issue Advocacy Report)



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 402 <filingforms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization))



* `Form 405 <filingforms.html#form-405>`_ (Amendment to Campaign Disclosure Statement)



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 415 <filingforms.html#form-415>`_ (Title Unknown)



* `Form 416 <filingforms.html#form-416>`_ (Title Unknown)



* `Form 419 <filingforms.html#form-419>`_ (Ballot Measure Committee Campaign Statement-Long Form)



* `Form 420 <filingforms.html#form-420>`_ (Recipient Committee Campaign Statement-Long Form)



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 430 <filingforms.html#form-430>`_ (Title Unknown)



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 470 <filingforms.html#form-470>`_ (Officeholder and Candidate Campaign Statement, Short Form)



* `Form 490 <filingforms.html#form-490>`_ (Officeholder/Candidate Campaign Statement-Long Form)



* `Form 495 <filingforms.html#form-495>`_ (Supplemental Pre-Election Campaign Statement)



* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 501 <filingforms.html#form-501>`_ (Candidate Intention Statement)



* `Form 502 <filingforms.html#form-502>`_ (Campaign Bank Account Statement)



* `Form 511 <filingforms.html#form-511>`_ (Paid Spokesperson Report)



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 605 <filingforms.html#form-605>`_ (Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)



* `Form 690 <filingforms.html#form-690>`_ (Amendment to Lobbying Disclosure Report)



* `Form 700 <filingforms.html#form-700>`_ (Statement of Economic Interest)



* `Form 900 <filingforms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)



* `Schedule 630 <filingforms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <filingforms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <filingforms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>period_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identifies the period when the filing was recieved.</td>
        </tr>
    
    
    
        <tr>
            <td>form_id</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td>filing_sequence</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment number where 0 is an original filing and 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td>filing_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the filing entered into the system</td>
        </tr>
    
    
    
        <tr>
            <td>stmnt_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td>stmnt_status</td>
            <td>Integer</td>
            <td>No</td>
            <td>The status of the statement. If the filing has been reviewed or not reviewed.</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>user_id</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>User identifier of the PRD user who logged the filing</td>
        </tr>
    
    
    
        <tr>
            <td>special_audit</td>
            <td>Integer</td>
            <td>No</td>
            <td>Denotes whether the filing has been audited for money laundering or other special condition.</td>
        </tr>
    
    
    
        <tr>
            <td>fine_audit</td>
            <td>Integer</td>
            <td>No</td>
            <td>Indicates whether a filing has been audited for a fine</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_start</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the filing represents</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_end</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the filing represents</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date filing received</td>
        </tr>
    
    
    
        <tr>
            <td>filing_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>The type of filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_id*


*CalAccessTablesWeb*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F400</td>
            <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F401</td>
            <td>Form 401: Slate Mailer Organization Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F402</td>
            <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F405</td>
            <td>Form 405: Amendment to Campaign Disclosure Statement</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410: Statement of Organization Recipient Committee</td>
        </tr>
    
        <tr>
            <td>F415</td>
            <td>Form 415: Title Unknown</td>
        </tr>
    
        <tr>
            <td>F416</td>
            <td>Form 416: Title Unknown</td>
        </tr>
    
        <tr>
            <td>F419</td>
            <td>Form 419: Ballot Measure Committee Campaign Statement-Long Form</td>
        </tr>
    
        <tr>
            <td>F420</td>
            <td>Form 420: Recipient Committee Campaign Statement-Long Form</td>
        </tr>
    
        <tr>
            <td>F425</td>
            <td>Form 425: Semi-Annual Statement of no Activity</td>
        </tr>
    
        <tr>
            <td>F430</td>
            <td>Form 430: Title Unknown</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F470</td>
            <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
        </tr>
    
        <tr>
            <td>F490</td>
            <td>Form 490: Officeholder/Candidate Campaign Statement-Long Form</td>
        </tr>
    
        <tr>
            <td>F495</td>
            <td>Form 495: Supplemental Pre-Election Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>F498</td>
            <td>Form 498: Slate Mailer Late Payment Report</td>
        </tr>
    
        <tr>
            <td>F501</td>
            <td>Form 501: Candidate Intention Statement</td>
        </tr>
    
        <tr>
            <td>F502</td>
            <td>Form 502: Campaign Bank Account Statement</td>
        </tr>
    
        <tr>
            <td>F511</td>
            <td>Form 511: Paid Spokesperson Report</td>
        </tr>
    
        <tr>
            <td>E530</td>
            <td>Electronic Form 530: Electronic Issue Advocacy Report</td>
        </tr>
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F602</td>
            <td>Form 602: Lobbying Firm Activity Authorization</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
        <tr>
            <td>F604</td>
            <td>Form 604: Lobbyist Certification Statement</td>
        </tr>
    
        <tr>
            <td>F605</td>
            <td>Form 605: Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F606</td>
            <td>Form 606: Notice of Termination</td>
        </tr>
    
        <tr>
            <td>F607</td>
            <td>Form 607: Notice of Withdrawal</td>
        </tr>
    
        <tr>
            <td>F615</td>
            <td>Form 615: Lobbyist Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>S630</td>
            <td>Schedule 630: Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) </td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>S635-C</td>
            <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
        </tr>
    
        <tr>
            <td>S640</td>
            <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
        <tr>
            <td>F690</td>
            <td>Form 690: Amendment to Lobbying Disclosure Report</td>
        </tr>
    
        <tr>
            <td>F700</td>
            <td>Form 700: Statement of Economic Interest</td>
        </tr>
    
        <tr>
            <td>F900</td>
            <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
        </tr>
    
        <tr>
            <td>F111</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F410 AT</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F410ATR</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F421</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F440</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F470S</td>
            <td>Form 470: Officeholder and Candidate Campaign Statement, Short Form</td>
        </tr>
    
        <tr>
            <td>F480</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F500</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F501502</td>
            <td>Forms 501 and/or 502 (Candidate Intention and/or Bank Account Statements)</td>
        </tr>
    
        <tr>
            <td>F555</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F666</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F777</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F888</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F999</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*stmnt_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p6-thumbnail.gif'></a><p>p. 6</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>10001</td>
            <td>ORIGINAL/INITIAL</td>
        </tr>
    
        <tr>
            <td>10002</td>
            <td>AMENDMENT</td>
        </tr>
    
        <tr>
            <td>10003</td>
            <td>TERMINATION</td>
        </tr>
    
        <tr>
            <td>10004</td>
            <td>REDESIGNATE THE ACCOUNT FOR FUTURE ELECTION TO THE SAME OFFICE</td>
        </tr>
    
        <tr>
            <td>10005</td>
            <td>LOG</td>
        </tr>
    
        <tr>
            <td>10006</td>
            <td>LOG/AMENDMENT</td>
        </tr>
    
        <tr>
            <td>10007</td>
            <td>AS FILED BY COMMITTEE</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*stmnt_status*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p6-thumbnail.gif'></a><p>p. 6</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>11001</td>
            <td>COMPLETE</td>
        </tr>
    
        <tr>
            <td>11002</td>
            <td>INCOMPLETE</td>
        </tr>
    
        <tr>
            <td>11003</td>
            <td>NEEDS REVIEW</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*filing_type*


*FAQ*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711615-FAQ/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711615/pages/FAQ-p2-thumbnail.gif'></a><p>p. 2</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>22001</td>
            <td>Electronic</td>
        </tr>
    
        <tr>
            <td>22006</td>
            <td>Cal Online</td>
        </tr>
    
    </tbody>
    </table>
    </div>




FilernameCd
~~~~~~~~~~~~~~~~~~~~~~~~~

A combination of CAL-ACCESS tables to provide the analyst with
filer information.

Full name of all PACs, firms, and employers are in the last
name field.

Major donors can be split between first and last name fields, but usually
are contained in the last name field only. Individual names of lobbyists,
candidates/officeholders, treasurers/responsible officers, and major donors
(when they are only an individual's name) use both the first and last name
fields in conjunction.

**Sample:** `FILERNAME_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILERNAME_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p67-thumbnail.gif'></a><p>p. 67</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p68-thumbnail.gif'></a><p>p. 68</p></div></div>


*FAQ*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711615-FAQ/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711615/pages/FAQ-p2-thumbnail.gif'></a><p>p. 2</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>xref_filer_id</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Alternative filer ID found on many forms</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>The type of filer. These values are found FILER_TYPES_CD.DESCRIPTION</td>
        </tr>
    
    
    
        <tr>
            <td>status</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>The status of the filer. Includes a mixture of values found in the STATUS_TYPE and STATUS_DESC columns on FILER_STATUS_TYPES_CD</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date for status</td>
        </tr>
    
    
    
        <tr>
            <td>naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name, sometimes full name</td>
        </tr>
    
    
    
        <tr>
            <td>namf</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>First name</td>
        </tr>
    
    
    
        <tr>
            <td>namt</td>
            <td>String (up to 70)</td>
            <td>No</td>
            <td>Name prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>nams</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>adr1</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>First line of street address</td>
        </tr>
    
    
    
        <tr>
            <td>adr2</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Second line of street address</td>
        </tr>
    
    
    
        <tr>
            <td>city</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>City address</td>
        </tr>
    
    
    
        <tr>
            <td>st</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>phon</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Phone number</td>
        </tr>
    
    
    
        <tr>
            <td>fax</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Fax number</td>
        </tr>
    
    
    
        <tr>
            <td>email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Email address</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*filer_type*


*Filer-Types-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774536-Filer-Types-Cd/pages/1.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774536/pages/Filer-Types-Cd-p1-thumbnail.gif'></a><p>p. 1</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>NOT DEFINED</td>
            <td>Undefined</td>
        </tr>
    
        <tr>
            <td>ALL FILERS</td>
            <td>All filers</td>
        </tr>
    
        <tr>
            <td>CANDIDATE/OFFICEHOLDER</td>
            <td>Candidate/officeholder</td>
        </tr>
    
        <tr>
            <td>CLIENT</td>
            <td>Client</td>
        </tr>
    
        <tr>
            <td>EMPLOYER</td>
            <td>Employer</td>
        </tr>
    
        <tr>
            <td>FIRM</td>
            <td>Firm</td>
        </tr>
    
        <tr>
            <td>INDIVIDUAL</td>
            <td>Individual</td>
        </tr>
    
        <tr>
            <td>INITIATIVE</td>
            <td>Initiative</td>
        </tr>
    
        <tr>
            <td>LOBBYIST</td>
            <td>Lobbyist</td>
        </tr>
    
        <tr>
            <td>MAJOR DONOR/INDEPENDENT EXPENDITURE COMMITTEE</td>
            <td>Major donor or indenpendent expenditure committee</td>
        </tr>
    
        <tr>
            <td>PAYMENT TO INFLUENCE</td>
            <td>Payment to influence</td>
        </tr>
    
        <tr>
            <td>PREPAID ACCOUNT</td>
            <td>Prepaid account</td>
        </tr>
    
        <tr>
            <td>PROPONENT</td>
            <td>Proponent</td>
        </tr>
    
        <tr>
            <td>PROPOSITION</td>
            <td>Proposition</td>
        </tr>
    
        <tr>
            <td>RECIPIENT COMMITTEE</td>
            <td>Recipient committee</td>
        </tr>
    
        <tr>
            <td>SLATE MAILER ORGANIZATIONS</td>
            <td>Slate mailer organization</td>
        </tr>
    
        <tr>
            <td>TREASURER/RESPONSIBLE OFFICER</td>
            <td>Treasurer/responsible officer</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*status*


*Filer-Status-Types-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774537-Filer-Status-Types-Cd/pages/1.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774537/pages/Filer-Status-Types-Cd-p1-thumbnail.gif'></a><p>p. 1</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td></td>
            <td>Undefined</td>
        </tr>
    
        <tr>
            <td>A</td>
            <td>ACTIVE</td>
        </tr>
    
        <tr>
            <td>P</td>
            <td>PENDING</td>
        </tr>
    
        <tr>
            <td>R</td>
            <td>REVOKED</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>SUSPENDED</td>
        </tr>
    
        <tr>
            <td>W</td>
            <td>WITHDRAWN</td>
        </tr>
    
        <tr>
            <td>Y</td>
            <td>ACTIVE</td>
        </tr>
    
        <tr>
            <td>N</td>
            <td>INACTIVE</td>
        </tr>
    
        <tr>
            <td>T</td>
            <td>TERMINATED</td>
        </tr>
    
        <tr>
            <td>ACTIVE</td>
            <td>ACTIVE</td>
        </tr>
    
        <tr>
            <td>INACTIVE</td>
            <td>INACTIVE</td>
        </tr>
    
        <tr>
            <td>TERMINATED</td>
            <td>TERMINATED</td>
        </tr>
    
    </tbody>
    </table>
    </div>




FilingsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table is the parent table from which all links and association to
a filing are derived.

**Sample:** `FILINGS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILINGS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p75-thumbnail.gif'></a><p>p. 75</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>The type of filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*filing_type*


*FAQ*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711615-FAQ/pages/2.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711615/pages/FAQ-p2-thumbnail.gif'></a><p>p. 2</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>22001</td>
            <td>Electronic</td>
        </tr>
    
        <tr>
            <td>22002</td>
            <td>Key data entry</td>
        </tr>
    
        <tr>
            <td>22003</td>
            <td>Historical lobby</td>
        </tr>
    
        <tr>
            <td>22004</td>
            <td>Historical campaign</td>
        </tr>
    
        <tr>
            <td>22005</td>
            <td>AMS</td>
        </tr>
    
        <tr>
            <td>22006</td>
            <td>Cal Online</td>
        </tr>
    
    </tbody>
    </table>
    </div>




HdrCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Electronic filing record header data. Contains information
identifying vendor and Cal Format version.

**Sample:** `HDR_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/HDR_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/1.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p1-thumbnail.gif'></a><p>p. 1</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/51.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p51-thumbnail.gif'></a><p>p. 51</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p5-thumbnail.gif'></a><p>p. 5</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p4-thumbnail.gif'></a><p>p. 4</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>cal_ver</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>CAL Version number the filing was made using</td>
        </tr>
    
    
    
        <tr>
            <td>ef_type</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Electronic filing type. This will always have the         value of &quot;CAL&quot;.</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>hdr_comment</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Typically used for development and test filings</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record Type. Value: HDR</td>
        </tr>
    
    
    
        <tr>
            <td>soft_name</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Filing software name used to electronically file</td>
        </tr>
    
    
    
        <tr>
            <td>soft_ver</td>
            <td>String (up to 16)</td>
            <td>No</td>
            <td>Filing software version number</td>
        </tr>
    
    
    
        <tr>
            <td>state_cd</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>The state code value entered in the electronic filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*ef_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p5-thumbnail.gif'></a><p>p. 5</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CAL</td>
            <td>.CAL format</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p5-thumbnail.gif'></a><p>p. 5</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>HDR</td>
            <td>HDR</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*state_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/5.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p5-thumbnail.gif'></a><p>p. 5</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CA</td>
            <td>California</td>
        </tr>
    
    </tbody>
    </table>
    </div>




HeaderCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lookup table used to report Form 460 information in the AMS.

**Sample:** `HEADER_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/HEADER_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p79-thumbnail.gif'></a><p>p. 79</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p80-thumbnail.gif'></a><p>p. 80</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>line_number</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>form_id</td>
            <td>String (up to 5)</td>
            <td>Yes</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 11)</td>
            <td>Yes</td>
            <td>Record Type</td>
        </tr>
    
    
    
        <tr>
            <td>section_label</td>
            <td>String (up to 58)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>comments1</td>
            <td>String (up to 48)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>comments2</td>
            <td>String (up to 48)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>label</td>
            <td>String (up to 98)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>column_a</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>column_b</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>column_c</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>show_c</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>show_b</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_id*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>AF490</td>
            <td>Form 490, Part A</td>
        </tr>
    
        <tr>
            <td>AP1</td>
            <td>Allocation Part 1</td>
        </tr>
    
        <tr>
            <td>AP2</td>
            <td>Allocation Part 2</td>
        </tr>
    
        <tr>
            <td>BF490</td>
            <td>Form 490, Part B</td>
        </tr>
    
        <tr>
            <td>CF490</td>
            <td>Form 490, Part C</td>
        </tr>
    
        <tr>
            <td>DF490</td>
            <td>Form 490, Part D</td>
        </tr>
    
        <tr>
            <td>EF490</td>
            <td>Form 490, Part E</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>FF490</td>
            <td>Form 490, Part F</td>
        </tr>
    
        <tr>
            <td>HF490</td>
            <td>Form 490, Part H</td>
        </tr>
    
        <tr>
            <td>IF490</td>
            <td>Form 490, Part I</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>AP1</td>
            <td>AP1</td>
        </tr>
    
        <tr>
            <td>AP2</td>
            <td>AP2</td>
        </tr>
    
        <tr>
            <td>SMRY_HEADER</td>
            <td>SMRY_HEADER</td>
        </tr>
    
    </tbody>
    </table>
    </div>




SmryCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Summary totals from filings.

**Sample:** `SMRY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/SMRY_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/131.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p131-thumbnail.gif'></a><p>p. 131</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/132.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p132-thumbnail.gif'></a><p>p. 132</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p86-thumbnail.gif'></a><p>p. 86</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p35-thumbnail.gif'></a><p>p. 35</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/36.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p36-thumbnail.gif'></a><p>p. 36</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p37-thumbnail.gif'></a><p>p. 37</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/73.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p73-thumbnail.gif'></a><p>p. 73</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/27.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p27-thumbnail.gif'></a><p>p. 27</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p28-thumbnail.gif'></a><p>p. 28</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p59-thumbnail.gif'></a><p>p. 59</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/60.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p60-thumbnail.gif'></a><p>p. 60</p></div></div>




Filing Forms
^^^^^^^^^^^^
SmryCd contains data collected from the following filing forms, form parts and schedules:



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)

    * Schedule A, Payments Received

    * Schedule B, Payments Made

    * Schedule B-1, Payments Made by Agent or Independent Contractor




* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule A, Monetary Contributions Received

    * Schedule B - Part 1, Loans Received

    * Schedule B - Part 2, Loan Guarantors

    * Schedule B - Part 3, Outstanding Bal

    * Schedule C, Non-Monetary Contributions Received

    * Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees

    * Schedule E, Payments Made

    * Schedule F, Accrued Expenses (Unpaid Bills)

    * Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)

    * Schedule H, Loans Made to Others

    * Schedule H - Part 1, Loans Made

    * Schedule H- Part 2, Repayments Rcvd

    * Schedule H - Part 3, Outstanding Loans

    * Schedule I, miscellanous increases to cash




* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)

    * Part 2, Payments Received in Connection with Lobbying Activity

    * Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses

    * Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made




* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section A: Payments To In-house Employee Lobbyists

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section D: Other Payments to Influence Legislative or Administrative Action

    * Part 3 (Payments Made in Connection with Lobbying Activities), Section E: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before The California Public Utilities Commission




* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)

    * Part 2 (Payments Made this Period), Section A: Activity Expenses

    * Part 2 (Payments Made this Period), Section B: Other Payments to Influence Legislative or Administrative Action

    * Part 2 (Payments Made this Period), Section C: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before the California Public Utilities Commission




* `Form 900 <filingforms.html#form-900>`_ (Public employee's retirement board, candidate campaign statement)



* `Schedule 640 <filingforms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: SMRY</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>amount_a</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column A</td>
        </tr>
    
    
    
        <tr>
            <td>amount_b</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column B</td>
        </tr>
    
    
    
        <tr>
            <td>amount_c</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Summary amount from column C</td>
        </tr>
    
    
    
        <tr>
            <td>elec_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p35-thumbnail.gif'></a><p>p. 35</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/27.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p27-thumbnail.gif'></a><p>p. 27</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p59-thumbnail.gif'></a><p>p. 59</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>SMRY</td>
            <td>SMRY</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/36.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p36-thumbnail.gif'></a><p>p. 36</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p37-thumbnail.gif'></a><p>p. 37</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/73.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p73-thumbnail.gif'></a><p>p. 73</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/27.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p27-thumbnail.gif'></a><p>p. 27</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/28.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p28-thumbnail.gif'></a><p>p. 28</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p59-thumbnail.gif'></a><p>p. 59</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/60.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p60-thumbnail.gif'></a><p>p. 60</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F401</td>
            <td>Form 401: Slate Mailer Organization Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F401A</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
        </tr>
    
        <tr>
            <td>F401B</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
        </tr>
    
        <tr>
            <td>F401B-1</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>A</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
        </tr>
    
        <tr>
            <td>B1</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 1, Loans Received</td>
        </tr>
    
        <tr>
            <td>B2</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 2, Loan Guarantors</td>
        </tr>
    
        <tr>
            <td>B3</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 3, Outstanding Bal</td>
        </tr>
    
        <tr>
            <td>C</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
        </tr>
    
        <tr>
            <td>D</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees</td>
        </tr>
    
        <tr>
            <td>E</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule E, Payments Made</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
        </tr>
    
        <tr>
            <td>G</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule G, Payments Made by an Agent or Independent Contractor (on Behalf of This Committee)</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H, Loans Made to Others</td>
        </tr>
    
        <tr>
            <td>H1</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H - Part 1, Loans Made</td>
        </tr>
    
        <tr>
            <td>H2</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H- Part 2, Repayments Rcvd</td>
        </tr>
    
        <tr>
            <td>H3</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H - Part 3, Outstanding Loans</td>
        </tr>
    
        <tr>
            <td>I</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule I, miscellanous increases to cash</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F625P2</td>
            <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
        </tr>
    
        <tr>
            <td>F625P3A</td>
            <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
        </tr>
    
        <tr>
            <td>F625P3B</td>
            <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F635P3A</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section A: Payments To In-house Employee Lobbyists</td>
        </tr>
    
        <tr>
            <td>F635P3B</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
        </tr>
    
        <tr>
            <td>F635P3C</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
        </tr>
    
        <tr>
            <td>F635P3D</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section D: Other Payments to Influence Legislative or Administrative Action</td>
        </tr>
    
        <tr>
            <td>F635P3E</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section E: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before The California Public Utilities Commission</td>
        </tr>
    
        <tr>
            <td>S640</td>
            <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
        <tr>
            <td>F645P2A</td>
            <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
        </tr>
    
        <tr>
            <td>F645P2B</td>
            <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section B: Other Payments to Influence Legislative or Administrative Action</td>
        </tr>
    
        <tr>
            <td>F645P2C</td>
            <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section C: Payments in Connection with Administrative Testimony in Ratemaking Proceedings Before the California Public Utilities Commission</td>
        </tr>
    
        <tr>
            <td>F900</td>
            <td>Form 900: Public employee&#39;s retirement board, candidate campaign statement</td>
        </tr>
    
        <tr>
            <td>401A</td>
            <td>A</td>
        </tr>
    
        <tr>
            <td>401B</td>
            <td>B</td>
        </tr>
    
        <tr>
            <td>401B-1</td>
            <td>B-1</td>
        </tr>
    
    </tbody>
    </table>
    </div>




SpltCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Split Transaction Record - Used as a child record for schedules:
A, B1, B2, C, D, H and/or F450P5 when disclosing Per Election to Date information.

**Sample:** `SPLT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/SPLT_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/132.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p132-thumbnail.gif'></a><p>p. 132</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p88-thumbnail.gif'></a><p>p. 88</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




Filing Forms
^^^^^^^^^^^^
SpltCd contains data collected from the following filing forms, form parts and schedules:



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)

    * Schedule A, Monetary Contributions Received

    * Schedule B - Part 1, Loans Received

    * Schedule B - Part 2, Loan Guarantors

    * Schedule C, Non-Monetary Contributions Received

    * Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees

    * Schedule H, Loans Made to Others





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>elec_amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Per Election to Date Amount</td>
        </tr>
    
    
    
        <tr>
            <td>elec_code</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Per Election to Date Code</td>
        </tr>
    
    
    
        <tr>
            <td>elec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of Election</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>pform_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Parent Schedule Type</td>
        </tr>
    
    
    
        <tr>
            <td>ptran_id</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Parent transaction ID</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*elec_code*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>P</td>
            <td>Primary</td>
        </tr>
    
        <tr>
            <td>G</td>
            <td>General</td>
        </tr>
    
        <tr>
            <td>S</td>
            <td>Special</td>
        </tr>
    
        <tr>
            <td>R</td>
            <td>Runoff</td>
        </tr>
    
        <tr>
            <td>g</td>
            <td>General</td>
        </tr>
    
        <tr>
            <td>p</td>
            <td>primary</td>
        </tr>
    
        <tr>
            <td>C</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>D</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>M</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>N</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>X</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>O</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>1</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>2</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*pform_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>A</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule A, Monetary Contributions Received</td>
        </tr>
    
        <tr>
            <td>B1</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 1, Loans Received</td>
        </tr>
    
        <tr>
            <td>B2</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule B - Part 2, Loan Guarantors</td>
        </tr>
    
        <tr>
            <td>C</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule C, Non-Monetary Contributions Received</td>
        </tr>
    
        <tr>
            <td>D</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule D, Summary of Expenditures Supporting / Opposing Other Candidates, Measures and Committees</td>
        </tr>
    
        <tr>
            <td>F450P5</td>
            <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule H, Loans Made to Others</td>
        </tr>
    
    </tbody>
    </table>
    </div>




TextMemoCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Text memos attached to electronic filings

**Sample:** `TEXT_MEMO_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/TEXT_MEMO_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/14.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p14-thumbnail.gif'></a><p>p. 14</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/133.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p133-thumbnail.gif'></a><p>p. 133</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/134.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p134-thumbnail.gif'></a><p>p. 134</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/89.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p89-thumbnail.gif'></a><p>p. 89</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p90-thumbnail.gif'></a><p>p. 90</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/15.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p15-thumbnail.gif'></a><p>p. 15</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p16-thumbnail.gif'></a><p>p. 16</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p13-thumbnail.gif'></a><p>p. 13</p></div></div>




Filing Forms
^^^^^^^^^^^^
TextMemoCd contains data collected from the following filing forms, form parts and schedules:



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 405 <filingforms.html#form-405>`_ (Amendment to Campaign Disclosure Statement)



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 605 <filingforms.html#form-605>`_ (Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)



* `Schedule 630 <filingforms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <filingforms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <filingforms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: TEXT</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 8)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>ref_no</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Links text memo to a specific record</td>
        </tr>
    
    
    
        <tr>
            <td>text4000</td>
            <td>String (up to 4000)</td>
            <td>No</td>
            <td>Contents of the text memo</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p16-thumbnail.gif'></a><p>p. 16</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p13-thumbnail.gif'></a><p>p. 13</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>TEXT</td>
            <td>TEXT</td>
        </tr>
    
        <tr>
            <td>MEMO</td>
            <td>MEMO</td>
        </tr>
    
        <tr>
            <td>trun</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Unde</td>
            <td>Under</td>
        </tr>
    
        <tr>
            <td>am</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>sele</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>Term</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>re</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>i</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p90-thumbnail.gif'></a><p>p. 90</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p16-thumbnail.gif'></a><p>p. 16</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p13-thumbnail.gif'></a><p>p. 13</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F401</td>
            <td>Form 401: Slate Mailer Organization Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F405</td>
            <td>Form 405: Amendment to Campaign Disclosure Statement</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410: Statement of Organization Recipient Committee</td>
        </tr>
    
        <tr>
            <td>F425</td>
            <td>Form 425: Semi-Annual Statement of no Activity</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>F498</td>
            <td>Form 498: Slate Mailer Late Payment Report</td>
        </tr>
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F602</td>
            <td>Form 602: Lobbying Firm Activity Authorization</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
        <tr>
            <td>F604</td>
            <td>Form 604: Lobbyist Certification Statement</td>
        </tr>
    
        <tr>
            <td>F605</td>
            <td>Form 605: Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F606</td>
            <td>Form 606: Notice of Termination</td>
        </tr>
    
        <tr>
            <td>F607</td>
            <td>Form 607: Notice of Withdrawal</td>
        </tr>
    
        <tr>
            <td>F615</td>
            <td>Form 615: Lobbyist Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
        <tr>
            <td>S630</td>
            <td>Schedule 630: Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) </td>
        </tr>
    
        <tr>
            <td>S635-C</td>
            <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
        </tr>
    
        <tr>
            <td>S640</td>
            <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
        </tr>
    
        <tr>
            <td>410</td>
            <td>Form 410: Statement of Organization Recipient Committee</td>
        </tr>
    
        <tr>
            <td>460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>497P1</td>
            <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
        </tr>
    
        <tr>
            <td>497P2</td>
            <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
        </tr>
    
        <tr>
            <td>F401A</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule A, Payments Received</td>
        </tr>
    
        <tr>
            <td>F401B</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B, Payments Made</td>
        </tr>
    
        <tr>
            <td>F401B-1</td>
            <td>Form 401 (Slate Mailer Organization Campaign Statement): Schedule B-1, Payments Made by Agent or Independent Contractor</td>
        </tr>
    
        <tr>
            <td>F450P5</td>
            <td>Form 450 (Recipient Committee Campaign Disclosure Statement - Short Form): Part 5, Payments Made</td>
        </tr>
    
        <tr>
            <td>F461P1</td>
            <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 1, Name and Address of Filer</td>
        </tr>
    
        <tr>
            <td>F461P2</td>
            <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 2, Nature and Interests of Filer</td>
        </tr>
    
        <tr>
            <td>F461P5</td>
            <td>Form 461 (Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement): Part 5, Contributions (Including Loans, Forgiveness of Loans, and LoanGuarantees) and Expenditures Made</td>
        </tr>
    
        <tr>
            <td>F465P3</td>
            <td>Form 465 (Supplemental Independent Expenditure Report): Part 3, Independent Expenditures Made</td>
        </tr>
    
        <tr>
            <td>F496P3</td>
            <td>Form 496 (Late Independent Expenditure Report): Part 3, Contributions &gt; $100 Received</td>
        </tr>
    
        <tr>
            <td>F497P1</td>
            <td>Form 497 (Late Contribution Report): Part 1, Contribution(s) Received</td>
        </tr>
    
        <tr>
            <td>F497P2</td>
            <td>Form 497 (Late Contribution Report): Part 2, Contribution(s) Made</td>
        </tr>
    
        <tr>
            <td>F498-A</td>
            <td>Form 498 (Slate Mailer Late Payment Report): Part A, Late Payments Attributed To</td>
        </tr>
    
        <tr>
            <td>F498-R</td>
            <td>Form 498 (Slate Mailer Late Payment Report): Part R, Late Payments Received From</td>
        </tr>
    
        <tr>
            <td>F601P2A</td>
            <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section A, Lobbyist Employers</td>
        </tr>
    
        <tr>
            <td>F601P2B</td>
            <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section B: Subcontracted Clients</td>
        </tr>
    
        <tr>
            <td>F615P1</td>
            <td>Form 615 (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist</td>
        </tr>
    
        <tr>
            <td>F615P2</td>
            <td>Form 615 (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered</td>
        </tr>
    
        <tr>
            <td>F625P2</td>
            <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
        </tr>
    
        <tr>
            <td>F625P3A</td>
            <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
        </tr>
    
        <tr>
            <td>F625P3B</td>
            <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
        </tr>
    
        <tr>
            <td>F625P4B</td>
            <td>Form 625 (Report of Lobbying Firm): Part 4: Campaign Contributions Made</td>
        </tr>
    
        <tr>
            <td>S635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F635P3B</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
        </tr>
    
        <tr>
            <td>F635P3C</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
        </tr>
    
        <tr>
            <td>F635P4B</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made</td>
        </tr>
    
        <tr>
            <td>F645P2A</td>
            <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
        </tr>
    
        <tr>
            <td>F645P3B</td>
            <td>Form 645 (Report of Person Spending $5,000 or More): Part 3: Campaign Contributions Made</td>
        </tr>
    
        <tr>
            <td>S497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>S635C</td>
            <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
        </tr>
    
        <tr>
            <td>A</td>
            <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
        </tr>
    
        <tr>
            <td>A4</td>
            <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
        </tr>
    
        <tr>
            <td>A6</td>
            <td>Schedule A of any form (e.g., Forms 401 or 460)</td>
        </tr>
    
        <tr>
            <td>B</td>
            <td>Schedule B of any form (e.g., Forms 401 or 460)</td>
        </tr>
    
        <tr>
            <td>B1</td>
            <td>Schedule B, Part 1 of Forms 401 or 460</td>
        </tr>
    
        <tr>
            <td>B2</td>
            <td>Schedule B, Part 2 of Forms 401 or 460</td>
        </tr>
    
        <tr>
            <td>B3</td>
            <td>Schedule B, Part 3 of Forms 401 or 460</td>
        </tr>
    
        <tr>
            <td>C</td>
            <td>Schedule C of any form (e.g., Forms 401 or F460)</td>
        </tr>
    
        <tr>
            <td>COMMENTS</td>
            <td>Possibly comments by FPPC for any form?</td>
        </tr>
    
        <tr>
            <td>CVR</td>
            <td>Cover page for any form (e.g., Forms 460, 461 or 497)</td>
        </tr>
    
        <tr>
            <td>D</td>
            <td>Schedule D of any form (e.g., Forms 401, 460 or 461)</td>
        </tr>
    
        <tr>
            <td>DEBTF</td>
            <td>Form 460 (Recipient Committee Campaign Statement): Schedule F, Accrued Expenses (Unpaid Bills)</td>
        </tr>
    
        <tr>
            <td>E</td>
            <td>Schedule E of any form (e.g., Forms 460, 461 or 465)</td>
        </tr>
    
        <tr>
            <td>EXPNT</td>
            <td>Expenditures outlined on any form (e.g. Form 460)</td>
        </tr>
    
        <tr>
            <td>F</td>
            <td>Schedule F of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>G</td>
            <td>Schedule G of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>H</td>
            <td>Schedule H of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>H1</td>
            <td>Schedule H, Part 1 of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>H2</td>
            <td>Schedule H2, Part 2 of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>H3</td>
            <td>Schedule H3, Part 3 of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>I</td>
            <td>Schedule I of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>PT5</td>
            <td>Part 5 of any form (e.g., Form 461</td>
        </tr>
    
        <tr>
            <td>RCPTB1</td>
            <td>Schedule B, Part 1 of any form (e.g., Form 460</td>
        </tr>
    
        <tr>
            <td>RCPTC</td>
            <td>Schedule C of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>RCPTI</td>
            <td>Schedule I of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>SCH A</td>
            <td>Schedule A of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>SF</td>
            <td>Schedule F of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>SPLT</td>
            <td>A memo that applies to multiple items?</td>
        </tr>
    
        <tr>
            <td>SMRY</td>
            <td>Summary section of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>SUM</td>
            <td>Summary section of any form (e.g., Form 460)</td>
        </tr>
    
        <tr>
            <td>SUMMARY</td>
            <td>Summary section of any form (e.g., Form 460)</td>
        </tr>
    
    </tbody>
    </table>
    </div>





Lobbying tables
---------------------------


Cvr2LobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Additional data from lobbyist disclosure forms (615, 625, 635, and 645)

**Sample:** `CVR2_LOBBY_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_LOBBY_DISCLOSURE_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/43.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p43-thumbnail.gif'></a><p>p. 43</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p44-thumbnail.gif'></a><p>p. 44</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/36.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p36-thumbnail.gif'></a><p>p. 36</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p57-thumbnail.gif'></a><p>p. 57</p></div></div>




Filing Forms
^^^^^^^^^^^^
Cvr2LobbyDisclosureCd contains data collected from the following filing forms, form parts and schedules:



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>entity_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Entity identification number</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>enty_title</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of partner, owner, officer, employer if the entity is an individual. Only required by Form 635.</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p57-thumbnail.gif'></a><p>p. 57</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>EMP</td>
            <td>Employer</td>
        </tr>
    
        <tr>
            <td>OFF</td>
            <td>Officer</td>
        </tr>
    
        <tr>
            <td>OWN</td>
            <td>Owner</td>
        </tr>
    
        <tr>
            <td>PTN</td>
            <td>Partner</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p57-thumbnail.gif'></a><p>p. 57</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p71-thumbnail.gif'></a><p>p. 71</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p57-thumbnail.gif'></a><p>p. 57</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR2</td>
            <td>CVR2</td>
        </tr>
    
    </tbody>
    </table>
    </div>




Cvr2RegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page of lobbying disclosure forms

**Sample:** `CVR2_REGISTRATION_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR2_REGISTRATION_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/44.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p44-thumbnail.gif'></a><p>p. 44</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/45.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p45-thumbnail.gif'></a><p>p. 45</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p37-thumbnail.gif'></a><p>p. 37</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p87-thumbnail.gif'></a><p>p. 87</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p88-thumbnail.gif'></a><p>p. 88</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p72-thumbnail.gif'></a><p>p. 72</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/73.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p73-thumbnail.gif'></a><p>p. 73</p></div></div>




Filing Forms
^^^^^^^^^^^^
Cvr2RegistrationCd contains data collected from the following filing forms, form parts and schedules:



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR2</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 10)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>entity_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the entity described by the record</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity last name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity first name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity title or suffix</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity suffix</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p72-thumbnail.gif'></a><p>p. 72</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR2</td>
            <td>CVR2</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p72-thumbnail.gif'></a><p>p. 72</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F602</td>
            <td>Form 602: Lobbying Firm Activity Authorization</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p72-thumbnail.gif'></a><p>p. 72</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>AGY</td>
            <td>State Agency</td>
        </tr>
    
        <tr>
            <td>EMP</td>
            <td>Employer</td>
        </tr>
    
        <tr>
            <td>FRM</td>
            <td>Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>LBY</td>
            <td>Lobbyist (an individual)</td>
        </tr>
    
        <tr>
            <td>MBR</td>
            <td>Member of Associaton</td>
        </tr>
    
        <tr>
            <td>SCL</td>
            <td>Subcontracted Client</td>
        </tr>
    
    </tbody>
    </table>
    </div>




CvrLobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page information for lobbying disclosure forms

**Sample:** `CVR_LOBBY_DISCLOSURE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_LOBBY_DISCLOSURE_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/32.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p32-thumbnail.gif'></a><p>p. 32</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/33.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p33-thumbnail.gif'></a><p>p. 33</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/34.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p34-thumbnail.gif'></a><p>p. 34</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p35-thumbnail.gif'></a><p>p. 35</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/17.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p17-thumbnail.gif'></a><p>p. 17</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p18-thumbnail.gif'></a><p>p. 18</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p19-thumbnail.gif'></a><p>p. 19</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p20-thumbnail.gif'></a><p>p. 20</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p21-thumbnail.gif'></a><p>p. 21</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p66-thumbnail.gif'></a><p>p. 66</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p67-thumbnail.gif'></a><p>p. 67</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p68-thumbnail.gif'></a><p>p. 68</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p69-thumbnail.gif'></a><p>p. 69</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p70-thumbnail.gif'></a><p>p. 70</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p53-thumbnail.gif'></a><p>p. 53</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p54-thumbnail.gif'></a><p>p. 54</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/55.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p55-thumbnail.gif'></a><p>p. 55</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p56-thumbnail.gif'></a><p>p. 56</p></div></div>




Filing Forms
^^^^^^^^^^^^
CvrLobbyDisclosureCd contains data collected from the following filing forms, form parts and schedules:



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_n_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Campaign contribtions? P4 attached&#39; checkbox. Applies to forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_y_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Campaign contribtions? P4 attached&#39; checkbox. Applies to forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>cum_beg_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Cumulative period beginning date</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the filer</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Firm, employer or coalition business city</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>firm_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Firm, employer or coalition business phone number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Firm, employer or coalition business state</td>
        </tr>
    
    
    
        <tr>
            <td>firm_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Form, employer or coalition business ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date</td>
        </tr>
    
    
    
        <tr>
            <td>lby_actvty</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Description of lobbying activity. Applies to forms 635 and 645. Additional description may be provided in text records.</td>
        </tr>
    
    
    
        <tr>
            <td>lobby_n_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying activity none&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>lobby_y_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying activity Form 630 attached&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td>mail_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer mailing address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer mailing address state</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer mailing address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>major_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Major donor first name. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>major_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Major donor last name. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>major_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Major donor suffix. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>major_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Major donor title or prefix. Applies only to individuals and forms 625, 635, 645.</td>
        </tr>
    
    
    
        <tr>
            <td>nopart1_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;No Part I information&#39; checkbox. Applies only to Form 615.</td>
        </tr>
    
    
    
        <tr>
            <td>nopart2_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;No Part II information&#39; checkbox. Applies only to Form 615.</td>
        </tr>
    
    
    
        <tr>
            <td>part1_1_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Partners, owners Form 615 attached ...&#39; checkbox. Applies only to form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>part1_2_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Partners, owners listed below ...&#39; checkbox. Applies only to Form 625.</td>
        </tr>
    
    
    
        <tr>
            <td>prn_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>prn_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>prn_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>prn_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>rcpcmte_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Recipient committee or major donor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>rcpcmte_nm</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient committee name</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number. 000 is the original. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report was filed, as reported by the filer</td>
        </tr>
    
    
    
        <tr>
            <td>sender_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of lobbyist entity that is submitting this report. The field is used to authenticate the filer and allows the firm to submit forms for its lobbyists.</td>
        </tr>
    
    
    
        <tr>
            <td>sig_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date when signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_loc</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer city and state</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>sig_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>sig_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>sig_title</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of signer</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period through date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p67-thumbnail.gif'></a><p>p. 67</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p53-thumbnail.gif'></a><p>p. 53</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CLI</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FRM</td>
            <td>Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Person (spending &gt; $5000)</td>
        </tr>
    
        <tr>
            <td>LBY</td>
            <td>Lobbyist (an individual)</td>
        </tr>
    
        <tr>
            <td>LCO</td>
            <td>Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>LEM</td>
            <td>Lobbying Employer</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p66-thumbnail.gif'></a><p>p. 66</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p53-thumbnail.gif'></a><p>p. 53</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F615</td>
            <td>Form 615: Lobbyist Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p66-thumbnail.gif'></a><p>p. 66</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p53-thumbnail.gif'></a><p>p. 53</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR</td>
            <td>CVR</td>
        </tr>
    
    </tbody>
    </table>
    </div>




CvrRegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Cover page of lobbying disclosure forms (601, 602, 603, 604, 606, and 607)

**Sample:** `CVR_REGISTRATION_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/CVR_REGISTRATION_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/35.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p35-thumbnail.gif'></a><p>p. 35</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/36.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p36-thumbnail.gif'></a><p>p. 36</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/37.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p37-thumbnail.gif'></a><p>p. 37</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/38.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p38-thumbnail.gif'></a><p>p. 38</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/39.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p39-thumbnail.gif'></a><p>p. 39</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p22-thumbnail.gif'></a><p>p. 22</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/23.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p23-thumbnail.gif'></a><p>p. 23</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/24.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p24-thumbnail.gif'></a><p>p. 24</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/25.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p25-thumbnail.gif'></a><p>p. 25</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/26.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p26-thumbnail.gif'></a><p>p. 26</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/27.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p27-thumbnail.gif'></a><p>p. 27</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/83.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p83-thumbnail.gif'></a><p>p. 83</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/84.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p84-thumbnail.gif'></a><p>p. 84</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/85.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p85-thumbnail.gif'></a><p>p. 85</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p68-thumbnail.gif'></a><p>p. 68</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p69-thumbnail.gif'></a><p>p. 69</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p70-thumbnail.gif'></a><p>p. 70</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p71-thumbnail.gif'></a><p>p. 71</p></div></div>




Filing Forms
^^^^^^^^^^^^
CvrRegistrationCd contains data collected from the following filing forms, form parts and schedules:



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>a_b_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Individual or business entity city</td>
        </tr>
    
    
    
        <tr>
            <td>a_b_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of individual or business entity</td>
        </tr>
    
    
    
        <tr>
            <td>a_b_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Individual or business entity state</td>
        </tr>
    
    
    
        <tr>
            <td>a_b_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Individual or business entity ZIP Code.</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>auth_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address city</td>
        </tr>
    
    
    
        <tr>
            <td>auth_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Authorized lobbying firm business name. Applies to Form 602.</td>
        </tr>
    
    
    
        <tr>
            <td>auth_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address state</td>
        </tr>
    
    
    
        <tr>
            <td>auth_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Authorized lobbying firm business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>bus_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Business included activity checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>bus_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer business address city</td>
        </tr>
    
    
    
        <tr>
            <td>bus_class</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Classifiction values of business related entities. This field is exclusive of the business class field. One these must be populated but not both.</td>
        </tr>
    
    
    
        <tr>
            <td>bus_descr</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of business classification if coded as other</td>
        </tr>
    
    
    
        <tr>
            <td>bus_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>Filer business address email</td>
        </tr>
    
    
    
        <tr>
            <td>bus_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer business address fax number</td>
        </tr>
    
    
    
        <tr>
            <td>bus_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer business address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>bus_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer business address state</td>
        </tr>
    
    
    
        <tr>
            <td>bus_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer business address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>c_less50</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry associations with fewer than 50 members check this box</td>
        </tr>
    
    
    
        <tr>
            <td>c_more50</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry associations with more than 50 check this box.</td>
        </tr>
    
    
    
        <tr>
            <td>complet_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ethics orientation class completion date. Applies to Form 604. As filed by the lobbyist.</td>
        </tr>
    
    
    
        <tr>
            <td>descrip_1</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of business activity, industry or other</td>
        </tr>
    
    
    
        <tr>
            <td>descrip_2</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of specific or other lobbying interest</td>
        </tr>
    
    
    
        <tr>
            <td>eff_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date of authoarization or termination</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code describing the filer</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Filer first name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Filer last name</td>
        </tr>
    
    
    
        <tr>
            <td>filer_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>filer_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of the lobbyist employer or firm. Applies to Forms 604, 606, 607.</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>ind_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Individual checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>ind_class</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Classification values to category industry related entities. This field is exclusive of the business class field. One these must be populated but not both.</td>
        </tr>
    
    
    
        <tr>
            <td>ind_descr</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of industry classification if coded as other</td>
        </tr>
    
    
    
        <tr>
            <td>influen_yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Attempt to influence state legislation</td>
        </tr>
    
    
    
        <tr>
            <td>l_firm_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying firm within the ... &#39; checkbox. Applies to Form 607.</td>
        </tr>
    
    
    
        <tr>
            <td>lby_604_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying Agency in this 604 statement&#39; checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>lby_reg_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying Agency in form 601/603 registration statement&#39; checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>lobby_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>&#39;Lobbying within the meaning...&#39; checkbox. Applies to Form 607.</td>
        </tr>
    
    
    
        <tr>
            <td>lobby_int</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Description of Part III lobbying interests. Applies to Form 603</td>
        </tr>
    
    
    
        <tr>
            <td>ls_beg_yr</td>
            <td>String (up to 5)</td>
            <td>No</td>
            <td>Year legislative session begins</td>
        </tr>
    
    
    
        <tr>
            <td>ls_end_yr</td>
            <td>String (up to 5)</td>
            <td>No</td>
            <td>Year legislative sessions ends</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filer mailing address city</td>
        </tr>
    
    
    
        <tr>
            <td>mail_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Filer mailing address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filer mailing address state</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filer mailing address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>newcert_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will require a new certification checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>oth_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>prn_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>prn_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>prn_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>prn_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>qual_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date qualified. Applies to forms 601 and 603. Only occurs once in lobbying filings.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: CVR</td>
        </tr>
    
    
    
        <tr>
            <td>rencert_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will take a renewel certification checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Amendment number as reported by the filer. 000 is the original. 001-999 are amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this report or amendment is filed, as reported by the filer</td>
        </tr>
    
    
    
        <tr>
            <td>sender_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the lobbyist entity submitting this report. This is equal to the filer ID if the filer is the submitting the report and the firm or employer if they are submitting the report.</td>
        </tr>
    
    
    
        <tr>
            <td>sig_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_loc</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer city and state</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Signer first name</td>
        </tr>
    
    
    
        <tr>
            <td>sig_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Signer last name</td>
        </tr>
    
    
    
        <tr>
            <td>sig_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Signer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>sig_title</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Title of signer</td>
        </tr>
    
    
    
        <tr>
            <td>st_agency</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>List of identified state agencies. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>st_leg_yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Will lobby state legislature checkbox. Applies to Form 604.</td>
        </tr>
    
    
    
        <tr>
            <td>stmt_firm</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Lobby firm named in &#39;Statement of Responsible Officer&#39;This field only applies to Form 601.</td>
        </tr>
    
    
    
        <tr>
            <td>trade_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Industry, trade or professional checkbox</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*bus_class*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p70-thumbnail.gif'></a><p>p. 70</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>ENT</td>
            <td>Entertainment/Recreation</td>
        </tr>
    
        <tr>
            <td>FIN</td>
            <td>Finance/Insurance</td>
        </tr>
    
        <tr>
            <td>LOG</td>
            <td>Lodging/Restaurants</td>
        </tr>
    
        <tr>
            <td>MAN</td>
            <td>Manufacturing/Industrial</td>
        </tr>
    
        <tr>
            <td>MER</td>
            <td>Merchandise/Retail</td>
        </tr>
    
        <tr>
            <td>OIL</td>
            <td>Oil and Gas</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>PRO</td>
            <td>Professional/Trade</td>
        </tr>
    
        <tr>
            <td>REA</td>
            <td>Real Estate</td>
        </tr>
    
        <tr>
            <td>TRN</td>
            <td>Transportation</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p68-thumbnail.gif'></a><p>p. 68</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>BUS</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>FRM</td>
            <td>Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>LBY</td>
            <td>Lobbyist (an individual)</td>
        </tr>
    
        <tr>
            <td>LCO</td>
            <td>Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>LEM</td>
            <td>Lobbying Employer</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p68-thumbnail.gif'></a><p>p. 68</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F602</td>
            <td>Form 602: Lobbying Firm Activity Authorization</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
        <tr>
            <td>F604</td>
            <td>Form 604: Lobbyist Certification Statement</td>
        </tr>
    
        <tr>
            <td>F606</td>
            <td>Form 606: Notice of Termination</td>
        </tr>
    
        <tr>
            <td>F607</td>
            <td>Form 607: Notice of Withdrawal</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*ind_class*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/85.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p85-thumbnail.gif'></a><p>p. 85</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p70-thumbnail.gif'></a><p>p. 70</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>AGR</td>
            <td>Agriculture</td>
        </tr>
    
        <tr>
            <td>EDU</td>
            <td>Education</td>
        </tr>
    
        <tr>
            <td>GOV</td>
            <td>Government</td>
        </tr>
    
        <tr>
            <td>HEA</td>
            <td>Health</td>
        </tr>
    
        <tr>
            <td>LAB</td>
            <td>Labor Unions</td>
        </tr>
    
        <tr>
            <td>LEG</td>
            <td>Legal</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>POL</td>
            <td>Political Organizations</td>
        </tr>
    
        <tr>
            <td>PUB</td>
            <td>Public Employees</td>
        </tr>
    
        <tr>
            <td>UTL</td>
            <td>Utilities</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*influen_yn*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p71-thumbnail.gif'></a><p>p. 71</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>Y</td>
            <td>Yes</td>
        </tr>
    
        <tr>
            <td>y</td>
            <td>Yes</td>
        </tr>
    
        <tr>
            <td>N</td>
            <td>No</td>
        </tr>
    
        <tr>
            <td>n</td>
            <td>No</td>
        </tr>
    
        <tr>
            <td>X</td>
            <td>Yes</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p68-thumbnail.gif'></a><p>p. 68</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>CVR</td>
            <td>CVR</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*st_leg_yn*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p71-thumbnail.gif'></a><p>p. 71</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>Y</td>
            <td>Yes</td>
        </tr>
    
        <tr>
            <td>y</td>
            <td>Yes</td>
        </tr>
    
        <tr>
            <td>N</td>
            <td>No</td>
        </tr>
    
        <tr>
            <td>n</td>
            <td>No</td>
        </tr>
    
        <tr>
            <td>X</td>
            <td>Yes</td>
        </tr>
    
        <tr>
            <td>x</td>
            <td>Yes</td>
        </tr>
    
    </tbody>
    </table>
    </div>




F690P2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Amends lobbying disclosure filings (Form 690)

**Sample:** `F690P2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/F690P2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p59-thumbnail.gif'></a><p>p. 59</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/60.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p60-thumbnail.gif'></a><p>p. 60</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/50.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p50-thumbnail.gif'></a><p>p. 50</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/51.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p51-thumbnail.gif'></a><p>p. 51</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p58-thumbnail.gif'></a><p>p. 58</p></div></div>




Filing Forms
^^^^^^^^^^^^
F690P2Cd contains data collected from the following filing forms, form parts and schedules:



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: F690</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>exec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the original report (or prior amendment to the original report) was executed on.</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Report period to/through date of original.</td>
        </tr>
    
    
    
        <tr>
            <td>chg_parts</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amended into affects items on part(s) text description.</td>
        </tr>
    
    
    
        <tr>
            <td>chg_sects</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Amended into affects items on sections(s) text description.</td>
        </tr>
    
    
    
        <tr>
            <td>amend_txt1</td>
            <td>String (up to 330)</td>
            <td>No</td>
            <td>Description of changes to the filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p58-thumbnail.gif'></a><p>p. 58</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F690</td>
            <td>F690</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p72-thumbnail.gif'></a><p>p. 72</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p58-thumbnail.gif'></a><p>p. 58</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F615</td>
            <td>Form 615: Lobbyist Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LattCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist disclosure attachment schedules for payments

**Sample:** `LATT_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LATT_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/81.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p81-thumbnail.gif'></a><p>p. 81</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/82.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p82-thumbnail.gif'></a><p>p. 82</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/52.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p52-thumbnail.gif'></a><p>p. 52</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/53.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p53-thumbnail.gif'></a><p>p. 53</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p80-thumbnail.gif'></a><p>p. 80</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




Filing Forms
^^^^^^^^^^^^
LattCd contains data collected from the following filing forms, form parts and schedules:



* `Schedule 630 <filingforms.html#schedule-630>`_ (Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) )



* `Schedule 635C <filingforms.html#schedule-635c>`_ (Payments Received by Lobbying Coalitions)



* `Schedule 640 <filingforms.html#schedule-640>`_ (Governmental Agencies Reporting (Attachment to Form 635 or Form 645))




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>cum_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>cumbeg_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Cumulative period beginning to date</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Payment Recipient/Payee</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 6)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>pmt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of payment</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LATT</td>
        </tr>
    
    
    
        <tr>
            <td>recip_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Recipient city</td>
        </tr>
    
    
    
        <tr>
            <td>recip_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Recipient first name</td>
        </tr>
    
    
    
        <tr>
            <td>recip_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>recip_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient suffix</td>
        </tr>
    
    
    
        <tr>
            <td>recip_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>recip_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Recipient state</td>
        </tr>
    
    
    
        <tr>
            <td>recip_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p80-thumbnail.gif'></a><p>p. 80</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>FRM</td>
            <td>Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>IND</td>
            <td>Person (spending &gt; $5000)</td>
        </tr>
    
        <tr>
            <td>LBY</td>
            <td>Lobbyist (an individual)</td>
        </tr>
    
        <tr>
            <td>LCO</td>
            <td>Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>LEM</td>
            <td>Lobbying Employer</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient Committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*MapCalFormat2Fields*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/52.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p52-thumbnail.gif'></a><p>p. 52</p></div></div>


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>S630</td>
            <td>Schedule 630: Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) </td>
        </tr>
    
        <tr>
            <td>S635-C</td>
            <td>Schedule 635C: Payments Received by Lobbying Coalitions</td>
        </tr>
    
        <tr>
            <td>S640</td>
            <td>Schedule 640: Governmental Agencies Reporting (Attachment to Form 635 or Form 645)</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p65-thumbnail.gif'></a><p>p. 65</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>LATT</td>
            <td>LATT</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LccmCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbying campaign contributions reported on Forms 615 Part 2,
625 Part 4B, 635 Part 4B and the 645 Part 3B.

**Sample:** `LCCM_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LCCM_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/83.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p83-thumbnail.gif'></a><p>p. 83</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/84.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p84-thumbnail.gif'></a><p>p. 84</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/54.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p54-thumbnail.gif'></a><p>p. 54</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/55.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p55-thumbnail.gif'></a><p>p. 55</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p64-thumbnail.gif'></a><p>p. 64</p></div></div>




Filing Forms
^^^^^^^^^^^^
LccmCd contains data collected from the following filing forms, form parts and schedules:



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm): Part 4: Campaign Contributions Made



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More): Part 3: Campaign Contributions Made




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Back reference to transaction identifier of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of contribution</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Contributor first name</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Contributor last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor suffix</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Contributor prefix or title.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code for Recipient of the Campaign Contribution Value</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text contained in the TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LCCM</td>
        </tr>
    
    
    
        <tr>
            <td>recip_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Recipient city</td>
        </tr>
    
    
    
        <tr>
            <td>recip_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Recipient identification number</td>
        </tr>
    
    
    
        <tr>
            <td>recip_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Recipient first name</td>
        </tr>
    
    
    
        <tr>
            <td>recip_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Recipient last name</td>
        </tr>
    
    
    
        <tr>
            <td>recip_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>recip_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient name prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>recip_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Recipient state</td>
        </tr>
    
    
    
        <tr>
            <td>recip_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Recipient ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p64-thumbnail.gif'></a><p>p. 64</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>COM</td>
            <td>Committee</td>
        </tr>
    
        <tr>
            <td>RCP</td>
            <td>Recipient Committee</td>
        </tr>
    
        <tr>
            <td>CTL</td>
            <td>Controlled committee</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p79-thumbnail.gif'></a><p>p. 79</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p64-thumbnail.gif'></a><p>p. 64</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F615P2</td>
            <td>Form 615 (Lobbyist Report): Part 2, Campaign Contributions Made or Delivered</td>
        </tr>
    
        <tr>
            <td>F625P4B</td>
            <td>Form 625 (Report of Lobbying Firm): Part 4: Campaign Contributions Made</td>
        </tr>
    
        <tr>
            <td>F635P4B</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 4: Campaign Contributions Made</td>
        </tr>
    
        <tr>
            <td>F645P3B</td>
            <td>Form 645 (Report of Person Spending $5,000 or More): Part 3: Campaign Contributions Made</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p64-thumbnail.gif'></a><p>p. 64</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>LCCM</td>
            <td>LCCM</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LempCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist employers and subcontracted clients (Form 601)

**Sample:** `LEMP_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEMP_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/85.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p85-thumbnail.gif'></a><p>p. 85</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p86-thumbnail.gif'></a><p>p. 86</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/56.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p56-thumbnail.gif'></a><p>p. 56</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/57.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p57-thumbnail.gif'></a><p>p. 57</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p90-thumbnail.gif'></a><p>p. 90</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/91.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p91-thumbnail.gif'></a><p>p. 91</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p75-thumbnail.gif'></a><p>p. 75</p></div></div>




Filing Forms
^^^^^^^^^^^^
LempCd contains data collected from the following filing forms, form parts and schedules:



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)

    * Part 2: Section A, Lobbyist Employers

    * Part 2: Section B: Subcontracted Clients





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>agencylist</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Agencies to be lobbied</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>cli_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employing client city</td>
        </tr>
    
    
    
        <tr>
            <td>cli_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Employing client first name</td>
        </tr>
    
    
    
        <tr>
            <td>cli_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employing client last name</td>
        </tr>
    
    
    
        <tr>
            <td>cli_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client suffix</td>
        </tr>
    
    
    
        <tr>
            <td>cli_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client prefix or title</td>
        </tr>
    
    
    
        <tr>
            <td>cli_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Employing client phone number</td>
        </tr>
    
    
    
        <tr>
            <td>cli_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employing client state</td>
        </tr>
    
    
    
        <tr>
            <td>cli_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employing client ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>client_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of the Part 2A employer or Part 2B Client/Employer</td>
        </tr>
    
    
    
        <tr>
            <td>con_period</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Period of the contract</td>
        </tr>
    
    
    
        <tr>
            <td>descrip</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of employer/client lobbying interest</td>
        </tr>
    
    
    
        <tr>
            <td>eff_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective Date of Lobbying Contract</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LEMP</td>
        </tr>
    
    
    
        <tr>
            <td>sub_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm city</td>
        </tr>
    
    
    
        <tr>
            <td>sub_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Subcontracting lobbying firms name</td>
        </tr>
    
    
    
        <tr>
            <td>sub_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm phone number</td>
        </tr>
    
    
    
        <tr>
            <td>sub_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm state</td>
        </tr>
    
    
    
        <tr>
            <td>sub_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Subcontracting lobbying firm ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>subfirm_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Identification number of subcontracting lobbying firm</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p90-thumbnail.gif'></a><p>p. 90</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p75-thumbnail.gif'></a><p>p. 75</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F601P2A</td>
            <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section A, Lobbyist Employers</td>
        </tr>
    
        <tr>
            <td>F601P2B</td>
            <td>Form 601 (Lobbying Firm Registration Statement): Part 2: Section B: Subcontracted Clients</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p90-thumbnail.gif'></a><p>p. 90</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p75-thumbnail.gif'></a><p>p. 75</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>LEMP</td>
            <td>LEMP</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LexpCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbying activity expenditures schedule information, reported in
Forms 615 Part 1, 625 Part 3A, 635 Part 3C, and 645 Part 2A.

**Sample:** `LEXP_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEXP_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/86.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p86-thumbnail.gif'></a><p>p. 86</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/87.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p87-thumbnail.gif'></a><p>p. 87</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/58.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p58-thumbnail.gif'></a><p>p. 58</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/59.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p59-thumbnail.gif'></a><p>p. 59</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p75-thumbnail.gif'></a><p>p. 75</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




Filing Forms
^^^^^^^^^^^^
LexpCd contains data collected from the following filing forms, form parts and schedules:



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Backreference to the tranaction identifer of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>bene_amt</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Amount benefiting benficiary</td>
        </tr>
    
    
    
        <tr>
            <td>bene_name</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Name of the person beneifiting</td>
        </tr>
    
    
    
        <tr>
            <td>bene_posit</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Official position of the person beneifiting</td>
        </tr>
    
    
    
        <tr>
            <td>credcardco</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of the credit card company, if paid using a card</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Payee</td>
        </tr>
    
    
    
        <tr>
            <td>expn_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of expenditure</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>Purpose of the expense and a description or explanation</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>payee_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Payee city</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Payee first name</td>
        </tr>
    
    
    
        <tr>
            <td>payee_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Payee last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>payee_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee suffix</td>
        </tr>
    
    
    
        <tr>
            <td>payee_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>payee_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Payee state</td>
        </tr>
    
    
    
        <tr>
            <td>payee_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Payee ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LEXP</td>
        </tr>
    
    
    
        <tr>
            <td>recsubtype</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Record Subtype</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p75-thumbnail.gif'></a><p>p. 75</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>IND</td>
            <td>Person (spending &gt; $5000)</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F615P1</td>
            <td>Form 615 (Lobbyist Report): Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist</td>
        </tr>
    
        <tr>
            <td>F625P3A</td>
            <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section A: Activity Expenses</td>
        </tr>
    
        <tr>
            <td>F635P3C</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section C: Activity Expenses</td>
        </tr>
    
        <tr>
            <td>F645P2A</td>
            <td>Form 645 (Report of Person Spending $5,000 or More): Part 2 (Payments Made this Period), Section A: Activity Expenses</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>LEXP</td>
            <td>LEXP</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*recsubtype*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p74-thumbnail.gif'></a><p>p. 74</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p61-thumbnail.gif'></a><p>p. 61</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>1</td>
            <td>Main</td>
        </tr>
    
        <tr>
            <td>2</td>
            <td>Detail</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LobbyAmendmentsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist registration amendment information (Form 605 Part I).

**Sample:** `LOBBY_AMENDMENTS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBY_AMENDMENTS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/90.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p90-thumbnail.gif'></a><p>p. 90</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/91.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p91-thumbnail.gif'></a><p>p. 91</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p64-thumbnail.gif'></a><p>p. 64</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/65.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p65-thumbnail.gif'></a><p>p. 65</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p66-thumbnail.gif'></a><p>p. 66</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p88-thumbnail.gif'></a><p>p. 88</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/89.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p89-thumbnail.gif'></a><p>p. 89</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p74-thumbnail.gif'></a><p>p. 74</p></div></div>




Filing Forms
^^^^^^^^^^^^
LobbyAmendmentsCd contains data collected from the following filing forms, form parts and schedules:



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: F605</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>exec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date this amendment executed on</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Reporting date to/through date of original</td>
        </tr>
    
    
    
        <tr>
            <td>add_l_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbyist checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>add_l_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbyist effective date</td>
        </tr>
    
    
    
        <tr>
            <td>a_l_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>a_l_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Add lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>a_l_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>a_l_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist suffix</td>
        </tr>
    
    
    
        <tr>
            <td>del_l_cb</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Delete lobbyist checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>del_l_eff</td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Delete lobbyist effective date</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Delete lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyist title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyiest suffix</td>
        </tr>
    
    
    
        <tr>
            <td>add_le_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbyiest employer checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>add_le_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbyist employer effective date</td>
        </tr>
    
    
    
        <tr>
            <td>a_le_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbyist employer last name</td>
        </tr>
    
    
    
        <tr>
            <td>a_le_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Add lobbyist or employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>a_le_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist employer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>a_le_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Add lobbyist employer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>del_le_cb</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Delete lobbyist employer check box</td>
        </tr>
    
    
    
        <tr>
            <td>del_le_eff</td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Delete lobbyist employer effective date</td>
        </tr>
    
    
    
        <tr>
            <td>d_le_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbyist employer last name</td>
        </tr>
    
    
    
        <tr>
            <td>d_le_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Delete lobbyiest employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>d_le_namt</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Delete lobbyist employer name title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>d_le_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Delete lobbyist employer name</td>
        </tr>
    
    
    
        <tr>
            <td>add_lf_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Add lobbying firm checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>add_lf_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Add lobbying firm effective date</td>
        </tr>
    
    
    
        <tr>
            <td>a_lf_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Add lobbying firm name</td>
        </tr>
    
    
    
        <tr>
            <td>del_lf_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Delete lobbying firm checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>del_lf_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Delete lobbying firm effective date</td>
        </tr>
    
    
    
        <tr>
            <td>d_lf_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Delete lobbying firm name</td>
        </tr>
    
    
    
        <tr>
            <td>other_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Other amendments checkbox</td>
        </tr>
    
    
    
        <tr>
            <td>other_eff</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Other amendments effective date</td>
        </tr>
    
    
    
        <tr>
            <td>other_desc</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of changes</td>
        </tr>
    
    
    
        <tr>
            <td>f606_yes</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Lobbyist ceasing all activity</td>
        </tr>
    
    
    
        <tr>
            <td>f606_no</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Lobbyist ceasing employment but staying active</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p88-thumbnail.gif'></a><p>p. 88</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p74-thumbnail.gif'></a><p>p. 74</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F605</td>
            <td>F605</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/88.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p88-thumbnail.gif'></a><p>p. 88</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p74-thumbnail.gif'></a><p>p. 74</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LobbyingChgLogCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Holds lobbyist log data for web display

**Sample:** `LOBBYING_CHG_LOG_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYING_CHG_LOG_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/91.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p91-thumbnail.gif'></a><p>p. 91</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/92.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p92-thumbnail.gif'></a><p>p. 92</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>change_no</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Number of changes this session</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>log_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>correction_flag</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>action</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>attribute_changed</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ethics_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>interests</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filer_full_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>filer_city</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>filer_st</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>filer_zip</td>
            <td>Integer</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>filer_phone</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>entity_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented. The values might refer to either FILER_TYPE_CD.FILER_TYPE or GROUP_TYPE_CD.GRP_ID, but that&#39;s just a guess.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_name</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_city</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_st</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_zip</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_phone</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Entity phone number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Entity identification number</td>
        </tr>
    
    
    
        <tr>
            <td>responsible_officer</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_type*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>n/a</td>
        </tr>
    
        <tr>
            <td>1</td>
            <td>Client</td>
        </tr>
    
        <tr>
            <td>2</td>
            <td>Employer</td>
        </tr>
    
        <tr>
            <td>3</td>
            <td>Firm</td>
        </tr>
    
        <tr>
            <td>4</td>
            <td>Lobbyist</td>
        </tr>
    
        <tr>
            <td>10</td>
            <td>Major Donor</td>
        </tr>
    
        <tr>
            <td>16</td>
            <td>Recipient Committee</td>
        </tr>
    
        <tr>
            <td>20</td>
            <td>Treasurer/Responsible Officer</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LobbyistContributions1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist contribution disclosure table.

**Sample:** `LOBBYIST_CONTRIBUTIONS1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/92.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p92-thumbnail.gif'></a><p>p. 92</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/93.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p93-thumbnail.gif'></a><p>p. 93</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>recipient_name</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistContributions2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist contribution disclosure table. Temporary table used to generate
disclosure table (Lobbyist Contributions 3)

**Sample:** `LOBBYIST_CONTRIBUTIONS2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/93.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p93-thumbnail.gif'></a><p>p. 93</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/94.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p94-thumbnail.gif'></a><p>p. 94</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>recipient_name</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistContributions3Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist contribution disclosure table.

**Sample:** `LOBBYIST_CONTRIBUTIONS3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_CONTRIBUTIONS3_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/94.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p94-thumbnail.gif'></a><p>p. 94</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>recipient_name</td>
            <td>String (up to 106)</td>
            <td>No</td>
            <td>Recipient&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>recipient_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Recipient&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Amount received</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistEmpLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMP_LOBBYIST1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMP_LOBBYIST1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/94.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p94-thumbnail.gif'></a><p>p. 94</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/95.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p95-thumbnail.gif'></a><p>p. 95</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_last_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_first_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistEmpLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMP_LOBBYIST2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMP_LOBBYIST2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/95.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p95-thumbnail.gif'></a><p>p. 95</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_last_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_first_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

Information for lobbyist's primary employer

**Sample:** `LOBBYIST_EMPLOYER1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/97.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p97-thumbnail.gif'></a><p>p. 97</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/98.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p98-thumbnail.gif'></a><p>p. 98</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>interest_name</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/98.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p98-thumbnail.gif'></a><p>p. 98</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/99.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p99-thumbnail.gif'></a><p>p. 99</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>interest_name</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistEmployer3Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER3_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/99.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p99-thumbnail.gif'></a><p>p. 99</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>interest_name</td>
            <td>String (up to 24)</td>
            <td>No</td>
            <td>Interest name</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistEmployerFirms1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_FIRMS1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_FIRMS1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/95.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p95-thumbnail.gif'></a><p>p. 95</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/96.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p96-thumbnail.gif'></a><p>p. 96</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>termination_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistEmployerFirms2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_FIRMS2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_FIRMS2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/96.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p96-thumbnail.gif'></a><p>p. 96</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>termination_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistEmployerHistoryCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_EMPLOYER_HISTORY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_EMPLOYER_HISTORY_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/96.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p96-thumbnail.gif'></a><p>p. 96</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/97.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p97-thumbnail.gif'></a><p>p. 97</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Current Quarter Amount</td>
        </tr>
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer Name</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest code.</td>
        </tr>
    
    
    
        <tr>
            <td>interest_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Interest name.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for the session.</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 1 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 2 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 1 year to date amount.</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 2 year to date amount.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistFirm1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/103.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p103-thumbnail.gif'></a><p>p. 103</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/104.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p104-thumbnail.gif'></a><p>p. 104</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistFirm2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/104.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p104-thumbnail.gif'></a><p>p. 104</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistFirm3Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM3_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM3_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/105.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p105-thumbnail.gif'></a><p>p. 105</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Current quarter amount</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total amount for the session</td>
        </tr>
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 1 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount of year 2 of the session</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistFirmEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_EMPLOYER1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_EMPLOYER1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/100.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p100-thumbnail.gif'></a><p>p. 100</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_sequence</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment number. 0 is the original filing. 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_start</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_end</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>per_total</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>cum_total</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>lby_actvty</td>
            <td>String (up to 182)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td>ext_lby_actvty</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistFirmEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_EMPLOYER2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_EMPLOYER2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/100.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p100-thumbnail.gif'></a><p>p. 100</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/101.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p101-thumbnail.gif'></a><p>p. 101</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_sequence</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment number. 0 is the original filing. 1 to 999 are amendments</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>employer_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Employer name</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_start</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_end</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date for the period the report covers</td>
        </tr>
    
    
    
        <tr>
            <td>per_total</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>cum_total</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>lby_actvty</td>
            <td>String (up to 182)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td>ext_lby_actvty</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistFirmHistoryCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_HISTORY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_HISTORY_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/101.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p101-thumbnail.gif'></a><p>p. 101</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/102.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p102-thumbnail.gif'></a><p>p. 102</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>contributor_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Contributor identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>current_qtr_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Current Quarter Amount</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the Firm/Employer/Coalition.</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>Name of Firm/Employer/Coalition</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Integer</td>
            <td>No</td>
            <td>Quarter total amount.</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>session_total_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for the session.</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_1</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 1 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>session_yr_2</td>
            <td>Integer</td>
            <td>No</td>
            <td>Total amount for year 2 of the session.</td>
        </tr>
    
    
    
        <tr>
            <td>yr_1_ytd_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>YR_1_YTD_AMT</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Integer</td>
            <td>No</td>
            <td>Year 2 year to date amount.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistFirmLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_LOBBYIST1_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_LOBBYIST1_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/102.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p102-thumbnail.gif'></a><p>p. 102</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_last_name</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_first_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LobbyistFirmLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "Matt
needs to describe the relationship between the multiple tables. Documentation
should be cloned from D H's documentation on these tables. Cox 5/11/2000"

**Sample:** `LOBBYIST_FIRM_LOBBYIST2_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOBBYIST_FIRM_LOBBYIST2_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/102.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p102-thumbnail.gif'></a><p>p. 102</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/103.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p103-thumbnail.gif'></a><p>p. 103</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_last_name</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>lobbyist_first_name</td>
            <td>String (up to 17)</td>
            <td>No</td>
            <td>Lobbyist first name</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LothCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Payment to other lobbying firms listed of Form 625 Part 3B

**Sample:** `LOTH_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOTH_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/106.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p106-thumbnail.gif'></a><p>p. 106</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/107.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p107-thumbnail.gif'></a><p>p. 107</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p67-thumbnail.gif'></a><p>p. 67</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/68.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p68-thumbnail.gif'></a><p>p. 68</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p77-thumbnail.gif'></a><p>p. 77</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p78-thumbnail.gif'></a><p>p. 78</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p63-thumbnail.gif'></a><p>p. 63</p></div></div>




Filing Forms
^^^^^^^^^^^^
LothCd contains data collected from the following filing forms, form parts and schedules:



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount of payment</td>
        </tr>
    
    
    
        <tr>
            <td>cum_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s city</td>
        </tr>
    
    
    
        <tr>
            <td>firm_name</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s name</td>
        </tr>
    
    
    
        <tr>
            <td>firm_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s phone number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Firm, employer or coalition&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>firm_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Firm ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>pmt_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date of payment</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LOTH</td>
        </tr>
    
    
    
        <tr>
            <td>subj_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>subj_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>subj_nams</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Suffix of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>subj_namt</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Prefix or title of employer/client subject of lobbying</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p77-thumbnail.gif'></a><p>p. 77</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p63-thumbnail.gif'></a><p>p. 63</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F625P3B</td>
            <td>Form 625 (Report of Lobbying Firm): Part 3 (Payments Made In Connection With Lobbying Activities), Section B: Payments Made</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p77-thumbnail.gif'></a><p>p. 77</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/63.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p63-thumbnail.gif'></a><p>p. 63</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>LOTH</td>
            <td>LOTH</td>
        </tr>
    
    </tbody>
    </table>
    </div>




LpayCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Payments made or received by lobbying firms, reported on
Form 625 Part 2 and 635 Part 3B

**Sample:** `LPAY_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LPAY_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/107.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p107-thumbnail.gif'></a><p>p. 107</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/108.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p108-thumbnail.gif'></a><p>p. 108</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/109.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p109-thumbnail.gif'></a><p>p. 109</p></div></div>


*MapCalFormat2Fields*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p69-thumbnail.gif'></a><p>p. 69</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711616-MapCalFormat2Fields/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711616/pages/MapCalFormat2Fields-p70-thumbnail.gif'></a><p>p. 70</p></div></div>


*Cal-Format-201*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p76-thumbnail.gif'></a><p>p. 76</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/77.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p77-thumbnail.gif'></a><p>p. 77</p></div></div>


*Cal-Format-1-05-02*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p62-thumbnail.gif'></a><p>p. 62</p></div></div>




Filing Forms
^^^^^^^^^^^^
LpayCd contains data collected from the following filing forms, form parts and schedules:



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>advan_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Advance and other payments amount</td>
        </tr>
    
    
    
        <tr>
            <td>advan_dscr</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Description of advance and other payments</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>bakref_tid</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Backreference to transaction identifer of parent record</td>
        </tr>
    
    
    
        <tr>
            <td>cum_total</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Cumulative total to date</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Employer city</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Employer first name</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Name of firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer suffix</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Employer phone number</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Employer state</td>
        </tr>
    
    
    
        <tr>
            <td>emplr_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Employer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity Code of the Employer Values</td>
        </tr>
    
    
    
        <tr>
            <td>fees_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Fees and retainers amount</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 7)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>lby_actvty</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Description of lobbying activity</td>
        </tr>
    
    
    
        <tr>
            <td>line_item</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Line item number of this record</td>
        </tr>
    
    
    
        <tr>
            <td>memo_code</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Memo amount flag</td>
        </tr>
    
    
    
        <tr>
            <td>memo_refno</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Reference to the text contained in a TEXT record</td>
        </tr>
    
    
    
        <tr>
            <td>per_total</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Total this reporting period</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record Type Value: LPAY</td>
        </tr>
    
    
    
        <tr>
            <td>reimb_amt</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Reimbursements of expense amount</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*entity_cd*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p76-thumbnail.gif'></a><p>p. 76</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p62-thumbnail.gif'></a><p>p. 62</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>FRM</td>
            <td>Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>LCO</td>
            <td>Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>LEM</td>
            <td>Lobbying Employer</td>
        </tr>
    
        <tr>
            <td>OTH</td>
            <td>Other</td>
        </tr>
    
        <tr>
            <td>128</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*form_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p76-thumbnail.gif'></a><p>p. 76</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p62-thumbnail.gif'></a><p>p. 62</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F625P2</td>
            <td>Form 625 (Report of Lobbying Firm): Part 2, Payments Received in Connection with Lobbying Activity</td>
        </tr>
    
        <tr>
            <td>F635P3B</td>
            <td>Form 635 (Report of Lobbyist Employer or Report of Lobbying Coalition): Part 3 (Payments Made in Connection with Lobbying Activities), Section B: Payments To Lobbying Firms</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*rec_type*


*Cal-Format-201*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712034-Cal-Format-201/pages/76.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712034/pages/Cal-Format-201-p76-thumbnail.gif'></a><p>p. 76</p></div></div>


*Cal-Format-1-05-02*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2712033-Cal-Format-1-05-02/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2712033/pages/Cal-Format-1-05-02-p62-thumbnail.gif'></a><p>p. 62</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>LPAY</td>
            <td>LPAY</td>
        </tr>
    
    </tbody>
    </table>
    </div>





Other tables
---------------------------


AcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Contains acronyms and their meaning.

**Sample:** `ACRONYMS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p16-thumbnail.gif'></a><p>p. 16</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>acronym</td>
            <td>String (up to 40)</td>
            <td>Yes</td>
            <td>Acronym text value</td>
        </tr>
    
    
    
        <tr>
            <td>stands_for</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Definition of the acronym</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date for the acronym</td>
        </tr>
    
    
    
        <tr>
            <td>a_desc</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Description of the acronym</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


AddressCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table holds all addresses for the system. This table can be used
for address-based searches and formes the bases for address information
desplayed by the AMS.

**Sample:** `ADDRESS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ADDRESS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p16-thumbnail.gif'></a><p>p. 16</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>adrid</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Address indentification number</td>
        </tr>
    
    
    
        <tr>
            <td>city</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address city</td>
        </tr>
    
    
    
        <tr>
            <td>st</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address state</td>
        </tr>
    
    
    
        <tr>
            <td>zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Address ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Address phone number</td>
        </tr>
    
    
    
        <tr>
            <td>fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Address fax number</td>
        </tr>
    
    
    
        <tr>
            <td>email</td>
            <td>String (up to 500)</td>
            <td>No</td>
            <td>Address email</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


BallotMeasuresCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Ballot measure dates and times

**Sample:** `BALLOT_MEASURES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/BALLOT_MEASURES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p7-thumbnail.gif'></a><p>p. 7</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p19-thumbnail.gif'></a><p>p. 19</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>election_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ballot measure election date</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>measure_no</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Ballot measure number</td>
        </tr>
    
    
    
        <tr>
            <td>measure_name</td>
            <td>String (up to 163)</td>
            <td>No</td>
            <td>Ballot measure full name</td>
        </tr>
    
    
    
        <tr>
            <td>measure_short_name</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Ballot measure short name</td>
        </tr>
    
    
    
        <tr>
            <td>jurisdiction</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


EfsFilingLogCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Sample:** `EFS_FILING_LOG_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/EFS_FILING_LOG_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/49.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p49-thumbnail.gif'></a><p>p. 49</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/50.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p50-thumbnail.gif'></a><p>p. 50</p></div></div>




Filing Forms
^^^^^^^^^^^^
EfsFilingLogCd contains data collected from the following filing forms, form parts and schedules:



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 402 <filingforms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization))



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filing_date</td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filingstatus</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>vendor</td>
            <td>String (up to 250)</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>error_no</td>
            <td>String (up to 250)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_type*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F400</td>
            <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F401</td>
            <td>Form 401: Slate Mailer Organization Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F402</td>
            <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410: Statement of Organization Recipient Committee</td>
        </tr>
    
        <tr>
            <td>F425</td>
            <td>Form 425: Semi-Annual Statement of no Activity</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>F498</td>
            <td>Form 498: Slate Mailer Late Payment Report</td>
        </tr>
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F602</td>
            <td>Form 602: Lobbying Firm Activity Authorization</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
        <tr>
            <td>F604</td>
            <td>Form 604: Lobbyist Certification Statement</td>
        </tr>
    
        <tr>
            <td>F606</td>
            <td>Form 606: Notice of Termination</td>
        </tr>
    
        <tr>
            <td>F607</td>
            <td>Form 607: Notice of Withdrawal</td>
        </tr>
    
        <tr>
            <td>F615</td>
            <td>Form 615: Lobbyist Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
        <tr>
            <td>BADFORMAT 253</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>form</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>




FilerAcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Links acronyms to filers

**Sample:** `FILER_ACRONYMS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ACRONYMS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p61-thumbnail.gif'></a><p>p. 61</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>acronym</td>
            <td>String (up to 32)</td>
            <td>Yes</td>
            <td>AMS acronym</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilerAddressCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Links filers and addresses. This table maintains a history of when
addresses change.

**Sample:** `FILER_ADDRESS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ADDRESS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/61.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p61-thumbnail.gif'></a><p>p. 61</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/62.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p62-thumbnail.gif'></a><p>p. 62</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>adrid</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Address identification number</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Address effective date</td>
        </tr>
    
    
    
        <tr>
            <td>add_type</td>
            <td>Integer</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilerEthicsClassCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table stores lobbyist ethics training dates.

**Sample:** `FILER_ETHICS_CLASS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_ETHICS_CLASS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/64.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p64-thumbnail.gif'></a><p>p. 64</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ethics_date</td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>Date ethics training was accomplished</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilerInterestsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Links a filer to their interest codes.

**Sample:** `FILER_INTERESTS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_INTERESTS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/66.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p66-thumbnail.gif'></a><p>p. 66</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>Yes</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>effect_date</td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td></td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilerLinksCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Links filers to each other and records their relationship type.

**Sample:** `FILER_LINKS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_LINKS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/67.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p67-thumbnail.gif'></a><p>p. 67</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id_a</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number for the first filer in the relationship</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id_b</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number for the second filer in the relationship</td>
        </tr>
    
    
    
        <tr>
            <td>active_flg</td>
            <td>String (up to 1)</td>
            <td>Yes</td>
            <td>Indicates if the link is active</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>link_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Denotes the type of the link</td>
        </tr>
    
    
    
        <tr>
            <td>link_desc</td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Unused</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date the link became active</td>
        </tr>
    
    
    
        <tr>
            <td>dominate_filer</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Unused</td>
        </tr>
    
    
    
        <tr>
            <td>termination_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*link_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/6.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p6-thumbnail.gif'></a><p>p. 6</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/7.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p7-thumbnail.gif'></a><p>p. 7</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>-12019</td>
            <td>CANDIDATE CONTROLLED CAUCUS COMMITTEE</td>
        </tr>
    
        <tr>
            <td>-12018</td>
            <td>PROPONENT</td>
        </tr>
    
        <tr>
            <td>-12016</td>
            <td>TREASURER/RESPONSIBLE OFFICER FOR</td>
        </tr>
    
        <tr>
            <td>-12015</td>
            <td>ASSOCIATED</td>
        </tr>
    
        <tr>
            <td>-12014</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>-12013</td>
            <td>OPPOSE</td>
        </tr>
    
        <tr>
            <td>-12011</td>
            <td>CONTROLLING CANDIDATE</td>
        </tr>
    
        <tr>
            <td>-12008</td>
            <td>FIRM OF A LOBBYIST</td>
        </tr>
    
        <tr>
            <td>-12005</td>
            <td>FIRM OF A CLIENT (WHO IS ALSO A FIRM)</td>
        </tr>
    
        <tr>
            <td>-12004</td>
            <td>FIRM OF A CLIENT (WHO IS AN EMPLOYER)</td>
        </tr>
    
        <tr>
            <td>-12002</td>
            <td>EMPLOYER OF  AN IN-HOUSE LOBBYIST</td>
        </tr>
    
        <tr>
            <td>-12001</td>
            <td>CLIENT OF A FIRM</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>12001</td>
            <td>FIRM OF A CLIENT</td>
        </tr>
    
        <tr>
            <td>12002</td>
            <td>IN-HOUSE LOBBYIST OF AN EMPLOYER</td>
        </tr>
    
        <tr>
            <td>12004</td>
            <td>CLIENT (WHO IS AN EMPLOYER) OF A FIRM</td>
        </tr>
    
        <tr>
            <td>12005</td>
            <td>CLIENT (WHO IS ALSO A FIRM) OF ANOTHER FIRM</td>
        </tr>
    
        <tr>
            <td>12008</td>
            <td>LOBBYIST OF A FIRM</td>
        </tr>
    
        <tr>
            <td>12011</td>
            <td>CANDIDATE CONTROLS THIS COMMITTEE</td>
        </tr>
    
        <tr>
            <td>12013</td>
            <td>OPPOSE</td>
        </tr>
    
        <tr>
            <td>12014</td>
            <td>SUPPORT</td>
        </tr>
    
        <tr>
            <td>12015</td>
            <td>ASSOCIATED</td>
        </tr>
    
        <tr>
            <td>12016</td>
            <td>TREASURER/RESPONSIBLE OFFICER</td>
        </tr>
    
        <tr>
            <td>12018</td>
            <td>PROPONENT</td>
        </tr>
    
        <tr>
            <td>12019</td>
            <td>CANDIDATE CONTROLLED CAUCUS COMMITTEE</td>
        </tr>
    
    </tbody>
    </table>
    </div>




FilerStatusTypesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model that contains a small number
of codes and definitions that map to values in FILERNAME_CD.STATUS.

**Sample:** `FILER_STATUS_TYPES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_STATUS_TYPES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p69-thumbnail.gif'></a><p>p. 69</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>status_type</td>
            <td>String (up to 11)</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>status_desc</td>
            <td>String (up to 11)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilerToFilerTypeCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table links a filer to a set of characteristics that describe the
filer. This table maintains a history of changes and allows the filer
to change characteristics over time.

**Sample:** `FILER_TO_FILER_TYPE_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TO_FILER_TYPE_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/69.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p69-thumbnail.gif'></a><p>p. 69</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/70.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p70-thumbnail.gif'></a><p>p. 70</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>Foreign Key (type determined by related field)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>active</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Indicates if the filer is currently active</td>
        </tr>
    
    
    
        <tr>
            <td>race</td>
            <td>Integer</td>
            <td>No</td>
            <td>If applicable indicates the race in which the filer is running</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>category</td>
            <td>Integer</td>
            <td>No</td>
            <td>Defines the filer&#39;s category such as controlled, jointly controlled, etc. (subset of filer&#39;s type)</td>
        </tr>
    
    
    
        <tr>
            <td>category_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable, the category type specifies additional information about the category. (e.g. state, local, etc.)</td>
        </tr>
    
    
    
        <tr>
            <td>sub_category</td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable specifies general purpose, primarily formed, etc.</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>Yes</td>
            <td>The date the filer assumed the current class or type</td>
        </tr>
    
    
    
        <tr>
            <td>sub_category_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>When applicable specifies broad based or small contributor</td>
        </tr>
    
    
    
        <tr>
            <td>election_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Indicates type of election (general, primary, special)</td>
        </tr>
    
    
    
        <tr>
            <td>sub_category_a</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Indicates if sponsored or not</td>
        </tr>
    
    
    
        <tr>
            <td>nyq_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Indicates the date when a committee reached its qualifying level of activity</td>
        </tr>
    
    
    
        <tr>
            <td>party_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s political party</td>
        </tr>
    
    
    
        <tr>
            <td>county_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s county code</td>
        </tr>
    
    
    
        <tr>
            <td>district_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s district number for the office being sought. Populated for Senate, Assembly or Board of Equalization races</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*race*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/16.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p16-thumbnail.gif'></a><p>p. 16</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/17.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p17-thumbnail.gif'></a><p>p. 17</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p18-thumbnail.gif'></a><p>p. 18</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p20-thumbnail.gif'></a><p>p. 20</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/21.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p21-thumbnail.gif'></a><p>p. 21</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/22.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p22-thumbnail.gif'></a><p>p. 22</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>30002</td>
            <td>GOVERNOR</td>
        </tr>
    
        <tr>
            <td>30003</td>
            <td>LIEUTENANT GOVERNOR</td>
        </tr>
    
        <tr>
            <td>30004</td>
            <td>SECRETARY OF STATE</td>
        </tr>
    
        <tr>
            <td>30005</td>
            <td>CONTROLLER</td>
        </tr>
    
        <tr>
            <td>30006</td>
            <td>TREASURER</td>
        </tr>
    
        <tr>
            <td>30007</td>
            <td>ATTORNEY GENERAL</td>
        </tr>
    
        <tr>
            <td>30008</td>
            <td>SUPERINTENDENT OF PUBLIC INSTRUCTION</td>
        </tr>
    
        <tr>
            <td>30009</td>
            <td>MEMBER BOARD OF EQUALIZATION</td>
        </tr>
    
        <tr>
            <td>30010</td>
            <td>OXNARD HARBOR COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30011</td>
            <td>CITY CONTROLLER</td>
        </tr>
    
        <tr>
            <td>30012</td>
            <td>STATE SENATE</td>
        </tr>
    
        <tr>
            <td>30013</td>
            <td>ASSEMBLY</td>
        </tr>
    
        <tr>
            <td>30014</td>
            <td>INSURANCE COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30015</td>
            <td>JUDGE</td>
        </tr>
    
        <tr>
            <td>30016</td>
            <td>BOARD MEMBER</td>
        </tr>
    
        <tr>
            <td>30017</td>
            <td>TAX COLLECTOR</td>
        </tr>
    
        <tr>
            <td>30018</td>
            <td>TRUSTEE</td>
        </tr>
    
        <tr>
            <td>30019</td>
            <td>SUPERVISOR</td>
        </tr>
    
        <tr>
            <td>30020</td>
            <td>SHERIFF</td>
        </tr>
    
        <tr>
            <td>30021</td>
            <td>CORONER</td>
        </tr>
    
        <tr>
            <td>30022</td>
            <td>MARSHALL</td>
        </tr>
    
        <tr>
            <td>30023</td>
            <td>CITY CLERK</td>
        </tr>
    
        <tr>
            <td>30024</td>
            <td>SCHOOL BOARD</td>
        </tr>
    
        <tr>
            <td>30025</td>
            <td>HARBOR COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30026</td>
            <td>DISTRICT ATTORNEY</td>
        </tr>
    
        <tr>
            <td>30027</td>
            <td>COUNTY CLERK</td>
        </tr>
    
        <tr>
            <td>30028</td>
            <td>AUDITOR</td>
        </tr>
    
        <tr>
            <td>30029</td>
            <td>MAYOR</td>
        </tr>
    
        <tr>
            <td>30030</td>
            <td>CITY ATTORNEY</td>
        </tr>
    
        <tr>
            <td>30031</td>
            <td>DEMOCRATIC COUNTY CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30032</td>
            <td>TOWN COUNCIL</td>
        </tr>
    
        <tr>
            <td>30033</td>
            <td>ASSESSOR</td>
        </tr>
    
        <tr>
            <td>30034</td>
            <td>CITY TREASURER</td>
        </tr>
    
        <tr>
            <td>30035</td>
            <td>CITY COUNCIL</td>
        </tr>
    
        <tr>
            <td>30036</td>
            <td>COMMISSIONER</td>
        </tr>
    
        <tr>
            <td>30037</td>
            <td>REPUBLICAN COUNTY CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30038</td>
            <td>DIRECTOR</td>
        </tr>
    
        <tr>
            <td>30039</td>
            <td>DIRECTOR OF ZONE 7</td>
        </tr>
    
        <tr>
            <td>30040</td>
            <td>COMMUNITY COLLEGE BOARD</td>
        </tr>
    
        <tr>
            <td>30041</td>
            <td>POLICE CHIEF</td>
        </tr>
    
        <tr>
            <td>30042</td>
            <td>CHIEF OF POLICE</td>
        </tr>
    
        <tr>
            <td>30043</td>
            <td>CENTRAL COMMITTEE</td>
        </tr>
    
        <tr>
            <td>30044</td>
            <td>BOARD OF EDUCATION</td>
        </tr>
    
        <tr>
            <td>30045</td>
            <td>BOARD OF DIRECTORS</td>
        </tr>
    
        <tr>
            <td>30046</td>
            <td>COLLEGE BOARD</td>
        </tr>
    
        <tr>
            <td>30047</td>
            <td>BART BOARD DIRECTOR</td>
        </tr>
    
        <tr>
            <td>30048</td>
            <td>BOARD OF TRUSTEES</td>
        </tr>
    
        <tr>
            <td>30049</td>
            <td>IRRIGATION</td>
        </tr>
    
        <tr>
            <td>30050</td>
            <td>WATER BOARD</td>
        </tr>
    
        <tr>
            <td>30051</td>
            <td>COMMUNITY PLANNING GROUP</td>
        </tr>
    
        <tr>
            <td>30052</td>
            <td>BOARD OF SUPERVISORS</td>
        </tr>
    
        <tr>
            <td>30053</td>
            <td>SUPERIOR COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>30054</td>
            <td>DISTRICT ATTORNEY/PUBLIC DEFENDER</td>
        </tr>
    
        <tr>
            <td>30055</td>
            <td>MEASURE</td>
        </tr>
    
        <tr>
            <td>30056</td>
            <td>CITY PROSECUTOR</td>
        </tr>
    
        <tr>
            <td>30057</td>
            <td>SUPREME COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>30058</td>
            <td>PUBLIC EMPLOYEES RETIREMENT BOARD</td>
        </tr>
    
        <tr>
            <td>30059</td>
            <td>APPELLATE COURT JUDGE</td>
        </tr>
    
        <tr>
            <td>50001</td>
            <td>Ag</td>
        </tr>
    
        <tr>
            <td>50002</td>
            <td>Assembly</td>
        </tr>
    
        <tr>
            <td>50003</td>
            <td>Assessor</td>
        </tr>
    
        <tr>
            <td>50004</td>
            <td>Assessor/Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50005</td>
            <td>Assessor/County Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50006</td>
            <td>Assessor/Recorder</td>
        </tr>
    
        <tr>
            <td>50007</td>
            <td>Associate Justice</td>
        </tr>
    
        <tr>
            <td>50008</td>
            <td>Auditor</td>
        </tr>
    
        <tr>
            <td>50009</td>
            <td>Auditor/Controller</td>
        </tr>
    
        <tr>
            <td>50010</td>
            <td>Auditor/Controller/Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50011</td>
            <td>Auditor/Controller/Recorder</td>
        </tr>
    
        <tr>
            <td>50012</td>
            <td>Auditor/Controller/Treasurer/Tax Collector</td>
        </tr>
    
        <tr>
            <td>50013</td>
            <td>Auditor/Recorder</td>
        </tr>
    
        <tr>
            <td>50014</td>
            <td>Board Member</td>
        </tr>
    
        <tr>
            <td>50015</td>
            <td>Board Of Director</td>
        </tr>
    
        <tr>
            <td>50016</td>
            <td>Board Of Supervisor</td>
        </tr>
    
        <tr>
            <td>50017</td>
            <td>Boe</td>
        </tr>
    
        <tr>
            <td>50018</td>
            <td>Chief Justice</td>
        </tr>
    
        <tr>
            <td>50019</td>
            <td>City</td>
        </tr>
    
        <tr>
            <td>50020</td>
            <td>City Attorney</td>
        </tr>
    
        <tr>
            <td>50021</td>
            <td>City Auditor</td>
        </tr>
    
        <tr>
            <td>50022</td>
            <td>City Clerk</td>
        </tr>
    
        <tr>
            <td>50023</td>
            <td>City Council</td>
        </tr>
    
        <tr>
            <td>50024</td>
            <td>City Of Los Angeles</td>
        </tr>
    
        <tr>
            <td>50025</td>
            <td>City Of South El Monte</td>
        </tr>
    
        <tr>
            <td>50026</td>
            <td>City Prosecutor</td>
        </tr>
    
        <tr>
            <td>50027</td>
            <td>City Treasurer</td>
        </tr>
    
        <tr>
            <td>50028</td>
            <td>Clerk/Auditor</td>
        </tr>
    
        <tr>
            <td>50029</td>
            <td>Clerk/Record/Public Admin</td>
        </tr>
    
        <tr>
            <td>50030</td>
            <td>Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50031</td>
            <td>Clerk/Recorder/Registar</td>
        </tr>
    
        <tr>
            <td>50032</td>
            <td>Clerk/Recorder/Registrar</td>
        </tr>
    
        <tr>
            <td>50033</td>
            <td>Commissioner</td>
        </tr>
    
        <tr>
            <td>50034</td>
            <td>Controller</td>
        </tr>
    
        <tr>
            <td>50035</td>
            <td>Costa Mesa</td>
        </tr>
    
        <tr>
            <td>50036</td>
            <td>Council Member</td>
        </tr>
    
        <tr>
            <td>50037</td>
            <td>County Clerk</td>
        </tr>
    
        <tr>
            <td>50038</td>
            <td>County Clerk/Auditor</td>
        </tr>
    
        <tr>
            <td>50039</td>
            <td>County Clerk/Auditor/Controller</td>
        </tr>
    
        <tr>
            <td>50040</td>
            <td>County Clerk/Recorder</td>
        </tr>
    
        <tr>
            <td>50041</td>
            <td>County Clerk/Recorder/Assessor</td>
        </tr>
    
        <tr>
            <td>50042</td>
            <td>County Clerk/Recorder/Public Admin</td>
        </tr>
    
        <tr>
            <td>50043</td>
            <td>Democratic County Central Committee</td>
        </tr>
    
        <tr>
            <td>50044</td>
            <td>Director</td>
        </tr>
    
        <tr>
            <td>50045</td>
            <td>District Attorney</td>
        </tr>
    
        <tr>
            <td>50046</td>
            <td>District Attorney/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50047</td>
            <td>Gccc</td>
        </tr>
    
        <tr>
            <td>50048</td>
            <td>Governor</td>
        </tr>
    
        <tr>
            <td>50049</td>
            <td>Harbor Commissioner</td>
        </tr>
    
        <tr>
            <td>50050</td>
            <td>Ic</td>
        </tr>
    
        <tr>
            <td>50051</td>
            <td>Irrigation Dist</td>
        </tr>
    
        <tr>
            <td>50052</td>
            <td>Judge</td>
        </tr>
    
        <tr>
            <td>50053</td>
            <td>Justice</td>
        </tr>
    
        <tr>
            <td>50054</td>
            <td>Legislature</td>
        </tr>
    
        <tr>
            <td>50055</td>
            <td>Lieutenant Governor</td>
        </tr>
    
        <tr>
            <td>50056</td>
            <td>Mayor</td>
        </tr>
    
        <tr>
            <td>50057</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>50058</td>
            <td>Placentia</td>
        </tr>
    
        <tr>
            <td>50059</td>
            <td>Public Administrator</td>
        </tr>
    
        <tr>
            <td>50060</td>
            <td>Public Administrator/Guardian</td>
        </tr>
    
        <tr>
            <td>50061</td>
            <td>Rent Stabilization Board</td>
        </tr>
    
        <tr>
            <td>50062</td>
            <td>Republican Central Committee</td>
        </tr>
    
        <tr>
            <td>50063</td>
            <td>San Francisco Dccc</td>
        </tr>
    
        <tr>
            <td>50064</td>
            <td>Sanger</td>
        </tr>
    
        <tr>
            <td>50065</td>
            <td>School Board</td>
        </tr>
    
        <tr>
            <td>50066</td>
            <td>Secretary Of State</td>
        </tr>
    
        <tr>
            <td>50067</td>
            <td>Senator</td>
        </tr>
    
        <tr>
            <td>50068</td>
            <td>Sheriff</td>
        </tr>
    
        <tr>
            <td>50069</td>
            <td>Sheriff/Coroner</td>
        </tr>
    
        <tr>
            <td>50070</td>
            <td>Sheriff/Coroner/Marshall</td>
        </tr>
    
        <tr>
            <td>50071</td>
            <td>Sheriff/Coroner/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50072</td>
            <td>Solana Beach</td>
        </tr>
    
        <tr>
            <td>50073</td>
            <td>Superintendent</td>
        </tr>
    
        <tr>
            <td>50074</td>
            <td>Supervisor</td>
        </tr>
    
        <tr>
            <td>50075</td>
            <td>Supt Of Schools</td>
        </tr>
    
        <tr>
            <td>50076</td>
            <td>Tax Collector</td>
        </tr>
    
        <tr>
            <td>50077</td>
            <td>Town Council</td>
        </tr>
    
        <tr>
            <td>50078</td>
            <td>Treasurer</td>
        </tr>
    
        <tr>
            <td>50079</td>
            <td>Treasurer/Tax Collector</td>
        </tr>
    
        <tr>
            <td>50080</td>
            <td>Treasurer/Tax Collector/Clerk</td>
        </tr>
    
        <tr>
            <td>50081</td>
            <td>Treasurer/Tax Collector/Public Administrator</td>
        </tr>
    
        <tr>
            <td>50082</td>
            <td>Treasurer/Tax Collector/Public Administrator/County Clerk</td>
        </tr>
    
        <tr>
            <td>50083</td>
            <td>Treasurer/Tax Collector/Recorder</td>
        </tr>
    
        <tr>
            <td>50084</td>
            <td>Trustee</td>
        </tr>
    
        <tr>
            <td>50085</td>
            <td>Weed Recreation Board Member</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*category*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40000</td>
            <td>CATEGORY</td>
        </tr>
    
        <tr>
            <td>40001</td>
            <td>JOINTLY CONTROLLED</td>
        </tr>
    
        <tr>
            <td>40002</td>
            <td>CONTROLLED</td>
        </tr>
    
        <tr>
            <td>40003</td>
            <td>CAUCUS COMMITTEE</td>
        </tr>
    
        <tr>
            <td>40004</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*category_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p19-thumbnail.gif'></a><p>p. 19</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/20.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p20-thumbnail.gif'></a><p>p. 20</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40501</td>
            <td>LOCAL</td>
        </tr>
    
        <tr>
            <td>40502</td>
            <td>STATE</td>
        </tr>
    
        <tr>
            <td>40503</td>
            <td>COUNTY</td>
        </tr>
    
        <tr>
            <td>40504</td>
            <td>MULTI-COUNTY</td>
        </tr>
    
        <tr>
            <td>40505</td>
            <td>CITY</td>
        </tr>
    
        <tr>
            <td>40506</td>
            <td>FEDERAL</td>
        </tr>
    
        <tr>
            <td>40507</td>
            <td>SUPERIOR COURT JUDGE</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sub_category*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p18-thumbnail.gif'></a><p>p. 18</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40101</td>
            <td>PRIMARILY FORMED MEASURE</td>
        </tr>
    
        <tr>
            <td>40102</td>
            <td>PRIMARILY FORMED CANDIDATE</td>
        </tr>
    
        <tr>
            <td>40103</td>
            <td>GENERAL PURPOSE</td>
        </tr>
    
        <tr>
            <td>40104</td>
            <td>GENERAL PURPOSE POLITICAL PARTY</td>
        </tr>
    
        <tr>
            <td>40105</td>
            <td>GENERAL PURPOSE MEASURE</td>
        </tr>
    
        <tr>
            <td>40112</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*sub_category_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/18.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p18-thumbnail.gif'></a><p>p. 18</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/19.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p19-thumbnail.gif'></a><p>p. 19</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>40202</td>
            <td>BROAD-BASED</td>
        </tr>
    
        <tr>
            <td>40203</td>
            <td>SMALL CONTRIBUTOR</td>
        </tr>
    
        <tr>
            <td>40204</td>
            <td>MPO - NON PROFIT</td>
        </tr>
    
        <tr>
            <td>40205</td>
            <td>MPO - NON PROFIT CY</td>
        </tr>
    
        <tr>
            <td>40206</td>
            <td>MPO - OTHER</td>
        </tr>
    
        <tr>
            <td>40207</td>
            <td>MPO - OTHER CY</td>
        </tr>
    
        <tr>
            <td>40208</td>
            <td>FEDERAL PAC</td>
        </tr>
    
        <tr>
            <td>40209</td>
            <td>OUT OF STATE PAC</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*election_type*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/3.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p3-thumbnail.gif'></a><p>p. 3</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/4.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p4-thumbnail.gif'></a><p>p. 4</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>3001</td>
            <td>GENERAL</td>
        </tr>
    
        <tr>
            <td>3002</td>
            <td>PRIMARY</td>
        </tr>
    
        <tr>
            <td>3003</td>
            <td>RECALL</td>
        </tr>
    
        <tr>
            <td>3004</td>
            <td>SPECIAL ELECTION</td>
        </tr>
    
        <tr>
            <td>3005</td>
            <td>OFFICEHOLDER</td>
        </tr>
    
        <tr>
            <td>3006</td>
            <td>SPECIAL RUNOFF</td>
        </tr>
    
        <tr>
            <td>3010</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>3007</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*party_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p11-thumbnail.gif'></a><p>p. 11</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>16001</td>
            <td>DEMOCRATIC</td>
        </tr>
    
        <tr>
            <td>16002</td>
            <td>REPUBLICAN</td>
        </tr>
    
        <tr>
            <td>16003</td>
            <td>GREEN PARTY</td>
        </tr>
    
        <tr>
            <td>16004</td>
            <td>REFORM PARTY</td>
        </tr>
    
        <tr>
            <td>16005</td>
            <td>AMERICAN INDEPENDENT PARTY</td>
        </tr>
    
        <tr>
            <td>16006</td>
            <td>PEACE AND FREEDOM</td>
        </tr>
    
        <tr>
            <td>16007</td>
            <td>INDEPENDENT</td>
        </tr>
    
        <tr>
            <td>16008</td>
            <td>LIBERTARIAN</td>
        </tr>
    
        <tr>
            <td>16009</td>
            <td>NON PARTISAN</td>
        </tr>
    
        <tr>
            <td>16010</td>
            <td>NATURAL LAW</td>
        </tr>
    
        <tr>
            <td>16011</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>16012</td>
            <td>NO PARTY PREFERENCE</td>
        </tr>
    
        <tr>
            <td>16013</td>
            <td>AMERICANS ELECT</td>
        </tr>
    
        <tr>
            <td>16020</td>
            <td>PEACE AND FREEDOM</td>
        </tr>
    
        <tr>
            <td>16014</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>0</td>
            <td>UNKNOWN</td>
        </tr>
    
        <tr>
            <td>None</td>
            <td>NONE</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*county_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/14.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p14-thumbnail.gif'></a><p>p. 14</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/15.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p15-thumbnail.gif'></a><p>p. 15</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>18001</td>
            <td>01</td>
        </tr>
    
        <tr>
            <td>18002</td>
            <td>12</td>
        </tr>
    
        <tr>
            <td>18003</td>
            <td>23</td>
        </tr>
    
        <tr>
            <td>18004</td>
            <td>34</td>
        </tr>
    
        <tr>
            <td>18005</td>
            <td>45</td>
        </tr>
    
        <tr>
            <td>18006</td>
            <td>55</td>
        </tr>
    
        <tr>
            <td>18007</td>
            <td>56</td>
        </tr>
    
        <tr>
            <td>18008</td>
            <td>57</td>
        </tr>
    
        <tr>
            <td>18009</td>
            <td>58</td>
        </tr>
    
        <tr>
            <td>18010</td>
            <td>02</td>
        </tr>
    
        <tr>
            <td>18011</td>
            <td>03</td>
        </tr>
    
        <tr>
            <td>18012</td>
            <td>04</td>
        </tr>
    
        <tr>
            <td>18013</td>
            <td>05</td>
        </tr>
    
        <tr>
            <td>18014</td>
            <td>06</td>
        </tr>
    
        <tr>
            <td>18015</td>
            <td>07</td>
        </tr>
    
        <tr>
            <td>18016</td>
            <td>08</td>
        </tr>
    
        <tr>
            <td>18017</td>
            <td>09</td>
        </tr>
    
        <tr>
            <td>18018</td>
            <td>10</td>
        </tr>
    
        <tr>
            <td>18019</td>
            <td>11</td>
        </tr>
    
        <tr>
            <td>18020</td>
            <td>13</td>
        </tr>
    
        <tr>
            <td>18021</td>
            <td>14</td>
        </tr>
    
        <tr>
            <td>18022</td>
            <td>15</td>
        </tr>
    
        <tr>
            <td>18023</td>
            <td>16</td>
        </tr>
    
        <tr>
            <td>18024</td>
            <td>17</td>
        </tr>
    
        <tr>
            <td>18025</td>
            <td>18</td>
        </tr>
    
        <tr>
            <td>18026</td>
            <td>19</td>
        </tr>
    
        <tr>
            <td>18027</td>
            <td>20</td>
        </tr>
    
        <tr>
            <td>18028</td>
            <td>21</td>
        </tr>
    
        <tr>
            <td>18029</td>
            <td>22</td>
        </tr>
    
        <tr>
            <td>18030</td>
            <td>24</td>
        </tr>
    
        <tr>
            <td>18031</td>
            <td>25</td>
        </tr>
    
        <tr>
            <td>18032</td>
            <td>26</td>
        </tr>
    
        <tr>
            <td>18033</td>
            <td>27</td>
        </tr>
    
        <tr>
            <td>18034</td>
            <td>28</td>
        </tr>
    
        <tr>
            <td>18035</td>
            <td>29</td>
        </tr>
    
        <tr>
            <td>18036</td>
            <td>30</td>
        </tr>
    
        <tr>
            <td>18037</td>
            <td>31</td>
        </tr>
    
        <tr>
            <td>18038</td>
            <td>32</td>
        </tr>
    
        <tr>
            <td>18039</td>
            <td>33</td>
        </tr>
    
        <tr>
            <td>18040</td>
            <td>35</td>
        </tr>
    
        <tr>
            <td>18041</td>
            <td>36</td>
        </tr>
    
        <tr>
            <td>18042</td>
            <td>37</td>
        </tr>
    
        <tr>
            <td>18043</td>
            <td>38</td>
        </tr>
    
        <tr>
            <td>18044</td>
            <td>39</td>
        </tr>
    
        <tr>
            <td>18045</td>
            <td>40</td>
        </tr>
    
        <tr>
            <td>18046</td>
            <td>41</td>
        </tr>
    
        <tr>
            <td>18047</td>
            <td>42</td>
        </tr>
    
        <tr>
            <td>18048</td>
            <td>43</td>
        </tr>
    
        <tr>
            <td>18049</td>
            <td>44</td>
        </tr>
    
        <tr>
            <td>18050</td>
            <td>46</td>
        </tr>
    
        <tr>
            <td>18051</td>
            <td>47</td>
        </tr>
    
        <tr>
            <td>18052</td>
            <td>48</td>
        </tr>
    
        <tr>
            <td>18053</td>
            <td>49</td>
        </tr>
    
        <tr>
            <td>18054</td>
            <td>50</td>
        </tr>
    
        <tr>
            <td>18055</td>
            <td>51</td>
        </tr>
    
        <tr>
            <td>18056</td>
            <td>52</td>
        </tr>
    
        <tr>
            <td>18057</td>
            <td>53</td>
        </tr>
    
        <tr>
            <td>18058</td>
            <td>54</td>
        </tr>
    
    </tbody>
    </table>
    </div>

*district_cd*


*Lookup-Codes-Cd*

.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/11.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p11-thumbnail.gif'></a><p>p. 11</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2774529-Lookup-Codes-Cd/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2774529/pages/Lookup-Codes-Cd-p13-thumbnail.gif'></a><p>p. 13</p></div></div>




.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>0</td>
            <td>N/A</td>
        </tr>
    
        <tr>
            <td>17001</td>
            <td>01</td>
        </tr>
    
        <tr>
            <td>17002</td>
            <td>13</td>
        </tr>
    
        <tr>
            <td>17003</td>
            <td>24</td>
        </tr>
    
        <tr>
            <td>17004</td>
            <td>35</td>
        </tr>
    
        <tr>
            <td>17005</td>
            <td>46</td>
        </tr>
    
        <tr>
            <td>17006</td>
            <td>57</td>
        </tr>
    
        <tr>
            <td>17007</td>
            <td>68</td>
        </tr>
    
        <tr>
            <td>17008</td>
            <td>79</td>
        </tr>
    
        <tr>
            <td>17009</td>
            <td>02</td>
        </tr>
    
        <tr>
            <td>17010</td>
            <td>05</td>
        </tr>
    
        <tr>
            <td>17011</td>
            <td>04</td>
        </tr>
    
        <tr>
            <td>17013</td>
            <td>06</td>
        </tr>
    
        <tr>
            <td>17014</td>
            <td>07</td>
        </tr>
    
        <tr>
            <td>17015</td>
            <td>08</td>
        </tr>
    
        <tr>
            <td>17016</td>
            <td>19</td>
        </tr>
    
        <tr>
            <td>17017</td>
            <td>10</td>
        </tr>
    
        <tr>
            <td>17018</td>
            <td>11</td>
        </tr>
    
        <tr>
            <td>17019</td>
            <td>12</td>
        </tr>
    
        <tr>
            <td>17020</td>
            <td>14</td>
        </tr>
    
        <tr>
            <td>17021</td>
            <td>15</td>
        </tr>
    
        <tr>
            <td>17022</td>
            <td>16</td>
        </tr>
    
        <tr>
            <td>17023</td>
            <td>17</td>
        </tr>
    
        <tr>
            <td>17024</td>
            <td>18</td>
        </tr>
    
        <tr>
            <td>17026</td>
            <td>20</td>
        </tr>
    
        <tr>
            <td>17027</td>
            <td>21</td>
        </tr>
    
        <tr>
            <td>17028</td>
            <td>22</td>
        </tr>
    
        <tr>
            <td>17029</td>
            <td>23</td>
        </tr>
    
        <tr>
            <td>17030</td>
            <td>25</td>
        </tr>
    
        <tr>
            <td>17031</td>
            <td>26</td>
        </tr>
    
        <tr>
            <td>17032</td>
            <td>27</td>
        </tr>
    
        <tr>
            <td>17033</td>
            <td>28</td>
        </tr>
    
        <tr>
            <td>17034</td>
            <td>29</td>
        </tr>
    
        <tr>
            <td>17035</td>
            <td>30</td>
        </tr>
    
        <tr>
            <td>17036</td>
            <td>31</td>
        </tr>
    
        <tr>
            <td>17037</td>
            <td>32</td>
        </tr>
    
        <tr>
            <td>17038</td>
            <td>33</td>
        </tr>
    
        <tr>
            <td>17039</td>
            <td>34</td>
        </tr>
    
        <tr>
            <td>17040</td>
            <td>36</td>
        </tr>
    
        <tr>
            <td>17041</td>
            <td>37</td>
        </tr>
    
        <tr>
            <td>17042</td>
            <td>38</td>
        </tr>
    
        <tr>
            <td>17043</td>
            <td>39</td>
        </tr>
    
        <tr>
            <td>17044</td>
            <td>40</td>
        </tr>
    
        <tr>
            <td>17045</td>
            <td>41</td>
        </tr>
    
        <tr>
            <td>17046</td>
            <td>42</td>
        </tr>
    
        <tr>
            <td>17047</td>
            <td>43</td>
        </tr>
    
        <tr>
            <td>17048</td>
            <td>44</td>
        </tr>
    
        <tr>
            <td>17049</td>
            <td>45</td>
        </tr>
    
        <tr>
            <td>17050</td>
            <td>47</td>
        </tr>
    
        <tr>
            <td>17051</td>
            <td>48</td>
        </tr>
    
        <tr>
            <td>17052</td>
            <td>49</td>
        </tr>
    
        <tr>
            <td>17053</td>
            <td>50</td>
        </tr>
    
        <tr>
            <td>17054</td>
            <td>51</td>
        </tr>
    
        <tr>
            <td>17055</td>
            <td>52</td>
        </tr>
    
        <tr>
            <td>17056</td>
            <td>53</td>
        </tr>
    
        <tr>
            <td>17057</td>
            <td>54</td>
        </tr>
    
        <tr>
            <td>17058</td>
            <td>55</td>
        </tr>
    
        <tr>
            <td>17059</td>
            <td>56</td>
        </tr>
    
        <tr>
            <td>17060</td>
            <td>03</td>
        </tr>
    
        <tr>
            <td>17061</td>
            <td>59</td>
        </tr>
    
        <tr>
            <td>17062</td>
            <td>60</td>
        </tr>
    
        <tr>
            <td>17063</td>
            <td>61</td>
        </tr>
    
        <tr>
            <td>17064</td>
            <td>62</td>
        </tr>
    
        <tr>
            <td>17065</td>
            <td>63</td>
        </tr>
    
        <tr>
            <td>17066</td>
            <td>64</td>
        </tr>
    
        <tr>
            <td>17067</td>
            <td>65</td>
        </tr>
    
        <tr>
            <td>17068</td>
            <td>66</td>
        </tr>
    
        <tr>
            <td>17069</td>
            <td>67</td>
        </tr>
    
        <tr>
            <td>17070</td>
            <td>69</td>
        </tr>
    
        <tr>
            <td>17071</td>
            <td>70</td>
        </tr>
    
        <tr>
            <td>17072</td>
            <td>71</td>
        </tr>
    
        <tr>
            <td>17073</td>
            <td>72</td>
        </tr>
    
        <tr>
            <td>17074</td>
            <td>73</td>
        </tr>
    
        <tr>
            <td>17075</td>
            <td>74</td>
        </tr>
    
        <tr>
            <td>17076</td>
            <td>75</td>
        </tr>
    
        <tr>
            <td>17077</td>
            <td>76</td>
        </tr>
    
        <tr>
            <td>17078</td>
            <td>77</td>
        </tr>
    
        <tr>
            <td>17079</td>
            <td>78</td>
        </tr>
    
        <tr>
            <td>17080</td>
            <td>80</td>
        </tr>
    
        <tr>
            <td>17081</td>
            <td>09</td>
        </tr>
    
        <tr>
            <td>17090</td>
            <td>58</td>
        </tr>
    
        <tr>
            <td>17091</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17083</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17093</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17094</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17088</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17096</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17012</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17095</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17092</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17086</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17099</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17082</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17025</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17085</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17084</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17087</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17098</td>
            <td>Unknown</td>
        </tr>
    
        <tr>
            <td>17089</td>
            <td>Unknown</td>
        </tr>
    
    </tbody>
    </table>
    </div>




FilerTypePeriodsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table and its fields are listed in the official CAL-ACCESS documentation,
but is not fully explained. The table's description contains this note: "J M needs
to document. This is in his list of tables designed for future enhancements."

**Sample:** `FILER_TYPE_PERIODS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TYPE_PERIODS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/8.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p8-thumbnail.gif'></a><p>p. 8</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p71-thumbnail.gif'></a><p>p. 71</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>election_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Election type</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer type identification number.</td>
        </tr>
    
    
    
        <tr>
            <td>period_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Period identification number.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilerTypesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This lookup table describes filer types.

**Sample:** `FILER_TYPES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_TYPES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/71.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p71-thumbnail.gif'></a><p>p. 71</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p72-thumbnail.gif'></a><p>p. 72</p></div></div>





Fields
^^^^^^

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
    
    
        <tr>
            <td>filer_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer type identification number</td>
        </tr>
    
    
    
        <tr>
            <td>description</td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Description of the filer type</td>
        </tr>
    
    
    
        <tr>
            <td>grp_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Group type assocated with the filer type</td>
        </tr>
    
    
    
        <tr>
            <td>calc_use</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Use checkbox flag</td>
        </tr>
    
    
    
        <tr>
            <td>grace_period</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilerXrefCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table maps legacy filer identification numbers to the system's filer
identification numbers. Although 60 percent of the FILER_ID and XREF_ID values
are equal.

**Sample:** `FILER_XREF_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILER_XREF_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/72.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p72-thumbnail.gif'></a><p>p. 72</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>xref_id</td>
            <td>String (up to 32)</td>
            <td>Yes</td>
            <td>Alternative filer ID found on many forms</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>migration_source</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Source of the XREF_ID. Migration or generated by the AMS.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilersCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table is the parent table from which all links and associations
to a filer are derived.

**Sample:** `FILERS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILERS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/9.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p9-thumbnail.gif'></a><p>p. 9</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/73.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p73-thumbnail.gif'></a><p>p. 73</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


FilingPeriodCd
~~~~~~~~~~~~~~~~~~~~~~~~~

An undocumented table that contains metadata for a variety
of filing periods.

**Sample:** `FILING_PERIOD_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/FILING_PERIOD_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/74.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p74-thumbnail.gif'></a><p>p. 74</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/75.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p75-thumbnail.gif'></a><p>p. 75</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>period_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique period identification number</td>
        </tr>
    
    
    
        <tr>
            <td>start_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Starting date for period</td>
        </tr>
    
    
    
        <tr>
            <td>end_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Ending date of period</td>
        </tr>
    
    
    
        <tr>
            <td>period_type</td>
            <td>Integer</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>per_grp_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Period group type</td>
        </tr>
    
    
    
        <tr>
            <td>period_desc</td>
            <td>String (up to 255)</td>
            <td>No</td>
            <td>Period description</td>
        </tr>
    
    
    
        <tr>
            <td>deadline</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Deadline date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*period_type*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>1500</td>
            <td>Standard period</td>
        </tr>
    
        <tr>
            <td>1501</td>
            <td>Non-standard period</td>
        </tr>
    
    </tbody>
    </table>
    </div>




GroupTypesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This lookup table stores group type information. Most (but not all) of the GRP_ID/
GRP_NAME value pairs in this table match the FILER_TYPE/DESCRIPTION value pairs in
the FILER_TYPE_CD table.

**Sample:** `GROUP_TYPES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/GROUP_TYPES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/78.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p78-thumbnail.gif'></a><p>p. 78</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/79.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p79-thumbnail.gif'></a><p>p. 79</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>grp_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Group identification number</td>
        </tr>
    
    
    
        <tr>
            <td>grp_name</td>
            <td>String (up to 28)</td>
            <td>No</td>
            <td>Group name. Many of the values in this column are empty strings.</td>
        </tr>
    
    
    
        <tr>
            <td>grp_desc</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Group Description. This column contains only empty strings.</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


ImageLinksCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table links images to filers and accounts.

**Sample:** `IMAGE_LINKS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/IMAGE_LINKS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/80.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p80-thumbnail.gif'></a><p>p. 80</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>img_link_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Image link identification number</td>
        </tr>
    
    
    
        <tr>
            <td>img_link_type</td>
            <td>Integer</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>img_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Image identification number</td>
        </tr>
    
    
    
        <tr>
            <td>img_type</td>
            <td>Integer</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    
        <tr>
            <td>img_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td></td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LegislativeSessionsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

Legislative session, begin and end dates look up table.

**Sample:** `LEGISLATIVE_SESSIONS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LEGISLATIVE_SESSIONS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/10.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p10-thumbnail.gif'></a><p>p. 10</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/84.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p84-thumbnail.gif'></a><p>p. 84</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>begin_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Session start date</td>
        </tr>
    
    
    
        <tr>
            <td>end_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Session end date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


LookupCodesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

The description of some lookup codes in the system.

**Sample:** `LOOKUP_CODES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/LOOKUP_CODES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/12.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p12-thumbnail.gif'></a><p>p. 12</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/106.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p106-thumbnail.gif'></a><p>p. 106</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>code_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>code_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>The code&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>code_desc</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Code description</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


NamesCd
~~~~~~~~~~~~~~~~~~~~~~~~~

The name of all entities in the system. Used for searches when
the name has an identification number.

**Sample:** `NAMES_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/NAMES_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/112.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p112-thumbnail.gif'></a><p>p. 112</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>namid</td>
            <td>Integer</td>
            <td>No</td>
            <td>Identification number unique to the name</td>
        </tr>
    
    
    
        <tr>
            <td>naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name</td>
        </tr>
    
    
    
        <tr>
            <td>namf</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>First name</td>
        </tr>
    
    
    
        <tr>
            <td>namt</td>
            <td>String (up to 100)</td>
            <td>No</td>
            <td>Name title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>nams</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Name suffix</td>
        </tr>
    
    
    
        <tr>
            <td>moniker</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Entity&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>moniker_pos</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Location of the entity&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>namm</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Middle name</td>
        </tr>
    
    
    
        <tr>
            <td>fullname</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Full name</td>
        </tr>
    
    
    
        <tr>
            <td>naml_search</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Last name</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


ReceivedFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This table is undocumented.

**Sample:** `RECEIVED_FILINGS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/RECEIVED_FILINGS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/121.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p121-thumbnail.gif'></a><p>p. 121</p></div></div>




Filing Forms
^^^^^^^^^^^^
ReceivedFilingsCd contains data collected from the following filing forms, form parts and schedules:



* `Form 400 <filingforms.html#form-400>`_ (Statement of Organization (Slate Mailer Organization))



* `Form 401 <filingforms.html#form-401>`_ (Slate Mailer Organization Campaign Statement)



* `Form 402 <filingforms.html#form-402>`_ (Statement of Termination (Slate Mailer Organization))



* `Form 410 <filingforms.html#form-410>`_ (Statement of Organization Recipient Committee)



* `Form 425 <filingforms.html#form-425>`_ (Semi-Annual Statement of no Activity)



* `Form 450 <filingforms.html#form-450>`_ (Recipient Committee Campaign Disclosure Statement - Short Form)



* `Form 460 <filingforms.html#form-460>`_ (Recipient Committee Campaign Statement)



* `Form 461 <filingforms.html#form-461>`_ (Independent Expenditure Committee & Major Donor Committee Campaign Statement)



* `Form 465 <filingforms.html#form-465>`_ (Supplemental Independent Expenditure Report)



* `Form 496 <filingforms.html#form-496>`_ (Late Independent Expenditure Report)



* `Form 497 <filingforms.html#form-497>`_ (Late Contribution Report)



* `Form 498 <filingforms.html#form-498>`_ (Slate Mailer Late Payment Report)



* `Form 601 <filingforms.html#form-601>`_ (Lobbying Firm Registration Statement)



* `Form 602 <filingforms.html#form-602>`_ (Lobbying Firm Activity Authorization)



* `Form 603 <filingforms.html#form-603>`_ (Lobbyist Employer or Lobbying Coalition Registration Statement)



* `Form 604 <filingforms.html#form-604>`_ (Lobbyist Certification Statement)



* `Form 606 <filingforms.html#form-606>`_ (Notice of Termination)



* `Form 607 <filingforms.html#form-607>`_ (Notice of Withdrawal)



* `Form 615 <filingforms.html#form-615>`_ (Lobbyist Report)



* `Form 625 <filingforms.html#form-625>`_ (Report of Lobbying Firm)



* `Form 635 <filingforms.html#form-635>`_ (Report of Lobbyist Employer or Report of Lobbying Coalition)



* `Form 645 <filingforms.html#form-645>`_ (Report of Person Spending $5,000 or More)




Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_file_name</td>
            <td>String (up to 14)</td>
            <td>No</td>
            <td>The field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>received_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Date received</td>
        </tr>
    
    
    
        <tr>
            <td>filing_directory</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_id</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td>receive_comment</td>
            <td>String (up to 51)</td>
            <td>No</td>
            <td>A comment</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Look-up Codes
^^^^^^^^^^^^^

*form_id*


.. raw:: html

    <div class="wy-table-responsive">
    <table border="1" class="docutils">
    <thead valign="bottom">
        <tr>
            <th class="head">Code</th>
            <th class="head">Definition</th>
        </tr>
    </thead>
    <tbody valign="top">
    
        <tr>
            <td>F400</td>
            <td>Form 400: Statement of Organization (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F401</td>
            <td>Form 401: Slate Mailer Organization Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F402</td>
            <td>Form 402: Statement of Termination (Slate Mailer Organization)</td>
        </tr>
    
        <tr>
            <td>F410</td>
            <td>Form 410: Statement of Organization Recipient Committee</td>
        </tr>
    
        <tr>
            <td>F425</td>
            <td>Form 425: Semi-Annual Statement of no Activity</td>
        </tr>
    
        <tr>
            <td>F450</td>
            <td>Form 450: Recipient Committee Campaign Disclosure Statement - Short Form</td>
        </tr>
    
        <tr>
            <td>F460</td>
            <td>Form 460: Recipient Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F461</td>
            <td>Form 461: Independent Expenditure Committee &amp; Major Donor Committee Campaign Statement</td>
        </tr>
    
        <tr>
            <td>F465</td>
            <td>Form 465: Supplemental Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F496</td>
            <td>Form 496: Late Independent Expenditure Report</td>
        </tr>
    
        <tr>
            <td>F497</td>
            <td>Form 497: Late Contribution Report</td>
        </tr>
    
        <tr>
            <td>F498</td>
            <td>Form 498: Slate Mailer Late Payment Report</td>
        </tr>
    
        <tr>
            <td>F601</td>
            <td>Form 601: Lobbying Firm Registration Statement</td>
        </tr>
    
        <tr>
            <td>F602</td>
            <td>Form 602: Lobbying Firm Activity Authorization</td>
        </tr>
    
        <tr>
            <td>F603</td>
            <td>Form 603: Lobbyist Employer or Lobbying Coalition Registration Statement</td>
        </tr>
    
        <tr>
            <td>F604</td>
            <td>Form 604: Lobbyist Certification Statement</td>
        </tr>
    
        <tr>
            <td>F606</td>
            <td>Form 606: Notice of Termination</td>
        </tr>
    
        <tr>
            <td>F607</td>
            <td>Form 607: Notice of Withdrawal</td>
        </tr>
    
        <tr>
            <td>F615</td>
            <td>Form 615: Lobbyist Report</td>
        </tr>
    
        <tr>
            <td>F625</td>
            <td>Form 625: Report of Lobbying Firm</td>
        </tr>
    
        <tr>
            <td>F635</td>
            <td>Form 635: Report of Lobbyist Employer or Report of Lobbying Coalition</td>
        </tr>
    
        <tr>
            <td>F645</td>
            <td>Form 645: Report of Person Spending $5,000 or More</td>
        </tr>
    
    </tbody>
    </table>
    </div>




ReportsCd
~~~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Sample:** `REPORTS_CD.TSV <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/REPORTS_CD.TSV>`_


Source Docs
^^^^^^^^^^^

*CalAccessTablesWeb*


.. raw:: html

    <div class="doc_pages_container"><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/13.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p13-thumbnail.gif'></a><p>p. 13</p></div><div class="doc_page_frame"><a class="reference external image-reference" href="https://www.documentcloud.org/documents/2711614-CalAccessTablesWeb/pages/122.html"><img class='doc_page' src='https://assets.documentcloud.org/documents/2711614/pages/CalAccessTablesWeb-p122-thumbnail.gif'></a><p>p. 122</p></div></div>





Fields
^^^^^^

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
    
    
    
    
        <tr>
            <td>rpt_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_name</td>
            <td>String (up to 74)</td>
            <td>No</td>
            <td>Name of the report</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_desc_field</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Description of the report</td>
        </tr>
    
    
    
        <tr>
            <td>path</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Report path</td>
        </tr>
    
    
    
        <tr>
            <td>data_object</td>
            <td>String (up to 38)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>parms_flg_y_n</td>
            <td>Integer</td>
            <td>No</td>
            <td>Parameters indication flag</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Type of the report</td>
        </tr>
    
    
    
        <tr>
            <td>parm_definition</td>
            <td>Integer</td>
            <td>No</td>
            <td>Parameter definition</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>




Empty files
-----------

The following tables are described in the official documentation, but the .TSV files of the same name are empty.

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
    
        <tr>
            <td>campaign</td>
            <td>CvrF470Cd</td>
        </tr>
    
        <tr>
            <td>other</td>
            <td>FilerTypePeriodsCd</td>
        </tr>
    
        <tr>
            <td>lobbying</td>
            <td>LobbyistEmployerHistoryCd</td>
        </tr>
    
        <tr>
            <td>lobbying</td>
            <td>LobbyistFirmHistoryCd</td>
        </tr>
    
    </tbody>
    </table>
    </div>