#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calaccess_raw.models.base import CalAccessForm

CALACCESS_FORMS = {
    '400': CalAccessForm(
            '400',
            'Statement of Organization (Slate Mailer Organization)',
            group='CAMPAIGN'
        ),
    '401': CalAccessForm(
            '401',
            'Slate Mailer Organization Campaign Statement',
            group='CAMPAIGN'
        ),
    '402': CalAccessForm(
            '402',
            'Statement of Termination (Slate Mailer Organization)',
            group='CAMPAIGN'
        ),
    '410': CalAccessForm(
            '410',
            'Statement of Organization Recipient Committee',
            group='CAMPAIGN'
        ),
    '425': CalAccessForm(
            '425',
            'Semi-Annual Statement of no Activity',
            group='CAMPAIGN'
        ),
    '450': CalAccessForm(
            '450',
            'Recipient Committee Campaign Disclosure Statement - Short Form',
            group='CAMPAIGN'
        ),
    '460': CalAccessForm(
            '460',
            'Recipient Committee Campaign Statement',
            group='CAMPAIGN'
        ),
    '461': CalAccessForm(
            '461',
            'Independent Expenditure Committee & Major Donor Committee \
Campaign Statement',
            group='CAMPAIGN'
        ),
    '465': CalAccessForm(
            '465',
            'Supplemental Independent Expenditure Report',
            group='CAMPAIGN'
        ),
    '470': CalAccessForm(
            '470',
            'Officeholder and Candidate Campaign Statement - \
Short Form 470S OfficerandCandidateCampaignStatement(Supplement)',
            group='CAMPAIGN'
        ),
    '495': CalAccessForm(
            '495',
            'Supplemental Pre-Election Campaign Statement',
            group='CAMPAIGN'
        ),
    '496': CalAccessForm(
            '496',
            'Late Independent Expenditure Report',
            group='CAMPAIGN'
        ),
    '497': CalAccessForm(
            '497',
            'Late Contribution Report',
            group='CAMPAIGN'
        ),
    '498': CalAccessForm(
            '498',
            'Slate Mailer Late Payment Report',
            group='CAMPAIGN'
        ),
    '601': CalAccessForm(
            '601',
            'Lobbying Firm Registration Statement',
            group='LOBBYIST'
        ),
    '602': CalAccessForm(
            '602',
            'Lobbying Firm Activity Authorization',
            group='LOBBYIST'
        ),
    '603': CalAccessForm(
            '603',
            'Lobbyist Employer or Lobbying Coalition Registration Statement',
            group='LOBBYIST'
        ),
    '604': CalAccessForm(
            '604',
            'Lobbyist Certification Statement',
            group='LOBBYIST'
        ),
    '605': CalAccessForm(
            '605',
            'Amendment to Registration, Lobbying Firm, Lobbyist Employer, \
Lobbying Coalition',
            group='LOBBYIST'
        ),
    '606': CalAccessForm(
            '606',
            'Notice of Termination',
            group='LOBBYIST'
        ),
    '607': CalAccessForm(
            '607',
            'Notice of Withdrawal',
            group='LOBBYIST'
        ),
    '615': CalAccessForm(
            '615',
            'Lobbyist Report',
            group='LOBBYIST'
        ),
    '625': CalAccessForm(
            '625',
            'Report of Lobbying Firm',
            group='LOBBYIST'
        ),
    '630': CalAccessForm(
            '630',
            'Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) ',
            group='LOBBYIST'
        ),
    '635': CalAccessForm(
            '635',
            'Report of Lobbyist Employer or Report of Lobbying Coalition',
            group='LOBBYIST'
        ),
    '635C': CalAccessForm(
            '635C',
            'Payments Received by Lobbying Coalitions',
            group='LOBBYIST'
        ),
    '640': CalAccessForm(
            '640',
            'Governmental Agencies Reporting (Attachment to Form 635 or Form 645) ',
            group='LOBBYIST'
        ),
    '645': CalAccessForm(
            '645',
            'Report of Person Spending $5,000 or More',
            group='LOBBYIST'
        ),
    '690': CalAccessForm(
            '690',
            'Amendment to Lobbying Disclosure Report',
            group='LOBBYIST'
        ),
}
