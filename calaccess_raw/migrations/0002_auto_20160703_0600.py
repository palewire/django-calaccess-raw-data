# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 06:00
from __future__ import unicode_literals

import calaccess_raw.annotations
import calaccess_raw.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_raw', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acronymscd',
            options={'ordering': ('acronym',)},
        ),
        migrations.AlterModelOptions(
            name='addresscd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='ballotmeasurescd',
            options={'ordering': ('-election_date', 'measure_no', 'measure_short_name', 'measure_name')},
        ),
        migrations.AlterModelOptions(
            name='cvr2campaigndisclosurecd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cvr2lobbydisclosurecd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cvr2registrationcd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cvr2socd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cvr3verificationinfocd',
            options={'ordering': ('-sig_date',)},
        ),
        migrations.AlterModelOptions(
            name='cvrcampaigndisclosurecd',
            options={'ordering': ('-rpt_date',)},
        ),
        migrations.AlterModelOptions(
            name='cvre530cd',
            options={'ordering': ('-pmnt_dt',)},
        ),
        migrations.AlterModelOptions(
            name='cvrf470cd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cvrlobbydisclosurecd',
            options={'ordering': ('-rpt_date',)},
        ),
        migrations.AlterModelOptions(
            name='cvrregistrationcd',
            options={'ordering': ('-rpt_date',)},
        ),
        migrations.AlterModelOptions(
            name='cvrsocd',
            options={'ordering': ('-rpt_date',)},
        ),
        migrations.AlterModelOptions(
            name='debtcd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='efsfilinglogcd',
            options={'ordering': ('-filing_date',)},
        ),
        migrations.AlterModelOptions(
            name='expncd',
            options={'ordering': ('-expn_date',)},
        ),
        migrations.AlterModelOptions(
            name='f495p2cd',
            options={'ordering': ('-elect_date',)},
        ),
        migrations.AlterModelOptions(
            name='f501502cd',
            options={'ordering': ('-rpt_date',)},
        ),
        migrations.AlterModelOptions(
            name='f690p2cd',
            options={'ordering': ('-exec_date',)},
        ),
        migrations.AlterModelOptions(
            name='fileracronymscd',
            options={'ordering': ('acronym',)},
        ),
        migrations.AlterModelOptions(
            name='fileraddresscd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='filerethicsclasscd',
            options={'ordering': ('-ethics_date',)},
        ),
        migrations.AlterModelOptions(
            name='filerfilingscd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='filerinterestscd',
            options={'ordering': ('-effect_date',)},
        ),
        migrations.AlterModelOptions(
            name='filerlinkscd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='filernamecd',
            options={'ordering': ('naml', 'namf')},
        ),
        migrations.AlterModelOptions(
            name='filerscd',
            options={'ordering': ('-filer_id',)},
        ),
        migrations.AlterModelOptions(
            name='filerstatustypescd',
            options={'ordering': ('status_type',)},
        ),
        migrations.AlterModelOptions(
            name='filertofilertypecd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='filertypeperiodscd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='filertypescd',
            options={'ordering': ('filer_type',)},
        ),
        migrations.AlterModelOptions(
            name='filerxrefcd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='filingperiodcd',
            options={'ordering': ('-end_date',)},
        ),
        migrations.AlterModelOptions(
            name='filingscd',
            options={'ordering': ('-filing_id',)},
        ),
        migrations.AlterModelOptions(
            name='grouptypescd',
            options={'ordering': ('grp_id',)},
        ),
        migrations.AlterModelOptions(
            name='hdrcd',
            options={'ordering': ('-filing_id', '-amend_id')},
        ),
        migrations.AlterModelOptions(
            name='headercd',
            options={'ordering': ('form_id', 'line_number')},
        ),
        migrations.AlterModelOptions(
            name='imagelinkscd',
            options={'ordering': ('-img_dt',)},
        ),
        migrations.AlterModelOptions(
            name='lattcd',
            options={'ordering': ('-pmt_date',)},
        ),
        migrations.AlterModelOptions(
            name='lccmcd',
            options={'ordering': ('-ctrib_date',)},
        ),
        migrations.AlterModelOptions(
            name='legislativesessionscd',
            options={'ordering': ('-begin_date',)},
        ),
        migrations.AlterModelOptions(
            name='lempcd',
            options={'ordering': ('-eff_date',)},
        ),
        migrations.AlterModelOptions(
            name='lexpcd',
            options={'ordering': ('-expn_date',)},
        ),
        migrations.AlterModelOptions(
            name='loancd',
            options={'ordering': ('-loan_date1',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyamendmentscd',
            options={'ordering': ('-exec_date',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyingchglogcd',
            options={'ordering': ('-log_dt',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistcontributions1cd',
            options={'ordering': ('-filing_period_start_dt',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistcontributions2cd',
            options={'ordering': ('-filing_period_start_dt',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistcontributions3cd',
            options={'ordering': ('-filing_period_start_dt',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistemplobbyist1cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistemplobbyist2cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistemployer1cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistemployer2cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistemployer3cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistemployerfirms1cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistemployerfirms2cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistemployerhistorycd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lobbyistfirm1cd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lobbyistfirm2cd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lobbyistfirm3cd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lobbyistfirmemployer1cd',
            options={'ordering': ('-rpt_start',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistfirmemployer2cd',
            options={'ordering': ('-rpt_start',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistfirmhistorycd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lobbyistfirmlobbyist1cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lobbyistfirmlobbyist2cd',
            options={'ordering': ('-session_id',)},
        ),
        migrations.AlterModelOptions(
            name='lookupcodescd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='lothcd',
            options={'ordering': ('-pmt_date',)},
        ),
        migrations.AlterModelOptions(
            name='lpaycd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='namescd',
            options={'ordering': ('naml', 'namf')},
        ),
        migrations.AlterModelOptions(
            name='rcptcd',
            options={'ordering': ('-rcpt_date',)},
        ),
        migrations.AlterModelOptions(
            name='receivedfilingscd',
            options={'ordering': ('-received_date',)},
        ),
        migrations.AlterModelOptions(
            name='reportscd',
            options={'ordering': ('rpt_name',)},
        ),
        migrations.AlterModelOptions(
            name='s401cd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='s496cd',
            options={'ordering': ('-exp_date',)},
        ),
        migrations.AlterModelOptions(
            name='s497cd',
            options={'ordering': ('-ctrib_date',)},
        ),
        migrations.AlterModelOptions(
            name='s498cd',
            options={'ordering': ('-date_rcvd',)},
        ),
        migrations.AlterModelOptions(
            name='smrycd',
            options={'ordering': ('filing_id', '-amend_id', 'form_type', 'line_item')},
        ),
        migrations.AlterModelOptions(
            name='spltcd',
            options={},
        ),
        migrations.AlterModelOptions(
            name='textmemocd',
            options={},
        ),
        migrations.AlterField(
            model_name='cvre530cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='filerfilingscd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='filernamecd',
            name='effect_dt',
            field=calaccess_raw.fields.DateField(db_column='EFFECT_DT', help_text='effective date for status', null=True),
        ),
        migrations.AlterField(
            model_name='filernamecd',
            name='filer_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILER_ID', db_index=True, help_text="filer's unique identification number", null=True, verbose_name='filer ID'),
        ),
        migrations.AlterField(
            model_name='filernamecd',
            name='xref_filer_id',
            field=calaccess_raw.fields.CharField(db_column='XREF_FILER_ID', db_index=True, help_text='alternative filer ID found on many forms', max_length=15, verbose_name='crossreference filer ID'),
        ),
        migrations.AlterField(
            model_name='filingscd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='hdrcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='receivedfilingscd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(blank=True, db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', null=True, verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='smrycd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='spltcd',
            name='amend_id',
            field=calaccess_raw.fields.IntegerField(db_column='AMEND_ID', db_index=True, help_text='amendment identification number. A number of 0 is the original filing and 1 to 999 amendments.', verbose_name='amendment ID'),
        ),
        migrations.AlterField(
            model_name='spltcd',
            name='elec_amount',
            field=calaccess_raw.fields.DecimalField(db_column='ELEC_AMOUNT', decimal_places=2, help_text='per election to date amount', max_digits=16, verbose_name='election amount'),
        ),
        migrations.AlterField(
            model_name='spltcd',
            name='elec_code',
            field=calaccess_raw.fields.CharField(blank=True, choices=[('P', 'Primary'), ('G', 'General'), ('S', 'Special'), ('R', 'Runoff'), ('g', 'General'), ('p', 'primary'), ('C', 'Unknown'), ('D', 'Unknown'), ('F', 'Unknown'), ('M', 'Unknown'), ('N', 'Unknown'), ('X', 'Unknown'), ('O', 'Unknown'), ('0', 'Unknown'), ('1', 'Unknown'), ('2', 'Unknown')], db_column='ELEC_CODE', documentcloud_pages=[calaccess_raw.annotations.DocumentCloud(id='2712034-Cal-Format-201', start_page=18)], help_text='per election to date code', max_length=2, verbose_name='election code'),
        ),
        migrations.AlterField(
            model_name='spltcd',
            name='elec_date',
            field=calaccess_raw.fields.DateField(db_column='ELEC_DATE', help_text='date of election', null=True),
        ),
        migrations.AlterField(
            model_name='spltcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='spltcd',
            name='line_item',
            field=calaccess_raw.fields.IntegerField(db_column='LINE_ITEM', db_index=True, help_text='line item number of this record'),
        ),
        migrations.AlterField(
            model_name='spltcd',
            name='ptran_id',
            field=calaccess_raw.fields.CharField(blank=True, db_column='PTRAN_ID', help_text='parent transaction ID', max_length=32, verbose_name='parent transaction ID'),
        ),
        migrations.AlterField(
            model_name='textmemocd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
    ]