Models
======

A crosswalk between the tables published by California's Secretary of State
and the models in this Django application.

Filings
-------

CvrSoCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page for a statement of organization creation or termination
    form filed by a slate-mailer organization or recipient committee.

.. py:class:: CvrSoCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: acct_opendt
        
    
    .. py:attribute:: actvty_lvl
        
            Organization's level of activity
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: bank_adr1
        
    
    .. py:attribute:: bank_adr2
        
    
    .. py:attribute:: bank_city
        
    
    .. py:attribute:: bank_nam
        
    
    .. py:attribute:: bank_phon
        
    
    .. py:attribute:: bank_st
        
    
    .. py:attribute:: bank_zip4
        
    
    .. py:attribute:: brdbase_cb
        
    
    .. py:attribute:: city
        
    
    .. py:attribute:: cmte_email
        
    
    .. py:attribute:: cmte_fax
        
    
    .. py:attribute:: com82013id
        
    
    .. py:attribute:: com82013nm
        
    
    .. py:attribute:: com82013yn
        
    
    .. py:attribute:: control_cb
        
    
    .. py:attribute:: county_act
        
    
    .. py:attribute:: county_res
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filer_namf
        
    
    .. py:attribute:: filer_naml
        
    
    .. py:attribute:: filer_nams
        
    
    .. py:attribute:: filer_namt
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: genpurp_cb
        
    
    .. py:attribute:: gpc_descr
        
    
    .. py:attribute:: mail_city
        
    
    .. py:attribute:: mail_st
        
    
    .. py:attribute:: mail_zip4
        
    
    .. py:attribute:: phone
        
    
    .. py:attribute:: primfc_cb
        
    
    .. py:attribute:: qualfy_dt
        
            Date qualified as an organization
        
    
    .. py:attribute:: qual_cb
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: report_num
        
    
    .. py:attribute:: rpt_date
        
    
    .. py:attribute:: smcont_qualdt
        
    
    .. py:attribute:: sponsor_cb
        
    
    .. py:attribute:: st
        
    
    .. py:attribute:: surplusdsp
        
    
    .. py:attribute:: term_date
        
    
    .. py:attribute:: tres_city
        
    
    .. py:attribute:: tres_namf
        
    
    .. py:attribute:: tres_naml
        
    
    .. py:attribute:: tres_nams
        
    
    .. py:attribute:: tres_namt
        
    
    .. py:attribute:: tres_phon
        
    
    .. py:attribute:: tres_st
        
    
    .. py:attribute:: tres_zip4
        
            Treasurer's ZIP Code
        
    
    .. py:attribute:: zip4
        
    

Cvr2SoCd
~~~~~~~~~~~~~~~~~~~~~~~
Additional names and committees information included on the second page
    of a statement of organization creation form filed
    by a slate-mailer organization or recipient committee.

.. py:class:: Cvr2SoCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: enty_naml
        
    
    .. py:attribute:: enty_namf
        
    
    .. py:attribute:: enty_namt
        
    
    .. py:attribute:: enty_nams
        
    
    .. py:attribute:: item_cd
        
    
    .. py:attribute:: mail_city
        
    
    .. py:attribute:: mail_st
        
    
    .. py:attribute:: mail_zip4
        
    
    .. py:attribute:: day_phone
        
    
    .. py:attribute:: fax_phone
        
    
    .. py:attribute:: email_adr
        
    
    .. py:attribute:: cmte_id
        
    
    .. py:attribute:: ind_group
        
    
    .. py:attribute:: office_cd
        
    
    .. py:attribute:: offic_dscr
        
    
    .. py:attribute:: juris_cd
        
    
    .. py:attribute:: juris_dscr
        
    
    .. py:attribute:: dist_no
        
    
    .. py:attribute:: off_s_h_cd
        
    
    .. py:attribute:: non_pty_cb
        
    
    .. py:attribute:: party_name
        
    
    .. py:attribute:: bal_num
        
    
    .. py:attribute:: bal_juris
        
    
    .. py:attribute:: sup_opp_cd
        
    
    .. py:attribute:: year_elect
        
    
    .. py:attribute:: pof_title
        
    

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
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: amendexp_1
        
    
    .. py:attribute:: amendexp_2
        
    
    .. py:attribute:: amendexp_3
        
    
    .. py:attribute:: assoc_cb
        
    
    .. py:attribute:: assoc_int
        
    
    .. py:attribute:: bal_id
        
    
    .. py:attribute:: bal_juris
        
    
    .. py:attribute:: bal_name
        
    
    .. py:attribute:: bal_num
        
    
    .. py:attribute:: brdbase_yn
        
    
    .. py:attribute:: bus_adr1
        
    
    .. py:attribute:: bus_adr2
        
    
    .. py:attribute:: bus_city
        
    
    .. py:attribute:: bus_inter
        
    
    .. py:attribute:: bus_name
        
    
    .. py:attribute:: bus_st
        
    
    .. py:attribute:: bus_zip4
        
    
    .. py:attribute:: busact_cb
        
    
    .. py:attribute:: busactvity
        
    
    .. py:attribute:: cand_adr1
        
    
    .. py:attribute:: cand_adr2
        
    
    .. py:attribute:: cand_city
        
    
    .. py:attribute:: cand_email
        
    
    .. py:attribute:: cand_fax
        
    
    .. py:attribute:: cand_id
        
    
    .. py:attribute:: cand_namf
        
    
    .. py:attribute:: cand_naml
        
    
    .. py:attribute:: cand_nams
        
    
    .. py:attribute:: cand_namt
        
    
    .. py:attribute:: cand_phon
        
    
    .. py:attribute:: cand_st
        
    
    .. py:attribute:: cand_zip4
        
    
    .. py:attribute:: cmtte_id
        
    
    .. py:attribute:: cmtte_type
        
    
    .. py:attribute:: control_yn
        
    
    .. py:attribute:: dist_no
        
    
    .. py:attribute:: elect_date
        
    
    .. py:attribute:: emplbus_cb
        
    
    .. py:attribute:: employer
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: file_email
        
    
    .. py:attribute:: filer_adr1
        
    
    .. py:attribute:: filer_adr2
        
    
    .. py:attribute:: filer_city
        
    
    .. py:attribute:: filer_fax
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filer_namf
        
    
    .. py:attribute:: filer_naml
        
    
    .. py:attribute:: filer_nams
        
    
    .. py:attribute:: filer_namt
        
    
    .. py:attribute:: filer_phon
        
    
    .. py:attribute:: filer_st
        
    
    .. py:attribute:: filer_zip4
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: from_date
        
    
    .. py:attribute:: juris_cd
        
    
    .. py:attribute:: juris_dscr
        
    
    .. py:attribute:: late_rptno
        
    
    .. py:attribute:: mail_adr1
        
    
    .. py:attribute:: mail_adr2
        
    
    .. py:attribute:: mail_city
        
    
    .. py:attribute:: mail_st
        
    
    .. py:attribute:: mail_zip4
        
    
    .. py:attribute:: occupation
        
    
    .. py:attribute:: off_s_h_cd
        
    
    .. py:attribute:: offic_dscr
        
    
    .. py:attribute:: office_cd
        
    
    .. py:attribute:: other_cb
        
    
    .. py:attribute:: other_int
        
    
    .. py:attribute:: primfrm_yn
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: report_num
        
    
    .. py:attribute:: reportname
        
    
    .. py:attribute:: rpt_att_cb
        
    
    .. py:attribute:: rpt_date
        
    
    .. py:attribute:: rptfromdt
        
    
    .. py:attribute:: rptthrudt
        
    
    .. py:attribute:: selfemp_cb
        
    
    .. py:attribute:: sponsor_yn
        
    
    .. py:attribute:: stmt_type
        
    
    .. py:attribute:: sup_opp_cd
        
    
    .. py:attribute:: thru_date
        
    
    .. py:attribute:: tres_adr1
        
    
    .. py:attribute:: tres_adr2
        
    
    .. py:attribute:: tres_city
        
    
    .. py:attribute:: tres_email
        
    
    .. py:attribute:: tres_fax
        
    
    .. py:attribute:: tres_namf
        
    
    .. py:attribute:: tres_naml
        
    
    .. py:attribute:: tres_nams
        
    
    .. py:attribute:: tres_namt
        
    
    .. py:attribute:: tres_phon
        
    
    .. py:attribute:: tres_st
        
    
    .. py:attribute:: tres_zip4
        
    

Cvr2CampaignDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~
Record used to carry additional names for the campaign
    disclosure forms below.

.. py:class:: Cvr2CampaignDisclosureCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: bal_juris
        
    
    .. py:attribute:: bal_name
        
    
    .. py:attribute:: bal_num
        
    
    .. py:attribute:: cmte_id
        
    
    .. py:attribute:: control_yn
        
    
    .. py:attribute:: dist_no
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: enty_adr1
        
    
    .. py:attribute:: enty_adr2
        
    
    .. py:attribute:: enty_city
        
    
    .. py:attribute:: enty_email
        
    
    .. py:attribute:: enty_fax
        
    
    .. py:attribute:: enty_namf
        
    
    .. py:attribute:: enty_naml
        
    
    .. py:attribute:: enty_nams
        
    
    .. py:attribute:: enty_namt
        
    
    .. py:attribute:: enty_phon
        
    
    .. py:attribute:: enty_st
        
    
    .. py:attribute:: enty_zip4
        
    
    .. py:attribute:: f460_part
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: juris_cd
        
    
    .. py:attribute:: juris_dscr
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: mail_adr1
        
    
    .. py:attribute:: mail_adr2
        
    
    .. py:attribute:: mail_city
        
    
    .. py:attribute:: mail_st
        
    
    .. py:attribute:: mail_zip4
        
    
    .. py:attribute:: off_s_h_cd
        
    
    .. py:attribute:: offic_dscr
        
    
    .. py:attribute:: office_cd
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: sup_opp_cd
        
    
    .. py:attribute:: title
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: tres_namf
        
    
    .. py:attribute:: tres_naml
        
    
    .. py:attribute:: tres_nams
        
    
    .. py:attribute:: tres_namt
        
    

RcptCd
~~~~~~~~~~~~~~~~~~~~~~~
Receipts schedules for the following forms.

        Form 460 (Recipient Committee Campaign Statement)
        Schedules A, C, I, and A-1.

        Form 401 (Slate Mailer Organization Campaign Statement) Schedule A.

.. py:class:: RcptCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: amount
        
            Amount Received (Monetary, Inkkind, Promise)
        
    
    .. py:attribute:: bakref_tid
        
            Back Reference to a transaction identifier of a parent record
        
    
    .. py:attribute:: bal_juris
        
            Jurisdiction of ballot measure. Used on the Form 401 Schedule A
        
    
    .. py:attribute:: bal_name
        
            Ballot measure name. Used on the Form 401 Schedule A
        
    
    .. py:attribute:: bal_num
        
            Ballot measure number or letter. Used on the Form 401 Schedule A
        
    
    .. py:attribute:: cand_namf
        
            Candidate/officeholder's first name. Used on the Form 401 Schedule A
        
    
    .. py:attribute:: cand_naml
        
            Candidate/officeholder's last name. Used on the Form 401 Schedule A
        
    
    .. py:attribute:: cand_nams
        
            Candidate/officeholder's name suffix. Used on the Form 401 Schedule A
        
    
    .. py:attribute:: cand_namt
        
            Candidate/officeholder's name prefix or title. Used on the Form 401 Schedule A
        
    
    .. py:attribute:: cmte_id
        
            Committee Identification number
        
    
    .. py:attribute:: ctrib_adr1
        
            First line of the contributor's street address
        
    
    .. py:attribute:: ctrib_adr2
        
            Second line of the contributor's street address
        
    
    .. py:attribute:: ctrib_city
        
            Contributor's City
        
    
    .. py:attribute:: ctrib_dscr
        
            Description of goods/services received
        
    
    .. py:attribute:: ctrib_emp
        
            Employer
        
    
    .. py:attribute:: ctrib_namf
        
            Contributor's First Name
        
    
    .. py:attribute:: ctrib_naml
        
            Contributor's last name or business name
        
    
    .. py:attribute:: ctrib_nams
        
            Contributor's Suffix
        
    
    .. py:attribute:: ctrib_namt
        
            Contributor's Prefix or Title
        
    
    .. py:attribute:: ctrib_occ
        
            Occupation
        
    
    .. py:attribute:: ctrib_self
        
            Self Employed Check-box
        
    
    .. py:attribute:: ctrib_st
        
            Contributor's State
        
    
    .. py:attribute:: ctrib_zip4
        
            Contributor's ZIP+4
        
    
    .. py:attribute:: cum_oth
        
            Cumulative Other (Sched A, A-1)
        
    
    .. py:attribute:: cum_ytd
        
            Cumulative year to date amount (Form 460 Schedule A and Form 401 Schedule A, A-1)
        
    
    .. py:attribute:: date_thru
        
            End of date range for items received
        
    
    .. py:attribute:: dist_no
        
            Office District Number (used on F401A)
        
    
    .. py:attribute:: entity_cd
        
            Entity code: Values [CMO|RCP|IND|OTH]
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: int_rate
        
    
    .. py:attribute:: intr_adr1
        
            First line of the intermediary's street address.
        
    
    .. py:attribute:: intr_adr2
        
            Second line of the Intermediary's street address.
        
    
    .. py:attribute:: intr_city
        
            Intermediary's City
        
    
    .. py:attribute:: intr_cmteid
        
    
    .. py:attribute:: intr_emp
        
            Intermediary's Employer
        
    
    .. py:attribute:: intr_namf
        
            Intermediary's First Name
        
    
    .. py:attribute:: intr_naml
        
            Intermediary's Last Name
        
    
    .. py:attribute:: intr_nams
        
            Intermediary's Suffix
        
    
    .. py:attribute:: intr_namt
        
            Intermediary's Prefix or Title
        
    
    .. py:attribute:: intr_occ
        
            Intermediary's Occupation
        
    
    .. py:attribute:: intr_self
        
            Intermediary's self employed check box
        
    
    .. py:attribute:: intr_st
        
            Intermediary's state
        
    
    .. py:attribute:: intr_zip4
        
            Intermediary's zip code
        
    
    .. py:attribute:: juris_cd
        
            Office jurisdiction code. See the CAL document for the list of legal values. Used on Form 401 Schedule A
        
    
    .. py:attribute:: juris_dscr
        
            Office Jurisdiction Description (used on F401A)
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: memo_code
        
            Memo amount flag (Date/Amount are informational only)
        
    
    .. py:attribute:: memo_refno
        
            Reference to text contained in a TEXT record
        
    
    .. py:attribute:: off_s_h_cd
        
            Office Sought/Held Code. Used on the Form 401 Schedule A. Legal values are 'S' for sought and 'H' for held
        
    
    .. py:attribute:: offic_dscr
        
            Office Sought Description (used on F401A)
        
    
    .. py:attribute:: office_cd
        
            Code that identifies the office being sought. See the CAL document for a list of valid codes. Used on the Form 401 Schedule A)
        
    
    .. py:attribute:: rcpt_date
        
            Date item received
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: sup_opp_cd
        
            Support/oppose code. Legal values are 'S' for support or 'O' for oppose. Used on Form 401 Sechedule A. Transaction identifier - permanent value unique to this item
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: tran_type
        
            Transaction Type: Values T- third party | F Forgiven loan | R Returned (Negative amount)
        
    
    .. py:attribute:: tres_adr1
        
            First line of the treasurer or responsible officer's street address
        
    
    .. py:attribute:: tres_adr2
        
            Second line of the treasurer or responsible officer's street address
        
    
    .. py:attribute:: tres_city
        
            City portion of the treasurer or responsible officer's street address
        
    
    .. py:attribute:: tres_namf
        
            Treasurer or responsible officer's first name
        
    
    .. py:attribute:: tres_naml
        
            Treasurer or responsible officer's last name
        
    
    .. py:attribute:: tres_nams
        
            Treasurer or responsible officer's suffix
        
    
    .. py:attribute:: tres_namt
        
            Treasurer or responsible officer's prefix or title
        
    
    .. py:attribute:: tres_st
        
            State portion of the treasurer or responsible officer's address
        
    
    .. py:attribute:: tres_zip4
        
            Zip code portion of the treasurer or responsible officer's address
        
    
    .. py:attribute:: xref_match
        
            Related item on other schedule has same transaction identifier. 'X' indicates this condition is true
        
    
    .. py:attribute:: xref_schnm
        
            Related record is included on Sched 'B2' or 'F'
        
    

Cvr3VerificationInfoCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page verification information from campaign disclosure forms

.. py:class:: Cvr3VerificationInfoCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: sig_date
        
            date when signed
        
    
    .. py:attribute:: sig_loc
        
            city and state where signed
        
    
    .. py:attribute:: sig_naml
        
            last name of the signer
        
    
    .. py:attribute:: sig_namf
        
            first name of the signer
        
    
    .. py:attribute:: sig_namt
        
            title of the signer
        
    
    .. py:attribute:: sig_nams
        
            suffix of the signer
        
    

LoanCd
~~~~~~~~~~~~~~~~~~~~~~~
Loans received and made.

.. py:class:: LoanCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: bakref_tid
        
    
    .. py:attribute:: cmte_id
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: intr_adr1
        
    
    .. py:attribute:: intr_adr2
        
    
    .. py:attribute:: intr_city
        
    
    .. py:attribute:: intr_namf
        
    
    .. py:attribute:: intr_naml
        
    
    .. py:attribute:: intr_nams
        
    
    .. py:attribute:: intr_namt
        
    
    .. py:attribute:: intr_st
        
    
    .. py:attribute:: intr_zip4
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: lndr_namf
        
    
    .. py:attribute:: lndr_naml
        
    
    .. py:attribute:: lndr_nams
        
    
    .. py:attribute:: lndr_namt
        
    
    .. py:attribute:: loan_adr1
        
    
    .. py:attribute:: loan_adr2
        
    
    .. py:attribute:: loan_amt1
        
    
    .. py:attribute:: loan_amt2
        
    
    .. py:attribute:: loan_amt3
        
    
    .. py:attribute:: loan_amt4
        
    
    .. py:attribute:: loan_amt5
        
    
    .. py:attribute:: loan_amt6
        
    
    .. py:attribute:: loan_amt7
        
    
    .. py:attribute:: loan_amt8
        
    
    .. py:attribute:: loan_city
        
    
    .. py:attribute:: loan_date1
        
    
    .. py:attribute:: loan_date2
        
    
    .. py:attribute:: loan_emp
        
    
    .. py:attribute:: loan_occ
        
    
    .. py:attribute:: loan_rate
        
    
    .. py:attribute:: loan_self
        
    
    .. py:attribute:: loan_st
        
    
    .. py:attribute:: loan_type
        
    
    .. py:attribute:: loan_zip4
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: tres_adr1
        
    
    .. py:attribute:: tres_adr2
        
    
    .. py:attribute:: tres_city
        
    
    .. py:attribute:: tres_namf
        
    
    .. py:attribute:: tres_naml
        
    
    .. py:attribute:: tres_nams
        
    
    .. py:attribute:: tres_namt
        
    
    .. py:attribute:: tres_st
        
    
    .. py:attribute:: tres_zip4
        
    
    .. py:attribute:: xref_match
        
    
    .. py:attribute:: xref_schnm
        
    

S401Cd
~~~~~~~~~~~~~~~~~~~~~~~
This table contains Form 401 (Slate Mailer Organization) payment and other
    disclosure schedule (F401B, F401B-1, F401C, F401D) information.

.. py:class:: S401Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: agent_naml
        
    
    .. py:attribute:: agent_namf
        
    
    .. py:attribute:: agent_namt
        
    
    .. py:attribute:: agent_nams
        
    
    .. py:attribute:: payee_naml
        
    
    .. py:attribute:: payee_namf
        
    
    .. py:attribute:: payee_namt
        
    
    .. py:attribute:: payee_nams
        
    
    .. py:attribute:: payee_city
        
    
    .. py:attribute:: payee_st
        
    
    .. py:attribute:: payee_zip4
        
    
    .. py:attribute:: amount
        
    
    .. py:attribute:: aggregate
        
    
    .. py:attribute:: expn_dscr
        
    
    .. py:attribute:: cand_naml
        
    
    .. py:attribute:: cand_namf
        
    
    .. py:attribute:: cand_namt
        
    
    .. py:attribute:: cand_nams
        
    
    .. py:attribute:: office_cd
        
    
    .. py:attribute:: offic_dscr
        
    
    .. py:attribute:: juris_cd
        
    
    .. py:attribute:: juris_dscr
        
    
    .. py:attribute:: dist_no
        
    
    .. py:attribute:: off_s_h_cd
        
    
    .. py:attribute:: bal_name
        
    
    .. py:attribute:: bal_num
        
    
    .. py:attribute:: bal_juris
        
    
    .. py:attribute:: sup_opp_cd
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: bakref_tid
        
    

ExpnCd
~~~~~~~~~~~~~~~~~~~~~~~
Campaign expenditures from a variety of forms

.. py:class:: ExpnCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: agent_namf
        
            Agent of Ind. Contractor's First name
        
    
    .. py:attribute:: agent_naml
        
            Agent of Ind. Contractor's Last name (Sched G)
        
    
    .. py:attribute:: agent_nams
        
            Agent of Ind. Contractor's Suffix
        
    
    .. py:attribute:: agent_namt
        
            Agent of Ind. Contractor's Prefix or Title
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: amount
        
            Amount of Payment
        
    
    .. py:attribute:: bakref_tid
        
            Back Reference to a Tran_ID of a 'parent' record
        
    
    .. py:attribute:: bal_juris
        
            Jurisdiction
        
    
    .. py:attribute:: bal_name
        
            Ballot Measure Name
        
    
    .. py:attribute:: bal_num
        
            Ballot Number or Letter
        
    
    .. py:attribute:: cand_namf
        
            Candidate's First name
        
    
    .. py:attribute:: cand_naml
        
            Candidate's Last name
        
    
    .. py:attribute:: cand_nams
        
            Candidate's Suffix
        
    
    .. py:attribute:: cand_namt
        
            Candidate's Prefix or Title
        
    
    .. py:attribute:: cmte_id
        
            Committee ID (If [COM|RCP] & no ID#, Treas info Req.)
        
    
    .. py:attribute:: cum_oth
        
            Cumulative / 'Other' (No Cumulative on Sched E & G)
        
    
    .. py:attribute:: cum_ytd
        
            Cumulative / Year-to-date amount         (No Cumulative on Sched E & G)
        
    
    .. py:attribute:: dist_no
        
            Office District Number (Req. if Juris_Cd=[SEN|ASM|BOE]
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: expn_chkno
        
            Check Number (Optional)
        
    
    .. py:attribute:: expn_code
        
            Expense Code - Values: (Refer to list in Overview)         Note: CTB & IND need explanation & listing on Sched D         TRC & TRS require explanation.
        
    
    .. py:attribute:: expn_date
        
            Date of Expenditure (Note: Date not on Sched E & G)
        
    
    .. py:attribute:: expn_dscr
        
            Purpose of Expense and/or Description/explanation
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: g_from_e_f
        
            Back Reference from Sched G to Sched 'E' or 'F'?
        
    
    .. py:attribute:: juris_cd
        
            Office Jurisdiction Code Values: STW=Statewide;         SEN=Senate District; ASM=Assembly District;         BOE=Board of Equalization District;         CIT=City; CTY=County; LOC=Local; OTH=Other
        
    
    .. py:attribute:: juris_dscr
        
            Office Jurisdiction Description         (Req. if Juris_Cd=[CIT|CTY|LOC|OTH]
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: memo_code
        
            Memo Amount? (Date/Amount are informational only)
        
    
    .. py:attribute:: memo_refno
        
            Reference to text contained in a TEXT record.
        
    
    .. py:attribute:: off_s_h_cd
        
            Office Sought/Held Code: H=Held; S=Sought
        
    
    .. py:attribute:: offic_dscr
        
            Office Sought Description (Req. if Office_Cd=OTH)
        
    
    .. py:attribute:: office_cd
        
            Office Sought (See table of code in Overview)
        
    
    .. py:attribute:: payee_adr1
        
            Address of Payee
        
    
    .. py:attribute:: payee_adr2
        
            Optional 2nd line of Address
        
    
    .. py:attribute:: payee_city
        
            Payee City
        
    
    .. py:attribute:: payee_namf
        
            Payee's First name
        
    
    .. py:attribute:: payee_naml
        
            Payee's Last name
        
    
    .. py:attribute:: payee_nams
        
            Payee's Suffix
        
    
    .. py:attribute:: payee_namt
        
            Payee's Prefix or Title
        
    
    .. py:attribute:: payee_st
        
            State code
        
    
    .. py:attribute:: payee_zip4
        
            Zip+4
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: sup_opp_cd
        
            Support/Oppose? Values: S; O (F450, F461)
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: tres_adr1
        
            Treasurer Street 1(Req if [COM|RCP] & no ID#)
        
    
    .. py:attribute:: tres_adr2
        
            Treasurer Street 2
        
    
    .. py:attribute:: tres_city
        
            Treasurer City
        
    
    .. py:attribute:: tres_namf
        
            Treasurer's First name (Req if [COM|RCP] & no ID#)
        
    
    .. py:attribute:: tres_naml
        
            Treasurer's Last name (Req if [COM|RCP] & no ID#)
        
    
    .. py:attribute:: tres_nams
        
            Treasurer's Suffix
        
    
    .. py:attribute:: tres_namt
        
            Treasurer's Prefix or Title
        
    
    .. py:attribute:: tres_st
        
            Treasurer State
        
    
    .. py:attribute:: tres_zip4
        
            Treasurer ZIP+4
        
    
    .. py:attribute:: xref_match
        
            X = Related item on other Sched has same Tran_ID
        
    
    .. py:attribute:: xref_schnm
        
            Related item is included on Sched 'C' or 'H2'
        
    

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
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: elect_date
        
    
    .. py:attribute:: electjuris
        
    
    .. py:attribute:: contribamt
        
    

DebtCd
~~~~~~~~~~~~~~~~~~~~~~~
Form 460 (Recipient Committee Campaign Statement)
    Schedule (F) Accrued Expenses (Unpaid Bills) records

.. py:class:: DebtCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: amt_incur
        
    
    .. py:attribute:: amt_paid
        
    
    .. py:attribute:: bakref_tid
        
    
    .. py:attribute:: beg_bal
        
    
    .. py:attribute:: cmte_id
        
    
    .. py:attribute:: end_bal
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: expn_code
        
    
    .. py:attribute:: expn_dscr
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: payee_adr1
        
    
    .. py:attribute:: payee_adr2
        
    
    .. py:attribute:: payee_city
        
    
    .. py:attribute:: payee_namf
        
    
    .. py:attribute:: payee_naml
        
    
    .. py:attribute:: payee_nams
        
    
    .. py:attribute:: payee_namt
        
    
    .. py:attribute:: payee_st
        
    
    .. py:attribute:: payee_zip4
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: tres_adr1
        
    
    .. py:attribute:: tres_adr2
        
    
    .. py:attribute:: tres_city
        
    
    .. py:attribute:: tres_namf
        
    
    .. py:attribute:: tres_naml
        
    
    .. py:attribute:: tres_nams
        
    
    .. py:attribute:: tres_namt
        
    
    .. py:attribute:: tres_st
        
    
    .. py:attribute:: tres_zip4
        
    
    .. py:attribute:: xref_match
        
    
    .. py:attribute:: xref_schnm
        
    

S496Cd
~~~~~~~~~~~~~~~~~~~~~~~
Form 496 Late Independent Expenditures

.. py:class:: S496Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: amount
        
    
    .. py:attribute:: exp_date
        
    
    .. py:attribute:: expn_dscr
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: date_thru
        
    

SpltCd
~~~~~~~~~~~~~~~~~~~~~~~
Split Records

        -- F450P5
        -- F460 (A-B1-B2-C-D-H)

.. py:class:: SpltCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: elec_amount
        
    
    .. py:attribute:: elec_code
        
    
    .. py:attribute:: elec_date
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: pform_type
        
    
    .. py:attribute:: ptran_id
        
            Permanent value unique to this item
        
    

S497Cd
~~~~~~~~~~~~~~~~~~~~~~~
Form 497 Late Contributions Received/Made

.. py:class:: S497Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: enty_naml
        
    
    .. py:attribute:: enty_namf
        
    
    .. py:attribute:: enty_namt
        
    
    .. py:attribute:: enty_nams
        
    
    .. py:attribute:: enty_city
        
    
    .. py:attribute:: enty_st
        
    
    .. py:attribute:: enty_zip4
        
    
    .. py:attribute:: ctrib_emp
        
    
    .. py:attribute:: ctrib_occ
        
    
    .. py:attribute:: ctrib_self
        
    
    .. py:attribute:: elec_date
        
    
    .. py:attribute:: ctrib_date
        
    
    .. py:attribute:: date_thru
        
    
    .. py:attribute:: amount
        
    
    .. py:attribute:: cmte_id
        
    
    .. py:attribute:: cand_naml
        
    
    .. py:attribute:: cand_namf
        
    
    .. py:attribute:: cand_namt
        
    
    .. py:attribute:: cand_nams
        
    
    .. py:attribute:: office_cd
        
    
    .. py:attribute:: offic_dscr
        
    
    .. py:attribute:: juris_cd
        
    
    .. py:attribute:: juris_dscr
        
    
    .. py:attribute:: dist_no
        
    
    .. py:attribute:: off_s_h_cd
        
    
    .. py:attribute:: bal_name
        
    
    .. py:attribute:: bal_num
        
    
    .. py:attribute:: bal_juris
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: bal_id
        
    
    .. py:attribute:: cand_id
        
    
    .. py:attribute:: sup_off_cd
        
    
    .. py:attribute:: sup_opp_cd
        
    

F501502Cd
~~~~~~~~~~~~~~~~~~~~~~~
Candidate Intention Statement

        -- F501
        -- F502

.. py:class:: F501502Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: committee_id
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: report_num
        
    
    .. py:attribute:: rpt_date
        
    
    .. py:attribute:: stmt_type
        
    
    .. py:attribute:: from_date
        
    
    .. py:attribute:: thru_date
        
    
    .. py:attribute:: elect_date
        
    
    .. py:attribute:: cand_naml
        
    
    .. py:attribute:: cand_namf
        
    
    .. py:attribute:: can_namm
        
    
    .. py:attribute:: cand_namt
        
    
    .. py:attribute:: cand_nams
        
    
    .. py:attribute:: moniker_pos
        
    
    .. py:attribute:: moniker
        
    
    .. py:attribute:: cand_city
        
    
    .. py:attribute:: cand_st
        
    
    .. py:attribute:: cand_zip4
        
    
    .. py:attribute:: cand_phon
        
    
    .. py:attribute:: cand_fax
        
    
    .. py:attribute:: cand_email
        
    
    .. py:attribute:: fin_naml
        
    
    .. py:attribute:: fin_namf
        
    
    .. py:attribute:: fin_namt
        
    
    .. py:attribute:: fin_nams
        
    
    .. py:attribute:: fin_city
        
    
    .. py:attribute:: fin_st
        
    
    .. py:attribute:: fin_zip4
        
    
    .. py:attribute:: fin_phon
        
    
    .. py:attribute:: fin_fax
        
    
    .. py:attribute:: fin_email
        
    
    .. py:attribute:: office_cd
        
    
    .. py:attribute:: offic_dscr
        
    
    .. py:attribute:: agency_nam
        
    
    .. py:attribute:: juris_cd
        
    
    .. py:attribute:: juris_dscr
        
    
    .. py:attribute:: dist_no
        
    
    .. py:attribute:: party
        
    
    .. py:attribute:: yr_of_elec
        
    
    .. py:attribute:: elec_type
        
    
    .. py:attribute:: execute_dt
        
    
    .. py:attribute:: can_sig
        
    
    .. py:attribute:: account_no
        
    
    .. py:attribute:: acct_op_dt
        
    
    .. py:attribute:: party_cd
        
    
    .. py:attribute:: district_cd
        
    
    .. py:attribute:: accept_limit_yn
        
    
    .. py:attribute:: did_exceed_dt
        
    
    .. py:attribute:: cntrb_prsnl_fnds_dt
        
    

S498Cd
~~~~~~~~~~~~~~~~~~~~~~~
Form 498 Slate Mailer Late Independent Expenditures Made

.. py:class:: S498Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: cmte_id
        
    
    .. py:attribute:: payor_naml
        
    
    .. py:attribute:: payor_namf
        
    
    .. py:attribute:: payor_namt
        
    
    .. py:attribute:: payor_nams
        
    
    .. py:attribute:: payor_city
        
    
    .. py:attribute:: payor_st
        
    
    .. py:attribute:: payor_zip4
        
    
    .. py:attribute:: date_rcvd
        
    
    .. py:attribute:: amt_rcvd
        
    
    .. py:attribute:: cand_naml
        
    
    .. py:attribute:: cand_namf
        
    
    .. py:attribute:: cand_namt
        
    
    .. py:attribute:: cand_nams
        
    
    .. py:attribute:: office_cd
        
    
    .. py:attribute:: offic_dscr
        
    
    .. py:attribute:: juris_cd
        
    
    .. py:attribute:: juris_dscr
        
    
    .. py:attribute:: dist_no
        
    
    .. py:attribute:: off_s_h_cd
        
    
    .. py:attribute:: bal_name
        
    
    .. py:attribute:: bal_num
        
    
    .. py:attribute:: bal_juris
        
    
    .. py:attribute:: sup_opp_cd
        
    
    .. py:attribute:: amt_attrib
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: employer
        
    
    .. py:attribute:: occupation
        
    
    .. py:attribute:: selfemp_cb
        
    

CvrRegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page of lobbying disclosure forms

.. py:class:: CvrRegistrationCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: a_b_adr1
        
    
    .. py:attribute:: a_b_adr2
        
    
    .. py:attribute:: a_b_city
        
    
    .. py:attribute:: a_b_name
        
    
    .. py:attribute:: a_b_st
        
    
    .. py:attribute:: a_b_zip4
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: auth_adr1
        
    
    .. py:attribute:: auth_adr2
        
    
    .. py:attribute:: auth_city
        
    
    .. py:attribute:: auth_name
        
    
    .. py:attribute:: auth_st
        
    
    .. py:attribute:: auth_zip4
        
    
    .. py:attribute:: bus_adr1
        
    
    .. py:attribute:: bus_adr2
        
    
    .. py:attribute:: bus_cb
        
    
    .. py:attribute:: bus_city
        
    
    .. py:attribute:: bus_class
        
    
    .. py:attribute:: bus_descr
        
    
    .. py:attribute:: bus_email
        
    
    .. py:attribute:: bus_fax
        
    
    .. py:attribute:: bus_phon
        
    
    .. py:attribute:: bus_st
        
    
    .. py:attribute:: bus_zip4
        
    
    .. py:attribute:: c_less50
        
    
    .. py:attribute:: c_more50
        
    
    .. py:attribute:: complet_dt
        
    
    .. py:attribute:: descrip_1
        
    
    .. py:attribute:: descrip_2
        
    
    .. py:attribute:: eff_date
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filer_namf
        
    
    .. py:attribute:: filer_naml
        
    
    .. py:attribute:: filer_nams
        
    
    .. py:attribute:: filer_namt
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: ind_cb
        
    
    .. py:attribute:: ind_class
        
    
    .. py:attribute:: ind_descr
        
    
    .. py:attribute:: influen_yn
        
    
    .. py:attribute:: l_firm_cb
        
    
    .. py:attribute:: lby_604_cb
        
    
    .. py:attribute:: lby_reg_cb
        
    
    .. py:attribute:: lobby_cb
        
    
    .. py:attribute:: lobby_int
        
    
    .. py:attribute:: ls_beg_yr
        
    
    .. py:attribute:: ls_end_yr
        
    
    .. py:attribute:: mail_adr1
        
    
    .. py:attribute:: mail_adr2
        
    
    .. py:attribute:: mail_city
        
    
    .. py:attribute:: mail_phon
        
    
    .. py:attribute:: mail_st
        
    
    .. py:attribute:: mail_zip4
        
    
    .. py:attribute:: newcert_cb
        
    
    .. py:attribute:: oth_cb
        
    
    .. py:attribute:: prn_namf
        
    
    .. py:attribute:: prn_naml
        
    
    .. py:attribute:: prn_nams
        
    
    .. py:attribute:: prn_namt
        
    
    .. py:attribute:: qual_date
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: rencert_cb
        
    
    .. py:attribute:: report_num
        
    
    .. py:attribute:: rpt_date
        
    
    .. py:attribute:: sender_id
        
    
    .. py:attribute:: sig_date
        
    
    .. py:attribute:: sig_loc
        
    
    .. py:attribute:: sig_namf
        
    
    .. py:attribute:: sig_naml
        
    
    .. py:attribute:: sig_nams
        
    
    .. py:attribute:: sig_namt
        
    
    .. py:attribute:: sig_title
        
    
    .. py:attribute:: st_agency
        
    
    .. py:attribute:: st_leg_yn
        
    
    .. py:attribute:: stmt_firm
        
    
    .. py:attribute:: trade_cb
        
    

Cvr2RegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page of lobbying dislcosure forms

.. py:class:: Cvr2RegistrationCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: entity_id
        
            Identification number of the entity described by the record
        
    
    .. py:attribute:: enty_naml
        
    
    .. py:attribute:: enty_namf
        
    
    .. py:attribute:: enty_namt
        
    
    .. py:attribute:: enty_nams
        
    

CvrLobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~
Cover page information for the lobbying disclosure forms

        F615 -- Lobbyist Report
        F625 -- Report of Lobbying Firm
        F635 -- Report of Lobbyist Employer and Report of Lobbying Coalition
        F645 -- Report of Person Spending $5,000 or more to influence
                Legislative or administrative action

.. py:class:: CvrLobbyDisclosureCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: ctrib_n_cb
        
    
    .. py:attribute:: ctrib_y_cb
        
    
    .. py:attribute:: cum_beg_dt
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filer_namf
        
    
    .. py:attribute:: filer_naml
        
    
    .. py:attribute:: filer_nams
        
    
    .. py:attribute:: filer_namt
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: firm_adr1
        
    
    .. py:attribute:: firm_adr2
        
    
    .. py:attribute:: firm_city
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: firm_phon
        
    
    .. py:attribute:: firm_st
        
    
    .. py:attribute:: firm_zip4
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: from_date
        
    
    .. py:attribute:: lby_actvty
        
    
    .. py:attribute:: lobby_n_cb
        
    
    .. py:attribute:: lobby_y_cb
        
    
    .. py:attribute:: mail_adr1
        
    
    .. py:attribute:: mail_adr2
        
    
    .. py:attribute:: mail_city
        
    
    .. py:attribute:: mail_phon
        
    
    .. py:attribute:: mail_st
        
    
    .. py:attribute:: mail_zip4
        
    
    .. py:attribute:: major_namf
        
    
    .. py:attribute:: major_naml
        
    
    .. py:attribute:: major_nams
        
    
    .. py:attribute:: major_namt
        
    
    .. py:attribute:: nopart1_cb
        
    
    .. py:attribute:: nopart2_cb
        
    
    .. py:attribute:: part1_1_cb
        
    
    .. py:attribute:: part1_2_cb
        
    
    .. py:attribute:: prn_namf
        
    
    .. py:attribute:: prn_naml
        
    
    .. py:attribute:: prn_nams
        
    
    .. py:attribute:: prn_namt
        
    
    .. py:attribute:: rcpcmte_id
        
    
    .. py:attribute:: rcpcmte_nm
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: report_num
        
    
    .. py:attribute:: rpt_date
        
    
    .. py:attribute:: sender_id
        
    
    .. py:attribute:: sig_date
        
    
    .. py:attribute:: sig_loc
        
    
    .. py:attribute:: sig_namf
        
    
    .. py:attribute:: sig_naml
        
    
    .. py:attribute:: sig_nams
        
    
    .. py:attribute:: sig_namt
        
    
    .. py:attribute:: sig_title
        
    
    .. py:attribute:: thru_date
        
    

Cvr2LobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~
Additional names data for the lobbyist disclosure forms

        F615 -- Lobbyist Report
        F625 -- Report of Lobbying Firm
        F635 -- Report of Lobbyist Employer and Report of Lobbying Coalition
        F645 -- Report of Person Spending $5,000 or more to influence
                Legislative or administrative action

.. py:class:: Cvr2LobbyDisclosureCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: entity_id
        
    
    .. py:attribute:: enty_namf
        
    
    .. py:attribute:: enty_naml
        
    
    .. py:attribute:: enty_nams
        
    
    .. py:attribute:: enty_namt
        
    
    .. py:attribute:: enty_title
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    

LobbyAmendmentsCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist registration amendment information

        Form 605 Part I

.. py:class:: LobbyAmendmentsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: exec_date
        
    
    .. py:attribute:: from_date
        
    
    .. py:attribute:: thru_date
        
    
    .. py:attribute:: add_l_cb
        
    
    .. py:attribute:: add_l_eff
        
    
    .. py:attribute:: a_l_naml
        
    
    .. py:attribute:: a_l_namf
        
    
    .. py:attribute:: a_l_namt
        
    
    .. py:attribute:: a_l_nams
        
    
    .. py:attribute:: del_l_cb
        
    
    .. py:attribute:: del_l_eff
        
    
    .. py:attribute:: d_l_naml
        
    
    .. py:attribute:: d_l_namf
        
    
    .. py:attribute:: d_l_namt
        
    
    .. py:attribute:: d_l_nams
        
    
    .. py:attribute:: add_le_cb
        
    
    .. py:attribute:: add_le_eff
        
    
    .. py:attribute:: a_le_naml
        
    
    .. py:attribute:: a_le_namf
        
    
    .. py:attribute:: a_le_namt
        
    
    .. py:attribute:: a_le_nams
        
    
    .. py:attribute:: del_le_cb
        
    
    .. py:attribute:: del_le_eff
        
    
    .. py:attribute:: d_le_naml
        
    
    .. py:attribute:: d_le_namf
        
    
    .. py:attribute:: d_le_namt
        
    
    .. py:attribute:: d_le_nams
        
    
    .. py:attribute:: add_lf_cb
        
    
    .. py:attribute:: add_lf_eff
        
    
    .. py:attribute:: a_lf_name
        
    
    .. py:attribute:: del_lf_cb
        
    
    .. py:attribute:: del_lf_eff
        
    
    .. py:attribute:: d_lf_name
        
    
    .. py:attribute:: other_cb
        
    
    .. py:attribute:: other_eff
        
    
    .. py:attribute:: other_desc
        
    
    .. py:attribute:: f606_yes
        
    
    .. py:attribute:: f606_no
        
    

F690P2Cd
~~~~~~~~~~~~~~~~~~~~~~~
Amends lobbying disclosure filings

        F690 Amendment to Lobbying Disclosure Report

.. py:class:: F690P2Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: exec_date
        
            date the original report (or prior amendment to the original report) was executed on.
        
    
    .. py:attribute:: from_date
        
            reporting period from date of original report
        
    
    .. py:attribute:: thru_date
        
            report period to/through date of original.
        
    
    .. py:attribute:: chg_parts
        
            amended into affects items on part(s) text description.
        
    
    .. py:attribute:: chg_sects
        
            amended into affects items on sections(s) text description.
        
    
    .. py:attribute:: amend_txt1
        
            description of changes to the filing
        
    

LattCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist disclosure attachment schedules for payments
        F630 -- Payments made to Lobbying Coalitions (Attatchment)
        F635C -- Payments received by Lobbying Coalitions (Attatchment)
        F640 -- Government Agencies Reporting of &quot;Other Payments to Influence
                Legislative or Administrative Action&quot; (Attatchment)

.. py:class:: LattCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: amount
        
    
    .. py:attribute:: cum_amt
        
    
    .. py:attribute:: cumbeg_dt
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: pmt_date
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: recip_adr1
        
    
    .. py:attribute:: recip_adr2
        
    
    .. py:attribute:: recip_city
        
    
    .. py:attribute:: recip_namf
        
    
    .. py:attribute:: recip_naml
        
    
    .. py:attribute:: recip_nams
        
    
    .. py:attribute:: recip_namt
        
    
    .. py:attribute:: recip_st
        
    
    .. py:attribute:: recip_zip4
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    

LexpCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbying Activity Expenditure Schedule information (Gifts)
    Reported in filings of the forms

        F615 Part 1
        F625 Part 3A
        F635 Part 3C
        F645 Part 2A

.. py:class:: LexpCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: amount
        
    
    .. py:attribute:: bakref_tid
        
    
    .. py:attribute:: bene_amt
        
    
    .. py:attribute:: bene_name
        
    
    .. py:attribute:: bene_posit
        
    
    .. py:attribute:: credcardco
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: expn_date
        
    
    .. py:attribute:: expn_dscr
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: payee_adr1
        
    
    .. py:attribute:: payee_adr2
        
    
    .. py:attribute:: payee_city
        
    
    .. py:attribute:: payee_namf
        
    
    .. py:attribute:: payee_naml
        
    
    .. py:attribute:: payee_nams
        
    
    .. py:attribute:: payee_namt
        
    
    .. py:attribute:: payee_st
        
    
    .. py:attribute:: payee_zip4
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: recsubtype
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    

LccmCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbying Campaign Contributions reported on forms

        F615 Part 2
        F625 Part 4B
        F635 Part 4B
        F645 Part 3B

.. py:class:: LccmCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: acct_name
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: amount
        
    
    .. py:attribute:: bakref_tid
        
    
    .. py:attribute:: ctrib_date
        
    
    .. py:attribute:: ctrib_namf
        
    
    .. py:attribute:: ctrib_naml
        
    
    .. py:attribute:: ctrib_nams
        
    
    .. py:attribute:: ctrib_namt
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: recip_adr1
        
    
    .. py:attribute:: recip_adr2
        
    
    .. py:attribute:: recip_city
        
    
    .. py:attribute:: recip_id
        
    
    .. py:attribute:: recip_namf
        
    
    .. py:attribute:: recip_naml
        
    
    .. py:attribute:: recip_nams
        
    
    .. py:attribute:: recip_namt
        
    
    .. py:attribute:: recip_st
        
    
    .. py:attribute:: recip_zip4
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    

LothCd
~~~~~~~~~~~~~~~~~~~~~~~
Payment to other lobbying firms reported on form

        F625 Part 3B

.. py:class:: LothCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: amount
        
    
    .. py:attribute:: cum_amt
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: firm_adr1
        
    
    .. py:attribute:: firm_adr2
        
    
    .. py:attribute:: firm_city
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: firm_phon
        
    
    .. py:attribute:: firm_st
        
    
    .. py:attribute:: firm_zip4
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: pmt_date
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: subj_namf
        
    
    .. py:attribute:: subj_naml
        
    
    .. py:attribute:: subj_nams
        
    
    .. py:attribute:: subj_namt
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    

LempCd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist Employers/Subcontracted Clients data from

        F601 -- Lobbying Firm Registration Statement
        F601 Part 2 A
        F601 Part 2 B

.. py:class:: LempCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: agencylist
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: cli_adr1
        
    
    .. py:attribute:: cli_adr2
        
    
    .. py:attribute:: cli_city
        
    
    .. py:attribute:: cli_namf
        
    
    .. py:attribute:: cli_naml
        
    
    .. py:attribute:: cli_nams
        
    
    .. py:attribute:: cli_namt
        
    
    .. py:attribute:: cli_phon
        
    
    .. py:attribute:: cli_st
        
    
    .. py:attribute:: cli_zip4
        
    
    .. py:attribute:: client_id
        
    
    .. py:attribute:: con_period
        
    
    .. py:attribute:: descrip
        
    
    .. py:attribute:: eff_date
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: sub_adr1
        
    
    .. py:attribute:: sub_adr2
        
    
    .. py:attribute:: sub_city
        
    
    .. py:attribute:: sub_name
        
    
    .. py:attribute:: sub_phon
        
    
    .. py:attribute:: sub_st
        
    
    .. py:attribute:: sub_zip4
        
    
    .. py:attribute:: subfirm_id
        
    

LpayCd
~~~~~~~~~~~~~~~~~~~~~~~
Payments made/received to/from Lobbying Firms reported on forms

        F625 Part 2
        F635 Part 3B

.. py:class:: LpayCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: advan_amt
        
    
    .. py:attribute:: advan_dscr
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: bakref_tid
        
    
    .. py:attribute:: cum_total
        
    
    .. py:attribute:: emplr_adr1
        
    
    .. py:attribute:: emplr_adr2
        
    
    .. py:attribute:: emplr_city
        
    
    .. py:attribute:: emplr_id
        
    
    .. py:attribute:: emplr_namf
        
    
    .. py:attribute:: emplr_naml
        
    
    .. py:attribute:: emplr_nams
        
    
    .. py:attribute:: emplr_namt
        
    
    .. py:attribute:: emplr_phon
        
    
    .. py:attribute:: emplr_st
        
    
    .. py:attribute:: emplr_zip4
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: fees_amt
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: lby_actvty
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: memo_code
        
    
    .. py:attribute:: memo_refno
        
    
    .. py:attribute:: per_total
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: reimb_amt
        
    
    .. py:attribute:: tran_id
        
            Permanent value unique to this item
        
    

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
    
    .. py:attribute:: id
        
    
    .. py:attribute:: xref_filer_id
        
            Alternative filer ID found on many forms
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filer_type
        
    
    .. py:attribute:: status
        
    
    .. py:attribute:: effect_dt
        
            Effective date for status
        
    
    .. py:attribute:: naml
        
            Last name, sometimes full name
        
    
    .. py:attribute:: namf
        
            First name
        
    
    .. py:attribute:: namt
        
            Name prefix or title
        
    
    .. py:attribute:: nams
        
            Name suffix
        
    
    .. py:attribute:: adr1
        
    
    .. py:attribute:: adr2
        
    
    .. py:attribute:: city
        
    
    .. py:attribute:: st
        
    
    .. py:attribute:: zip4
        
    
    .. py:attribute:: phon
        
    
    .. py:attribute:: fax
        
    
    .. py:attribute:: email
        
    

FilerFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~
Key table that links filers to their paper, key data entry, legacy,
    and electronic filings. This table is used as an index to locate
    filing information.

.. py:class:: FilerFilingsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: period_id
        
            Identifies the period when the filing was recieved.
        
    
    .. py:attribute:: form_id
        
            Form identification code
        
    
    .. py:attribute:: filing_sequence
        
            Amendment number where 0 is an original filing and 1 to 999 are amendments
        
    
    .. py:attribute:: filing_date
        
            Date the filing entered into the system
        
    
    .. py:attribute:: stmnt_type
        
            Type of statement
        
    
    .. py:attribute:: stmnt_status
        
            The status of the statement. If the filing has been reviewed or not reviewed.
        
    
    .. py:attribute:: session_id
        
            Legislative session that the filing applies to
        
    
    .. py:attribute:: user_id
        
    
    .. py:attribute:: special_audit
        
            Denotes whether the filing has been audited for money laundering or other special condition.
        
    
    .. py:attribute:: fine_audit
        
            Indicates whether a filing has been audited for a fine
        
    
    .. py:attribute:: rpt_start
        
            Starting date for the period the filing represents
        
    
    .. py:attribute:: rpt_end
        
            Ending date for the period the filing represents
        
    
    .. py:attribute:: rpt_date
        
            Date filing received
        
    
    .. py:attribute:: filing_type
        
    

FilingsCd
~~~~~~~~~~~~~~~~~~~~~~~
This table is the parent table from which all links and association to
    a filing are derived.

.. py:class:: FilingsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: filing_type
        
    

SmryCd
~~~~~~~~~~~~~~~~~~~~~~~
Summary totals from filings.

.. py:class:: SmryCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: amount_a
        
            Summary amount from column A
        
    
    .. py:attribute:: amount_b
        
            Summary amount from column B
        
    
    .. py:attribute:: amount_c
        
            Summary amount from column C
        
    
    .. py:attribute:: elec_dt
        
    

CvrE530Cd
~~~~~~~~~~~~~~~~~~~~~~~
This table method is undocumented in the print docs.

.. py:class:: CvrE530Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: entity_cd
        
    
    .. py:attribute:: filer_naml
        
    
    .. py:attribute:: filer_namf
        
    
    .. py:attribute:: filer_namt
        
    
    .. py:attribute:: filer_nams
        
    
    .. py:attribute:: report_num
        
    
    .. py:attribute:: rpt_date
        
    
    .. py:attribute:: filer_city
        
    
    .. py:attribute:: filer_st
        
    
    .. py:attribute:: filer_zip4
        
    
    .. py:attribute:: occupation
        
    
    .. py:attribute:: employer
        
    
    .. py:attribute:: cand_naml
        
    
    .. py:attribute:: cand_namf
        
    
    .. py:attribute:: cand_namt
        
    
    .. py:attribute:: cand_nams
        
    
    .. py:attribute:: district_cd
        
    
    .. py:attribute:: office_cd
        
    
    .. py:attribute:: pmnt_dt
        
    
    .. py:attribute:: pmnt_amount
        
    
    .. py:attribute:: type_literature
        
    
    .. py:attribute:: type_printads
        
    
    .. py:attribute:: type_radio
        
    
    .. py:attribute:: type_tv
        
    
    .. py:attribute:: type_it
        
    
    .. py:attribute:: type_billboards
        
    
    .. py:attribute:: type_other
        
    
    .. py:attribute:: other_desc
        
    

TextMemoCd
~~~~~~~~~~~~~~~~~~~~~~~
Text memos attached to electronic filings

.. py:class:: TextMemoCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: line_item
        
            Line item number of this record
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: ref_no
        
            Links text memo to a specific record
        
    
    .. py:attribute:: text4000
        
            Contents of the text memo
        
    

AcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~
Contains acronyms and their meaning.

.. py:class:: AcronymsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: acronym
        
    
    .. py:attribute:: stands_for
        
    
    .. py:attribute:: effect_dt
        
    
    .. py:attribute:: a_desc
        
    

AddressCd
~~~~~~~~~~~~~~~~~~~~~~~
This table holds all addresses for the system. This table can be used
    for address-based searches and formes the bases for address information
    desplayed by the AMS.

.. py:class:: AddressCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: adrid
        
    
    .. py:attribute:: city
        
    
    .. py:attribute:: st
        
    
    .. py:attribute:: zip4
        
    
    .. py:attribute:: phon
        
    
    .. py:attribute:: fax
        
    
    .. py:attribute:: email
        
    

BallotMeasuresCd
~~~~~~~~~~~~~~~~~~~~~~~
Ballot measures dates and times

.. py:class:: BallotMeasuresCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: election_date
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: measure_no
        
    
    .. py:attribute:: measure_name
        
    
    .. py:attribute:: measure_short_name
        
    
    .. py:attribute:: jurisdiction
        
    

EfsFilingLogCd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: EfsFilingLogCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filing_date
        
    
    .. py:attribute:: filingstatus
        
    
    .. py:attribute:: vendor
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: form_type
        
            Name of the source filing form or schedule
        
    
    .. py:attribute:: error_no
        
    

FilersCd
~~~~~~~~~~~~~~~~~~~~~~~
This table is the parent table from which all links and associations
    to a filer are derived.

.. py:class:: FilersCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    

FilerAcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~
links acronyms to filers

.. py:class:: FilerAcronymsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: acronym
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    

FilerAddressCd
~~~~~~~~~~~~~~~~~~~~~~~
Links filers and addresses. This table maintains a history of when
    addresses change.

.. py:class:: FilerAddressCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: adrid
        
    
    .. py:attribute:: effect_dt
        
    
    .. py:attribute:: add_type
        
    
    .. py:attribute:: session_id
        
    

FilerEthicsClassCd
~~~~~~~~~~~~~~~~~~~~~~~
This table stores lobbyist ethics training dates.

.. py:class:: FilerEthicsClassCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: ethics_date
        
    

FilerInterestsCd
~~~~~~~~~~~~~~~~~~~~~~~
Links a filer to their interest codes.

.. py:class:: FilerInterestsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: interest_cd
        
    
    .. py:attribute:: effect_date
        
    

FilerLinksCd
~~~~~~~~~~~~~~~~~~~~~~~
Links filers to each other and records their relationship type.

.. py:class:: FilerLinksCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id_a
        
            Unique identification number for the first filer in the relationship
        
    
    .. py:attribute:: filer_id_b
        
            Unique identification number for the second filer in the relationship
        
    
    .. py:attribute:: active_flg
        
            Indicates if the link is active
        
    
    .. py:attribute:: session_id
        
            Session identification number
        
    
    .. py:attribute:: link_type
        
            Denotes the type of the link
        
    
    .. py:attribute:: link_desc
        
            Unused
        
    
    .. py:attribute:: effect_dt
        
            Date the link became active
        
    
    .. py:attribute:: dominate_filer
        
            Unused
        
    
    .. py:attribute:: termination_dt
        
            Date the relationship was terminated
        
    

FilerStatusTypesCd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: FilerStatusTypesCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: status_type
        
    
    .. py:attribute:: status_desc
        
    

FilerToFilerTypeCd
~~~~~~~~~~~~~~~~~~~~~~~
This table links a filer to a set of characteristics that describe the
    filer. This table maintains a history of changes and allows the filer
    to change characteristics over time.

.. py:class:: FilerToFilerTypeCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filer_type
        
            Filer type identification number
        
    
    .. py:attribute:: active
        
            Indicates if the filer is currently active
        
    
    .. py:attribute:: race
        
            If applicable indicates the race in which the filer is running
        
    
    .. py:attribute:: session_id
        
            Legislative session identification number
        
    
    .. py:attribute:: category
        
            Defines the filer's category such as controlled, jointly controlled, etc. (subset of filer's type)
        
    
    .. py:attribute:: category_type
        
            When applicable, the category type specifies additional information about the category. (e.g. state, local, etc.)
        
    
    .. py:attribute:: sub_category
        
            When applicable specifies general purpose, primarily formed, etc.
        
    
    .. py:attribute:: effect_dt
        
            The date the filer assumed the current class or type
        
    
    .. py:attribute:: sub_category_type
        
            When applicable specifies broad based or small contributor
        
    
    .. py:attribute:: election_type
        
            Indicates type of election (general, primary, special)
        
    
    .. py:attribute:: sub_category_a
        
            Indicates if sponsored or not
        
    
    .. py:attribute:: nyq_dt
        
            Indicates the date when a committee reached its qualifying level of activity
        
    
    .. py:attribute:: party_cd
        
            Filer's political party
        
    
    .. py:attribute:: county_cd
        
            Filer's county code
        
    
    .. py:attribute:: district_cd
        
            Filer's district number for the office being sought. Populated for Senate, Assembly or Board of Equalization races
        
    

FilerTypesCd
~~~~~~~~~~~~~~~~~~~~~~~
This lookup table describes filer types.

.. py:class:: FilerTypesCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_type
        
            Filer type identification number
        
    
    .. py:attribute:: description
        
            Description of the filer type
        
    
    .. py:attribute:: grp_type
        
            Group type assocated with the filer type
        
    
    .. py:attribute:: calc_use
        
            Use checkbox flag
        
    
    .. py:attribute:: grace_period
        
    

FilerXrefCd
~~~~~~~~~~~~~~~~~~~~~~~
This table maps legacy filer identification numbers to the system&#39;s filer
    identification numbers.

.. py:class:: FilerXrefCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: xref_id
        
            Alternative filer ID found on many forms
        
    
    .. py:attribute:: effect_dt
        
    
    .. py:attribute:: migration_source
        
    

FilingPeriodCd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: FilingPeriodCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: period_id
        
            Unique period identification number
        
    
    .. py:attribute:: start_date
        
            Starting date for period
        
    
    .. py:attribute:: end_date
        
            Ending date of period
        
    
    .. py:attribute:: period_type
        
    
    .. py:attribute:: per_grp_type
        
            Period group type
        
    
    .. py:attribute:: period_desc
        
            Period description
        
    
    .. py:attribute:: deadline
        
            Deadline date
        
    

GroupTypesCd
~~~~~~~~~~~~~~~~~~~~~~~
This lookup table stores group type information.

.. py:class:: GroupTypesCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: grp_id
        
    
    .. py:attribute:: grp_name
        
    
    .. py:attribute:: grp_desc
        
    

HeaderCd
~~~~~~~~~~~~~~~~~~~~~~~
Lookup table used to report form 460 information in the AMS.

.. py:class:: HeaderCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: line_number
        
    
    .. py:attribute:: form_id
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: section_label
        
    
    .. py:attribute:: comments1
        
    
    .. py:attribute:: comments2
        
    
    .. py:attribute:: label
        
    
    .. py:attribute:: column_a
        
    
    .. py:attribute:: column_b
        
    
    .. py:attribute:: column_c
        
    
    .. py:attribute:: show_c
        
    
    .. py:attribute:: show_b
        
    

HdrCd
~~~~~~~~~~~~~~~~~~~~~~~
Electronic filing record header data

.. py:class:: HdrCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: amend_id
        
            Amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.
        
    
    .. py:attribute:: cal_ver
        
    
    .. py:attribute:: ef_type
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: hdr_comment
        
    
    .. py:attribute:: rec_type
        
    
    .. py:attribute:: soft_name
        
    
    .. py:attribute:: soft_ver
        
    
    .. py:attribute:: state_cd
        
    

ImageLinksCd
~~~~~~~~~~~~~~~~~~~~~~~
This table links images to filers and accounts.

.. py:class:: ImageLinksCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: img_link_id
        
    
    .. py:attribute:: img_link_type
        
    
    .. py:attribute:: img_id
        
    
    .. py:attribute:: img_type
        
    
    .. py:attribute:: img_dt
        
    

LegislativeSessionsCd
~~~~~~~~~~~~~~~~~~~~~~~
Legislative session, begin and end dates look up table.

.. py:class:: LegislativeSessionsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: begin_date
        
    
    .. py:attribute:: end_date
        
    

LobbyingChgLogCd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyingChgLogCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: change_no
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: log_dt
        
    
    .. py:attribute:: filer_type
        
    
    .. py:attribute:: correction_flag
        
    
    .. py:attribute:: action
        
    
    .. py:attribute:: attribute_changed
        
    
    .. py:attribute:: ethics_dt
        
    
    .. py:attribute:: interests
        
    
    .. py:attribute:: filer_full_name
        
    
    .. py:attribute:: filer_city
        
    
    .. py:attribute:: filer_st
        
    
    .. py:attribute:: filer_zip
        
    
    .. py:attribute:: filer_phone
        
    
    .. py:attribute:: entity_type
        
    
    .. py:attribute:: entity_name
        
    
    .. py:attribute:: entity_city
        
    
    .. py:attribute:: entity_st
        
    
    .. py:attribute:: entity_zip
        
    
    .. py:attribute:: entity_phone
        
    
    .. py:attribute:: entity_id
        
    
    .. py:attribute:: responsible_officer
        
    
    .. py:attribute:: effect_dt
        
    

LobbyistContributions1Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistContributions1Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filing_period_start_dt
        
    
    .. py:attribute:: filing_period_end_dt
        
    
    .. py:attribute:: contribution_dt
        
    
    .. py:attribute:: recipient_name
        
    
    .. py:attribute:: recipient_id
        
    
    .. py:attribute:: amount
        
    

LobbyistContributions2Cd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist contribution disclosure table. Temporary table used to generate
    disclosure table (Lobbyist Contributions 3)

.. py:class:: LobbyistContributions2Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filing_period_start_dt
        
    
    .. py:attribute:: filing_period_end_dt
        
    
    .. py:attribute:: contribution_dt
        
    
    .. py:attribute:: recipient_name
        
    
    .. py:attribute:: recipient_id
        
    
    .. py:attribute:: amount
        
    

LobbyistContributions3Cd
~~~~~~~~~~~~~~~~~~~~~~~
Lobbyist contribution disclosure table.

.. py:class:: LobbyistContributions3Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filing_period_start_dt
        
    
    .. py:attribute:: filing_period_end_dt
        
    
    .. py:attribute:: contribution_dt
        
    
    .. py:attribute:: recipient_name
        
    
    .. py:attribute:: recipient_id
        
    
    .. py:attribute:: amount
        
    

LobbyistEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmployer1Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: employer_id
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: employer_name
        
    
    .. py:attribute:: current_qtr_amt
        
    
    .. py:attribute:: session_total_amt
        
    
    .. py:attribute:: contributor_id
        
    
    .. py:attribute:: interest_cd
        
    
    .. py:attribute:: interest_name
        
    
    .. py:attribute:: session_yr_1
        
    
    .. py:attribute:: session_yr_2
        
    
    .. py:attribute:: yr_1_ytd_amt
        
    
    .. py:attribute:: yr_2_ytd_amt
        
    
    .. py:attribute:: qtr_1
        
    
    .. py:attribute:: qtr_2
        
    
    .. py:attribute:: qtr_3
        
    
    .. py:attribute:: qtr_4
        
    
    .. py:attribute:: qtr_5
        
    
    .. py:attribute:: qtr_6
        
    
    .. py:attribute:: qtr_7
        
    
    .. py:attribute:: qtr_8
        
    

LobbyistEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmployer2Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: employer_id
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: employer_name
        
    
    .. py:attribute:: current_qtr_amt
        
    
    .. py:attribute:: session_total_amt
        
    
    .. py:attribute:: contributor_id
        
    
    .. py:attribute:: interest_cd
        
    
    .. py:attribute:: interest_name
        
    
    .. py:attribute:: session_yr_1
        
    
    .. py:attribute:: session_yr_2
        
    
    .. py:attribute:: yr_1_ytd_amt
        
    
    .. py:attribute:: yr_2_ytd_amt
        
    
    .. py:attribute:: qtr_1
        
    
    .. py:attribute:: qtr_2
        
    
    .. py:attribute:: qtr_3
        
    
    .. py:attribute:: qtr_4
        
    
    .. py:attribute:: qtr_5
        
    
    .. py:attribute:: qtr_6
        
    
    .. py:attribute:: qtr_7
        
    
    .. py:attribute:: qtr_8
        
    

LobbyistEmployer3Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmployer3Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: employer_id
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: employer_name
        
    
    .. py:attribute:: current_qtr_amt
        
    
    .. py:attribute:: session_total_amt
        
    
    .. py:attribute:: contributor_id
        
    
    .. py:attribute:: interest_cd
        
    
    .. py:attribute:: interest_name
        
    
    .. py:attribute:: session_yr_1
        
    
    .. py:attribute:: session_yr_2
        
    
    .. py:attribute:: yr_1_ytd_amt
        
    
    .. py:attribute:: yr_2_ytd_amt
        
    
    .. py:attribute:: qtr_1
        
    
    .. py:attribute:: qtr_2
        
    
    .. py:attribute:: qtr_3
        
    
    .. py:attribute:: qtr_4
        
    
    .. py:attribute:: qtr_5
        
    
    .. py:attribute:: qtr_6
        
    
    .. py:attribute:: qtr_7
        
    
    .. py:attribute:: qtr_8
        
    

LobbyistEmployerFirms1Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmployerFirms1Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: employer_id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: termination_dt
        
    

LobbyistEmployerFirms2Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistEmployerFirms2Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: employer_id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: termination_dt
        
    

LobbyistEmpLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistEmpLobbyist1Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: lobbyist_id
        
    
    .. py:attribute:: employer_id
        
    
    .. py:attribute:: lobbyist_last_name
        
    
    .. py:attribute:: lobbyist_first_name
        
    
    .. py:attribute:: employer_name
        
    
    .. py:attribute:: session_id
        
    

LobbyistEmpLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistEmpLobbyist2Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: lobbyist_id
        
    
    .. py:attribute:: employer_id
        
    
    .. py:attribute:: lobbyist_last_name
        
    
    .. py:attribute:: lobbyist_first_name
        
    
    .. py:attribute:: employer_name
        
    
    .. py:attribute:: session_id
        
    

LobbyistFirm1Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistFirm1Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: current_qtr_amt
        
    
    .. py:attribute:: session_total_amt
        
    
    .. py:attribute:: contributor_id
        
    
    .. py:attribute:: session_yr_1
        
    
    .. py:attribute:: session_yr_2
        
    
    .. py:attribute:: yr_1_ytd_amt
        
    
    .. py:attribute:: yr_2_ytd_amt
        
    
    .. py:attribute:: qtr_1
        
    
    .. py:attribute:: qtr_2
        
    
    .. py:attribute:: qtr_3
        
    
    .. py:attribute:: qtr_4
        
    
    .. py:attribute:: qtr_5
        
    
    .. py:attribute:: qtr_6
        
    
    .. py:attribute:: qtr_7
        
    
    .. py:attribute:: qtr_8
        
    

LobbyistFirm2Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: LobbyistFirm2Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: current_qtr_amt
        
    
    .. py:attribute:: session_total_amt
        
    
    .. py:attribute:: contributor_id
        
    
    .. py:attribute:: session_yr_1
        
    
    .. py:attribute:: session_yr_2
        
    
    .. py:attribute:: yr_1_ytd_amt
        
    
    .. py:attribute:: yr_2_ytd_amt
        
    
    .. py:attribute:: qtr_1
        
    
    .. py:attribute:: qtr_2
        
    
    .. py:attribute:: qtr_3
        
    
    .. py:attribute:: qtr_4
        
    
    .. py:attribute:: qtr_5
        
    
    .. py:attribute:: qtr_6
        
    
    .. py:attribute:: qtr_7
        
    
    .. py:attribute:: qtr_8
        
    

LobbyistFirm3Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistFirm3Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: session_id
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: current_qtr_amt
        
    
    .. py:attribute:: session_total_amt
        
    
    .. py:attribute:: contributor_id
        
    
    .. py:attribute:: session_yr_1
        
    
    .. py:attribute:: session_yr_2
        
    
    .. py:attribute:: yr_1_ytd_amt
        
    
    .. py:attribute:: yr_2_ytd_amt
        
    
    .. py:attribute:: qtr_1
        
    
    .. py:attribute:: qtr_2
        
    
    .. py:attribute:: qtr_3
        
    
    .. py:attribute:: qtr_4
        
    
    .. py:attribute:: qtr_5
        
    
    .. py:attribute:: qtr_6
        
    
    .. py:attribute:: qtr_7
        
    
    .. py:attribute:: qtr_8
        
    

LobbyistFirmEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model (Ask Matt)

.. py:class:: LobbyistFirmEmployer1Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: filing_sequence
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: employer_name
        
    
    .. py:attribute:: rpt_start
        
    
    .. py:attribute:: rpt_end
        
    
    .. py:attribute:: per_total
        
    
    .. py:attribute:: cum_total
        
    
    .. py:attribute:: lby_actvty
        
    
    .. py:attribute:: ext_lby_actvty
        
    

LobbyistFirmEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model

.. py:class:: LobbyistFirmEmployer2Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: filing_sequence
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: employer_name
        
    
    .. py:attribute:: rpt_start
        
    
    .. py:attribute:: rpt_end
        
    
    .. py:attribute:: per_total
        
    
    .. py:attribute:: cum_total
        
    
    .. py:attribute:: lby_actvty
        
    
    .. py:attribute:: ext_lby_actvty
        
    

LobbyistFirmLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~
It&#39;s an undocumented model.

.. py:class:: LobbyistFirmLobbyist1Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: lobbyist_id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: lobbyist_last_name
        
    
    .. py:attribute:: lobbyist_first_name
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: session_id
        
    

LobbyistFirmLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LobbyistFirmLobbyist2Cd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: lobbyist_id
        
    
    .. py:attribute:: firm_id
        
    
    .. py:attribute:: lobbyist_last_name
        
    
    .. py:attribute:: lobbyist_first_name
        
    
    .. py:attribute:: firm_name
        
    
    .. py:attribute:: session_id
        
    

LookupCode
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: LookupCode
    
    .. py:attribute:: id
        
    
    .. py:attribute:: code_type
        
    
    .. py:attribute:: code_id
        
    
    .. py:attribute:: code_desc
        
    

NamesCd
~~~~~~~~~~~~~~~~~~~~~~~


.. py:class:: NamesCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: namid
        
    
    .. py:attribute:: naml
        
    
    .. py:attribute:: namf
        
    
    .. py:attribute:: namt
        
    
    .. py:attribute:: nams
        
    
    .. py:attribute:: moniker
        
    
    .. py:attribute:: moniker_pos
        
    
    .. py:attribute:: namm
        
    
    .. py:attribute:: fullname
        
    
    .. py:attribute:: naml_search
        
    

ReceivedFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~
This is undocumented. J M needs to describe this table.

.. py:class:: ReceivedFilingsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: filer_id
        
            Filer's unique identification number
        
    
    .. py:attribute:: filing_file_name
        
    
    .. py:attribute:: received_date
        
    
    .. py:attribute:: filing_directory
        
    
    .. py:attribute:: filing_id
        
            Unique filing identificiation number
        
    
    .. py:attribute:: form_id
        
    
    .. py:attribute:: receive_comment
        
    

ReportsCd
~~~~~~~~~~~~~~~~~~~~~~~
This is an undocumented model.

.. py:class:: ReportsCd
    
    .. py:attribute:: id
        
    
    .. py:attribute:: rpt_id
        
            Unique identification number
        
    
    .. py:attribute:: rpt_name
        
            Name of the report
        
    
    .. py:attribute:: rpt_desc_field
        
            Description of the report
        
    
    .. py:attribute:: path
        
            Reportpath
        
    
    .. py:attribute:: data_object
        
    
    .. py:attribute:: parms_flg_y_n
        
            Parameters indication flag
        
    
    .. py:attribute:: rpt_type
        
            Type of the report
        
    
    .. py:attribute:: parm_definition
        
            Parameter definition
        
    


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
