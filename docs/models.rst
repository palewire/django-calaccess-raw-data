Database tables
===============

The 76 tab-delimited database exports published by California's Secretary of State and loaded by this Django application.

.. warning::

    Most definitions below are drawn from the spotty and incomplete
    `official documentation <http://django-calaccess-raw-data.californiacivicdata.org/en/latest/officialdocumentation.html>`_ verbatim. As we continue our research, we plan to improve the descriptions.

    For the time being, to be absolutely certain about
    what each table and field contains, you should compare the electronic data back to
    the original paper records published by the state.



Campaign tables
---------------------------


Cvr2CampaignDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~

Record used to carry additional names for the campaign
disclosure forms below.

**Source:** `CVR2_CAMPAIGN_DISCLOSURE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code</td>
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
            <td>Part of 460 cover page coded on ths cvr2 record. Legal values are 3, 4a, 4b, 5a, 5b, or 6.</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Office code: Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
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

Cvr2SoCd
~~~~~~~~~~~~~~~~~~~~~~~

Additional names and committees information included on the second page
of a statement of organization creation form filed
by a slate-mailer organization or recipient committee.

**Source:** `CVR2_SO_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 194)</td>
            <td>No</td>
            <td>Entity&#39;s business name or last name if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 34)</td>
            <td>No</td>
            <td>Entity&#39;s first name if the entity is an individual</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 9)</td>
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
            <td>String (up to 25)</td>
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
            <td>String (up to 40)</td>
            <td>No</td>
            <td>Email address. Not contained in current forms.</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Committee ID: Entity&#39;s identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ind_group</td>
            <td>String (up to 87)</td>
            <td>No</td>
            <td>Industry group/affiliation description</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Office code: Identifies the office being sought</td>
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
            <td>Office is sought or held code</td>
        </tr>
    
    
    
        <tr>
            <td>non_pty_cb</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Non-partisan check-box. Legal values are &#39;X&#39; and null.</td>
        </tr>
    
    
    
        <tr>
            <td>party_name</td>
            <td>String (up to 63)</td>
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
            <td>String (up to 44)</td>
            <td>No</td>
            <td>Position/title of the principal officer</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Cvr3VerificationInfoCd
~~~~~~~~~~~~~~~~~~~~~~~

Cover page verification information from campaign disclosure forms

**Source:** `CVR3_VERIFICATION_INFO_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>sig_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Signed date: Date when signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_loc</td>
            <td>String (up to 39)</td>
            <td>No</td>
            <td>Signed location: City and state where signed</td>
        </tr>
    
    
    
        <tr>
            <td>sig_naml</td>
            <td>String (up to 56)</td>
            <td>No</td>
            <td>Last name: Last name of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>First name: First name of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Title: Title of the signer</td>
        </tr>
    
    
    
        <tr>
            <td>sig_nams</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Suffix: Suffix of the signer</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

CvrCampaignDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~

Cover page information from campaign disclosure forms

**Source:** `CVR_CAMPAIGN_DISCLOSURE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>This field is undocumented</td>
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
            <td>This field is not documented</td>
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
            <td>Committee ID: Committee ID (Filer_id) of recipient Committee who&#39;s campaign statement is attached. This field applies to the form 401.</td>
        </tr>
    
    
    
        <tr>
            <td>cmtte_type</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Committee type: Type of Recipient Committee. Applies to the 450/460.</td>
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
            <td>Date (with time)</td>
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
            <td>Entity code</td>
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
            <td>Filer ID: Filer&#39;s unique identification number</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>Date (with time)</td>
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
            <td>Office code: Identifies the office being sought</td>
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
            <td>Record type</td>
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
            <td>Date (with time)</td>
            <td>No</td>
            <td>Date this report was filed, according to the filer</td>
        </tr>
    
    
    
        <tr>
            <td>rptfromdt</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement - Period from date.</td>
        </tr>
    
    
    
        <tr>
            <td>rptthrudt</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>Attached campaign disclosure statement - Period through date.</td>
        </tr>
    
    
    
        <tr>
            <td>selfemp_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Self employed check-box</td>
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
            <td>Date (with time)</td>
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

CvrSoCd
~~~~~~~~~~~~~~~~~~~~~~~

Cover page for a statement of organization creation or termination
form filed by a slate-mailer organization or recipient committee.

**Source:** `CVR_SO_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>acct_opendt</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>actvty_lvl</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Activity level: Organization&#39;s level of activity</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>bank_adr1</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>bank_adr2</td>
            <td>String (up to 55)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>bank_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>bank_nam</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>bank_phon</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>bank_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>bank_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>brdbase_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_email</td>
            <td>String (up to 60)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>cmte_fax</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>com82013id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>com82013nm</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>com82013yn</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>control_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>county_act</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>county_res</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>gpc_descr</td>
            <td>String (up to 300)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>mail_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>mail_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>mail_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>phone</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>primfc_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>qualfy_dt</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>Date qualified: Date qualified as an organization</td>
        </tr>
    
    
    
        <tr>
            <td>qual_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record type</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>smcont_qualdt</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>sponsor_cb</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>surplusdsp</td>
            <td>String (up to 90)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>term_date</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
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
            <td>This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

DebtCd
~~~~~~~~~~~~~~~~~~~~~~~

Form 460 (Recipient Committee Campaign Statement)
Schedule (F) Accrued Expenses (Unpaid Bills) records

**Source:** `DEBT_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code: Entity code of the payee</td>
        </tr>
    
    
    
        <tr>
            <td>expn_code</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Expense code</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Expense description: Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number of the parent filing</td>
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
            <td>Record type: Record type value: DEBT</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Transaction ID: Transaction identifier - permanent value unique to this item</td>
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

ExpnCd
~~~~~~~~~~~~~~~~~~~~~~~

Campaign expenditures from a variety of forms

**Source:** `EXPN_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code</td>
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
            <td>Expense code: CTB &amp; IND need explanation &amp; listing on Sched D TRC &amp; TRS require explanation</td>
        </tr>
    
    
    
        <tr>
            <td>expn_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Expense date: Date of Expenditure (Note: Date not on Sched E &amp; G)</td>
        </tr>
    
    
    
        <tr>
            <td>expn_dscr</td>
            <td>String (up to 400)</td>
            <td>No</td>
            <td>Espense description: Purpose of expense and/or description/explanation</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Office Jurisdiction Code Values: STW=Statewide;         SEN=Senate District; ASM=Assembly District;         BOE=Board of Equalization District;         CIT=City; CTY=County; LOC=Local; OTH=Other</td>
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
            <td>Office code: Identifies the office being sought</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
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

F495P2Cd
~~~~~~~~~~~~~~~~~~~~~~~

F495 Supplemental Preelection Campaign Statement

It's attatchment to the forms below

    F450 Recipient Committee Campaign Statement Short Form
    F460 Recipient Committee Campaign Statement

Form 495 is for use by a recipient committee that
makes contributions totaling $10,000 or more in
connection with an election for which the committee
is not required to file regular preelection reports.
Form 495 is filed as an attachment to a campaign
disclosure statement (Form 450 or 460). On the
Form 450 or 460, the committee will report all
contributions received and expenditures made since
its last report.

**Source:** `F495P2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
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

F501502Cd
~~~~~~~~~~~~~~~~~~~~~~~

Candidate intention statement

**Source:** `F501_502_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record type</td>
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
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>committee_id</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Committee ID: Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>report_num</td>
            <td>Integer</td>
            <td>No</td>
            <td>Report Number; 000 Original; 001-999 Amended</td>
        </tr>
    
    
    
        <tr>
            <td>rpt_date</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>Date this report is filed</td>
        </tr>
    
    
    
        <tr>
            <td>stmt_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Statement type</td>
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
            <td>String (up to 81)</td>
            <td>No</td>
            <td>Candidate/officerholder last name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namf</td>
            <td>String (up to 25)</td>
            <td>No</td>
            <td>Candidate/officerholder first name</td>
        </tr>
    
    
    
        <tr>
            <td>can_namm</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Candidate/officeholder middle name</td>
        </tr>
    
    
    
        <tr>
            <td>cand_namt</td>
            <td>String (up to 7)</td>
            <td>No</td>
            <td>Candidate/officerholder title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>cand_nams</td>
            <td>String (up to 7)</td>
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
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Candidate/officeholder&#39;s moniker</td>
        </tr>
    
    
    
        <tr>
            <td>cand_city</td>
            <td>String (up to 22)</td>
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
            <td>String (up to 14)</td>
            <td>No</td>
            <td>Candidate/officeholder phone number</td>
        </tr>
    
    
    
        <tr>
            <td>cand_fax</td>
            <td>String (up to 14)</td>
            <td>No</td>
            <td>Candidate/officerholder fax</td>
        </tr>
    
    
    
        <tr>
            <td>cand_email</td>
            <td>String (up to 37)</td>
            <td>No</td>
            <td>Candidate/officeholder email address</td>
        </tr>
    
    
    
        <tr>
            <td>fin_naml</td>
            <td>String (up to 53)</td>
            <td>No</td>
            <td>Financial institution&#39;s business name</td>
        </tr>
    
    
    
        <tr>
            <td>fin_namf</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Unused. Financial institution&#39;s first name.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_namt</td>
            <td>String (up to 32)</td>
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
            <td>String (up to 20)</td>
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
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Financial institution&#39;s zip code.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_phon</td>
            <td>String (up to 14)</td>
            <td>No</td>
            <td>Financial institution&#39;s phone number.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_fax</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Financial institution&#39;s FAX Number.</td>
        </tr>
    
    
    
        <tr>
            <td>fin_email</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Financial institution&#39;s e-mail address.</td>
        </tr>
    
    
    
        <tr>
            <td>office_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Office code: Identifies the office being sought</td>
        </tr>
    
    
    
        <tr>
            <td>offic_dscr</td>
            <td>String (up to 50)</td>
            <td>No</td>
            <td>Office sought description</td>
        </tr>
    
    
    
        <tr>
            <td>agency_nam</td>
            <td>String (up to 63)</td>
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
            <td>String (up to 14)</td>
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
            <td>String (up to 20)</td>
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
            <td>Date (with time)</td>
            <td>No</td>
            <td>Execution date</td>
        </tr>
    
    
    
        <tr>
            <td>can_sig</td>
            <td>String (up to 13)</td>
            <td>No</td>
            <td>Candidate signature</td>
        </tr>
    
    
    
        <tr>
            <td>account_no</td>
            <td>String (up to 22)</td>
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

LoanCd
~~~~~~~~~~~~~~~~~~~~~~~

Loans received and made

**Source:** `LOAN_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Committee ID: Committee identification number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Transaction ID: Permanent value unique to this item</td>
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

RcptCd
~~~~~~~~~~~~~~~~~~~~~~~

Receipts schedules for the following forms.

    Form 460 (Recipient Committee Campaign Statement)
    Schedules A, C, I, and A-1.

    Form 401 (Slate Mailer Organization Campaign Statement) Schedule A.

**Source:** `RCPT_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code: Values [CMO|RCP|IND|OTH]</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Office code: Identifies the office being sought</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>tran_type</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Transaction Type: Values T- third party | F Forgiven loan | R Returned (Negative amount)</td>
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

S401Cd
~~~~~~~~~~~~~~~~~~~~~~~

This table contains Form 401 (Slate Mailer Organization) payment and other
disclosure schedule (F401B, F401B-1, F401C, F401D) information.

**Source:** `S401_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
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
            <td>Office code: Identifies the office being sought</td>
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

S496Cd
~~~~~~~~~~~~~~~~~~~~~~~

Form 496 Late Independent Expenditures

**Source:** `S496_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
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

S497Cd
~~~~~~~~~~~~~~~~~~~~~~~

Form 497: Late Contributions Received/Made

**Source:** `S497_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>enty_naml</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Entity&#39;s last name or business name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namf</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>Entity&#39;s first name</td>
        </tr>
    
    
    
        <tr>
            <td>enty_namt</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity&#39;s title or prefix</td>
        </tr>
    
    
    
        <tr>
            <td>enty_nams</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Entity&#39;s suffix</td>
        </tr>
    
    
    
        <tr>
            <td>enty_city</td>
            <td>String (up to 30)</td>
            <td>No</td>
            <td>Filing committee&#39;s city address</td>
        </tr>
    
    
    
        <tr>
            <td>enty_st</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>Filing committee&#39;s state address</td>
        </tr>
    
    
    
        <tr>
            <td>enty_zip4</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>Filing committee&#39;s ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>ctrib_emp</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Employer</td>
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
            <td>Self employed checkbox. &quot;X&quot; indicates the contributor is self-employed.</td>
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
            <td>Committee ID: Committee identification number</td>
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
            <td>Office code: Identifies the office being sought</td>
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
            <td>Jurisdiction code</td>
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

S498Cd
~~~~~~~~~~~~~~~~~~~~~~~

Form 498: Slate Mailer Late Independent Expenditures Made

**Source:** `S498_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
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
            <td>Committee ID: Committee identification number</td>
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
            <td>Office code: Identifies the office being sought</td>
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

SpltCd
~~~~~~~~~~~~~~~~~~~~~~~

Split records

**Source:** `SPLT_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>elec_amount</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>elec_code</td>
            <td>String (up to 2)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>elec_date</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>This field is undocumented</td>
        </tr>
    
    
    
        <tr>
            <td>ptran_id</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Common tables
---------------------------


CvrE530Cd
~~~~~~~~~~~~~~~~~~~~~~~

This table method is undocumented.

**Source:** `CVR_E530_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record type</td>
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
            <td>Filer state</td>
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
            <td>Office code: Identifies the office being sought</td>
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

FilerFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~

Key table that links filers to their paper, key data entry, legacy,
and electronic filings. This table is used as an index to locate
filing information.

**Source:** `FILER_FILINGS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Form type: Form identification code</td>
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
            <td>Statement type: Type of statement</td>
        </tr>
    
    
    
        <tr>
            <td>stmnt_status</td>
            <td>Integer</td>
            <td>No</td>
            <td>Statement status: The status of the statement. If the filing has been reviewed or not reviewed.</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>user_id</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>User ID: User identifier of the PRD user who logged the filing</td>
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

FilernameCd
~~~~~~~~~~~~~~~~~~~~~~~

A combination of CAL-ACCESS tables to provide the analyst with
filer information.

Full name of all PACs, firms, and employers are in the last
name field.

Major donors can be split between first and last name fields, but usually
are contained in the last name field only. Individual names of lobbyists,
candidates/officeholders, treasurers/responsible officers, and major donors
(when they are only an individual's name) use both the first and last name
fields in conjunction.

**Source:** `FILERNAME_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>xref_filer_id</td>
            <td>String (up to 15)</td>
            <td>No</td>
            <td>Crossreference filer ID: Alternative filer ID found on many forms</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>String (up to 45)</td>
            <td>No</td>
            <td>The type of filer</td>
        </tr>
    
    
    
        <tr>
            <td>status</td>
            <td>String (up to 10)</td>
            <td>No</td>
            <td>The status of the filer</td>
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
            <td>State</td>
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
            <td>Phone: Phone number</td>
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

FilingsCd
~~~~~~~~~~~~~~~~~~~~~~~

This table is the parent table from which all links and association to
a filing are derived.

**Source:** `FILINGS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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

SmryCd
~~~~~~~~~~~~~~~~~~~~~~~

Summary totals from filings.

**Source:** `SMRY_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Amount A: Summary amount from column A</td>
        </tr>
    
    
    
        <tr>
            <td>amount_b</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount B: Summary amount from column B</td>
        </tr>
    
    
    
        <tr>
            <td>amount_c</td>
            <td>Decimal number</td>
            <td>No</td>
            <td>Amount C: Summary amount from column C</td>
        </tr>
    
    
    
        <tr>
            <td>elec_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Election date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

TextMemoCd
~~~~~~~~~~~~~~~~~~~~~~~

Text memos attached to electronic filings

**Source:** `TEXT_MEMO_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Reference number: Links text memo to a specific record</td>
        </tr>
    
    
    
        <tr>
            <td>text4000</td>
            <td>String (up to 4000)</td>
            <td>No</td>
            <td>Text: Contents of the text memo</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Lobbying tables
---------------------------


Cvr2LobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~

Additional data from lobbyist disclosure forms

**Source:** `CVR2_LOBBY_DISCLOSURE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

Cvr2RegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~

Cover page of lobbying disclosure forms

**Source:** `CVR2_REGISTRATION_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    
        <tr>
            <td>entity_cd</td>
            <td>String (up to 3)</td>
            <td>No</td>
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>entity_id</td>
            <td>String (up to 9)</td>
            <td>No</td>
            <td>Entity ID: Identification number of the entity described by the record</td>
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

CvrLobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~

Cover page information for lobbying disclosure forms

**Source:** `CVR_LOBBY_DISCLOSURE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
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

CvrRegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~

Cover page of lobbying disclosure forms

**Source:** `CVR_REGISTRATION_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>String (up to 8)</td>
            <td>No</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
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

F690P2Cd
~~~~~~~~~~~~~~~~~~~~~~~

Amends lobbying disclosure filings

**Source:** `F690P2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Record type</td>
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

LattCd
~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist disclosure attachment schedules for payments

**Source:** `LATT_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LccmCd
~~~~~~~~~~~~~~~~~~~~~~~

Lobbying campaign contributions

**Source:** `LCCM_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>String (up to 120)</td>
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
            <td>Entity code</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LempCd
~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist employers and subcontracted clients

**Source:** `LEMP_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
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

LexpCd
~~~~~~~~~~~~~~~~~~~~~~~

Lobbying activity expenditures

**Source:** `LEXP_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
        </tr>
    
    
    
        <tr>
            <td>recsubtype</td>
            <td>String (up to 1)</td>
            <td>No</td>
            <td>Record subtype</td>
        </tr>
    
    
    
        <tr>
            <td>tran_id</td>
            <td>String (up to 20)</td>
            <td>No</td>
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyAmendmentsCd
~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist registration amendment information

**Source:** `LOBBY_AMENDMENTS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>Yes</td>
            <td>Record type</td>
        </tr>
    
    
    
        <tr>
            <td>form_type</td>
            <td>String (up to 9)</td>
            <td>Yes</td>
            <td>Name of the source filing form or schedule</td>
        </tr>
    
    
    
        <tr>
            <td>exec_date</td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Date this amendment executed on</td>
        </tr>
    
    
    
        <tr>
            <td>from_date</td>
            <td>String (up to 22)</td>
            <td>No</td>
            <td>Reporting period from date of original report</td>
        </tr>
    
    
    
        <tr>
            <td>thru_date</td>
            <td>String (up to 22)</td>
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
            <td>String (up to 56)</td>
            <td>No</td>
            <td>Delete lobbyist last name</td>
        </tr>
    
    
    
        <tr>
            <td>d_l_namf</td>
            <td>String (up to 35)</td>
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
            <td>String (up to 8)</td>
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
            <td>String (up to 160)</td>
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
            <td>String (up to 9)</td>
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

LothCd
~~~~~~~~~~~~~~~~~~~~~~~

Payment to other lobbying firms

**Source:** `LOTH_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LpayCd
~~~~~~~~~~~~~~~~~~~~~~~

Payments made or received by lobbying firms

**Source:** `LPAY_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Entity code</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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
            <td>Record type</td>
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
            <td>Transaction ID: Permanent value unique to this item</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>


Other tables
---------------------------


AcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~

Contains acronyms and their meaning.

**Source:** `ACRONYMS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
~~~~~~~~~~~~~~~~~~~~~~~

This table holds all addresses for the system. This table can be used
for address-based searches and formes the bases for address information
desplayed by the AMS.

**Source:** `ADDRESS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>adrid</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Address ID: Address indentification number</td>
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
            <td>State: Address state</td>
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
            <td>Phone: Address phone number</td>
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
~~~~~~~~~~~~~~~~~~~~~~~

Ballot measure dates and times

**Source:** `BALLOT_MEASURES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>election_date</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>Ballot measure election date</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
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
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `EFS_FILING_LOG_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filing_date</td>
            <td>Date (with time)</td>
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
            <td>Filer ID: Filer&#39;s unique identification number</td>
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

FilerAcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~

Links acronyms to filers

**Source:** `FILER_ACRONYMS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

FilerAddressCd
~~~~~~~~~~~~~~~~~~~~~~~

Links filers and addresses. This table maintains a history of when
addresses change.

**Source:** `FILER_ADDRESS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>adrid</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Address ID: Address identification number</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (with time)</td>
            <td>No</td>
            <td>Effective date: Address effective date</td>
        </tr>
    
    
    
        <tr>
            <td>add_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Address type</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

FilerEthicsClassCd
~~~~~~~~~~~~~~~~~~~~~~~

This table stores lobbyist ethics training dates.

**Source:** `FILER_ETHICS_CLASS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>ethics_date</td>
            <td>Date (with time)</td>
            <td>Yes</td>
            <td>Date ethics training was accomplished</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

FilerInterestsCd
~~~~~~~~~~~~~~~~~~~~~~~

Links a filer to their interest codes.

**Source:** `FILER_INTERESTS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Interest code</td>
        </tr>
    
    
    
        <tr>
            <td>effect_date</td>
            <td>Date (with time)</td>
            <td>Yes</td>
            <td>Effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

FilerLinksCd
~~~~~~~~~~~~~~~~~~~~~~~

Links filers to each other and records their relationship type.

**Source:** `FILER_LINKS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id_a</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID A: Unique identification number for the first filer in the relationship</td>
        </tr>
    
    
    
        <tr>
            <td>filer_id_b</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID B: Unique identification number for the second filer in the relationship</td>
        </tr>
    
    
    
        <tr>
            <td>active_flg</td>
            <td>String (up to 1)</td>
            <td>Yes</td>
            <td>Active flag: Indicates if the link is active</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Session ID: Legislative session identification number</td>
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
            <td>Link description: Unused</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date: Date the link became active</td>
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
            <td>Termination date: Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

FilerStatusTypesCd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model that contains a small number
of codes and definitions.

**Source:** `FILER_STATUS_TYPES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
            <td>Status description: This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

FilerToFilerTypeCd
~~~~~~~~~~~~~~~~~~~~~~~

This table links a filer to a set of characteristics that describe the
filer. This table maintains a history of changes and allows the filer
to change characteristics over time.

**Source:** `FILER_TO_FILER_TYPE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filer_type</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer type identification number</td>
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
            <td>Session ID: Legislative session identification number</td>
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

FilerTypesCd
~~~~~~~~~~~~~~~~~~~~~~~

This lookup table describes filer types.

**Source:** `FILER_TYPES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
~~~~~~~~~~~~~~~~~~~~~~~

This table maps legacy filer identification numbers to the system's filer
identification numbers.

**Source:** `FILER_XREF_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>xref_id</td>
            <td>String (up to 32)</td>
            <td>Yes</td>
            <td>Crossreference filer ID: Alternative filer ID found on many forms</td>
        </tr>
    
    
    
        <tr>
            <td>effect_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Effective date</td>
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
~~~~~~~~~~~~~~~~~~~~~~~

This table is the parent table from which all links and associations
to a filer are derived.

**Source:** `FILERS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

FilingPeriodCd
~~~~~~~~~~~~~~~~~~~~~~~

An undocumented table that contains metadata for a variety
of filing periods.

**Source:** `FILING_PERIOD_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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

GroupTypesCd
~~~~~~~~~~~~~~~~~~~~~~~

This lookup table stores group type information.

**Source:** `GROUP_TYPES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>grp_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Group ID: Group identification number</td>
        </tr>
    
    
    
        <tr>
            <td>grp_name</td>
            <td>String (up to 28)</td>
            <td>No</td>
            <td>Group name</td>
        </tr>
    
    
    
        <tr>
            <td>grp_desc</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Group description</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

HdrCd
~~~~~~~~~~~~~~~~~~~~~~~

Electronic filing record header data

**Source:** `HDR_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>amend_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Amendment ID: Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
        </tr>
    
    
    
        <tr>
            <td>hdr_comment</td>
            <td>String (up to 200)</td>
            <td>No</td>
            <td>Header comment: Typically used for development and test filings</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 4)</td>
            <td>No</td>
            <td>Record type</td>
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
            <td>State code: The state code value entered in the electronic filing</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

HeaderCd
~~~~~~~~~~~~~~~~~~~~~~~

Lookup table used to report form 460 information in the AMS.

**Source:** `HEADER_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
            <td>Form ID: Form identification code</td>
        </tr>
    
    
    
        <tr>
            <td>rec_type</td>
            <td>String (up to 11)</td>
            <td>Yes</td>
            <td>Record type</td>
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

ImageLinksCd
~~~~~~~~~~~~~~~~~~~~~~~

This table links images to filers and accounts.

**Source:** `IMAGE_LINKS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>img_link_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Image link ID: Image link identification number</td>
        </tr>
    
    
    
        <tr>
            <td>img_link_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Image link type</td>
        </tr>
    
    
    
        <tr>
            <td>img_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Image ID: Image identification number</td>
        </tr>
    
    
    
        <tr>
            <td>img_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>Image type</td>
        </tr>
    
    
    
        <tr>
            <td>img_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Image date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LegislativeSessionsCd
~~~~~~~~~~~~~~~~~~~~~~~

Legislative session, begin and end dates look up table.

**Source:** `LEGISLATIVE_SESSIONS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Session ID: Legislative session identification number</td>
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

LobbyingChgLogCd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented table.

**Source:** `LOBBYING_CHG_LOG_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>Yes</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
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
            <td>Session ID: Legislative session identification number</td>
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
            <td>Filer state</td>
        </tr>
    
    
    
        <tr>
            <td>filer_zip</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer ZIP Code</td>
        </tr>
    
    
    
        <tr>
            <td>filer_phone</td>
            <td>String (up to 12)</td>
            <td>No</td>
            <td>Filer phone number</td>
        </tr>
    
    
    
        <tr>
            <td>entity_type</td>
            <td>Integer</td>
            <td>No</td>
            <td>This field is undocumented</td>
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
            <td>Effective date: This field is undocumented</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistContributions1Cd
~~~~~~~~~~~~~~~~~~~~~~~



**Source:** `LOBBYIST_CONTRIBUTIONS1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Filing period start date</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Filing period end date</td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Contribution date</td>
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
~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist contribution disclosure table. Temporary table used to generate
disclosure table (Lobbyist Contributions 3)

**Source:** `LOBBYIST_CONTRIBUTIONS2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Filing period start date</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Filing period end date</td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Contribution date</td>
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
~~~~~~~~~~~~~~~~~~~~~~~

Lobbyist contribution disclosure table.

**Source:** `LOBBYIST_CONTRIBUTIONS3_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_start_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Filing period start date</td>
        </tr>
    
    
    
        <tr>
            <td>filing_period_end_dt</td>
            <td>Date (without time)</td>
            <td>No</td>
            <td>Filing period end date</td>
        </tr>
    
    
    
        <tr>
            <td>contribution_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Contribution date</td>
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
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_EMP_LOBBYIST1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist ID: Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer ID: Employer identification number</td>
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
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistEmpLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_EMP_LOBBYIST2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist ID: Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer ID: Employer identification number</td>
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
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_EMPLOYER1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer ID: Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session ID: Legislative session identification number</td>
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
            <td>Contributor ID: Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest code</td>
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
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8: Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_EMPLOYER2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer ID: Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session ID: Legislative session identification number</td>
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
            <td>Contributor ID: Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest code</td>
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
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8: Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistEmployer3Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_EMPLOYER3_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer ID: Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session ID: Legislative session identification number</td>
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
            <td>Contributor ID: Contributor identification number</td>
        </tr>
    
    
    
        <tr>
            <td>interest_cd</td>
            <td>Integer</td>
            <td>No</td>
            <td>Interest code</td>
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
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8: Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistEmployerFirms1Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_EMPLOYER_FIRMS1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer ID: Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
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
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>termination_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Termination date: Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistEmployerFirms2Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_EMPLOYER_FIRMS2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>employer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Employer ID: Employer identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
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
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    
        <tr>
            <td>termination_dt</td>
            <td>String (up to 32)</td>
            <td>No</td>
            <td>Termination date: Termination effective date</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistFirm1Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_FIRM1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session ID: Legislative session identification number</td>
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
            <td>Contributor ID: Contributor identification number</td>
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
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8: Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistFirm2Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_FIRM2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session ID: Legislative session identification number</td>
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
            <td>Contributor ID: Contributor identification number</td>
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
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8: Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistFirm3Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_FIRM3_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>session_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Session ID: Legislative session identification number</td>
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
            <td>Contributor ID: Contributor identification number</td>
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
            <td>Year 1 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>yr_2_ytd_amt</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Year 2 year-to-date-amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_1</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 1: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_2</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 2: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_3</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 3: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_4</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 4: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_5</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 5: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_6</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 6: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_7</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 7: Quarter total amount</td>
        </tr>
    
    
    
        <tr>
            <td>qtr_8</td>
            <td>Floating point number</td>
            <td>No</td>
            <td>Quarter 8: Quarter total amount</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistFirmEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_FIRM_EMPLOYER1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filing ID: Unique filing identificiation number</td>
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
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `LOBBYIST_FIRM_EMPLOYER2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
        </tr>
    
    
    
        <tr>
            <td>filing_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filing ID: Unique filing identificiation number</td>
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

LobbyistFirmLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~

It's an undocumented model.

**Source:** `LOBBYIST_FIRM_LOBBYIST1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist ID: Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
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
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LobbyistFirmLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~

It's an undocumented model.

**Source:** `LOBBYIST_FIRM_LOBBYIST2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>lobbyist_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Lobbyist ID: Lobbyist identification number</td>
        </tr>
    
    
    
        <tr>
            <td>firm_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Firm ID: Identification number of the firm, employer or coalition</td>
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
            <td>Session ID: Legislative session identification number</td>
        </tr>
    
    
    </tbody>
    </table>
    </div>

LookupCode
~~~~~~~~~~~~~~~~~~~~~~~

The description of some lookup codes in the system.

**Source:** `LOOKUP_CODES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
~~~~~~~~~~~~~~~~~~~~~~~

The name of all entities in the system. Used for searches when
the name has an identification number.

**Source:** `NAMES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
~~~~~~~~~~~~~~~~~~~~~~~

This table is undocumented.

**Source:** `RECEIVED_FILINGS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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
    
    
    
    
        <tr>
            <td>filer_id</td>
            <td>Integer</td>
            <td>No</td>
            <td>Filer ID: Filer&#39;s unique identification number</td>
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
            <td>Filing ID: Unique filing identificiation number</td>
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

ReportsCd
~~~~~~~~~~~~~~~~~~~~~~~

This is an undocumented model.

**Source:** `REPORTS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

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

+------------------------------+
|Source TSV                    |
+==============================+
| FILER_TYPE_PERIODS_CD        |
+------------------------------+
| LOBBYIST_EMPLOYER_HISTORY_CD |
+------------------------------+
| LOBBYIST_FIRM_HISTORY_CD     |
+------------------------------+
