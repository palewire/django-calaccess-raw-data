# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-23 22:19
from __future__ import unicode_literals

import calaccess_raw.annotations
import calaccess_raw.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("calaccess_raw", "0012_auto_20161123_2217"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expncd",
            name="expn_code",
            field=calaccess_raw.fields.CharField(
                blank=True,
                choices=[
                    (b"CMP", b"campaign paraphernalia/miscellaneous"),
                    (b"CNS", b"campaign consultants"),
                    (b"CTB", b"contribution (if nonmonetary, explain)*"),
                    (b"CVC", b"civic donations"),
                    (b"FIL", b"candidate filing/ballot feeds"),
                    (b"FND", b"fundraising events"),
                    (b"IKD", b"In-kind contribution (nonmonetary)"),
                    (
                        b"IND",
                        b"independent expenditure supporting/opposing others (explain)*",
                    ),
                    (b"LEG", b"legal defense"),
                    (b"LIT", b"campaign literature and mailings"),
                    (b"LON", b"loan"),
                    (b"MBR", b"member communications"),
                    (b"MON", b"monetary contribution"),
                    (b"MTG", b"meetings and appearances"),
                    (b"OFC", b"office expenses"),
                    (b"PET", b"petition circulating"),
                    (b"PHO", b"phone banks"),
                    (b"POL", b"polling and survey research"),
                    (b"POS", b"postage, delivery and messenger services"),
                    (b"PRO", b"professional services (legal, accounting)"),
                    (b"PRT", b"print ads"),
                    (b"RAD", b"radio airtime and production costs"),
                    (b"RFD", b"returned contributions"),
                    (b"SAL", b"campaign workers salaries"),
                    (b"TEL", b"T.V. or cable airtime and production costs"),
                    (b"TRC", b"candidate travel, lodging and meals (explain)"),
                    (b"TRS", b"staff/spouse travel, lodging and meals (explain)"),
                    (
                        b"TSF",
                        b"transfer between committees of the same candidate/sponsor",
                    ),
                    (b"VOT", b"voter registration"),
                    (b"WEB", b"information technology costs (internet, e-mail)"),
                    ("ctb", b"contribution (if nonmonetary, explain)*"),
                    ("ikd", b"In-kind contribution (nonmonetary)"),
                    ("Mon", b"monetary contribution"),
                    ("ofc", b"office expenses"),
                    ("OFc", b"office expenses"),
                    ("Ofc", b"office expenses"),
                    ("", "Unknown"),
                    ("*", "Unknown"),
                    ("0", "Unknown"),
                    ("001", "Unknown"),
                    ("011", "Unknown"),
                    ("200", "Unknown"),
                    ("401", "Unknown"),
                    ("ADV", "Unknown"),
                    ("ANN", "Unknown"),
                    ("APR", "Unknown"),
                    ("AUG", "Unknown"),
                    ("AUT", "Unknown"),
                    ("Ban", "Unknown"),
                    ("BAN", "Unknown"),
                    ("BOO", "Unknown"),
                    ("BOX", "Unknown"),
                    ("C", "Unknown"),
                    ("CAT", "Unknown"),
                    ("CC", "Unknown"),
                    ("CHE", "Unknown"),
                    ("CIV", "Unknown"),
                    ("CNT", "Unknown"),
                    ("CON", "Unknown"),
                    ("COP", "Unknown"),
                    ("CRE", "Unknown"),
                    ("CSN", "Unknown"),
                    ("CT", "Unknown"),
                    (",CT", "Unknown"),
                    (".CT", "Unknown"),
                    ("CTN", "Unknown"),
                    ("CVD", "Unknown"),
                    ("DAT", "Unknown"),
                    ("DEC", "Unknown"),
                    ("Dem", "Unknown"),
                    ("DIN", "Unknown"),
                    ("Don", "Unknown"),
                    ("DON", "Unknown"),
                    ("Ear", "Unknown"),
                    ("EIM", "Unknown"),
                    ("EMP", "Unknown"),
                    ("F", "Unknown"),
                    ("FAX", "Unknown"),
                    ("FDN", "Unknown"),
                    ("FED", "Unknown"),
                    ("FEE", "Unknown"),
                    ("FIN", "Unknown"),
                    ("Fun", "Unknown"),
                    ("FUN", "Unknown"),
                    ("G", "Unknown"),
                    ("GEN", "Unknown"),
                    ("GGG", "Unknown"),
                    ("GOT", "Unknown"),
                    ("IEs", "Unknown"),
                    ("IN-", "Unknown"),
                    ("Ina", "Unknown"),
                    ("INK", "Unknown"),
                    ("INS", "Unknown"),
                    ("ITE", "Unknown"),
                    ("JAN", "Unknown"),
                    ("JUL", "Unknown"),
                    ("JUN", "Unknown"),
                    ("KIC", "Unknown"),
                    ("L", "Unknown"),
                    ("LEV", "Unknown"),
                    ("Lit", "Unknown"),
                    ("LN#", "Unknown"),
                    ("LOG", "Unknown"),
                    ("M", "Unknown"),
                    ("MAI", "Unknown"),
                    ("Mar", "Unknown"),
                    ("MAR", "Unknown"),
                    ("MAY", "Unknown"),
                    ("MED", "Unknown"),
                    ("MEE", "Unknown"),
                    ("MGT", "Unknown"),
                    ("Mis", "Unknown"),
                    ("MRB", "Unknown"),
                    ("NGP", "Unknown"),
                    ("NON", "Unknown"),
                    ("NOT", "Unknown"),
                    ("NOV", "Unknown"),
                    ("O", "Unknown"),
                    ("OCT", "Unknown"),
                    (".OF", "Unknown"),
                    ("OFF", "Unknown"),
                    ("OPE", "Unknown"),
                    ("OTH", "Unknown"),
                    ("P", "Unknown"),
                    ("Pac", "Unknown"),
                    ("PAI", "Unknown"),
                    ("PAR", "Unknown"),
                    ("PAY", "Unknown"),
                    ("PEN", "Unknown"),
                    ("PMT", "Unknown"),
                    (".PO", "Unknown"),
                    ("Pos", "Unknown"),
                    ("PRE", "Unknown"),
                    ("PRI", "Unknown"),
                    ("PRP", "Unknown"),
                    ("R", "Unknown"),
                    (".Re", "Unknown"),
                    (".RE", "Unknown"),
                    ("REF", "Unknown"),
                    ("REI", "Unknown"),
                    ("RFP", "Unknown"),
                    ("S", "Unknown"),
                    ("S-A", "Unknown"),
                    ("SA", "Unknown"),
                    ("Sal", "Unknown"),
                    ("S C", "Unknown"),
                    ("S.C", "Unknown"),
                    ("SCU", "Unknown"),
                    ("SEE", "Unknown"),
                    ("SEN", "Unknown"),
                    ("SEP", "Unknown"),
                    ("S.M.", "Unknown"),
                    ("SOF", "Unknown"),
                    ("SWI", "Unknown"),
                    ("T", "Unknown"),
                    ("TAX", "Unknown"),
                    ("TB", "Unknown"),
                    ("TB,", "Unknown"),
                    ("TIC", "Unknown"),
                    ("Tor", "Unknown"),
                    ("TRA", "Unknown"),
                    ("TRF", "Unknown"),
                    ("TRV", "Unknown"),
                    ("UN", "Unknown"),
                    ("UTI", "Unknown"),
                    ("V", "Unknown"),
                    ("VEN", "Unknown"),
                    ("-VO", "Unknown"),
                    ("VOI", "Unknown"),
                    ("VOY", "Unknown"),
                    ("WI", "Unknown"),
                    ("x", "Unknown"),
                    ("X", "Unknown"),
                    ("S-6", "Unknown"),
                    ("S.M", "Unknown"),
                    ("S-4", "Unknown"),
                    ("SA:", "Unknown"),
                    ("100", "Unknown"),
                    ("RFN", "Unknown"),
                    ("REN", "Unknown"),
                    ("003", "Unknown"),
                    ("S-1", "Unknown"),
                    ("08", "Unknown"),
                ],
                db_column="EXPN_CODE",
                documentcloud_pages=[
                    calaccess_raw.annotations.DocumentCloud(
                        id=b"2712033-Cal-Format-1-05-02", start_page=11
                    ),
                    calaccess_raw.annotations.DocumentCloud(
                        end_page=14, id=b"2712034-Cal-Format-201", start_page=13
                    ),
                ],
                help_text="The type of expenditure",
                max_length=3,
                verbose_name="expense code",
            ),
        ),
    ]
