#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calaccess_raw.models.base import CalAccessForm, DocumentCloud

CALACCESS_FORMS = {
    'F400': CalAccessForm(
            'F400',
            'Statement of Organization (Slate Mailer Organization)',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781370-400-2016-01'),
        ),
    'F401': CalAccessForm(
            'F401',
            'Slate Mailer Organization Campaign Statement',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781366-401-2005-01'),
        ),
    'F402': CalAccessForm(
            'F402',
            'Statement of Termination (Slate Mailer Organization)',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781369-402-2005-01'),
        ),
    'F410': CalAccessForm(
            'F410',
            'Statement of Organization Recipient Committee',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781368-410-2016-01'),
        ),
    'F425': CalAccessForm(
            'F425',
            'Semi-Annual Statement of no Activity',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781365-425-2001-01'),
        ),
    'F450': CalAccessForm(
            'F450',
            'Recipient Committee Campaign Disclosure Statement - Short Form',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781364-450-2016-01'),
        ),
    'F460': CalAccessForm(
            'F460',
            'Recipient Committee Campaign Statement',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781363-460-2016-01'),
        ),
    'F461': CalAccessForm(
            'F461',
            'Independent Expenditure Committee & Major Donor Committee \
Campaign Statement',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781361-461-2016-01'),
        ),
    'F465': CalAccessForm(
            'F465',
            'Supplemental Independent Expenditure Report',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781358-465-2009-06'),
        ),
    'F470': CalAccessForm(
            'F470',
            'Officeholder and Candidate Campaign Statement, Short Form',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781357-470-2016-01'),
        ),
    'F470S': CalAccessForm(
            'F470S',
            'Officeholder and Candidate Campaign Statement (Supplement)',
            group='CAMPAIGN',
        ),
    'F495': CalAccessForm(
            'F495',
            'Supplemental Pre-Election Campaign Statement',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781356-495-2005-01'),
        ),
    'F496': CalAccessForm(
            'F496',
            'Late Independent Expenditure Report',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781355-496-2016-01'),
        ),
    'F497': CalAccessForm(
            'F497',
            'Late Contribution Report',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781353-497-2016-01'),
        ),
    'F498': CalAccessForm(
            'F498',
            'Slate Mailer Late Payment Report',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781352-498-2016-01'),
        ),
    'F501': CalAccessForm(
            'F501',
            'Candidate Intention Statement',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781351-501-2016-01'),
        ),
    'F502': CalAccessForm(
            'F502',
            'Campaign bank account statement',
            group='CAMPAIGN',
    ),
    'F511': CalAccessForm(
            'F511',
            'Paid Spokesperson Report',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781350-511-2015-01'),
        ),
    'E530': CalAccessForm(
            'E350',
            'Electronic Issue Advocacy Report',
            group='CAMPAIGN',
            documentcloud=DocumentCloud('2781349-E530-Instructions'),
        ),
    'F601': CalAccessForm(
            'F601',
            'Lobbying Firm Registration Statement',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781348-601-2014-10'),
        ),
    'F602': CalAccessForm(
            'F602',
            'Lobbying Firm Activity Authorization',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781347-602-1998-07'),
        ),
    'F603': CalAccessForm(
            'F603',
            'Lobbyist Employer or Lobbying Coalition Registration Statement',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781346-603-2014-10'),
        ),
    'F604': CalAccessForm(
            'F604',
            'Lobbyist Certification Statement',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781345-604-2014-10'),
        ),
    'F605': CalAccessForm(
            'F605',
            'Amendment to Registration, Lobbying Firm, Lobbyist Employer, \
Lobbying Coalition',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781344-605-2014-10'),
        ),
    'F606': CalAccessForm(
            'F606',
            'Notice of Termination',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781343-606-1997'),
        ),
    'F607': CalAccessForm(
            'F607',
            'Notice of Withdrawal',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781342-607-1997-08'),
        ),
    'F615': CalAccessForm(
            'F615',
            'Lobbyist Report',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781341-615-1990'),
        ),
    'F625': CalAccessForm(
            'F625',
            'Report of Lobbying Firm',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781340-625-1990'),
        ),
    'F630': CalAccessForm(
            'F630',
            'Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) ',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2782806-630-1990'),
        ),
    'F635': CalAccessForm(
            'F635',
            'Report of Lobbyist Employer or Report of Lobbying Coalition',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781339-635-1993'),
        ),
    'F635C': CalAccessForm(
            'F635C',
            'Payments Received by Lobbying Coalitions',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781338-635C-1990'),
        ),
    'F640': CalAccessForm(
            'F640',
            'Governmental Agencies Reporting (Attachment to Form 635 or Form 645)',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781337-640-1993'),
        ),
    'F645': CalAccessForm(
            'F645',
            'Report of Person Spending $5,000 or More',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781336-645-1993'),
        ),
    'F690': CalAccessForm(
            'F690',
            'Amendment to Lobbying Disclosure Report',
            group='LOBBYIST',
            documentcloud=DocumentCloud('2781335-690-1990'),
        ),
    'F900': CalAccessForm(
            'F900',
            'Public employee\'s retirement board, candidate campaign statement',
            group='CAMPAIGN',
        ),
}
