#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Includes dicts of cannonical look-up / choice field values (e.g., 'codes' and 'types').

The keys of each look up dict are the valid values for the corresponding database
columns, and the values are the full descriptions. This allows for mapping of invalid
values observed in db columns to their valid equivalents in the _CHOICES attrs of our
models, like so:

    OFFICE_CD_CHOICES = (
        ('gov', look_ups.OFFICE_CODES['GOV']),
        ('GUV', look_ups.OFFICE_CODES['GOV']),
        # ...
    ),

DOCS is a dict of look-up set names to sets of DocumentCloud objects referencing
where the look-ups are defined. This allows for easy referencing to these document
pages in our models, like so:

    documentcloud_pages=look_ups.DOCS['office_codes'],

"""
from .documents import DocumentCloud

DOCS = {
    'entity_codes': [
        DocumentCloud(id='2712033', start_page=8, end_page=9),
        DocumentCloud(id='2712034', start_page=9, end_page=11),
    ],
    'expense_codes': [
        DocumentCloud(id='2712033', start_page=11),
        DocumentCloud(id='2712034', start_page=13, end_page=14),
    ],
    'office_codes': [
        DocumentCloud(id='2712033', start_page=10),
        DocumentCloud(id='2712034', start_page=12),
        DocumentCloud(id='2712032', start_page=2),
    ],
}

CAMPAIGN_ENTITY_CODES = {
    # for CVR records
    'CAO': 'Candidate/officeholder',
    'BMC': 'Ballot measure committee',
    'CTL': 'Controlled committee',
    'MDI': 'Major Donor/Ind Expenditure',
    'RCP': 'Recipient committee',
    'SMO': 'Slate-mailer organization',
    # for CVR2 records (includes CAO, CTL, RCP)
    'ATH': 'Authorizing individual',
    'ATR': 'Assistant treasurer',
    'BNM': 'Ballot measure\'s name/title',
    'COM': 'Committee',
    'OFF': 'Officer',
    'POF': 'Principal officer',
    'PRO': 'Proponent',
    'SPO': 'Sponsor',
    # for CVR3 records (includes CAO, OFF, PRO, SPO)
    'TRE': 'Treasurer',
    # for schedule records (includes COM and RCP)
    'IND': 'Individual',
    'OTH': 'Other',
    'PTY': 'Political Party',
    'SCC': 'Small Contributor Committee',
}

LOBBYING_ENTITY_CODES = {
    # for CVR records
    'FRM': 'Lobbying Firm',
    'IND': 'Person (spending > $5000)',
    'LBY': 'Lobbyist (an individual)',
    'LCO': 'Lobbying Coalition',
    'LEM': 'Lobbying Employer',
    # for CVR2 records (includes FRM)
    'AGY': 'State Agency',
    'EMP': 'Employer',
    'FRM': 'Lobbying Firm',
    'MBR': 'Member of Associaton',
    'OFF': 'Officer',
    'OWN': 'Owner',
    'PTN': 'Partner',
    'SCL': 'Subcontracted Client',
    # for schedule records (includes IND)
    'COM': 'Committee',
    'OTH': 'Other',
    'PTY': 'Political Party',
    'RCP': 'Recipient Committee',
    'SCC': 'Small Contributor Committee'
}

EXPENSE_CODES = {
    'CMP': 'campaign paraphernalia/miscellaneous',
    'CNS': 'campaign consultants',
    'CTB': 'contribution (if nonmonetary, explain)*',
    'CVC': 'civic donations',
    'FIL': 'candidate filing/ballot feeds',
    'FND': 'fundraising events',
    'IKD': 'In-kind contribution (nonmonetary)',
    'IND': 'independent expenditure supporting/opposing others (explain)*',
    'LEG': 'legal defense',
    'LIT': 'campaign literature and mailings',
    'LON': 'loan',
    'MBR': 'member communications',
    'MON': 'monetary contribution',
    'MTG': 'meetings and appearances',
    'OFC': 'office expenses',
    'PET': 'petition circulating',
    'PHO': 'phone banks',
    'POL': 'polling and survey research',
    'POS': 'postage, delivery and messenger services',
    'PRO': 'professional services (legal, accounting)',
    'PRT': 'print ads',
    'RAD': 'radio airtime and production costs',
    'RFD': 'returned contributions',
    'SAL': 'campaign workers salaries',
    'TEL': 'T.V. or cable airtime and production costs',
    'TRC': 'candidate travel, lodging and meals (explain)',
    'TRS': 'staff/spouse travel, lodging and meals (explain)',
    'TSF': 'transfer between committees of the same candidate/sponsor',
    'VOT': 'voter registration',
    'WEB': 'information technology costs (internet, e-mail)',
}

OFF_S_H_CODES = {
    'S': 'SOUGHT',
    'H': 'HELD',
}

OFFICE_CODES = {
    'APP': "State Appellate Court Justice",
    'ASM': 'State Assembly Person',
    'ASR': 'Assessor',
    'ATT': 'Attorney General',
    'BED': 'Board of Education',
    'BOE': 'Board of Equalization Member',
    'BSU': 'Board of Supervisors',
    'CAT': 'City Attorney',
    'CCB': 'Community College Board',
    'CCM': 'City Council Member',
    'CON': 'State Controller',
    'COU': 'County Counsel',
    'CSU': 'County Supervisor',
    'CTR': 'Local Controller',
    'DAT': 'District Attorney',
    'GOV': 'Governor',
    'INS': 'Insurance Commissioner',
    'LTG': 'Lieutenant Governor',
    'MAY': 'Mayor',
    'OTH': 'Other',
    'PDR': 'Public Defender',
    'PER': 'Public Employees Retirement System',
    'PLN': 'Planning Commissioner',
    'SCJ': 'Superior Court Judge',
    'SEN': 'State Senator',
    'SHC': 'Sheriff-Coroner',
    'SOS': 'Secretary of State',
    'SPM': 'Supreme Court Justice',
    'SUP': 'Superintendent of Public Instruction',
    'TRE': 'State Treasurer',
    'TRS': 'Local Treasurer',
}

JURIS_CODES = {
    'ASM': 'Assembly District',
    'BOE': 'Board of Equalization District',
    'CIT': 'City',
    'CTY': 'County',
    'LOC': 'Local',
    'OTH': 'Other',
    'SEN': 'Senate District',
    'STW': 'Statewide',
}

STMT_TYPES = {
    'PE': 'Pre-Election (F450, F460)',
    'QT': 'Quarterly Stmt (F450,F460)',
    'SA': 'Semi-annual (F450, F460)',
    'SE': 'Supplemental Pre-elect (F450, F460, F495)',
    'SY': 'Special Odd-Yr. Campaign (F450, F460)',
    'S1': 'Semi-Annual (Jan1-Jun30) (F425)',
    'S2': 'Semi-Annual (Jul1-Dec31) (F425)',
    'TS': 'Termination Statement (F450, F460)',
}

SUP_OPP_CODES = {
    'S': 'SUPPORT',
    'O': 'OPPOSITION',
}
