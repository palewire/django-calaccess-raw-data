Models!!
========

A crosswalk between the tables published by California's Secretary of State
and the models in this Django application.

Filings
-------

CvrSoCd
~~~~~~~~~~~~~~~~~~~~~~~


    Cover page for a statement of organization creation or termination
    form filed by a slate-mailer organization or recipient committee.
    

.. py:class:: CvrSoCd


Cvr2SoCd
~~~~~~~~~~~~~~~~~~~~~~~


    Additional names and committees information included on the second page
    of a statement of organization creation form filed
    by a slate-mailer organization or recipient committee.
    

.. py:class:: Cvr2SoCd


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


Cvr2CampaignDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~


    Record used to carry additional names for the campaign
    disclosure forms below.
    

.. py:class:: Cvr2CampaignDisclosureCd


RcptCd
~~~~~~~~~~~~~~~~~~~~~~~


    Receipts schedules for the following forms.

        Form 460 (Recipient Committee Campaign Statement)
        Schedules A, C, I, and A-1.

        Form 401 (Slate Mailer Organization Campaign Statement) Schedule A.
    

.. py:class:: RcptCd


Cvr3VerificationInfoCd
~~~~~~~~~~~~~~~~~~~~~~~


    Cover page verification information from campaign disclosure forms
    

.. py:class:: Cvr3VerificationInfoCd


LoanCd
~~~~~~~~~~~~~~~~~~~~~~~


    Loans received and made.
    

.. py:class:: LoanCd


S401Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This table contains Form 401 (Slate Mailer Organization) payment and other
    disclosure schedule (F401B, F401B-1, F401C, F401D) information.
    

.. py:class:: S401Cd


ExpnCd
~~~~~~~~~~~~~~~~~~~~~~~


    Campaign expenditures from a variety of forms
    

.. py:class:: ExpnCd


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


DebtCd
~~~~~~~~~~~~~~~~~~~~~~~


    Form 460 (Recipient Committee Campaign Statement)
    Schedule (F) Accrued Expenses (Unpaid Bills) records
    

.. py:class:: DebtCd


S496Cd
~~~~~~~~~~~~~~~~~~~~~~~


    Form 496 Late Independent Expenditures
    

.. py:class:: S496Cd


SpltCd
~~~~~~~~~~~~~~~~~~~~~~~


    Split Records

        -- F450P5
        -- F460 (A-B1-B2-C-D-H)
    

.. py:class:: SpltCd


S497Cd
~~~~~~~~~~~~~~~~~~~~~~~


    Form 497 Late Contributions Received/Made
    

.. py:class:: S497Cd


F501502Cd
~~~~~~~~~~~~~~~~~~~~~~~


    Candidate Intention Statement

        -- F501
        -- F502
    

.. py:class:: F501502Cd


S498Cd
~~~~~~~~~~~~~~~~~~~~~~~


    Form 498 Slate Mailer Late Independent Expenditures Made
    

.. py:class:: S498Cd


CvrRegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~


    Cover page of lobbying disclosure forms
    

.. py:class:: CvrRegistrationCd


Cvr2RegistrationCd
~~~~~~~~~~~~~~~~~~~~~~~


    Cover page of lobbying dislcosure forms
    

.. py:class:: Cvr2RegistrationCd


CvrLobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~


    Cover page information for the lobbying disclosure forms

        F615 -- Lobbyist Report
        F625 -- Report of Lobbying Firm
        F635 -- Report of Lobbyist Employer and Report of Lobbying Coalition
        F645 -- Report of Person Spending $5,000 or more to influence
                Legislative or administrative action
    

.. py:class:: CvrLobbyDisclosureCd


Cvr2LobbyDisclosureCd
~~~~~~~~~~~~~~~~~~~~~~~


    Additional names data for the lobbyist disclosure forms

        F615 -- Lobbyist Report
        F625 -- Report of Lobbying Firm
        F635 -- Report of Lobbyist Employer and Report of Lobbying Coalition
        F645 -- Report of Person Spending $5,000 or more to influence
                Legislative or administrative action
    

.. py:class:: Cvr2LobbyDisclosureCd


LobbyAmendmentsCd
~~~~~~~~~~~~~~~~~~~~~~~


    Lobbyist registration amendment information

        Form 605 Part I
    

.. py:class:: LobbyAmendmentsCd


F690P2Cd
~~~~~~~~~~~~~~~~~~~~~~~


    Amends lobbying disclosure filings

        F690 Amendment to Lobbying Disclosure Report
    

.. py:class:: F690P2Cd


LattCd
~~~~~~~~~~~~~~~~~~~~~~~


    Lobbyist disclosure attachment schedules for payments
        F630 -- Payments made to Lobbying Coalitions (Attatchment)
        F635C -- Payments received by Lobbying Coalitions (Attatchment)
        F640 -- Government Agencies Reporting of &quot;Other Payments to Influence
                Legislative or Administrative Action&quot; (Attatchment)
    

.. py:class:: LattCd


LexpCd
~~~~~~~~~~~~~~~~~~~~~~~


    Lobbying Activity Expenditure Schedule information (Gifts)
    Reported in filings of the forms

        F615 Part 1
        F625 Part 3A
        F635 Part 3C
        F645 Part 2A
    

.. py:class:: LexpCd


LccmCd
~~~~~~~~~~~~~~~~~~~~~~~


    Lobbying Campaign Contributions reported on forms

        F615 Part 2
        F625 Part 4B
        F635 Part 4B
        F645 Part 3B
    

.. py:class:: LccmCd


LothCd
~~~~~~~~~~~~~~~~~~~~~~~


    Payment to other lobbying firms reported on form

        F625 Part 3B
    

.. py:class:: LothCd


LempCd
~~~~~~~~~~~~~~~~~~~~~~~


    Lobbyist Employers/Subcontracted Clients data from

        F601 -- Lobbying Firm Registration Statement
        F601 Part 2 A
        F601 Part 2 B
    

.. py:class:: LempCd


LpayCd
~~~~~~~~~~~~~~~~~~~~~~~


    Payments made/received to/from Lobbying Firms reported on forms

        F625 Part 2
        F635 Part 3B
    

.. py:class:: LpayCd


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


FilerFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~


    Key table that links filers to their paper, key data entry, legacy,
    and electronic filings. This table is used as an index to locate
    filing information.
    

.. py:class:: FilerFilingsCd


FilingsCd
~~~~~~~~~~~~~~~~~~~~~~~


    This table is the parent table from which all links and association to
    a filing are derived.
    

.. py:class:: FilingsCd


SmryCd
~~~~~~~~~~~~~~~~~~~~~~~


    Summary totals from filings.
    

.. py:class:: SmryCd


CvrE530Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This table method is undocumented in the print docs.
    

.. py:class:: CvrE530Cd


TextMemoCd
~~~~~~~~~~~~~~~~~~~~~~~


    Text memos attached to electronic filings
    

.. py:class:: TextMemoCd


AcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~


    Contains acronyms and their meaning.
    

.. py:class:: AcronymsCd


AddressCd
~~~~~~~~~~~~~~~~~~~~~~~


    This table holds all addresses for the system. This table can be used
    for address-based searches and formes the bases for address information
    desplayed by the AMS.
    

.. py:class:: AddressCd


BallotMeasuresCd
~~~~~~~~~~~~~~~~~~~~~~~

 Ballot measures dates and times 

.. py:class:: BallotMeasuresCd


EfsFilingLogCd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: EfsFilingLogCd


FilersCd
~~~~~~~~~~~~~~~~~~~~~~~


    This table is the parent table from which all links and associations
    to a filer are derived.
    

.. py:class:: FilersCd


FilerAcronymsCd
~~~~~~~~~~~~~~~~~~~~~~~


    links acronyms to filers
    

.. py:class:: FilerAcronymsCd


FilerAddressCd
~~~~~~~~~~~~~~~~~~~~~~~


    Links filers and addresses. This table maintains a history of when
    addresses change.
    

.. py:class:: FilerAddressCd


FilerEthicsClassCd
~~~~~~~~~~~~~~~~~~~~~~~


    This table stores lobbyist ethics training dates.
    

.. py:class:: FilerEthicsClassCd


FilerInterestsCd
~~~~~~~~~~~~~~~~~~~~~~~


    Links a filer to their interest codes.
    

.. py:class:: FilerInterestsCd


FilerLinksCd
~~~~~~~~~~~~~~~~~~~~~~~


    Links filers to each other and records their relationship type.
    

.. py:class:: FilerLinksCd


FilerStatusTypesCd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: FilerStatusTypesCd


FilerToFilerTypeCd
~~~~~~~~~~~~~~~~~~~~~~~


    This table links a filer to a set of characteristics that describe the
    filer. This table maintains a history of changes and allows the filer
    to change characteristics over time.
    

.. py:class:: FilerToFilerTypeCd


FilerTypesCd
~~~~~~~~~~~~~~~~~~~~~~~


    This lookup table describes filer types.
    

.. py:class:: FilerTypesCd


FilerXrefCd
~~~~~~~~~~~~~~~~~~~~~~~


    This table maps legacy filer identification numbers to the system&#39;s filer
    identification numbers.
    

.. py:class:: FilerXrefCd


FilingPeriodCd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: FilingPeriodCd


GroupTypesCd
~~~~~~~~~~~~~~~~~~~~~~~


    This lookup table stores group type information.
    

.. py:class:: GroupTypesCd


HeaderCd
~~~~~~~~~~~~~~~~~~~~~~~


    Lookup table used to report form 460 information in the AMS.
    

.. py:class:: HeaderCd


HdrCd
~~~~~~~~~~~~~~~~~~~~~~~


    Electronic filing record header data
    

.. py:class:: HdrCd


ImageLinksCd
~~~~~~~~~~~~~~~~~~~~~~~


    This table links images to filers and accounts.
    

.. py:class:: ImageLinksCd


LegislativeSessionsCd
~~~~~~~~~~~~~~~~~~~~~~~


    Legislative session, begin and end dates look up table.
    

.. py:class:: LegislativeSessionsCd


LobbyingChgLogCd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: LobbyingChgLogCd


LobbyistContributions1Cd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: LobbyistContributions1Cd


LobbyistContributions2Cd
~~~~~~~~~~~~~~~~~~~~~~~


    Lobbyist contribution disclosure table. Temporary table used to generate
    disclosure table (Lobbyist Contributions 3)
    

.. py:class:: LobbyistContributions2Cd


LobbyistContributions3Cd
~~~~~~~~~~~~~~~~~~~~~~~


    Lobbyist contribution disclosure table.
    

.. py:class:: LobbyistContributions3Cd


LobbyistEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: LobbyistEmployer1Cd


LobbyistEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: LobbyistEmployer2Cd


LobbyistEmployer3Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: LobbyistEmployer3Cd


LobbyistEmployerFirms1Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: LobbyistEmployerFirms1Cd


LobbyistEmployerFirms2Cd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: LobbyistEmployerFirms2Cd


LobbyistEmpLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: LobbyistEmpLobbyist1Cd


LobbyistEmpLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: LobbyistEmpLobbyist2Cd


LobbyistFirm1Cd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: LobbyistFirm1Cd


LobbyistFirm2Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: LobbyistFirm2Cd


LobbyistFirm3Cd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: LobbyistFirm3Cd


LobbyistFirmEmployer1Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model (Ask Matt)
    

.. py:class:: LobbyistFirmEmployer1Cd


LobbyistFirmEmployer2Cd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model
    

.. py:class:: LobbyistFirmEmployer2Cd


LobbyistFirmLobbyist1Cd
~~~~~~~~~~~~~~~~~~~~~~~


    It&#39;s an undocumented model.
    

.. py:class:: LobbyistFirmLobbyist1Cd


LobbyistFirmLobbyist2Cd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: LobbyistFirmLobbyist2Cd


LookupCode
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: LookupCode


NamesCd
~~~~~~~~~~~~~~~~~~~~~~~



.. py:class:: NamesCd


ReceivedFilingsCd
~~~~~~~~~~~~~~~~~~~~~~~


    This is undocumented. J M needs to describe this table.
    

.. py:class:: ReceivedFilingsCd


ReportsCd
~~~~~~~~~~~~~~~~~~~~~~~


    This is an undocumented model.
    

.. py:class:: ReportsCd



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
