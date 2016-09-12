#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All the CAL-ACCESS forms cataloged by our research.
"""
from calaccess_raw.annotations import FilingForm

all_filing_forms = (
    FilingForm(
        'F400',
        'Statement of Organization (Slate Mailer Organization)',
        group='CAMPAIGN',
        documentcloud_id='2781370-400-2016-01',
        description='Form 400 must be filed within 10 days after the slate \
mailer organization receives, or is promised to receive, $500 or more for \
producing one or more slate mailers.',
    ),
    FilingForm(
        'F401',
        'Campaign Disclosure Statement (Slate Mailer Organization)',
        group='CAMPAIGN',
        documentcloud_id='2781366-401-2005-01',
        description='Form 401 is filed by slate mailer organizations to \
disclose payments made and received in connection with producing slate mailers.',
    ),
    FilingForm(
        'F402',
        'Statement of Termination (Slate Mailer Organization)',
        group='CAMPAIGN',
        documentcloud_id='2781369-402-2005-01',
        description='Form 402 is filed by slate mailer organizations to \
terminate the organization.',
    ),
    FilingForm(
        'F405',
        'Amendment to Campaign Disclosure Statement',
        group='CAMPAIGN',
        documentcloud_id='2811582-405-1994',
        description="Form 405 is used to amend many campaign disclosure statements, with the exception of \
Statement of Organization (410), Candidate Intention (501) or Campaign Bank Account (502) forms.",
    ),
    FilingForm(
        'F410',
        'Statement of Organization (Recipient Committee)',
        group='CAMPAIGN',
        documentcloud_id='2781368-410-2016-01',
        description='Form 410 must be filed within 10 days of receiving \
$2,000 in contributions. If the committee has not yet reached the $2,000 \
threshold, the not-yet-qualified box should be checked.',
    ),
    FilingForm(
        'F415',
        'Title Unknown',
        group='Deprecated',
        description='Form 415 was deprecated in or around 2001. The information \
previously reported on this form is now reported on Form 410 (Statement of \
Organization Recipient Committee). There are 51,047 filings with this form ID.',
    ),
    FilingForm(
        'F416',
        'Title Unknown',
        group='Deprecated',
        description='Form 416 was deprecated in or around 2001. The information \
previously reported on this form is now reported on Form 410 (Statement of \
Organization Recipient Committee). There are 521 filings with this form ID.',
    ),
    FilingForm(
        'F419',
        'Campaign Disclosure Statement, Long Form (Ballot Measure Committee)',
        group='Deprecated',
        description='Form 419 was replaced by Form 460 (Recipient Committee \
Campaign Statement) in or around 2001. There are 2,293 filings with this form ID.',
    ),
    FilingForm(
        'F420',
        'Campaign Disclosure Statement, Long Form (Recipient Committee)',
        group='Deprecated',
        description='Form 420 was replaced by Form 460 (Recipient Committee \
Campaign Statement) in or around 2001. There are 70,704 filings with this form ID.',
    ),
    FilingForm(
        'F425',
        'Semi-Annual Statement of No Activity (Recipient Committee)',
        group='CAMPAIGN',
        documentcloud_id='2781365-425-2001-01',
        description='Form 425 is filed by recipient committees that have not \
received any contributions and have not made any expenditures during the six-\
month period covered by a semi-annual statement.',
    ),
    FilingForm(
        'F430',
        'Title Unknown',
        group='Deprecated',
        description='Form 430 was deprecated in or around 1980. The information \
previously reported on this form is (probably) now reported on Form 460 (Recipient \
Committee Campaign Statement). There are 2,293 filings with this form ID.',
    ),
    FilingForm(
        'F450',
        'Campaign Disclosure Statement, Short Form (Recipient Committee)',
        group='CAMPAIGN',
        documentcloud_id='2781364-450-2016-01',
        description='Form 450 is filed by recipient committees that meet \
certain specific criteria listed in the Form 450.',
    ),
    FilingForm(
        'F460',
        'Campaign Disclosure Statement (Recipient Committee)',
        group='CAMPAIGN',
        documentcloud_id='2781363-460-2016-01',
        description='Form 460 is filed by recipient committees to report \
expenditures and contributions. It can be used to file a pre-election statement, \
semi-annual statement, quarterly statement, termination statement, special odd-\
year report or an amendment to a previously filed statement.',
    ),
    FilingForm(
        'F461',
        'Campaign Disclosure Statement (Independent Expenditure Committee & Major Donor Committee)',
        group='CAMPAIGN',
        documentcloud_id='2781361-461-2016-01',
        description='Form 461 is filed by major donors, independent \
expenditure committees and multipurpose organizations including nonprofits.',
    ),
    FilingForm(
        'F465',
        'Supplemental Independent Expenditure Report',
        group='CAMPAIGN',
        documentcloud_id='2781358-465-2009-06',
        description='Form 465 is filed by officeholders, candidates, recipient \
committees, major donor committees and independent expenditure committees that \
make independent expenditures totaling $1,000 or more in a calendar year to support \
or oppose a single candidate, a single measure, or the qualification of a single \
measure. Filed in the same periods the candidate or committee \
supported or opposed by the independent expenditures is required to file.',
    ),
    FilingForm(
        'F470',
        'Campaign Disclosure Statement, Short Form (Officeholders and Candidates)',
        group='CAMPAIGN',
        documentcloud_id='2781357-470-2016-01',
        description='Form 470 is filed by officeholders and candidates who do \
not have a controlled committee, do not spend or receive contributions totaling $2,000 or \
more during the calendar year.'),
    FilingForm(
        'F490',
        'Campaign Disclosure Statement, Long Form (Officeholders and Candidates)',
        group='Deprecated',
        description='Form 490 was replaced by Form 460 in or around 2001. There \
are 58,266 filings with this form ID.',
    ),
    FilingForm(
        'F495',
        'Supplemental Pre-Election Campaign Statement (Recipient Committee)',
        group='CAMPAIGN',
        documentcloud_id='2781356-495-2005-01',
        description='Form 495 is filed by recipient committees that make \
contributions totaling $10,000 or more in connection with an election in which \
the committee is not required to file regular preelection reports. Form 495 is \
filed as an attachment to Form 450 or Form 460.'
    ),
    FilingForm(
        'F496',
        'Late Independent Expenditure Report',
        group='CAMPAIGN',
        documentcloud_id='2781355-496-2016-01',
        description='Form 496 is filed by committees that make independent \
expenditures whose combined total is $1,000 or more to support or oppose a single \
candidate for office or a single ballot measure. Form 496 should be \
filed within 24-hours of making the expenditure during the 90 days immediately \
preceding the election.',
    ),
    FilingForm(
        'F497',
        'Late Contribution Report',
        group='CAMPAIGN',
        documentcloud_id='2781353-497-2016-01',
        description='Form 497 is filed by state and local committees making \
or receiving contributions totaling $1,000 or more in the 90 \
days before an election, committees reporting contributions of $5,000 or more in \
connection with a state ballot measure and state candidates as well as state \
ballot measure committees that receive $5,000 or more at any time other than a \
90-day election cycle.',
    ),
    FilingForm(
        'F498',
        'Late Payment Report (Slate Mailer Organization)',
        group='CAMPAIGN',
        documentcloud_id='2781352-498-2016-01',
        description='Form 498 is filed by a slate mailer organization on \
receipt of a late payment.',
    ),
    FilingForm(
        'F501',
        'Candidate Intention Statement',
        group='CAMPAIGN',
        documentcloud_id='2781351-501-2016-01',
        description='Form 501 is filed each election by candidates for state \
or local office.'
    ),
    FilingForm(
        'F502',
        'Campaign Bank Account Statement',
        group='CAMPAIGN',
        description='Form 502 must be filed within 10 days of opening a \
campaign bank account at a financial institution in California.'
    ),
    FilingForm(
        'F511',
        'Paid Spokesperson Report',
        group='CAMPAIGN',
        documentcloud_id='2781350-511-2015-01',
        description='Form 511 is filed by committees that make expenditures \
totaling $5,000 or more to an individual for his or her appearance in a printed, \
televised, or radio advertisement, or in a telephone message to support or \
oppose the qualification, passage, or defeat of a state or local ballot measure.'
    ),
    FilingForm(
        'E530',
        'Electronic Issue Advocacy Report',
        group='CAMPAIGN',
        documentcloud_id='2781349-E530-Instructions',
        description='On-line Form E-530 reports must be filed by anyone \
spending or promising to pay $50,000 or more for a communication disseminated \
within 45 days of an election, if the communication clearly identifies a candidate \
for state elective office but does not expressly advocate the election or defeat \
of that candidate.'
    ),
    FilingForm(
        'F601',
        'Lobbying Firm Registration Statement',
        group='LOBBYIST',
        documentcloud_id='2781348-601-2014-10',
        description='Form 601 is filed on a biennial basis by a lobbying \
firm or individual contract lobbyist wishing to register or renew an existing \
registration. The form must be filed within 10 days of qualifying as a lobbying \
firm. Renewal of existing registration is due between November 1 and December 31 \
of each even-numbered year. This registration is valid for the complete two-year \
cycle of such session.'),
    FilingForm(
        'F602',
        'Lobbying Firm Activity Authorization',
        group='LOBBYIST',
        documentcloud_id='2781347-602-1998-07',
        description='Form 602 is an authorization form filed by each person \
who employs or contracts with a lobbying firm. This form serves as an attachment \
to Form 601, and is filed by the applicable lobbying firm. Form 602 also contains \
a schedule which describes by category the nature and interest of the client of \
the firm. Like Form 601 this registration attachment is valid for the length of \
the state legislative session for which it is filed. Form 602 must be filed by \
a firm or its client, prior to attempting to influence legislative or \
administrative action on behalf of that client.'
    ),
    FilingForm(
        'F603',
        'Lobbyist Employer or Lobbying Coalition Registration Statement',
        group='LOBBYIST',
        documentcloud_id='2781346-603-2014-10',
        description='Form 603 is a registration statement filed by registered \
lobbyists employers or lobbying coalitions upon qualifying as an employer or \
coalition. This form is also used to renew an existing registration on a biennial \
basis. Form 603 must be filed within 10 days of qualifying as a lobbyist employer \
or lobbying coalition. Renewal of an existing registration is due between November \
1 and December 31 of each even-numbered year. This registration is valid for the \
complete two-year cycle of such session.'
    ),
    FilingForm(
        'F604',
        'Lobbyist Certification Statement',
        group='LOBBYIST',
        documentcloud_id='2781345-604-2014-10',
        description="Form 604 is the certification statement filed by an \
individual who qualifies as a lobbyist (including an individual contract lobbyist\
). Form 604 is the initial certification statement and is also used as a renewal \
of a previous lobbyist certification. This form includes verification as to \
whether the lobbyist has attended a required course within the previous 12 months \
on ethical issues and laws relating to lobbying. When submitted as a paper filing\
, this form is an attachment to either the firm's Form 601 or the employer's Form \
603. If the form is filed electronically, it is filed separately by the lobbyist."
    ),
    FilingForm(
        'F605',
        'Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition',
        group='LOBBYIST',
        documentcloud_id='2781344-605-2014-10',
        description='Form 605 is the standard amendment form used to amend \
any previously filed registration information. It is used to add or delete both \
lobbyists and clients to an existing registration. It is also used to change name\
, address, and responsible officer information, as well as any other pertinent \
information found on forms 601, 602, 603 or 604.'
    ),
    FilingForm(
        'F606',
        'Notice of Termination',
        group='LOBBYIST',
        documentcloud_id='2781343-606-1997',
        description='Form 606 is filed by any lobbying firm, registered \
lobbyist employer, lobbying coalition or lobbyist who wishes to terminate a filed \
registration or certification statement. A client of a firm (non-registered employer\
) does not use this form to cease lobbying activity. Instead it is deleted by the \
associated firm, which files a Form 605. Form 606 is filed within 20 days of \
ceasing all lobbying activity. A final quarterly disclosure statement must be filed \
for the quarter in which the date of termination is effective.'
    ),
    FilingForm(
        'F607',
        'Notice of Withdrawal',
        group='LOBBYIST',
        documentcloud_id='2781342-607-1997-08',
        description='Form 607 is filed by a lobbying firm or lobbyist wishing \
to withdraw the filed registration statement of a firm which has never met the \
statutory definition of a lobbying firm or lobbyist. Submittal of this form \
relieves the filer of any duty to file any previously-required quarterly \
disclosure statements.'
    ),
    FilingForm(
        'F615',
        'Lobbyist Report',
        group='LOBBYIST',
        documentcloud_id='2781341-615-1990',
        description='Form 615 is the quarterly disclosure statement completed \
by the in-house lobbyist of a lobbying firm, lobbyist employer, or lobbying \
coalition. It is not filed on its own. For paper filers, it is an \
attachment to either Form 625 (Report of Lobbying Firm) or Form 635. (Report of \
Lobbyist Employer/Lobbying Coalition). Electronic or online filers file these as \
separate documents.'
    ),
    FilingForm(
        'F625',
        'Report of Lobbying Firm',
        group='LOBBYIST',
        documentcloud_id='2781340-625-1990',
        description='Form 625 is the quarterly disclosure statement filed by \
a lobbying firm (including individual contract lobbyists) each calendar quarter. \
If the firm employs one or more in-house lobbyists, then, for paper filers, a \
separate Form 615 (Lobbyist Report) must be attached for each lobbyist. Electronic \
or online filers file these as separate documents.'
    ),
    FilingForm(
        'S630',
        'Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) ',
        group='LOBBYIST',
        documentcloud_id='2782806-630-1990',
        description='An attachment to the quarterly disclosure report filed \
by a lobbying firm or lobbyist employer which makes payments to a lobbying \
coalition. This attachment itemizes such payments.'
    ),
    FilingForm(
        'F635',
        'Report of Lobbyist Employer or Report of Lobbying Coalition',
        group='LOBBYIST',
        documentcloud_id='2781339-635-1993',
        description='Form 635 is the quarterly disclosure statement filed by \
a lobbyist employer or a lobbying coalition. For employers and lobbying \
coalitions filing on paper, a separate Form 615 must be completed for each in-\
house lobbyist and attached to Form 635. Electronic or online filers file these \
as separate documents. This form is also used as a quarterly disclosure statement \
for a client of a firm which has no in-house lobbyist (also referred to as a \
non-registered employer).'
    ),
    FilingForm(
        'S635C',
        'Payments Received by Lobbying Coalitions',
        db_value='S635-C',
        group='LOBBYIST',
        documentcloud_id='2781338-635C-1990',
        description='Form 635C is filed by a lobbying coalition as an \
attachment to the Form 635 (Report of a Lobbying Coalition) and discloses all \
payment received from the members of a coalition.'
    ),
    FilingForm(
        'S640',
        'Governmental Agencies Reporting (Attachment to Form 635 or Form 645)',
        group='LOBBYIST',
        documentcloud_id='2781337-640-1993',
        description='Form 640 is filed by a state or local governmental agency \
which qualifies as a lobbyist employer or $5,000 filer. The attachment replaces \
Section D of Form 635 and Section B of Form 645 (Other Payments to \
Influence Legislative or Administrative Action). It is filed in conjunction with \
either Form 635 if a lobbyist employer or Form 645 if a $5,000 filer.'
    ),
    FilingForm(
        'F645',
        'Report of Person Spending $5,000 or More',
        group='LOBBYIST',
        documentcloud_id='2781336-645-1993',
        description='Form 645 is the quarterly disclosure document filed by a \
$5,000 filer (i.e. a person who does not employ a lobbyist or contract with a lobbying \
firm, but who makes payments to influence legislative or administrative action \
in aggregation of $5,000 or more in any calendar quarter). The filer does not \
submit a registration or termination statement, and is only required to file Form \
645 in those calendar quarters which $5,000 or more is spent to influence legislative \
or administrative action. Form 645 must be filed electronically.'
    ),
    FilingForm(
        'F690',
        'Amendment to Lobbying Disclosure Report',
        group='LOBBYIST',
        documentcloud_id='2781335-690-1990',
        description='Form 690 is filed by a lobbying firm, lobbyist employer, \
lobbying coalition, $5,000 filer or lobbyist seeking to amend any information \
previously submitted on a quarterly disclosure report. Any amendment to the \
registration statement should be made on Form 605 rather than Form 690. \
Amendments must be filed by the same method (paper or electronic) as the original \
form.'
    ),
    FilingForm(
        'F700',
        'Statement of Economic Interest',
        group='FINANCIAL DISCLOSURE',
        documentcloud_id='2792958-700-2015-12',
        description='Every public official who makes or participates in making \
governmental decisions is required to file.',
    ),
    FilingForm(
        'F900',
        'Campaign Disclosure Statement (Public employee retirement board candidate)',
        group='CAMPAIGN',
    ),
)


def get_filing_form(id):
    """
    Takes an id for a filing form and returns a FilingForm object.
    """
    return next((x for x in all_filing_forms if x.id == id.upper()), None)


# adding Filing Form Sections

form = get_filing_form('F400')
form.add_section(
    id='P1',
    title='Part 1, Slate Mailer Organization Information',
    start_page=2,
)
form.add_section(
    id='P2',
    title='Part 2, Treasurer And Other Principal Officers',
    start_page=2,
)
form.add_section(
    id='P3',
    title='Part 3, Individuals Who Authorize Contents Of Slate Mailers',
    start_page=3,
)
form.add_section(
    id='P4',
    title='Part 4, Is This Organization A "Committee" Pursuant To Government Code Section 82013?',
    start_page=3,
)
form.add_section(
    id='P5',
    title='Part 5, Verification',
    start_page=3,
)

form = get_filing_form('F401')
form.add_section(
    id='CVR',
    title='Cover Page',
    start_page=3,
    end_page=4,
)
form.add_section(
    id='A',
    db_value='F401A',
    title='Schedule A, Payments Received',
    start_page=5,
    end_page=7,
)
form.add_section(
    id='B',
    db_value='F401B',
    title='Schedule B, Payments Made',
    start_page=8,
    end_page=9,
)
form.add_section(
    id='B-1',
    db_value='F401B-1',
    title='Schedule B-1, Payments Made by Agent or Independent Contractor',
    start_page=10,
)
form.add_section(
    id='C',
    db_value='F401C',
    title='Schedule C, Persons Receiving $1,000 or More',
    start_page=11,
    end_page=12,
)
form.add_section(
    id='D',
    db_value='F401D',
    title='Schedule D, Candidates and Measures Not Listed on Schedule A',
    start_page=13,
    end_page=14,
)

form = get_filing_form('F402')
form.add_section(
    id='CVR',
    title='Cover Page',
    start_page=2,
)
form.add_section(
    id='VER',
    title='Verification',
    start_page=2,
)

form = get_filing_form('F410')
form.add_section(
    id='P1',
    title='Part 1, Committee Information',
    start_page=2,
)
form.add_section(
    id='P2',
    title='Part 2, Treasurer and Other Principal Officers',
    start_page=2,
)
form.add_section(
    id='P3',
    title='Part 3, Verification',
    start_page=2,
)
form.add_section(
    id='P4',
    title='Part 4, Type of Committee',
    start_page=2,
    end_page=3,
)

form = get_filing_form('F425')
form.add_section(
    id='P1',
    title='Part 1, Committee Information',
    start_page=1,
)
form.add_section(
    id='P2',
    title='Part 2, Period of No Activity',
    start_page=1,
)
form.add_section(
    id='P3',
    title='Part 3, Verification',
    start_page=1,
)

form = get_filing_form('F450')
form.add_section(
    id='CVR',
    title='Cover Page, Type of Recipient Committee',
    start_page=3
)
form.add_section(
    id='P1',
    title='Part 1, Payments Made',
    start_page=3
)
form.add_section(
    id='P2',
    title='Part 2, Type of Statement',
    start_page=3
)
form.add_section(
    id='P3',
    title='Part 3, Committee Information',
    start_page=3
)
form.add_section(
    id='P4',
    title='Part 4, Verification',
    start_page=3
)
form.add_section(
    id='SMRY',
    title='Summary Page',
    start_page=5
)
form.add_section(
    id='P5',
    db_value='F450P5',
    title='Part 5, Payments Made',
    start_page=6,
    end_page=7,
)

form = get_filing_form('F460')
form.add_section(
    id='CVR',
    title='Cover Page, Part 1',
    start_page=3,
    end_page=4,
    db_value='CVR',
)
form.add_section(
    id='CVR2',
    title='Cover Page, Part 2',
    start_page=2,
    db_value='CVR2',
)
form.add_section(
    id='SMRY',
    title='Summary Page',
    start_page=7,
    end_page=8,
    db_value='SMRY',
)
form.add_section(
    id='A',
    title='Schedule A, Monetary Contributions Received',
    start_page=9,
    end_page=11,
    db_value='A',
)
# this section is not in the sample form downloaded from the FPPC site
# but does appear in the filings
form.add_section(
    id='A-1',
    title='Schedule A-1, Contributions Transferred to Special Election Commitee',
    db_value='A-1',
)
form.add_section(
    id='B1',
    title='Schedule B, Part 1, Loans Received',
    start_page=12,
    end_page=13,
    db_value='B1',
)
form.add_section(
    id='B2',
    title='Schedule B, Part 2, Loan Guarantors',
    start_page=14,
    end_page=15,
    db_value='B2',
)
# this section appears in older versions of Form 460, but not in the current one
form.add_section(
    id='B3',
    title='Schedule B, Part 3, Outstanding Balance',
    db_value='B3',
)
form.add_section(
    id='C',
    title='Schedule C, Non-Monetary Contributions Received',
    start_page=16,
    end_page=17,
    db_value='C',
)
form.add_section(
    id='D',
    title='Schedule D, Summary of Expenditures Supporting / Opposing Other \
Candidates, Measures and Committees',
    start_page=18,
    end_page=20,
    db_value='D',
)
form.add_section(
    id='E',
    title='Schedule E, Payments Made',
    start_page=21,
    end_page=24,
    db_value='E',
)
form.add_section(
    id='F',
    title='Schedule F, Accrued Expenses (Unpaid Bills)',
    start_page=25,
    end_page=27,
    db_value='F',
)
form.add_section(
    id='G',
    title='Schedule G, Payments Made by an Agent or Independent Contractor \
(on Behalf of This Committee)',
    start_page=28,
    end_page=29,
    db_value='G',
)
form.add_section(
    id='H',
    title='Schedule H, Loans Made to Others',
    start_page=29,
    end_page=30,
    db_value='H',
)
# this section is not in the sample form downloaded from the FPPC site
# but does appear in the filings
form.add_section(
    id='H1',
    title='Schedule H, Part 1, Loans Made',
    db_value='H1',
)
# this section is not in the sample form downloaded from the FPPC site
# but does appear in the filings
form.add_section(
    id='H2',
    title='Schedule H, Part 2, Repayments Rcvd',
    db_value='H2',
)
# this section is not in the sample form downloaded from the FPPC site
# but does appear in the filings
form.add_section(
    id='H3',
    title='Schedule H, Part 3, Outstanding Loans',
    db_value='H3',
)
form.add_section(
    id='I',
    title='Schedule I, Miscellanous increases to cash',
    start_page=31,
    end_page=32,
    db_value='I',
)

form = get_filing_form('F461')
form.add_section(
    id='P1',
    title='Part 1, Name and Address of Filer',
    start_page=3,
    db_value='F461P1',
)
form.add_section(
    id='P2',
    title='Part 2, Nature and Interests of Filer',
    start_page=3,
    db_value='F461P2',
)
form.add_section(
    id='P3',
    title='Part 3, Summary',
    start_page=3,
    db_value='F461P3',
)
form.add_section(
    id='P4',
    title='Part 4, Verification',
    start_page=3,
    db_value='F461P4',
)
form.add_section(
    id='P5',
    title='Part 5, Contributions (Including Loans, Forgiveness of Loans, and Loan\
Guarantees) and Expenditures Made',
    start_page=5,
    end_page=6,
    db_value='F461P5',
)

form = get_filing_form('F465')
form.add_section(
    id='P1',
    title='Part 1, Committee/Filer Information',
    start_page=2,
    db_value='F465P1',
)
form.add_section(
    id='P2',
    title='Part 2, Name of Candidate or Measure Supported or Opposed',
    start_page=2,
    db_value='F465P2',
)
form.add_section(
    id='P3',
    title='Part 3, Independent Expenditures Made',
    start_page=2,
    db_value='F465P3',
)
form.add_section(
    id='P4',
    title='Part 4, Summary',
    start_page=4,
    db_value='F465P4',
)
form.add_section(
    id='P5',
    title='Part 5, Filing Officers',
    start_page=4,
    db_value='F465P5',
)
form.add_section(
    id='P6',
    title='Part 6, Verification',
    start_page=4,
    db_value='F465P6',
)

form = get_filing_form('F496')
form.add_section(
    id='P1',
    title='Part 1, List Only One Candidate or Ballot Measure',
    start_page=3,
    db_value='F496P1',
)
form.add_section(
    id='P2',
    title='Part 2, Independent Expenditures Made',
    start_page=3,
    db_value='F496P2',
)
form.add_section(
    id='P3',
    title='Part 3, Contributions > $100 Received',
    start_page=3,
    db_value='F496P3',
)

form = get_filing_form('F497')
form.add_section(
    id='P1',
    title='Part 1, Contributions Received',
    start_page=2,
    db_value='F497P1',
)
form.add_section(
    id='P2',
    title='Part 2, Contributions Made',
    start_page=4,
    db_value='F497P2',
)

form = get_filing_form('F498')
form.add_section(
    id='A',
    title='Part A, Late Payments Attributed To',
    db_value='F498-A',
)
form.add_section(
    id='R',
    title='Part R, Late Payments Received From',
    start_page=2,
    db_value='F498-R',
)

form = get_filing_form('F601')
form.add_section(
    id='P1',
    db_value='F601P1',
    title='Part 1, Individual Lobbyists',
    start_page=2,
)
form.add_section(
    id='P2A',
    db_value='F601P2A',
    title='Part 2, Section A, Lobbyist Employers',
    start_page=2,
    end_page=4,
)
form.add_section(
    id='P2B',
    db_value='F601P2B',
    title='Part 2, Section B, Subcontracted Clients',
    start_page=4,
)

form = get_filing_form('F615')
form.add_section(
    id='P1',
    db_value='F615P1',
    title='Part 1, Activity Expenses Paid, Incurred, Arranged or Provided by the Lobbyist',
    start_page=2,
    end_page=4,
)
form.add_section(
    id='P2',
    db_value='F615P2',
    title='Part 2, Campaign Contributions Made or Delivered',
    start_page=5,
)

form = get_filing_form('F625')
form.add_section(
    id='P1',
    db_value='F625P1',
    title='Part 1, Partners, Owners, Officers, and Employees',
    start_page=2,
)
form.add_section(
    id='P2',
    db_value='F625P2',
    title='Part 2, Payments Received in Connection with Lobbying Activity',
    start_page=4,
)
form.add_section(
    id='P3A',
    db_value='F625P3A',
    title='Part 3, Payments Made In Connection With Lobbying Activities, \
Section A, Activity Expenses',
    start_page=4,
)
form.add_section(
    id='P3B',
    db_value='F625P3B',
    title='Part 3, Payments Made In Connection With Lobbying Activities, \
Section B, Payments Made',
    start_page=8,
)
form.add_section(
    id='P3C',
    db_value='F625P3C',
    title='Part 3, Payments Made In Connection With Lobbying Activities, \
Section C, Summary of Payments',
    start_page=2,
)
form.add_section(
    id='P4B',
    db_value='F625P4B',
    title='Part 4, Campaign Contributions Made',
    start_page=2,
)

form = get_filing_form('F635')
form.add_section(
    id='P1',
    db_value='F635P1',
    title='Part 1, Legislative or State Agency Administrative Actions Actively \
Lobbied During the Period',
    start_page=2,
)
form.add_section(
    id='P2',
    db_value='F635P2',
    title='Part 2, Partners, Owners, and Employees whose "Lobbyist Reports" \
(Form 615) are Attached to this Report',
    start_page=4,
)
form.add_section(
    id='P3A',
    db_value='F635P3A',
    title='Part 3, Payments Made in Connection with Lobbying Activities, \
Section A, Payments To In-house Employee Lobbyists',
    start_page=4,
)
form.add_section(
    id='P3B',
    db_value='F635P3B',
    title='Part 3, Payments Made in Connection with Lobbying Activities, \
Section B, Payments To Lobbying Firms',
    start_page=4,
)
form.add_section(
    id='P3C',
    db_value='F635P3C',
    title='Part 3, Payments Made in Connection with Lobbying Activities, \
Section C, Activity Expenses',
    start_page=6,
)
form.add_section(
    id='P3D',
    db_value='F635P3D',
    title='Part 3, Payments Made in Connection with Lobbying Activities, \
Section D, Other Payments to Influence Legislative or Administrative Action',
    start_page=6,
)
form.add_section(
    id='P3E',
    db_value='F635P3E',
    title='Part 3, Payments Made in Connection with Lobbying Activities, \
Section E, Payments in Connection with Administrative Testimony in Ratemaking \
Proceedings Before The California Public Utilities Commission',
    start_page=6,
)
form.add_section(
    id='P4B',
    db_value='F635P4B',
    title='Part 4, Campaign Contributions Made',
    start_page=8,
)

form = get_filing_form('F645')
form.add_section(
    id='P1',
    db_value='F645P1',
    title='Part 1, Legislative or State Agency Administrative Actions Actively \
Lobbied during the Period',
    start_page=2,
)
form.add_section(
    id='P2A',
    db_value='F645P2A',
    title='Part 2, Payments Made this Period, Section A, Activity Expenses',
    start_page=4,
)
form.add_section(
    id='P2B',
    db_value='F645P2B',
    title='Part 2, Payments Made this Period, Section B, Other Payments to \
Influence Legislative or Administrative Action',
    start_page=4,
)
form.add_section(
    id='P2C',
    db_value='F645P2C',
    title='Part 2, Payments Made this Period, Section C, Payments in Connection \
with Administrative Testimony in Ratemaking Proceedings Before the California \
Public Utilities Commission',
    start_page=4,
)
form.add_section(
    id='P3B',
    db_value='F645P3B',
    title='Part 3, Campaign Contributions Made',
    start_page=4,
)
