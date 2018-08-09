#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All the CAL-ACCESS forms cataloged by our research.
"""
import os
import csv
from calaccess_raw.annotations.forms import FilingForm


def load_filing_forms():
    """
    Load all the FilingForm objects from the source CSV.
    """
    this_dir = os.path.dirname(__file__)
    file_path = os.path.join(this_dir, 'forms.csv')
    file_obj = open(file_path, 'r')
    file_reader = csv.DictReader(file_obj)
    return [FilingForm(**row) for row in file_reader]


all_filing_forms = load_filing_forms()


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
