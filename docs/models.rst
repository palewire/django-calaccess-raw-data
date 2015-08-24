Database table models
=====================

The database models in this Django application, which are intended to serve
as a mirror of the bulk dumps published by California's Secretary of State.

They are grouped here in the same as manner as the state's `official documentation <officialdocumentation.html>`_.

Campaign
--------

Cvr2CampaignDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~
Record used to carry additional names for the campaign
disclosure forms below.

.. py:class:: Cvr2CampaignDisclosureCd

    **Source data**

        `CVR2_CAMPAIGN_DISCLOSURE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: bal_juris

            *Bal juris*

        .. py:attribute:: bal_name

            *Bal name*

        .. py:attribute:: bal_num

            *Bal num*

        .. py:attribute:: cmte_id

            *Cmte id*

        .. py:attribute:: control_yn

            *Control yn*

        .. py:attribute:: dist_no

            *Dist no*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: enty_city

            *Enty city*

        .. py:attribute:: enty_email

            *Enty email*

        .. py:attribute:: enty_fax

            *Enty fax*

        .. py:attribute:: enty_namf

            *Enty namf*

        .. py:attribute:: enty_naml

            *Enty naml*

        .. py:attribute:: enty_nams

            *Enty nams*

        .. py:attribute:: enty_namt

            *Enty namt*

        .. py:attribute:: enty_phon

            *Enty phon*

        .. py:attribute:: enty_st

            *Enty st*

        .. py:attribute:: enty_zip4

            *Enty zip4*

        .. py:attribute:: f460_part

            *F460 part*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: juris_cd

            *Juris cd*

        .. py:attribute:: juris_dscr

            *Juris dscr*

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: mail_city

            *Mail city*

        .. py:attribute:: mail_st

            *Mail st*

        .. py:attribute:: mail_zip4

            *Mail zip4*

        .. py:attribute:: off_s_h_cd

            *Off s h cd*

        .. py:attribute:: offic_dscr

            *Offic dscr*

        .. py:attribute:: office_cd

            *Office cd*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: sup_opp_cd

            *Sup opp cd*

        .. py:attribute:: title

            *Title*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: tres_namf

            *Tres namf*

        .. py:attribute:: tres_naml

            *Tres naml*

        .. py:attribute:: tres_nams

            *Tres nams*

        .. py:attribute:: tres_namt

            *Tres namt*



Cvr2SoCd
~~~~~~~~~~~~~~~~~~~~~~~
Additional names and committees information included on the second page
of a statement of organization creation form filed
by a slate-mailer organization or recipient committee.

.. py:class:: Cvr2SoCd

    **Source data**

        `CVR2_SO_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: enty_naml

            *Enty naml*

        .. py:attribute:: enty_namf

            *Enty namf*

        .. py:attribute:: enty_namt

            *Enty namt*

        .. py:attribute:: enty_nams

            *Enty nams*

        .. py:attribute:: item_cd

            *Item cd*

        .. py:attribute:: mail_city

            *Mail city*

        .. py:attribute:: mail_st

            *Mail st*

        .. py:attribute:: mail_zip4

            *Mail zip4*

        .. py:attribute:: day_phone

            *Day phone*

        .. py:attribute:: fax_phone

            *Fax phone*

        .. py:attribute:: email_adr

            *Email adr*

        .. py:attribute:: cmte_id

            *Cmte id*

        .. py:attribute:: ind_group

            *Ind group*

        .. py:attribute:: office_cd

            *Office cd*

        .. py:attribute:: offic_dscr

            *Offic dscr*

        .. py:attribute:: juris_cd

            *Juris cd*

        .. py:attribute:: juris_dscr

            *Juris dscr*

        .. py:attribute:: dist_no

            *Dist no*

        .. py:attribute:: off_s_h_cd

            *Off s h cd*

        .. py:attribute:: non_pty_cb

            *Non pty cb*

        .. py:attribute:: party_name

            *Party name*

        .. py:attribute:: bal_num

            *Bal num*

        .. py:attribute:: bal_juris

            *Bal juris*

        .. py:attribute:: sup_opp_cd

            *Sup opp cd*

        .. py:attribute:: year_elect

            *Year elect*

        .. py:attribute:: pof_title

            *Pof title*



Cvr3VerificationInfoCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page verification information from campaign disclosure forms

.. py:class:: Cvr3VerificationInfoCd

    **Source data**

        `CVR3_VERIFICATION_INFO_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: sig_date

            *Signed date* date when signed

        .. py:attribute:: sig_loc

            *Signed location* city and state where signed

        .. py:attribute:: sig_naml

            *Last name* last name of the signer

        .. py:attribute:: sig_namf

            *First name* first name of the signer

        .. py:attribute:: sig_namt

            *Title* title of the signer

        .. py:attribute:: sig_nams

            *Suffix* suffix of the signer



CvrCampaignDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page information for the campaign disclosure forms below.
This data comes from the electronic filing.
The data contained herin is &quot;as filed&quot; by the entity making the filing.

    F401 -- Slate Mailer Organization Campaign Statement
    F425 -- Semi-Annual Statement of No Activity
    F450 -- Recipient Committee Campaign Statement (Short Form)
    F460 -- Recipient Committee Campaign Statement
    F461 -- Independent Expenditure and Major Donor Committee
            Campaign Statement
    F465 -- Supplemental Independent Expenditure Report
    F496 -- Late Independent Expenditure Report
    F497 -- Late Contribution Report
    F498 -- Slate Mailer Late Payment Report

.. py:class:: CvrCampaignDisclosureCd

    **Source data**

        `CVR_CAMPAIGN_DISCLOSURE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: amendexp_1

            *Amendexp 1*

        .. py:attribute:: amendexp_2

            *Amendexp 2*

        .. py:attribute:: amendexp_3

            *Amendexp 3*

        .. py:attribute:: assoc_cb

            *Assoc cb*

        .. py:attribute:: assoc_int

            *Assoc int*

        .. py:attribute:: bal_id

            *Bal id*

        .. py:attribute:: bal_juris

            *Bal juris*

        .. py:attribute:: bal_name

            *Bal name*

        .. py:attribute:: bal_num

            *Bal num*

        .. py:attribute:: brdbase_yn

            *Brdbase yn*

        .. py:attribute:: bus_city

            *Bus city*

        .. py:attribute:: bus_inter

            *Bus inter*

        .. py:attribute:: bus_name

            *Bus name*

        .. py:attribute:: bus_st

            *Bus st*

        .. py:attribute:: bus_zip4

            *Bus zip4*

        .. py:attribute:: busact_cb

            *Busact cb*

        .. py:attribute:: busactvity

            *Busactvity*

        .. py:attribute:: cand_city

            *Cand city*

        .. py:attribute:: cand_email

            *Cand email*

        .. py:attribute:: cand_fax

            *Cand fax*

        .. py:attribute:: cand_id

            *Cand id*

        .. py:attribute:: cand_namf

            *Cand namf*

        .. py:attribute:: cand_naml

            *Cand naml*

        .. py:attribute:: cand_nams

            *Cand nams*

        .. py:attribute:: cand_namt

            *Cand namt*

        .. py:attribute:: cand_phon

            *Cand phon*

        .. py:attribute:: cand_st

            *Cand st*

        .. py:attribute:: cand_zip4

            *Cand zip4*

        .. py:attribute:: cmtte_id

            *Cmtte id*

        .. py:attribute:: cmtte_type

            *Cmtte type*

        .. py:attribute:: control_yn

            *Control yn*

        .. py:attribute:: dist_no

            *Dist no*

        .. py:attribute:: elect_date

            *Elect date*

        .. py:attribute:: emplbus_cb

            *Emplbus cb*

        .. py:attribute:: employer

            *Employer*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: file_email

            *File email*

        .. py:attribute:: filer_city

            *Filer city*

        .. py:attribute:: filer_fax

            *Filer fax*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filer_namf

            *Filer namf*

        .. py:attribute:: filer_naml

            *Filer naml*

        .. py:attribute:: filer_nams

            *Filer nams*

        .. py:attribute:: filer_namt

            *Filer namt*

        .. py:attribute:: filer_phon

            *Filer phon*

        .. py:attribute:: filer_st

            *Filer st*

        .. py:attribute:: filer_zip4

            *Filer zip4*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: from_date

            *From date*

        .. py:attribute:: juris_cd

            *Juris cd*

        .. py:attribute:: juris_dscr

            *Juris dscr*

        .. py:attribute:: late_rptno

            *Late rptno*

        .. py:attribute:: mail_city

            *Mail city*

        .. py:attribute:: mail_st

            *Mail st*

        .. py:attribute:: mail_zip4

            *Mail zip4*

        .. py:attribute:: occupation

            *Occupation*

        .. py:attribute:: off_s_h_cd

            *Off s h cd*

        .. py:attribute:: offic_dscr

            *Offic dscr*

        .. py:attribute:: office_cd

            *Office cd*

        .. py:attribute:: other_cb

            *Other cb*

        .. py:attribute:: other_int

            *Other int*

        .. py:attribute:: primfrm_yn

            *Primfrm yn*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: report_num

            *Report num*

        .. py:attribute:: reportname

            *Reportname*

        .. py:attribute:: rpt_att_cb

            *Rpt att cb*

        .. py:attribute:: rpt_date

            *Rpt date*

        .. py:attribute:: rptfromdt

            *Rptfromdt*

        .. py:attribute:: rptthrudt

            *Rptthrudt*

        .. py:attribute:: selfemp_cb

            *Selfemp cb*

        .. py:attribute:: sponsor_yn

            *Sponsor yn*

        .. py:attribute:: stmt_type

            *Stmt type*

        .. py:attribute:: sup_opp_cd

            *Sup opp cd*

        .. py:attribute:: thru_date

            *Thru date*

        .. py:attribute:: tres_city

            *Tres city*

        .. py:attribute:: tres_email

            *Tres email*

        .. py:attribute:: tres_fax

            *Tres fax*

        .. py:attribute:: tres_namf

            *Tres namf*

        .. py:attribute:: tres_naml

            *Tres naml*

        .. py:attribute:: tres_nams

            *Tres nams*

        .. py:attribute:: tres_namt

            *Tres namt*

        .. py:attribute:: tres_phon

            *Tres phon*

        .. py:attribute:: tres_st

            *Tres st*

        .. py:attribute:: tres_zip4

            *Tres zip4*



CvrSoCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page for a statement of organization creation or termination
form filed by a slate-mailer organization or recipient committee.

.. py:class:: CvrSoCd

    **Source data**

        `CVR_SO_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: acct_opendt

            *Acct opendt*

        .. py:attribute:: actvty_lvl

            *Activity level* Organization's level of activity

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: bank_adr1

            *Bank adr1*

        .. py:attribute:: bank_adr2

            *Bank adr2*

        .. py:attribute:: bank_city

            *Bank city*

        .. py:attribute:: bank_nam

            *Bank nam*

        .. py:attribute:: bank_phon

            *Bank phon*

        .. py:attribute:: bank_st

            *Bank st*

        .. py:attribute:: bank_zip4

            *Bank zip4*

        .. py:attribute:: brdbase_cb

            *Brdbase cb*

        .. py:attribute:: city

            *City*

        .. py:attribute:: cmte_email

            *Cmte email*

        .. py:attribute:: cmte_fax

            *Cmte fax*

        .. py:attribute:: com82013id

            *Com82013id*

        .. py:attribute:: com82013nm

            *Com82013nm*

        .. py:attribute:: com82013yn

            *Com82013yn*

        .. py:attribute:: control_cb

            *Control cb*

        .. py:attribute:: county_act

            *County act*

        .. py:attribute:: county_res

            *County res*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filer_namf

            *Filer first name*

        .. py:attribute:: filer_naml

            *Filer last name*

        .. py:attribute:: filer_nams

            *Filer name suffix*

        .. py:attribute:: filer_namt

            *Filer name title*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: genpurp_cb

            *Genpurp cb*

        .. py:attribute:: gpc_descr

            *Gpc descr*

        .. py:attribute:: mail_city

            *Mail city*

        .. py:attribute:: mail_st

            *Mail st*

        .. py:attribute:: mail_zip4

            *Mail zip4*

        .. py:attribute:: phone

            *Phone*

        .. py:attribute:: primfc_cb

            *Primfc cb*

        .. py:attribute:: qualfy_dt

            *Date qualified* Date qualified as an organization

        .. py:attribute:: qual_cb

            *Qual cb*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: report_num

            *Report num*

        .. py:attribute:: rpt_date

            *Rpt date*

        .. py:attribute:: smcont_qualdt

            *Smcont qualdt*

        .. py:attribute:: sponsor_cb

            *Sponsor cb*

        .. py:attribute:: st

            *St*

        .. py:attribute:: surplusdsp

            *Surplusdsp*

        .. py:attribute:: term_date

            *Term date*

        .. py:attribute:: tres_city

            *Treasurer&#39;s city*

        .. py:attribute:: tres_namf

            *Treasurer&#39;s first name*

        .. py:attribute:: tres_naml

            *Treasurer&#39;s last name*

        .. py:attribute:: tres_nams

            *Treasurer&#39;s name suffix*

        .. py:attribute:: tres_namt

            *Treasurer&#39;s name title*

        .. py:attribute:: tres_phon

            *Treasurer&#39;s phone number*

        .. py:attribute:: tres_st

            *Treasurer&#39;s street*

        .. py:attribute:: tres_zip4

            *Tres zip4* Treasurer's ZIP Code

        .. py:attribute:: zip4

            *Zip4*



DebtCd
~~~~~~~~~~~~~~~~~~~~~~~
Form 460 (Recipient Committee Campaign Statement)
Schedule (F) Accrued Expenses (Unpaid Bills) records

.. py:class:: DebtCd

    **Source data**

        `DEBT_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: amt_incur

            *Amt incur*

        .. py:attribute:: amt_paid

            *Amt paid*

        .. py:attribute:: bakref_tid

            *Bakref tid*

        .. py:attribute:: beg_bal

            *Beg bal*

        .. py:attribute:: cmte_id

            *Cmte id*

        .. py:attribute:: end_bal

            *End bal*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: expn_code

            *Expn code*

        .. py:attribute:: expn_dscr

            *Expn dscr*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: payee_city

            *Payee city*

        .. py:attribute:: payee_namf

            *Payee namf*

        .. py:attribute:: payee_naml

            *Payee naml*

        .. py:attribute:: payee_nams

            *Payee nams*

        .. py:attribute:: payee_namt

            *Payee namt*

        .. py:attribute:: payee_st

            *Payee st*

        .. py:attribute:: payee_zip4

            *Payee zip4*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: tres_city

            *Tres city*

        .. py:attribute:: tres_namf

            *Tres namf*

        .. py:attribute:: tres_naml

            *Tres naml*

        .. py:attribute:: tres_nams

            *Tres nams*

        .. py:attribute:: tres_namt

            *Tres namt*

        .. py:attribute:: tres_st

            *Tres st*

        .. py:attribute:: tres_zip4

            *Tres zip4*

        .. py:attribute:: xref_match

            *Xref match*

        .. py:attribute:: xref_schnm

            *Xref schnm*



ExpnCd
~~~~~~~~~~~~~~~~~~~~~~~
Campaign expenditures from a variety of forms

.. py:class:: ExpnCd

    **Source data**

        `EXPN_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: agent_namf

            *Agent namf* Agent of Ind. Contractor's First name

        .. py:attribute:: agent_naml

            *Agent naml* Agent of Ind. Contractor's Last name (Sched G)

        .. py:attribute:: agent_nams

            *Agent nams* Agent of Ind. Contractor's Suffix

        .. py:attribute:: agent_namt

            *Agent namt* Agent of Ind. Contractor's Prefix or Title

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: amount

            *Amount* Amount of Payment

        .. py:attribute:: bakref_tid

            *Bakref tid* Back Reference to a Tran_ID of a 'parent' record

        .. py:attribute:: bal_juris

            *Bal juris* Jurisdiction

        .. py:attribute:: bal_name

            *Bal name* Ballot Measure Name

        .. py:attribute:: bal_num

            *Bal num* Ballot Number or Letter

        .. py:attribute:: cand_namf

            *Cand namf* Candidate's First name

        .. py:attribute:: cand_naml

            *Cand naml* Candidate's Last name

        .. py:attribute:: cand_nams

            *Cand nams* Candidate's Suffix

        .. py:attribute:: cand_namt

            *Cand namt* Candidate's Prefix or Title

        .. py:attribute:: cmte_id

            *Cmte id* Committee ID (If [COM|RCP] & no ID#, Treas info Req.)

        .. py:attribute:: cum_oth

            *Cum oth* Cumulative / 'Other' (No Cumulative on Sched E & G)

        .. py:attribute:: cum_ytd

            *Cum ytd* Cumulative / Year-to-date amount         (No Cumulative on Sched E & G)

        .. py:attribute:: dist_no

            *Dist no* Office District Number (Req. if Juris_Cd=[SEN|ASM|BOE]

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: expn_chkno

            *Expn chkno* Check Number (Optional)

        .. py:attribute:: expn_code

            *Expn code* Expense Code - Values: (Refer to list in Overview)         Note: CTB & IND need explanation & listing on Sched D         TRC & TRS require explanation.

        .. py:attribute:: expn_date

            *Expn date* Date of Expenditure (Note: Date not on Sched E & G)

        .. py:attribute:: expn_dscr

            *Expn dscr* Purpose of Expense and/or Description/explanation

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: g_from_e_f

            *G from e f* Back Reference from Sched G to Sched 'E' or 'F'?

        .. py:attribute:: juris_cd

            *Juris cd* Office Jurisdiction Code Values: STW=Statewide;         SEN=Senate District; ASM=Assembly District;         BOE=Board of Equalization District;         CIT=City; CTY=County; LOC=Local; OTH=Other

        .. py:attribute:: juris_dscr

            *Juris dscr* Office Jurisdiction Description         (Req. if Juris_Cd=[CIT|CTY|LOC|OTH]

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: memo_code

            *Memo code* Memo Amount? (Date/Amount are informational only)

        .. py:attribute:: memo_refno

            *Memo refno* Reference to text contained in a TEXT record.

        .. py:attribute:: off_s_h_cd

            *Off s h cd* Office Sought/Held Code: H=Held; S=Sought

        .. py:attribute:: offic_dscr

            *Offic dscr* Office Sought Description (Req. if Office_Cd=OTH)

        .. py:attribute:: office_cd

            *Office cd* Office Sought (See table of code in Overview)

        .. py:attribute:: payee_city

            *Payee city* Payee City

        .. py:attribute:: payee_namf

            *Payee namf* Payee's First name

        .. py:attribute:: payee_naml

            *Payee naml* Payee's Last name

        .. py:attribute:: payee_nams

            *Payee nams* Payee's Suffix

        .. py:attribute:: payee_namt

            *Payee namt* Payee's Prefix or Title

        .. py:attribute:: payee_st

            *Payee st* State code

        .. py:attribute:: payee_zip4

            *Payee zip4* Zip+4

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: sup_opp_cd

            *Sup opp cd* Support/Oppose? Values: S; O (F450, F461)

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: tres_city

            *Tres city* Treasurer City

        .. py:attribute:: tres_namf

            *Tres namf* Treasurer's First name (Req if [COM|RCP] & no ID#)

        .. py:attribute:: tres_naml

            *Tres naml* Treasurer's Last name (Req if [COM|RCP] & no ID#)

        .. py:attribute:: tres_nams

            *Tres nams* Treasurer's Suffix

        .. py:attribute:: tres_namt

            *Tres namt* Treasurer's Prefix or Title

        .. py:attribute:: tres_st

            *Tres st* Treasurer State

        .. py:attribute:: tres_zip4

            *Tres zip4* Treasurer ZIP+4

        .. py:attribute:: xref_match

            *Xref match* X = Related item on other Sched has same Tran_ID

        .. py:attribute:: xref_schnm

            *Xref schnm* Related item is included on Sched 'C' or 'H2'



F495P2Cd
~~~~~~~~~~~~~~~~~~~~~~~
F495 Supplemental Preelection Campaign Statement

It&#39;s attatchment to the forms below

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

.. py:class:: F495P2Cd

    **Source data**

        `F495P2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: elect_date

            *Elect date*

        .. py:attribute:: electjuris

            *Electjuris*

        .. py:attribute:: contribamt

            *Contribamt*



F501502Cd
~~~~~~~~~~~~~~~~~~~~~~~
Candidate Intention Statement

    -- F501
    -- F502

.. py:class:: F501502Cd

    **Source data**

        `F501_502_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: committee_id

            *Committee id*

        .. py:attribute:: entity_cd

            *Entity cd*

        .. py:attribute:: report_num

            *Report num*

        .. py:attribute:: rpt_date

            *Rpt date*

        .. py:attribute:: stmt_type

            *Stmt type*

        .. py:attribute:: from_date

            *From date*

        .. py:attribute:: thru_date

            *Thru date*

        .. py:attribute:: elect_date

            *Elect date*

        .. py:attribute:: cand_naml

            *Cand naml*

        .. py:attribute:: cand_namf

            *Cand namf*

        .. py:attribute:: can_namm

            *Can namm*

        .. py:attribute:: cand_namt

            *Cand namt*

        .. py:attribute:: cand_nams

            *Cand nams*

        .. py:attribute:: moniker_pos

            *Moniker pos*

        .. py:attribute:: moniker

            *Moniker*

        .. py:attribute:: cand_city

            *Cand city*

        .. py:attribute:: cand_st

            *Cand st*

        .. py:attribute:: cand_zip4

            *Cand zip4*

        .. py:attribute:: cand_phon

            *Cand phon*

        .. py:attribute:: cand_fax

            *Cand fax*

        .. py:attribute:: cand_email

            *Cand email*

        .. py:attribute:: fin_naml

            *Fin naml*

        .. py:attribute:: fin_namf

            *Fin namf*

        .. py:attribute:: fin_namt

            *Fin namt*

        .. py:attribute:: fin_nams

            *Fin nams*

        .. py:attribute:: fin_city

            *Fin city*

        .. py:attribute:: fin_st

            *Fin st*

        .. py:attribute:: fin_zip4

            *Fin zip4*

        .. py:attribute:: fin_phon

            *Fin phon*

        .. py:attribute:: fin_fax

            *Fin fax*

        .. py:attribute:: fin_email

            *Fin email*

        .. py:attribute:: office_cd

            *Office cd*

        .. py:attribute:: offic_dscr

            *Offic dscr*

        .. py:attribute:: agency_nam

            *Agency nam*

        .. py:attribute:: juris_cd

            *Juris cd*

        .. py:attribute:: juris_dscr

            *Juris dscr*

        .. py:attribute:: dist_no

            *Dist no*

        .. py:attribute:: party

            *Party*

        .. py:attribute:: yr_of_elec

            *Yr of elec*

        .. py:attribute:: elec_type

            *Elec type*

        .. py:attribute:: execute_dt

            *Execute dt*

        .. py:attribute:: can_sig

            *Can sig*

        .. py:attribute:: account_no

            *Account no*

        .. py:attribute:: acct_op_dt

            *Acct op dt*

        .. py:attribute:: party_cd

            *Party cd*

        .. py:attribute:: district_cd

            *District cd*

        .. py:attribute:: accept_limit_yn

            *Accept limit yn*

        .. py:attribute:: did_exceed_dt

            *Did exceed dt*

        .. py:attribute:: cntrb_prsnl_fnds_dt

            *Cntrb prsnl fnds dt*



LoanCd
~~~~~~~~~~~~~~~~~~~~~~~
Loans received and made.

.. py:class:: LoanCd

    **Source data**

        `LOAN_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: bakref_tid

            *Bakref tid*

        .. py:attribute:: cmte_id

            *Cmte id*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: intr_city

            *Intr city*

        .. py:attribute:: intr_namf

            *Intr namf*

        .. py:attribute:: intr_naml

            *Intr naml*

        .. py:attribute:: intr_nams

            *Intr nams*

        .. py:attribute:: intr_namt

            *Intr namt*

        .. py:attribute:: intr_st

            *Intr st*

        .. py:attribute:: intr_zip4

            *Intr zip4*

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: lndr_namf

            *Lndr namf*

        .. py:attribute:: lndr_naml

            *Lndr naml*

        .. py:attribute:: lndr_nams

            *Lndr nams*

        .. py:attribute:: lndr_namt

            *Lndr namt*

        .. py:attribute:: loan_amt1

            *Loan amt1*

        .. py:attribute:: loan_amt2

            *Loan amt2*

        .. py:attribute:: loan_amt3

            *Loan amt3*

        .. py:attribute:: loan_amt4

            *Loan amt4*

        .. py:attribute:: loan_amt5

            *Loan amt5*

        .. py:attribute:: loan_amt6

            *Loan amt6*

        .. py:attribute:: loan_amt7

            *Loan amt7*

        .. py:attribute:: loan_amt8

            *Loan amt8*

        .. py:attribute:: loan_city

            *Loan city*

        .. py:attribute:: loan_date1

            *Loan date1*

        .. py:attribute:: loan_date2

            *Loan date2*

        .. py:attribute:: loan_emp

            *Loan emp*

        .. py:attribute:: loan_occ

            *Loan occ*

        .. py:attribute:: loan_rate

            *Loan rate*

        .. py:attribute:: loan_self

            *Loan self*

        .. py:attribute:: loan_st

            *Loan st*

        .. py:attribute:: loan_type

            *Loan type*

        .. py:attribute:: loan_zip4

            *Loan zip4*

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: tres_city

            *Tres city*

        .. py:attribute:: tres_namf

            *Tres namf*

        .. py:attribute:: tres_naml

            *Tres naml*

        .. py:attribute:: tres_nams

            *Tres nams*

        .. py:attribute:: tres_namt

            *Tres namt*

        .. py:attribute:: tres_st

            *Tres st*

        .. py:attribute:: tres_zip4

            *Tres zip4*

        .. py:attribute:: xref_match

            *Xref match*

        .. py:attribute:: xref_schnm

            *Xref schnm*



RcptCd
~~~~~~~~~~~~~~~~~~~~~~~
Receipts schedules for the following forms.

    Form 460 (Recipient Committee Campaign Statement)
    Schedules A, C, I, and A-1.

    Form 401 (Slate Mailer Organization Campaign Statement) Schedule A.

.. py:class:: RcptCd

    **Source data**

        `RCPT_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: amount

            *Amount* Amount Received (Monetary, Inkkind, Promise)

        .. py:attribute:: bakref_tid

            *Bakref tid* Back Reference to a transaction identifier of a parent record

        .. py:attribute:: bal_juris

            *Bal juris* Jurisdiction of ballot measure. Used on the Form 401 Schedule A

        .. py:attribute:: bal_name

            *Bal name* Ballot measure name. Used on the Form 401 Schedule A

        .. py:attribute:: bal_num

            *Bal num* Ballot measure number or letter. Used on the Form 401 Schedule A

        .. py:attribute:: cand_namf

            *Cand namf* Candidate/officeholder's first name. Used on the Form 401 Schedule A

        .. py:attribute:: cand_naml

            *Cand naml* Candidate/officeholder's last name. Used on the Form 401 Schedule A

        .. py:attribute:: cand_nams

            *Cand nams* Candidate/officeholder's name suffix. Used on the Form 401 Schedule A

        .. py:attribute:: cand_namt

            *Cand namt* Candidate/officeholder's name prefix or title. Used on the Form 401 Schedule A

        .. py:attribute:: cmte_id

            *Cmte id* Committee Identification number

        .. py:attribute:: ctrib_city

            *Ctrib city* Contributor's City

        .. py:attribute:: ctrib_dscr

            *Ctrib dscr* Description of goods/services received

        .. py:attribute:: ctrib_emp

            *Ctrib emp* Employer

        .. py:attribute:: ctrib_namf

            *Ctrib namf* Contributor's First Name

        .. py:attribute:: ctrib_naml

            *Ctrib naml* Contributor's last name or business name

        .. py:attribute:: ctrib_nams

            *Ctrib nams* Contributor's Suffix

        .. py:attribute:: ctrib_namt

            *Ctrib namt* Contributor's Prefix or Title

        .. py:attribute:: ctrib_occ

            *Ctrib occ* Occupation

        .. py:attribute:: ctrib_self

            *Ctrib self* Self Employed Check-box

        .. py:attribute:: ctrib_st

            *Ctrib st* Contributor's State

        .. py:attribute:: ctrib_zip4

            *Ctrib zip4* Contributor's ZIP+4

        .. py:attribute:: cum_oth

            *Cum oth* Cumulative Other (Sched A, A-1)

        .. py:attribute:: cum_ytd

            *Cum ytd* Cumulative year to date amount (Form 460 Schedule A and Form 401 Schedule A, A-1)

        .. py:attribute:: date_thru

            *Date thru* End of date range for items received

        .. py:attribute:: dist_no

            *Dist no* Office District Number (used on F401A)

        .. py:attribute:: entity_cd

            *Entity cd* Entity code: Values [CMO|RCP|IND|OTH]

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: int_rate

            *Int rate*

        .. py:attribute:: intr_city

            *Intr city* Intermediary's City

        .. py:attribute:: intr_cmteid

            *Intr cmteid*

        .. py:attribute:: intr_emp

            *Intr emp* Intermediary's Employer

        .. py:attribute:: intr_namf

            *Intr namf* Intermediary's First Name

        .. py:attribute:: intr_naml

            *Intr naml* Intermediary's Last Name

        .. py:attribute:: intr_nams

            *Intr nams* Intermediary's Suffix

        .. py:attribute:: intr_namt

            *Intr namt* Intermediary's Prefix or Title

        .. py:attribute:: intr_occ

            *Intr occ* Intermediary's Occupation

        .. py:attribute:: intr_self

            *Intr self* Intermediary's self employed check box

        .. py:attribute:: intr_st

            *Intr st* Intermediary's state

        .. py:attribute:: intr_zip4

            *Intr zip4* Intermediary's zip code

        .. py:attribute:: juris_cd

            *Juris cd* Office jurisdiction code. See the CAL document for the list of legal values. Used on Form 401 Schedule A

        .. py:attribute:: juris_dscr

            *Juris dscr* Office Jurisdiction Description (used on F401A)

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: memo_code

            *Memo code* Memo amount flag (Date/Amount are informational only)

        .. py:attribute:: memo_refno

            *Memo refno* Reference to text contained in a TEXT record

        .. py:attribute:: off_s_h_cd

            *Off s h cd* Office Sought/Held Code. Used on the Form 401 Schedule A. Legal values are 'S' for sought and 'H' for held

        .. py:attribute:: offic_dscr

            *Offic dscr* Office Sought Description (used on F401A)

        .. py:attribute:: office_cd

            *Office cd* Code that identifies the office being sought. See the CAL document for a list of valid codes. Used on the Form 401 Schedule A)

        .. py:attribute:: rcpt_date

            *Rcpt date* Date item received

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: sup_opp_cd

            *Sup opp cd* Support/oppose code. Legal values are 'S' for support or 'O' for oppose. Used on Form 401 Sechedule A. Transaction identifier - permanent value unique to this item

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: tran_type

            *Tran type* Transaction Type: Values T- third party | F Forgiven loan | R Returned (Negative amount)

        .. py:attribute:: tres_city

            *Tres city* City portion of the treasurer or responsible officer's street address

        .. py:attribute:: tres_namf

            *Tres namf* Treasurer or responsible officer's first name

        .. py:attribute:: tres_naml

            *Tres naml* Treasurer or responsible officer's last name

        .. py:attribute:: tres_nams

            *Tres nams* Treasurer or responsible officer's suffix

        .. py:attribute:: tres_namt

            *Tres namt* Treasurer or responsible officer's prefix or title

        .. py:attribute:: tres_st

            *Tres st* State portion of the treasurer or responsible officer's address

        .. py:attribute:: tres_zip4

            *Tres zip4* Zip code portion of the treasurer or responsible officer's address

        .. py:attribute:: xref_match

            *Xref match* Related item on other schedule has same transaction identifier. 'X' indicates this condition is true

        .. py:attribute:: xref_schnm

            *Xref schnm* Related record is included on Sched 'B2' or 'F'



S401Cd
~~~~~~~~~~~~~~~~~~~~~~~
This table contains Form 401 (Slate Mailer Organization) payment and other
disclosure schedule (F401B, F401B-1, F401C, F401D) information.

.. py:class:: S401Cd

    **Source data**

        `S401_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: agent_naml

            *Agent naml*

        .. py:attribute:: agent_namf

            *Agent namf*

        .. py:attribute:: agent_namt

            *Agent namt*

        .. py:attribute:: agent_nams

            *Agent nams*

        .. py:attribute:: payee_naml

            *Payee naml*

        .. py:attribute:: payee_namf

            *Payee namf*

        .. py:attribute:: payee_namt

            *Payee namt*

        .. py:attribute:: payee_nams

            *Payee nams*

        .. py:attribute:: payee_city

            *Payee city*

        .. py:attribute:: payee_st

            *Payee st*

        .. py:attribute:: payee_zip4

            *Payee zip4*

        .. py:attribute:: amount

            *Amount*

        .. py:attribute:: aggregate

            *Aggregate*

        .. py:attribute:: expn_dscr

            *Expn dscr*

        .. py:attribute:: cand_naml

            *Cand naml*

        .. py:attribute:: cand_namf

            *Cand namf*

        .. py:attribute:: cand_namt

            *Cand namt*

        .. py:attribute:: cand_nams

            *Cand nams*

        .. py:attribute:: office_cd

            *Office cd*

        .. py:attribute:: offic_dscr

            *Offic dscr*

        .. py:attribute:: juris_cd

            *Juris cd*

        .. py:attribute:: juris_dscr

            *Juris dscr*

        .. py:attribute:: dist_no

            *Dist no*

        .. py:attribute:: off_s_h_cd

            *Off s h cd*

        .. py:attribute:: bal_name

            *Bal name*

        .. py:attribute:: bal_num

            *Bal num*

        .. py:attribute:: bal_juris

            *Bal juris*

        .. py:attribute:: sup_opp_cd

            *Sup opp cd*

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: bakref_tid

            *Bakref tid*



S496Cd
~~~~~~~~~~~~~~~~~~~~~~~
Form 496 Late Independent Expenditures

.. py:class:: S496Cd

    **Source data**

        `S496_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: amount

            *Amount*

        .. py:attribute:: exp_date

            *Exp date*

        .. py:attribute:: expn_dscr

            *Expn dscr*

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: date_thru

            *Date thru*



S497Cd
~~~~~~~~~~~~~~~~~~~~~~~
Form 497 Late Contributions Received/Made

.. py:class:: S497Cd

    **Source data**

        `S497_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: enty_naml

            *Enty naml*

        .. py:attribute:: enty_namf

            *Enty namf*

        .. py:attribute:: enty_namt

            *Enty namt*

        .. py:attribute:: enty_nams

            *Enty nams*

        .. py:attribute:: enty_city

            *Enty city*

        .. py:attribute:: enty_st

            *Enty st*

        .. py:attribute:: enty_zip4

            *Enty zip4*

        .. py:attribute:: ctrib_emp

            *Ctrib emp*

        .. py:attribute:: ctrib_occ

            *Ctrib occ*

        .. py:attribute:: ctrib_self

            *Ctrib self*

        .. py:attribute:: elec_date

            *Elec date*

        .. py:attribute:: ctrib_date

            *Ctrib date*

        .. py:attribute:: date_thru

            *Date thru*

        .. py:attribute:: amount

            *Amount*

        .. py:attribute:: cmte_id

            *Cmte id*

        .. py:attribute:: cand_naml

            *Cand naml*

        .. py:attribute:: cand_namf

            *Cand namf*

        .. py:attribute:: cand_namt

            *Cand namt*

        .. py:attribute:: cand_nams

            *Cand nams*

        .. py:attribute:: office_cd

            *Office cd*

        .. py:attribute:: offic_dscr

            *Offic dscr*

        .. py:attribute:: juris_cd

            *Juris cd*

        .. py:attribute:: juris_dscr

            *Juris dscr*

        .. py:attribute:: dist_no

            *Dist no*

        .. py:attribute:: off_s_h_cd

            *Off s h cd*

        .. py:attribute:: bal_name

            *Bal name*

        .. py:attribute:: bal_num

            *Bal num*

        .. py:attribute:: bal_juris

            *Bal juris*

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: bal_id

            *Bal id*

        .. py:attribute:: cand_id

            *Cand id*

        .. py:attribute:: sup_off_cd

            *Sup off cd*

        .. py:attribute:: sup_opp_cd

            *Sup opp cd*



S498Cd
~~~~~~~~~~~~~~~~~~~~~~~
Form 498 Slate Mailer Late Independent Expenditures Made

.. py:class:: S498Cd

    **Source data**

        `S498_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: cmte_id

            *Cmte id*

        .. py:attribute:: payor_naml

            *Payor naml*

        .. py:attribute:: payor_namf

            *Payor namf*

        .. py:attribute:: payor_namt

            *Payor namt*

        .. py:attribute:: payor_nams

            *Payor nams*

        .. py:attribute:: payor_city

            *Payor city*

        .. py:attribute:: payor_st

            *Payor st*

        .. py:attribute:: payor_zip4

            *Payor zip4*

        .. py:attribute:: date_rcvd

            *Date rcvd*

        .. py:attribute:: amt_rcvd

            *Amt rcvd*

        .. py:attribute:: cand_naml

            *Cand naml*

        .. py:attribute:: cand_namf

            *Cand namf*

        .. py:attribute:: cand_namt

            *Cand namt*

        .. py:attribute:: cand_nams

            *Cand nams*

        .. py:attribute:: office_cd

            *Office cd*

        .. py:attribute:: offic_dscr

            *Offic dscr*

        .. py:attribute:: juris_cd

            *Juris cd*

        .. py:attribute:: juris_dscr

            *Juris dscr*

        .. py:attribute:: dist_no

            *Dist no*

        .. py:attribute:: off_s_h_cd

            *Off s h cd*

        .. py:attribute:: bal_name

            *Bal name*

        .. py:attribute:: bal_num

            *Bal num*

        .. py:attribute:: bal_juris

            *Bal juris*

        .. py:attribute:: sup_opp_cd

            *Sup opp cd*

        .. py:attribute:: amt_attrib

            *Amt attrib*

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: employer

            *Employer*

        .. py:attribute:: occupation

            *Occupation*

        .. py:attribute:: selfemp_cb

            *Selfemp cb*



SpltCd
~~~~~~~~~~~~~~~~~~~~~~~
Split Records

    -- F450P5
    -- F460 (A-B1-B2-C-D-H)

.. py:class:: SpltCd

    **Source data**

        `SPLT_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: elec_amount

            *Elec amount*

        .. py:attribute:: elec_code

            *Elec code*

        .. py:attribute:: elec_date

            *Elec date*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: pform_type

            *Pform type*

        .. py:attribute:: ptran_id

            *Transaction ID* Permanent value unique to this item




Common
-------

CvrE530Cd
~~~~~~~~~~~~~~~~~~~~~~~
This table method is undocumented in the print docs.

.. py:class:: CvrE530Cd

    **Source data**

        `CVR_E530_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: filer_naml

            *Filer naml*

        .. py:attribute:: filer_namf

            *Filer namf*

        .. py:attribute:: filer_namt

            *Filer namt*

        .. py:attribute:: filer_nams

            *Filer nams*

        .. py:attribute:: report_num

            *Report num*

        .. py:attribute:: rpt_date

            *Rpt date*

        .. py:attribute:: filer_city

            *Filer city*

        .. py:attribute:: filer_st

            *Filer st*

        .. py:attribute:: filer_zip4

            *Filer zip4*

        .. py:attribute:: occupation

            *Occupation*

        .. py:attribute:: employer

            *Employer*

        .. py:attribute:: cand_naml

            *Cand naml*

        .. py:attribute:: cand_namf

            *Cand namf*

        .. py:attribute:: cand_namt

            *Cand namt*

        .. py:attribute:: cand_nams

            *Cand nams*

        .. py:attribute:: district_cd

            *District cd*

        .. py:attribute:: office_cd

            *Office cd*

        .. py:attribute:: pmnt_dt

            *Pmnt dt*

        .. py:attribute:: pmnt_amount

            *Pmnt amount*

        .. py:attribute:: type_literature

            *Type literature*

        .. py:attribute:: type_printads

            *Type printads*

        .. py:attribute:: type_radio

            *Type radio*

        .. py:attribute:: type_tv

            *Type tv*

        .. py:attribute:: type_it

            *Type it*

        .. py:attribute:: type_billboards

            *Type billboards*

        .. py:attribute:: type_other

            *Type other*

        .. py:attribute:: other_desc

            *Other desc*



FilerFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~
Key table that links filers to their paper, key data entry, legacy,
and electronic filings. This table is used as an index to locate
filing information.

.. py:class:: FilerFilingsCd

    **Source data**

        `FILER_FILINGS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: period_id

            *Period id* Identifies the period when the filing was recieved.

        .. py:attribute:: form_id

            *Form type* Form identification code

        .. py:attribute:: filing_sequence

            *Filing sequence* Amendment number where 0 is an original filing and 1 to 999 are amendments

        .. py:attribute:: filing_date

            *Filing date* Date the filing entered into the system

        .. py:attribute:: stmnt_type

            *Statement type* Type of statement

        .. py:attribute:: stmnt_status

            *Statement status* The status of the statement. If the filing has been reviewed or not reviewed.

        .. py:attribute:: session_id

            *Session id* Legislative session that the filing applies to

        .. py:attribute:: user_id

            *User id*

        .. py:attribute:: special_audit

            *Special audit* Denotes whether the filing has been audited for money laundering or other special condition.

        .. py:attribute:: fine_audit

            *Fine audit* Indicates whether a filing has been audited for a fine

        .. py:attribute:: rpt_start

            *Rpt start* Starting date for the period the filing represents

        .. py:attribute:: rpt_end

            *Rpt end* Ending date for the period the filing represents

        .. py:attribute:: rpt_date

            *Rpt date* Date filing received

        .. py:attribute:: filing_type

            *Filing type*



FilernameCd
~~~~~~~~~~~~~~~~~~~~~~~
A combination of CAL-ACCESS tables to provide the analyst with
filer information.

Full name of all PACs, firms, and employers are in the last
name field.

Major donors can be split between first and last name fields, but usually
are contained in the last name field only. Individual names of lobbyists,
candidates/officeholders, treasurers/responsible officers, and major donors
(when they are only an individual&#39;s name) use both the first and last name
fields in conjunction.

.. py:class:: FilernameCd

    **Source data**

        `FILERNAME_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: xref_filer_id

            *Crossreference filer ID* Alternative filer ID found on many forms

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filer_type

            *Filer type*

        .. py:attribute:: status

            *Status*

        .. py:attribute:: effect_dt

            *Effect dt* Effective date for status

        .. py:attribute:: naml

            *Naml* Last name, sometimes full name

        .. py:attribute:: namf

            *Namf* First name

        .. py:attribute:: namt

            *Namt* Name prefix or title

        .. py:attribute:: nams

            *Nams* Name suffix

        .. py:attribute:: adr1

            *Adr1*

        .. py:attribute:: adr2

            *Adr2*

        .. py:attribute:: city

            *City*

        .. py:attribute:: st

            *St*

        .. py:attribute:: zip4

            *Zip4*

        .. py:attribute:: phon

            *Phon*

        .. py:attribute:: fax

            *Fax*

        .. py:attribute:: email

            *Email*



FilingsCd
~~~~~~~~~~~~~~~~~~~~~~~
This table is the parent table from which all links and association to
a filing are derived.

.. py:class:: FilingsCd

    **Source data**

        `FILINGS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: filing_type

            *Filing type*



SmryCd
~~~~~~~~~~~~~~~~~~~~~~~
Summary totals from filings.

.. py:class:: SmryCd

    **Source data**

        `SMRY_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: amount_a

            *Amount A* Summary amount from column A

        .. py:attribute:: amount_b

            *Amount B* Summary amount from column B

        .. py:attribute:: amount_c

            *Amount C* Summary amount from column C

        .. py:attribute:: elec_dt

            *Election date*



TextMemoCd
~~~~~~~~~~~~~~~~~~~~~~~
Text memos attached to electronic filings

.. py:class:: TextMemoCd

    **Source data**

        `TEXT_MEMO_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: ref_no

            *Reference number* Links text memo to a specific record

        .. py:attribute:: text4000

            *Text* Contents of the text memo




Lobbying
-------

Cvr2LobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~
Additional names data for the lobbyist disclosure forms

    F615 -- Lobbyist Report
    F625 -- Report of Lobbying Firm
    F635 -- Report of Lobbyist Employer and Report of Lobbying Coalition
    F645 -- Report of Person Spending $5,000 or more to influence
            Legislative or administrative action

.. py:class:: Cvr2LobbyDisclosureCd

    **Source data**

        `CVR2_LOBBY_DISCLOSURE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: entity_id

            *Entity id*

        .. py:attribute:: enty_namf

            *Enty namf*

        .. py:attribute:: enty_naml

            *Enty naml*

        .. py:attribute:: enty_nams

            *Enty nams*

        .. py:attribute:: enty_namt

            *Enty namt*

        .. py:attribute:: enty_title

            *Enty title*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item



Cvr2RegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page of lobbying dislcosure forms

.. py:class:: Cvr2RegistrationCd

    **Source data**

        `CVR2_REGISTRATION_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: entity_id

            *Entity ID* Identification number of the entity described by the record

        .. py:attribute:: enty_naml

            *Last name*

        .. py:attribute:: enty_namf

            *First name*

        .. py:attribute:: enty_namt

            *Title*

        .. py:attribute:: enty_nams

            *Title*



CvrLobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page information for the lobbying disclosure forms

    F615 -- Lobbyist Report
    F625 -- Report of Lobbying Firm
    F635 -- Report of Lobbyist Employer and Report of Lobbying Coalition
    F645 -- Report of Person Spending $5,000 or more to influence
            Legislative or administrative action

.. py:class:: CvrLobbyDisclosureCd

    **Source data**

        `CVR_LOBBY_DISCLOSURE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: ctrib_n_cb

            *Ctrib n cb*

        .. py:attribute:: ctrib_y_cb

            *Ctrib y cb*

        .. py:attribute:: cum_beg_dt

            *Cum beg dt*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filer_namf

            *Filer namf*

        .. py:attribute:: filer_naml

            *Filer naml*

        .. py:attribute:: filer_nams

            *Filer nams*

        .. py:attribute:: filer_namt

            *Filer namt*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: firm_city

            *Firm city*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: firm_phon

            *Firm phon*

        .. py:attribute:: firm_st

            *Firm st*

        .. py:attribute:: firm_zip4

            *Firm zip4*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: from_date

            *From date*

        .. py:attribute:: lby_actvty

            *Lby actvty*

        .. py:attribute:: lobby_n_cb

            *Lobby n cb*

        .. py:attribute:: lobby_y_cb

            *Lobby y cb*

        .. py:attribute:: mail_city

            *Mail city*

        .. py:attribute:: mail_phon

            *Mail phon*

        .. py:attribute:: mail_st

            *Mail st*

        .. py:attribute:: mail_zip4

            *Mail zip4*

        .. py:attribute:: major_namf

            *Major namf*

        .. py:attribute:: major_naml

            *Major naml*

        .. py:attribute:: major_nams

            *Major nams*

        .. py:attribute:: major_namt

            *Major namt*

        .. py:attribute:: nopart1_cb

            *Nopart1 cb*

        .. py:attribute:: nopart2_cb

            *Nopart2 cb*

        .. py:attribute:: part1_1_cb

            *Part1 1 cb*

        .. py:attribute:: part1_2_cb

            *Part1 2 cb*

        .. py:attribute:: prn_namf

            *Prn namf*

        .. py:attribute:: prn_naml

            *Prn naml*

        .. py:attribute:: prn_nams

            *Prn nams*

        .. py:attribute:: prn_namt

            *Prn namt*

        .. py:attribute:: rcpcmte_id

            *Rcpcmte id*

        .. py:attribute:: rcpcmte_nm

            *Rcpcmte nm*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: report_num

            *Report num*

        .. py:attribute:: rpt_date

            *Rpt date*

        .. py:attribute:: sender_id

            *Sender id*

        .. py:attribute:: sig_date

            *Sig date*

        .. py:attribute:: sig_loc

            *Sig loc*

        .. py:attribute:: sig_namf

            *Sig namf*

        .. py:attribute:: sig_naml

            *Sig naml*

        .. py:attribute:: sig_nams

            *Sig nams*

        .. py:attribute:: sig_namt

            *Sig namt*

        .. py:attribute:: sig_title

            *Sig title*

        .. py:attribute:: thru_date

            *Thru date*



CvrRegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page of lobbying disclosure forms

.. py:class:: CvrRegistrationCd

    **Source data**

        `CVR_REGISTRATION_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: a_b_city

            *A b city*

        .. py:attribute:: a_b_name

            *A b name*

        .. py:attribute:: a_b_st

            *A b st*

        .. py:attribute:: a_b_zip4

            *A b zip4*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: auth_city

            *Auth city*

        .. py:attribute:: auth_name

            *Auth name*

        .. py:attribute:: auth_st

            *Auth st*

        .. py:attribute:: auth_zip4

            *Auth zip4*

        .. py:attribute:: bus_cb

            *Bus cb*

        .. py:attribute:: bus_city

            *Bus city*

        .. py:attribute:: bus_class

            *Bus class*

        .. py:attribute:: bus_descr

            *Bus descr*

        .. py:attribute:: bus_email

            *Bus email*

        .. py:attribute:: bus_fax

            *Bus fax*

        .. py:attribute:: bus_phon

            *Bus phon*

        .. py:attribute:: bus_st

            *Bus st*

        .. py:attribute:: bus_zip4

            *Bus zip4*

        .. py:attribute:: c_less50

            *C less50*

        .. py:attribute:: c_more50

            *C more50*

        .. py:attribute:: complet_dt

            *Complet dt*

        .. py:attribute:: descrip_1

            *Descrip 1*

        .. py:attribute:: descrip_2

            *Descrip 2*

        .. py:attribute:: eff_date

            *Eff date*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filer_namf

            *Filer namf*

        .. py:attribute:: filer_naml

            *Filer naml*

        .. py:attribute:: filer_nams

            *Filer nams*

        .. py:attribute:: filer_namt

            *Filer namt*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: ind_cb

            *Ind cb*

        .. py:attribute:: ind_class

            *Ind class*

        .. py:attribute:: ind_descr

            *Ind descr*

        .. py:attribute:: influen_yn

            *Influen yn*

        .. py:attribute:: l_firm_cb

            *L firm cb*

        .. py:attribute:: lby_604_cb

            *Lby 604 cb*

        .. py:attribute:: lby_reg_cb

            *Lby reg cb*

        .. py:attribute:: lobby_cb

            *Lobby cb*

        .. py:attribute:: lobby_int

            *Lobby int*

        .. py:attribute:: ls_beg_yr

            *Ls beg yr*

        .. py:attribute:: ls_end_yr

            *Ls end yr*

        .. py:attribute:: mail_city

            *Mail city*

        .. py:attribute:: mail_phon

            *Mail phon*

        .. py:attribute:: mail_st

            *Mail st*

        .. py:attribute:: mail_zip4

            *Mail zip4*

        .. py:attribute:: newcert_cb

            *Newcert cb*

        .. py:attribute:: oth_cb

            *Oth cb*

        .. py:attribute:: prn_namf

            *Prn namf*

        .. py:attribute:: prn_naml

            *Prn naml*

        .. py:attribute:: prn_nams

            *Prn nams*

        .. py:attribute:: prn_namt

            *Prn namt*

        .. py:attribute:: qual_date

            *Qual date*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: rencert_cb

            *Rencert cb*

        .. py:attribute:: report_num

            *Report num*

        .. py:attribute:: rpt_date

            *Rpt date*

        .. py:attribute:: sender_id

            *Sender id*

        .. py:attribute:: sig_date

            *Sig date*

        .. py:attribute:: sig_loc

            *Sig loc*

        .. py:attribute:: sig_namf

            *Sig namf*

        .. py:attribute:: sig_naml

            *Sig naml*

        .. py:attribute:: sig_nams

            *Sig nams*

        .. py:attribute:: sig_namt

            *Sig namt*

        .. py:attribute:: sig_title

            *Sig title*

        .. py:attribute:: st_agency

            *St agency*

        .. py:attribute:: st_leg_yn

            *St leg yn*

        .. py:attribute:: stmt_firm

            *Stmt firm*

        .. py:attribute:: trade_cb

            *Trade cb*



F690P2Cd
~~~~~~~~~~~~~~~~~~~~~~~
Amends lobbying disclosure filings

    F690 Amendment to Lobbying Disclosure Report

.. py:class:: F690P2Cd

    **Source data**

        `F690P2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: exec_date

            *Exec date* date the original report (or prior amendment to the original report) was executed on.

        .. py:attribute:: from_date

            *From date* reporting period from date of original report

        .. py:attribute:: thru_date

            *Thru date* report period to/through date of original.

        .. py:attribute:: chg_parts

            *Chg parts* amended into affects items on part(s) text description.

        .. py:attribute:: chg_sects

            *Chg sects* amended into affects items on sections(s) text description.

        .. py:attribute:: amend_txt1

            *Amend txt1* description of changes to the filing



LattCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist disclosure attachment schedules for payments
    F630 -- Payments made to Lobbying Coalitions (Attatchment)
    F635C -- Payments received by Lobbying Coalitions (Attatchment)
    F640 -- Government Agencies Reporting of &quot;Other Payments to Influence
            Legislative or Administrative Action&quot; (Attatchment)

.. py:class:: LattCd

    **Source data**

        `LATT_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: amount

            *Amount*

        .. py:attribute:: cum_amt

            *Cum amt*

        .. py:attribute:: cumbeg_dt

            *Cumbeg dt*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: pmt_date

            *Pmt date*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: recip_city

            *Recip city*

        .. py:attribute:: recip_namf

            *Recip namf*

        .. py:attribute:: recip_naml

            *Recip naml*

        .. py:attribute:: recip_nams

            *Recip nams*

        .. py:attribute:: recip_namt

            *Recip namt*

        .. py:attribute:: recip_st

            *Recip st*

        .. py:attribute:: recip_zip4

            *Recip zip4*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item



LccmCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbying Campaign Contributions reported on forms

    F615 Part 2
    F625 Part 4B
    F635 Part 4B
    F645 Part 3B

.. py:class:: LccmCd

    **Source data**

        `LCCM_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: amount

            *Amount*

        .. py:attribute:: bakref_tid

            *Bakref tid*

        .. py:attribute:: ctrib_date

            *Ctrib date*

        .. py:attribute:: ctrib_namf

            *Ctrib namf*

        .. py:attribute:: ctrib_naml

            *Ctrib naml*

        .. py:attribute:: ctrib_nams

            *Ctrib nams*

        .. py:attribute:: ctrib_namt

            *Ctrib namt*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: recip_city

            *Recip city*

        .. py:attribute:: recip_id

            *Recip id*

        .. py:attribute:: recip_namf

            *Recip namf*

        .. py:attribute:: recip_naml

            *Recip naml*

        .. py:attribute:: recip_nams

            *Recip nams*

        .. py:attribute:: recip_namt

            *Recip namt*

        .. py:attribute:: recip_st

            *Recip st*

        .. py:attribute:: recip_zip4

            *Recip zip4*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item



LempCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist Employers/Subcontracted Clients data from

    F601 -- Lobbying Firm Registration Statement
    F601 Part 2 A
    F601 Part 2 B

.. py:class:: LempCd

    **Source data**

        `LEMP_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: agencylist

            *Agencylist*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: cli_city

            *Cli city*

        .. py:attribute:: cli_namf

            *Cli namf*

        .. py:attribute:: cli_naml

            *Cli naml*

        .. py:attribute:: cli_nams

            *Cli nams*

        .. py:attribute:: cli_namt

            *Cli namt*

        .. py:attribute:: cli_phon

            *Cli phon*

        .. py:attribute:: cli_st

            *Cli st*

        .. py:attribute:: cli_zip4

            *Cli zip4*

        .. py:attribute:: client_id

            *Client id*

        .. py:attribute:: con_period

            *Con period*

        .. py:attribute:: descrip

            *Descrip*

        .. py:attribute:: eff_date

            *Eff date*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: sub_city

            *Sub city*

        .. py:attribute:: sub_name

            *Sub name*

        .. py:attribute:: sub_phon

            *Sub phon*

        .. py:attribute:: sub_st

            *Sub st*

        .. py:attribute:: sub_zip4

            *Sub zip4*

        .. py:attribute:: subfirm_id

            *Subfirm id*



LexpCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbying Activity Expenditure Schedule information (Gifts)
Reported in filings of the forms

    F615 Part 1
    F625 Part 3A
    F635 Part 3C
    F645 Part 2A

.. py:class:: LexpCd

    **Source data**

        `LEXP_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: amount

            *Amount*

        .. py:attribute:: bakref_tid

            *Bakref tid*

        .. py:attribute:: bene_amt

            *Bene amt*

        .. py:attribute:: bene_name

            *Bene name*

        .. py:attribute:: bene_posit

            *Bene posit*

        .. py:attribute:: credcardco

            *Credcardco*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: expn_date

            *Expn date*

        .. py:attribute:: expn_dscr

            *Expn dscr*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: payee_city

            *Payee city*

        .. py:attribute:: payee_namf

            *Payee namf*

        .. py:attribute:: payee_naml

            *Payee naml*

        .. py:attribute:: payee_nams

            *Payee nams*

        .. py:attribute:: payee_namt

            *Payee namt*

        .. py:attribute:: payee_st

            *Payee st*

        .. py:attribute:: payee_zip4

            *Payee zip4*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: recsubtype

            *Recsubtype*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item



LobbyAmendmentsCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist registration amendment information

    Form 605 Part I

.. py:class:: LobbyAmendmentsCd

    **Source data**

        `LOBBY_AMENDMENTS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: exec_date

            *Exec date*

        .. py:attribute:: from_date

            *From date*

        .. py:attribute:: thru_date

            *Thru date*

        .. py:attribute:: add_l_cb

            *Add l cb*

        .. py:attribute:: add_l_eff

            *Add l eff*

        .. py:attribute:: a_l_naml

            *A l naml*

        .. py:attribute:: a_l_namf

            *A l namf*

        .. py:attribute:: a_l_namt

            *A l namt*

        .. py:attribute:: a_l_nams

            *A l nams*

        .. py:attribute:: del_l_cb

            *Del l cb*

        .. py:attribute:: del_l_eff

            *Del l eff*

        .. py:attribute:: d_l_naml

            *D l naml*

        .. py:attribute:: d_l_namf

            *D l namf*

        .. py:attribute:: d_l_namt

            *D l namt*

        .. py:attribute:: d_l_nams

            *D l nams*

        .. py:attribute:: add_le_cb

            *Add le cb*

        .. py:attribute:: add_le_eff

            *Add le eff*

        .. py:attribute:: a_le_naml

            *A le naml*

        .. py:attribute:: a_le_namf

            *A le namf*

        .. py:attribute:: a_le_namt

            *A le namt*

        .. py:attribute:: a_le_nams

            *A le nams*

        .. py:attribute:: del_le_cb

            *Del le cb*

        .. py:attribute:: del_le_eff

            *Del le eff*

        .. py:attribute:: d_le_naml

            *D le naml*

        .. py:attribute:: d_le_namf

            *D le namf*

        .. py:attribute:: d_le_namt

            *D le namt*

        .. py:attribute:: d_le_nams

            *D le nams*

        .. py:attribute:: add_lf_cb

            *Add lf cb*

        .. py:attribute:: add_lf_eff

            *Add lf eff*

        .. py:attribute:: a_lf_name

            *A lf name*

        .. py:attribute:: del_lf_cb

            *Del lf cb*

        .. py:attribute:: del_lf_eff

            *Del lf eff*

        .. py:attribute:: d_lf_name

            *D lf name*

        .. py:attribute:: other_cb

            *Other cb*

        .. py:attribute:: other_eff

            *Other eff*

        .. py:attribute:: other_desc

            *Other desc*

        .. py:attribute:: f606_yes

            *F606 yes*

        .. py:attribute:: f606_no

            *F606 no*



LothCd
~~~~~~~~~~~~~~~~~~~~~~~
Payment to other lobbying firms reported on form

    F625 Part 3B

.. py:class:: LothCd

    **Source data**

        `LOTH_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: amount

            *Amount*

        .. py:attribute:: cum_amt

            *Cum amt*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: firm_city

            *Firm city*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: firm_phon

            *Firm phon*

        .. py:attribute:: firm_st

            *Firm st*

        .. py:attribute:: firm_zip4

            *Firm zip4*

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: pmt_date

            *Pmt date*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: subj_namf

            *Subj namf*

        .. py:attribute:: subj_naml

            *Subj naml*

        .. py:attribute:: subj_nams

            *Subj nams*

        .. py:attribute:: subj_namt

            *Subj namt*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item



LpayCd
~~~~~~~~~~~~~~~~~~~~~~~
Payments made/received to/from Lobbying Firms reported on forms

    F625 Part 2
    F635 Part 3B

.. py:class:: LpayCd

    **Source data**

        `LPAY_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: advan_amt

            *Advan amt*

        .. py:attribute:: advan_dscr

            *Advan dscr*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: bakref_tid

            *Bakref tid*

        .. py:attribute:: cum_total

            *Cum total*

        .. py:attribute:: emplr_city

            *Emplr city*

        .. py:attribute:: emplr_id

            *Emplr id*

        .. py:attribute:: emplr_namf

            *Emplr namf*

        .. py:attribute:: emplr_naml

            *Emplr naml*

        .. py:attribute:: emplr_nams

            *Emplr nams*

        .. py:attribute:: emplr_namt

            *Emplr namt*

        .. py:attribute:: emplr_phon

            *Emplr phon*

        .. py:attribute:: emplr_st

            *Emplr st*

        .. py:attribute:: emplr_zip4

            *Emplr zip4*

        .. py:attribute:: entity_cd

            *Entity code*

        .. py:attribute:: fees_amt

            *Fees amt*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: lby_actvty

            *Lby actvty*

        .. py:attribute:: line_item

            *Line item* Line item number of this record

        .. py:attribute:: memo_code

            *Memo code*

        .. py:attribute:: memo_refno

            *Memo refno*

        .. py:attribute:: per_total

            *Per total*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: reimb_amt

            *Reimb amt*

        .. py:attribute:: tran_id

            *Transaction ID* Permanent value unique to this item




Other
-------

AcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~
Contains acronyms and their meaning.

.. py:class:: AcronymsCd

    **Source data**

        `ACRONYMS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: acronym

            *Acronym* Acronym text value

        .. py:attribute:: stands_for

            *Stands for* Definition of the acronym

        .. py:attribute:: effect_dt

            *Effect dt* Effective date for the acronym

        .. py:attribute:: a_desc

            *A desc* Description of the acronym



AddressCd
~~~~~~~~~~~~~~~~~~~~~~~
This table holds all addresses for the system. This table can be used
for address-based searches and formes the bases for address information
desplayed by the AMS.

.. py:class:: AddressCd

    **Source data**

        `ADDRESS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: adrid

            *Adrid* Address indentification number

        .. py:attribute:: city

            *City*

        .. py:attribute:: st

            *St*

        .. py:attribute:: zip4

            *Zip4*

        .. py:attribute:: phon

            *Phon*

        .. py:attribute:: fax

            *Fax*

        .. py:attribute:: email

            *Email*



BallotMeasuresCd
~~~~~~~~~~~~~~~~~~~~~~~
Ballot measure dates and times

.. py:class:: BallotMeasuresCd

    **Source data**

        `BALLOT_MEASURES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: election_date

            *Election date*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: measure_no

            *Measure no*

        .. py:attribute:: measure_name

            *Measure name*

        .. py:attribute:: measure_short_name

            *Measure short name*

        .. py:attribute:: jurisdiction

            *Jurisdiction*



EfsFilingLogCd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: EfsFilingLogCd

    **Source data**

        `EFS_FILING_LOG_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filing_date

            *Filing date*

        .. py:attribute:: filingstatus

            *Filingstatus*

        .. py:attribute:: vendor

            *Vendor*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: form_type

            *Form type* Name of the source filing form or schedule

        .. py:attribute:: error_no

            *Error no*



FilerAcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~
links acronyms to filers

.. py:class:: FilerAcronymsCd

    **Source data**

        `FILER_ACRONYMS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: acronym

            *Acronym*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number



FilerAddressCd
~~~~~~~~~~~~~~~~~~~~~~~
Links filers and addresses. This table maintains a history of when
addresses change.

.. py:class:: FilerAddressCd

    **Source data**

        `FILER_ADDRESS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: adrid

            *Adrid*

        .. py:attribute:: effect_dt

            *Effect dt*

        .. py:attribute:: add_type

            *Add type*

        .. py:attribute:: session_id

            *Session id*



FilerEthicsClassCd
~~~~~~~~~~~~~~~~~~~~~~~
This table stores lobbyist ethics training dates.

.. py:class:: FilerEthicsClassCd

    **Source data**

        `FILER_ETHICS_CLASS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: ethics_date

            *Ethics date*



FilerInterestsCd
~~~~~~~~~~~~~~~~~~~~~~~
Links a filer to their interest codes.

.. py:class:: FilerInterestsCd

    **Source data**

        `FILER_INTERESTS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: interest_cd

            *Interest cd*

        .. py:attribute:: effect_date

            *Effect date*



FilerLinksCd
~~~~~~~~~~~~~~~~~~~~~~~
Links filers to each other and records their relationship type.

.. py:class:: FilerLinksCd

    **Source data**

        `FILER_LINKS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id_a

            *Filer ID A* Unique identification number for the first filer in the relationship

        .. py:attribute:: filer_id_b

            *Filer ID B* Unique identification number for the second filer in the relationship

        .. py:attribute:: active_flg

            *Active flag* Indicates if the link is active

        .. py:attribute:: session_id

            *Session ID* Session identification number

        .. py:attribute:: link_type

            *Link type* Denotes the type of the link

        .. py:attribute:: link_desc

            *Link description* Unused

        .. py:attribute:: effect_dt

            *Effective date* Date the link became active

        .. py:attribute:: dominate_filer

            *Dominate filer* Unused

        .. py:attribute:: termination_dt

            *Termination date* Date the relationship was terminated



FilerStatusTypesCd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: FilerStatusTypesCd

    **Source data**

        `FILER_STATUS_TYPES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: status_type

            *Status type*

        .. py:attribute:: status_desc

            *Status desc*



FilerToFilerTypeCd
~~~~~~~~~~~~~~~~~~~~~~~
This table links a filer to a set of characteristics that describe the
filer. This table maintains a history of changes and allows the filer
to change characteristics over time.

.. py:class:: FilerToFilerTypeCd

    **Source data**

        `FILER_TO_FILER_TYPE_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filer_type

            *Filer type* Filer type identification number

        .. py:attribute:: active

            *Active* Indicates if the filer is currently active

        .. py:attribute:: race

            *Race* If applicable indicates the race in which the filer is running

        .. py:attribute:: session_id

            *Session id* Legislative session identification number

        .. py:attribute:: category

            *Category* Defines the filer's category such as controlled, jointly controlled, etc. (subset of filer's type)

        .. py:attribute:: category_type

            *Category type* When applicable, the category type specifies additional information about the category. (e.g. state, local, etc.)

        .. py:attribute:: sub_category

            *Sub category* When applicable specifies general purpose, primarily formed, etc.

        .. py:attribute:: effect_dt

            *Effect dt* The date the filer assumed the current class or type

        .. py:attribute:: sub_category_type

            *Sub category type* When applicable specifies broad based or small contributor

        .. py:attribute:: election_type

            *Election type* Indicates type of election (general, primary, special)

        .. py:attribute:: sub_category_a

            *Sub category a* Indicates if sponsored or not

        .. py:attribute:: nyq_dt

            *Nyq dt* Indicates the date when a committee reached its qualifying level of activity

        .. py:attribute:: party_cd

            *Party cd* Filer's political party

        .. py:attribute:: county_cd

            *County cd* Filer's county code

        .. py:attribute:: district_cd

            *District cd* Filer's district number for the office being sought. Populated for Senate, Assembly or Board of Equalization races



FilerTypesCd
~~~~~~~~~~~~~~~~~~~~~~~
This lookup table describes filer types.

.. py:class:: FilerTypesCd

    **Source data**

        `FILER_TYPES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_type

            *Filer type* Filer type identification number

        .. py:attribute:: description

            *Description* Description of the filer type

        .. py:attribute:: grp_type

            *Grp type* Group type assocated with the filer type

        .. py:attribute:: calc_use

            *Calc use* Use checkbox flag

        .. py:attribute:: grace_period

            *Grace period*



FilerXrefCd
~~~~~~~~~~~~~~~~~~~~~~~
This table maps legacy filer identification numbers to the system&#39;s filer
identification numbers.

.. py:class:: FilerXrefCd

    **Source data**

        `FILER_XREF_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: xref_id

            *Crossreference filer ID* Alternative filer ID found on many forms

        .. py:attribute:: effect_dt

            *Effect dt*

        .. py:attribute:: migration_source

            *Migration source*



FilersCd
~~~~~~~~~~~~~~~~~~~~~~~
This table is the parent table from which all links and associations
to a filer are derived.

.. py:class:: FilersCd

    **Source data**

        `FILERS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number



FilingPeriodCd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: FilingPeriodCd

    **Source data**

        `FILING_PERIOD_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: period_id

            *Period id* Unique period identification number

        .. py:attribute:: start_date

            *Start date* Starting date for period

        .. py:attribute:: end_date

            *End date* Ending date of period

        .. py:attribute:: period_type

            *Period type*

        .. py:attribute:: per_grp_type

            *Per grp type* Period group type

        .. py:attribute:: period_desc

            *Period desc* Period description

        .. py:attribute:: deadline

            *Deadline* Deadline date



GroupTypesCd
~~~~~~~~~~~~~~~~~~~~~~~
This lookup table stores group type information.

.. py:class:: GroupTypesCd

    **Source data**

        `GROUP_TYPES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: grp_id

            *Grp id*

        .. py:attribute:: grp_name

            *Grp name*

        .. py:attribute:: grp_desc

            *Grp desc*



HdrCd
~~~~~~~~~~~~~~~~~~~~~~~
Electronic filing record header data

.. py:class:: HdrCd

    **Source data**

        `HDR_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: amend_id

            *Amendment ID* Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.

        .. py:attribute:: cal_ver

            *Cal ver*

        .. py:attribute:: ef_type

            *Ef type*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: hdr_comment

            *Hdr comment*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: soft_name

            *Soft name*

        .. py:attribute:: soft_ver

            *Soft ver*

        .. py:attribute:: state_cd

            *State cd*



HeaderCd
~~~~~~~~~~~~~~~~~~~~~~~
Lookup table used to report form 460 information in the AMS.

.. py:class:: HeaderCd

    **Source data**

        `HEADER_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: line_number

            *Line number*

        .. py:attribute:: form_id

            *Form id*

        .. py:attribute:: rec_type

            *Record type*

        .. py:attribute:: section_label

            *Section label*

        .. py:attribute:: comments1

            *Comments1*

        .. py:attribute:: comments2

            *Comments2*

        .. py:attribute:: label

            *Label*

        .. py:attribute:: column_a

            *Column a*

        .. py:attribute:: column_b

            *Column b*

        .. py:attribute:: column_c

            *Column c*

        .. py:attribute:: show_c

            *Show c*

        .. py:attribute:: show_b

            *Show b*



ImageLinksCd
~~~~~~~~~~~~~~~~~~~~~~~
This table links images to filers and accounts.

.. py:class:: ImageLinksCd

    **Source data**

        `IMAGE_LINKS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: img_link_id

            *Img link id*

        .. py:attribute:: img_link_type

            *Img link type*

        .. py:attribute:: img_id

            *Img id*

        .. py:attribute:: img_type

            *Img type*

        .. py:attribute:: img_dt

            *Img dt*



LegislativeSessionsCd
~~~~~~~~~~~~~~~~~~~~~~~
Legislative session, begin and end dates look up table.

.. py:class:: LegislativeSessionsCd

    **Source data**

        `LEGISLATIVE_SESSIONS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: begin_date

            *Begin date*

        .. py:attribute:: end_date

            *End date*



LobbyingChgLogCd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyingChgLogCd

    **Source data**

        `LOBBYING_CHG_LOG_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: change_no

            *Change no*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: log_dt

            *Log dt*

        .. py:attribute:: filer_type

            *Filer type*

        .. py:attribute:: correction_flag

            *Correction flag*

        .. py:attribute:: action

            *Action*

        .. py:attribute:: attribute_changed

            *Attribute changed*

        .. py:attribute:: ethics_dt

            *Ethics dt*

        .. py:attribute:: interests

            *Interests*

        .. py:attribute:: filer_full_name

            *Filer full name*

        .. py:attribute:: filer_city

            *Filer city*

        .. py:attribute:: filer_st

            *Filer st*

        .. py:attribute:: filer_zip

            *Filer zip*

        .. py:attribute:: filer_phone

            *Filer phone*

        .. py:attribute:: entity_type

            *Entity type*

        .. py:attribute:: entity_name

            *Entity name*

        .. py:attribute:: entity_city

            *Entity city*

        .. py:attribute:: entity_st

            *Entity st*

        .. py:attribute:: entity_zip

            *Entity zip*

        .. py:attribute:: entity_phone

            *Entity phone*

        .. py:attribute:: entity_id

            *Entity id*

        .. py:attribute:: responsible_officer

            *Responsible officer*

        .. py:attribute:: effect_dt

            *Effect dt*



LobbyistContributions1Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistContributions1Cd

    **Source data**

        `LOBBYIST_CONTRIBUTIONS1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filing_period_start_dt

            *Filing period start dt*

        .. py:attribute:: filing_period_end_dt

            *Filing period end dt*

        .. py:attribute:: contribution_dt

            *Contribution dt*

        .. py:attribute:: recipient_name

            *Recipient name*

        .. py:attribute:: recipient_id

            *Recipient id*

        .. py:attribute:: amount

            *Amount*



LobbyistContributions2Cd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist contribution disclosure table. Temporary table used to generate
disclosure table (Lobbyist Contributions 3)

.. py:class:: LobbyistContributions2Cd

    **Source data**

        `LOBBYIST_CONTRIBUTIONS2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filing_period_start_dt

            *Filing period start dt*

        .. py:attribute:: filing_period_end_dt

            *Filing period end dt*

        .. py:attribute:: contribution_dt

            *Contribution dt*

        .. py:attribute:: recipient_name

            *Recipient name*

        .. py:attribute:: recipient_id

            *Recipient id*

        .. py:attribute:: amount

            *Amount*



LobbyistContributions3Cd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist contribution disclosure table.

.. py:class:: LobbyistContributions3Cd

    **Source data**

        `LOBBYIST_CONTRIBUTIONS3_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filing_period_start_dt

            *Filing period start dt*

        .. py:attribute:: filing_period_end_dt

            *Filing period end dt*

        .. py:attribute:: contribution_dt

            *Contribution dt*

        .. py:attribute:: recipient_name

            *Recipient name*

        .. py:attribute:: recipient_id

            *Recipient id*

        .. py:attribute:: amount

            *Amount*



LobbyistEmpLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistEmpLobbyist1Cd

    **Source data**

        `LOBBYIST_EMP_LOBBYIST1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: lobbyist_id

            *Lobbyist id*

        .. py:attribute:: employer_id

            *Employer id*

        .. py:attribute:: lobbyist_last_name

            *Lobbyist last name*

        .. py:attribute:: lobbyist_first_name

            *Lobbyist first name*

        .. py:attribute:: employer_name

            *Employer name*

        .. py:attribute:: session_id

            *Session id*



LobbyistEmpLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmpLobbyist2Cd

    **Source data**

        `LOBBYIST_EMP_LOBBYIST2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: lobbyist_id

            *Lobbyist id*

        .. py:attribute:: employer_id

            *Employer id*

        .. py:attribute:: lobbyist_last_name

            *Lobbyist last name*

        .. py:attribute:: lobbyist_first_name

            *Lobbyist first name*

        .. py:attribute:: employer_name

            *Employer name*

        .. py:attribute:: session_id

            *Session id*



LobbyistEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmployer1Cd

    **Source data**

        `LOBBYIST_EMPLOYER1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: employer_id

            *Employer id*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: employer_name

            *Employer name*

        .. py:attribute:: current_qtr_amt

            *Current qtr amt*

        .. py:attribute:: session_total_amt

            *Session total amt*

        .. py:attribute:: contributor_id

            *Contributor id*

        .. py:attribute:: interest_cd

            *Interest cd*

        .. py:attribute:: interest_name

            *Interest name*

        .. py:attribute:: session_yr_1

            *Session yr 1*

        .. py:attribute:: session_yr_2

            *Session yr 2*

        .. py:attribute:: yr_1_ytd_amt

            *Yr 1 ytd amt*

        .. py:attribute:: yr_2_ytd_amt

            *Yr 2 ytd amt*

        .. py:attribute:: qtr_1

            *Qtr 1*

        .. py:attribute:: qtr_2

            *Qtr 2*

        .. py:attribute:: qtr_3

            *Qtr 3*

        .. py:attribute:: qtr_4

            *Qtr 4*

        .. py:attribute:: qtr_5

            *Qtr 5*

        .. py:attribute:: qtr_6

            *Qtr 6*

        .. py:attribute:: qtr_7

            *Qtr 7*

        .. py:attribute:: qtr_8

            *Qtr 8*



LobbyistEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmployer2Cd

    **Source data**

        `LOBBYIST_EMPLOYER2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: employer_id

            *Employer id*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: employer_name

            *Employer name*

        .. py:attribute:: current_qtr_amt

            *Current qtr amt*

        .. py:attribute:: session_total_amt

            *Session total amt*

        .. py:attribute:: contributor_id

            *Contributor id*

        .. py:attribute:: interest_cd

            *Interest cd*

        .. py:attribute:: interest_name

            *Interest name*

        .. py:attribute:: session_yr_1

            *Session yr 1*

        .. py:attribute:: session_yr_2

            *Session yr 2*

        .. py:attribute:: yr_1_ytd_amt

            *Yr 1 ytd amt*

        .. py:attribute:: yr_2_ytd_amt

            *Yr 2 ytd amt*

        .. py:attribute:: qtr_1

            *Qtr 1*

        .. py:attribute:: qtr_2

            *Qtr 2*

        .. py:attribute:: qtr_3

            *Qtr 3*

        .. py:attribute:: qtr_4

            *Qtr 4*

        .. py:attribute:: qtr_5

            *Qtr 5*

        .. py:attribute:: qtr_6

            *Qtr 6*

        .. py:attribute:: qtr_7

            *Qtr 7*

        .. py:attribute:: qtr_8

            *Qtr 8*



LobbyistEmployer3Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmployer3Cd

    **Source data**

        `LOBBYIST_EMPLOYER3_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: employer_id

            *Employer id*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: employer_name

            *Employer name*

        .. py:attribute:: current_qtr_amt

            *Current qtr amt*

        .. py:attribute:: session_total_amt

            *Session total amt*

        .. py:attribute:: contributor_id

            *Contributor id*

        .. py:attribute:: interest_cd

            *Interest cd*

        .. py:attribute:: interest_name

            *Interest name*

        .. py:attribute:: session_yr_1

            *Session yr 1*

        .. py:attribute:: session_yr_2

            *Session yr 2*

        .. py:attribute:: yr_1_ytd_amt

            *Yr 1 ytd amt*

        .. py:attribute:: yr_2_ytd_amt

            *Yr 2 ytd amt*

        .. py:attribute:: qtr_1

            *Qtr 1*

        .. py:attribute:: qtr_2

            *Qtr 2*

        .. py:attribute:: qtr_3

            *Qtr 3*

        .. py:attribute:: qtr_4

            *Qtr 4*

        .. py:attribute:: qtr_5

            *Qtr 5*

        .. py:attribute:: qtr_6

            *Qtr 6*

        .. py:attribute:: qtr_7

            *Qtr 7*

        .. py:attribute:: qtr_8

            *Qtr 8*



LobbyistEmployerFirms1Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmployerFirms1Cd

    **Source data**

        `LOBBYIST_EMPLOYER_FIRMS1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: employer_id

            *Employer id*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: termination_dt

            *Termination dt*



LobbyistEmployerFirms2Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistEmployerFirms2Cd

    **Source data**

        `LOBBYIST_EMPLOYER_FIRMS2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: employer_id

            *Employer id*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: termination_dt

            *Termination dt*



LobbyistFirm1Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistFirm1Cd

    **Source data**

        `LOBBYIST_FIRM1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: current_qtr_amt

            *Current qtr amt*

        .. py:attribute:: session_total_amt

            *Session total amt*

        .. py:attribute:: contributor_id

            *Contributor id*

        .. py:attribute:: session_yr_1

            *Session yr 1*

        .. py:attribute:: session_yr_2

            *Session yr 2*

        .. py:attribute:: yr_1_ytd_amt

            *Yr 1 ytd amt*

        .. py:attribute:: yr_2_ytd_amt

            *Yr 2 ytd amt*

        .. py:attribute:: qtr_1

            *Qtr 1*

        .. py:attribute:: qtr_2

            *Qtr 2*

        .. py:attribute:: qtr_3

            *Qtr 3*

        .. py:attribute:: qtr_4

            *Qtr 4*

        .. py:attribute:: qtr_5

            *Qtr 5*

        .. py:attribute:: qtr_6

            *Qtr 6*

        .. py:attribute:: qtr_7

            *Qtr 7*

        .. py:attribute:: qtr_8

            *Qtr 8*



LobbyistFirm2Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistFirm2Cd

    **Source data**

        `LOBBYIST_FIRM2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: current_qtr_amt

            *Current qtr amt*

        .. py:attribute:: session_total_amt

            *Session total amt*

        .. py:attribute:: contributor_id

            *Contributor id*

        .. py:attribute:: session_yr_1

            *Session yr 1*

        .. py:attribute:: session_yr_2

            *Session yr 2*

        .. py:attribute:: yr_1_ytd_amt

            *Yr 1 ytd amt*

        .. py:attribute:: yr_2_ytd_amt

            *Yr 2 ytd amt*

        .. py:attribute:: qtr_1

            *Qtr 1*

        .. py:attribute:: qtr_2

            *Qtr 2*

        .. py:attribute:: qtr_3

            *Qtr 3*

        .. py:attribute:: qtr_4

            *Qtr 4*

        .. py:attribute:: qtr_5

            *Qtr 5*

        .. py:attribute:: qtr_6

            *Qtr 6*

        .. py:attribute:: qtr_7

            *Qtr 7*

        .. py:attribute:: qtr_8

            *Qtr 8*



LobbyistFirm3Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistFirm3Cd

    **Source data**

        `LOBBYIST_FIRM3_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: session_id

            *Session id*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: current_qtr_amt

            *Current qtr amt*

        .. py:attribute:: session_total_amt

            *Session total amt*

        .. py:attribute:: contributor_id

            *Contributor id*

        .. py:attribute:: session_yr_1

            *Session yr 1*

        .. py:attribute:: session_yr_2

            *Session yr 2*

        .. py:attribute:: yr_1_ytd_amt

            *Yr 1 ytd amt*

        .. py:attribute:: yr_2_ytd_amt

            *Yr 2 ytd amt*

        .. py:attribute:: qtr_1

            *Qtr 1*

        .. py:attribute:: qtr_2

            *Qtr 2*

        .. py:attribute:: qtr_3

            *Qtr 3*

        .. py:attribute:: qtr_4

            *Qtr 4*

        .. py:attribute:: qtr_5

            *Qtr 5*

        .. py:attribute:: qtr_6

            *Qtr 6*

        .. py:attribute:: qtr_7

            *Qtr 7*

        .. py:attribute:: qtr_8

            *Qtr 8*



LobbyistFirmEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model (Ask Matt)

.. py:class:: LobbyistFirmEmployer1Cd

    **Source data**

        `LOBBYIST_FIRM_EMPLOYER1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: filing_sequence

            *Filing sequence*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: employer_name

            *Employer name*

        .. py:attribute:: rpt_start

            *Rpt start*

        .. py:attribute:: rpt_end

            *Rpt end*

        .. py:attribute:: per_total

            *Per total*

        .. py:attribute:: cum_total

            *Cum total*

        .. py:attribute:: lby_actvty

            *Lby actvty*

        .. py:attribute:: ext_lby_actvty

            *Ext lby actvty*



LobbyistFirmEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model

.. py:class:: LobbyistFirmEmployer2Cd

    **Source data**

        `LOBBYIST_FIRM_EMPLOYER2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: filing_sequence

            *Filing sequence*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: employer_name

            *Employer name*

        .. py:attribute:: rpt_start

            *Rpt start*

        .. py:attribute:: rpt_end

            *Rpt end*

        .. py:attribute:: per_total

            *Per total*

        .. py:attribute:: cum_total

            *Cum total*

        .. py:attribute:: lby_actvty

            *Lby actvty*

        .. py:attribute:: ext_lby_actvty

            *Ext lby actvty*



LobbyistFirmLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~
It&#39;s an undocumented model.

.. py:class:: LobbyistFirmLobbyist1Cd

    **Source data**

        `LOBBYIST_FIRM_LOBBYIST1_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: lobbyist_id

            *Lobbyist id*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: lobbyist_last_name

            *Lobbyist last name*

        .. py:attribute:: lobbyist_first_name

            *Lobbyist first name*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: session_id

            *Session id*



LobbyistFirmLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistFirmLobbyist2Cd

    **Source data**

        `LOBBYIST_FIRM_LOBBYIST2_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: lobbyist_id

            *Lobbyist id*

        .. py:attribute:: firm_id

            *Firm id*

        .. py:attribute:: lobbyist_last_name

            *Lobbyist last name*

        .. py:attribute:: lobbyist_first_name

            *Lobbyist first name*

        .. py:attribute:: firm_name

            *Firm name*

        .. py:attribute:: session_id

            *Session id*



LookupCode
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LookupCode

    **Source data**

        `LOOKUP_CODES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: code_type

            *Code type*

        .. py:attribute:: code_id

            *Code id*

        .. py:attribute:: code_desc

            *Code desc*



NamesCd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: NamesCd

    **Source data**

        `NAMES_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: namid

            *Namid*

        .. py:attribute:: naml

            *Naml*

        .. py:attribute:: namf

            *Namf*

        .. py:attribute:: namt

            *Namt*

        .. py:attribute:: nams

            *Nams*

        .. py:attribute:: moniker

            *Moniker*

        .. py:attribute:: moniker_pos

            *Moniker pos*

        .. py:attribute:: namm

            *Namm*

        .. py:attribute:: fullname

            *Fullname*

        .. py:attribute:: naml_search

            *Naml search*



ReceivedFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~
This is undocumented. J M needs to describe this table.

.. py:class:: ReceivedFilingsCd

    **Source data**

        `RECEIVED_FILINGS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: filer_id

            *Filer ID* Filer's unique identification number

        .. py:attribute:: filing_file_name

            *Filing file name*

        .. py:attribute:: received_date

            *Received date*

        .. py:attribute:: filing_directory

            *Filing directory*

        .. py:attribute:: filing_id

            *Filing ID* Unique filing identificiation number

        .. py:attribute:: form_id

            *Form id*

        .. py:attribute:: receive_comment

            *Receive comment*



ReportsCd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: ReportsCd

    **Source data**

        `REPORTS_CD.tsv <https://github.com/california-civic-data-coalition/django-calaccess-raw-data/blob/master/example/test-data/tsv/ACRONYMS_CD.TSV>`_

    **Fields**


        .. py:attribute:: id

            *ID*

        .. py:attribute:: rpt_id

            *Rpt id* Unique identification number

        .. py:attribute:: rpt_name

            *Rpt name* Name of the report

        .. py:attribute:: rpt_desc_field

            *Rpt desc field* Description of the report

        .. py:attribute:: path

            *Path* Reportpath

        .. py:attribute:: data_object

            *Data object*

        .. py:attribute:: parms_flg_y_n

            *Parms flg y n* Parameters indication flag

        .. py:attribute:: rpt_type

            *Rpt type* Type of the report

        .. py:attribute:: parm_definition

            *Parm definition* Parameter definition





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
