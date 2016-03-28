#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calaccess_raw.models.base import CalAccessForm

CALACCESS_FORMS = {
    'F400': CalAccessForm(
            'F400',
            'Statement of Organization (Slate Mailer Organization)',
            group='CAMPAIGN'
        ),
    'F401': CalAccessForm(
            'F401',
            'Slate Mailer Organization Campaign Statement',
            group='CAMPAIGN'
        ),
    'F402': CalAccessForm(
            'F402',
            'Statement of Termination (Slate Mailer Organization)',
            group='CAMPAIGN'
        ),
    'F410': CalAccessForm(
            'F410',
            'Statement of Organization Recipient Committee',
            group='CAMPAIGN'
        ),
    'F425': CalAccessForm(
            'F425',
            'Semi-Annual Statement of no Activity',
            group='CAMPAIGN'
        ),
    'F450': CalAccessForm(
            'F450',
            'Recipient Committee Campaign Disclosure Statement - Short Form',
            group='CAMPAIGN'
        ),
    'F460': CalAccessForm(
            'F460',
            'Recipient Committee Campaign Statement',
            group='CAMPAIGN'
        ),
    'F461': CalAccessForm(
            'F461',
            'Independent Expenditure Committee & Major Donor Committee \
Campaign Statement',
            group='CAMPAIGN'
        ),
    'F465': CalAccessForm(
            'F465',
            'Supplemental Independent Expenditure Report',
            group='CAMPAIGN'
        ),
    'F470': CalAccessForm(
            'F470',
            'Officeholder and Candidate Campaign Statement - \
Short Form 470S OfficerandCandidateCampaignStatement(Supplement)',
            group='CAMPAIGN'
        ),
    'F495': CalAccessForm(
            'F495',
            'Supplemental Pre-Election Campaign Statement',
            group='CAMPAIGN'
        ),
    'F496': CalAccessForm(
            'F496',
            'Late Independent Expenditure Report',
            group='CAMPAIGN'
        ),
    'F497': CalAccessForm(
            'F497',
            'Late Contribution Report',
            group='CAMPAIGN'
        ),
    'F498': CalAccessForm(
            'F498',
            'Slate Mailer Late Payment Report',
            group='CAMPAIGN'
        ),
    'F601': CalAccessForm(
            'F601',
            'Lobbying Firm Registration Statement',
            group='LOBBYIST'
        ),
    'F602': CalAccessForm(
            'F602',
            'Lobbying Firm Activity Authorization',
            group='LOBBYIST'
        ),
    'F603': CalAccessForm(
            'F603',
            'Lobbyist Employer or Lobbying Coalition Registration Statement',
            group='LOBBYIST'
        ),
    'F604': CalAccessForm(
            'F604',
            'Lobbyist Certification Statement',
            group='LOBBYIST'
        ),
    'F605': CalAccessForm(
            'F605',
            'Amendment to Registration, Lobbying Firm, Lobbyist Employer, \
Lobbying Coalition',
            group='LOBBYIST'
        ),
    'F606': CalAccessForm(
            'F606',
            'Notice of Termination',
            group='LOBBYIST'
        ),
    'F607': CalAccessForm(
            'F607',
            'Notice of Withdrawal',
            group='LOBBYIST'
        ),
    'F615': CalAccessForm(
            'F615',
            'Lobbyist Report',
            group='LOBBYIST'
        ),
    'F625': CalAccessForm(
            'F625',
            'Report of Lobbying Firm',
            group='LOBBYIST'
        ),
    'F630': CalAccessForm(
            'F630',
            'Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) ',
            group='LOBBYIST'
        ),
    'F635': CalAccessForm(
            'F635',
            'Report of Lobbyist Employer or Report of Lobbying Coalition',
            group='LOBBYIST'
        ),
    'F635C': CalAccessForm(
            'F635C',
            'Payments Received by Lobbying Coalitions',
            group='LOBBYIST'
        ),
    'F640': CalAccessForm(
            'F640',
            'Governmental Agencies Reporting (Attachment to Form 635 or Form 645) ',
            group='LOBBYIST'
        ),
    'F645': CalAccessForm(
            'F645',
            'Report of Person Spending $5,000 or More',
            group='LOBBYIST'
        ),
    'F690': CalAccessForm(
            'F690',
            'Amendment to Lobbying Disclosure Report',
            group='LOBBYIST'
        ),
}
