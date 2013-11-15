#!/usr/bin/env python
from env_settings import clean_data_dir, data_root_dir, db_name, db_password, db_user_name
import MySQLdb

conn = MySQLdb.Connection(db=db_name, host='localhost', user=db_user_name, passwd=db_password, local_infile=1)
mysql = conn.cursor()


##CVR_CAMPAIGN_DISCLOSURE_CD
mysql.execute('DELETE FROM CVR_CAMPAIGN_DISCLOSURE_CD;')
cvr_path = clean_data_dir + 'cvr_campaign_disclosure_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % cvr_path
mysql.execute( first_line + '''
INTO TABLE CVR_CAMPAIGN_DISCLOSURE_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILING_ID`,
`AMEND_ID`,
`REC_TYPE`,
`FORM_TYPE`,
`FILER_ID`,
`ENTITY_CD`,
`FILER_NAML`,
`FILER_NAMF`,
`FILER_NAMT`,
`FILER_NAMS`,
`REPORT_NUM`,
@`RPT_DATE`,
`STMT_TYPE`,
`LATE_RPTNO`,
@`FROM_DATE`,
@`THRU_DATE`,
@`ELECT_DATE`,
`FILER_CITY`,
`FILER_ST`,
`FILER_ZIP4`,
`FILER_PHON`,
`FILER_FAX`,
`FILE_EMAIL`,
`MAIL_CITY`,
`MAIL_ST`,
`MAIL_ZIP4`,
`TRES_NAML`,
`TRES_NAMF`,
`TRES_NAMT`,
`TRES_NAMS`,
`TRES_CITY`,
`TRES_ST`,
`TRES_ZIP4`,
`TRES_PHON`,
`TRES_FAX`,
`TRES_EMAIL`,
`CMTTE_TYPE`,
`CONTROL_YN`,
`SPONSOR_YN`,
`PRIMFRM_YN`,
`BRDBASE_YN`,
`AMENDEXP_1`,
`AMENDEXP_2`,
`AMENDEXP_3`,
`RPT_ATT_CB`,
`CMTTE_ID`,
`REPORTNAME`,
@`RPTFROMDT`,
@`RPTTHRUDT`,
`EMPLBUS_CB`,
`BUS_NAME`,
`BUS_CITY`,
`BUS_ST`,
`BUS_ZIP4`,
`BUS_INTER`,
`BUSACT_CB`,
`BUSACTVITY`,
`ASSOC_CB`,
`ASSOC_INT`,
`OTHER_CB`,
`OTHER_INT`,
`CAND_NAML`,
`CAND_NAMF`,
`CAND_NAMT`,
`CAND_NAMS`,
`CAND_CITY`,
`CAND_ST`,
`CAND_ZIP4`,
`CAND_PHON`,
`CAND_FAX`,
`CAND_EMAIL`,
`BAL_NAME`,
`BAL_NUM`,
`BAL_JURIS`,
`OFFICE_CD`,
`OFFIC_DSCR`,
`JURIS_CD`,
`JURIS_DSCR`,
`DIST_NO`,
`OFF_S_H_CD`,
`SUP_OPP_CD`,
`EMPLOYER`,
`OCCUPATION`,
@`SELFEMP_CB`,
`BAL_ID`,
`CAND_ID`
)
SET
`ELECT_DATE` = str_to_Date(@`ELECT_DATE`, '%m/%d/%Y %r'),
`FROM_DATE` = str_to_Date(@`FROM_DATE`, '%m/%d/%Y %r'),
`RPT_DATE` = str_to_Date(@`RPT_DATE`, '%m/%d/%Y %r'),
`RPTFROMDT` = str_to_Date(@`RPTFROMDT`, '%m/%d/%Y %r'),
`RPTTHRUDT` = str_to_Date(@`RPTTHRUDT`, '%m/%d/%Y %r'),
`SELFEMP_CB` = str_to_Date(@`SELFEMP_CB`, '%m/%d/%Y %r'),
`THRU_DATE` = str_to_Date(@`THRU_DATE`, '%m/%d/%Y %r');
''') 
print 'loaded up CVR_CAMPAIGN_DISCLOSURE_CD'

cvr_lobby_path = clean_data_dir + 'cvr_lobby_disclosure_cd.csv'
## CVR LOBBY DISCLOSURE
mysql.execute('DELETE FROM CVR_LOBBY_DISCLOSURE_CD;')
first_line = "LOAD DATA LOCAL INFILE '%s'" % cvr_lobby_path
mysql.execute(first_line + '''
INTO TABLE CVR_LOBBY_DISCLOSURE_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILING_ID`,
`AMEND_ID`,
`REC_TYPE`,
`FORM_TYPE`,
`SENDER_ID`,
`FILER_ID`,
`ENTITY_CD`,
`FILER_NAML`,
`FILER_NAMF`,
`FILER_NAMT`,
`FILER_NAMS`,
`REPORT_NUM`,
@`RPT_DATE`,
@`FROM_DATE`,
@`THRU_DATE`,
@`CUM_BEG_DT`,
`FIRM_ID`,
`FIRM_NAME`,
`FIRM_CITY`,
`FIRM_ST`,
`FIRM_ZIP4`,
`FIRM_PHON`,
`MAIL_CITY`,
`MAIL_ST`,
`MAIL_ZIP4`,
`MAIL_PHON`,
@`SIG_DATE`,
`SIG_LOC`,
`SIG_NAML`,
`SIG_NAMF`,
`SIG_NAMT`,
`SIG_NAMS`,
`PRN_NAML`,
`PRN_NAMF`,
`PRN_NAMT`,
`PRN_NAMS`,
`SIG_TITLE`,
`NOPART1_CB`,
`NOPART2_CB`,
`PART1_1_CB`,
`PART1_2_CB`,
`CTRIB_N_CB`,
`CTRIB_Y_CB`,
`LBY_ACTVTY`,
`LOBBY_N_CB`,
`LOBBY_Y_CB`,
`MAJOR_NAML`,
`MAJOR_NAMF`,
`MAJOR_NAMT`,
`MAJOR_NAMS`,
`RCPCMTE_NM`,
`RCPCMTE_ID`
)
SET
`CUM_BEG_DT` = str_to_Date(@`CUM_BEG_DT`, '%m/%d/%Y %r'),
`FROM_DATE` = str_to_Date(@`FROM_DATE`, '%m/%d/%Y %r'),
`RPT_DATE` = str_to_Date(@`RPT_DATE`, '%m/%d/%Y %r'),
`SIG_DATE` = str_to_Date(@`SIG_DATE`, '%m/%d/%Y %r'),
`THRU_DATE` = str_to_Date(@`THRU_DATE`, '%m/%d/%Y %r')
''') 


## CVR REGISTRATION
mysql.execute('DELETE FROM CVR_REGISTRATION_CD;')
csv_registration = clean_data_dir + 'cvr_registration_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % csv_registration
mysql.execute(first_line + '''
INTO TABLE CVR_REGISTRATION_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILING_ID`,
`AMEND_ID`,
`REC_TYPE`,
`FORM_TYPE`,
`SENDER_ID`,
`FILER_ID`,
`ENTITY_CD`,
`FILER_NAML`,
`FILER_NAMF`,
`FILER_NAMT`,
`FILER_NAMS`,
`REPORT_NUM`,
@`RPT_DATE`,
`LS_BEG_YR`,
`LS_END_YR`,
@`QUAL_DATE`,
@`EFF_DATE`,
`BUS_CITY`,
`BUS_ST`,
`BUS_ZIP4`,
`BUS_PHON`,
`BUS_FAX`,
`BUS_EMAIL`,
`MAIL_CITY`,
`MAIL_ST`,
`MAIL_ZIP4`,
`MAIL_PHON`,
@`SIG_DATE`,
`SIG_LOC`,
`SIG_NAML`,
`SIG_NAMF`,
`SIG_NAMT`,
`SIG_NAMS`,
`PRN_NAML`,
`PRN_NAMF`,
`PRN_NAMT`,
`PRN_NAMS`,
`SIG_TITLE`,
`STMT_FIRM`,
`IND_CB`,
`BUS_CB`,
`TRADE_CB`,
`OTH_CB`,
`A_B_NAME`,
`A_B_CITY`,
`A_B_ST`,
`A_B_ZIP4`,
`DESCRIP_1`,
`DESCRIP_2`,
`C_LESS50`,
`C_MORE50`,
`IND_CLASS`,
`IND_DESCR`,
`BUS_CLASS`,
`BUS_DESCR`,
`AUTH_NAME`,
`AUTH_CITY`,
`AUTH_ST`,
`AUTH_ZIP4`,
`LOBBY_INT`,
`INFLUEN_YN`,
`FIRM_NAME`,
`NEWCERT_CB`,
`RENCERT_CB`,
@`COMPLET_DT`,
`LBY_REG_CB`,
`LBY_604_CB`,
`ST_LEG_YN`,
`ST_AGENCY`,
`LOBBY_CB`,
`L_FIRM_CB`
)
SET
`COMPLET_DT` = str_to_Date(@`COMPLET_DT`, '%m/%d/%Y %r'),
`EFF_DATE` = str_to_Date(@`EFF_DATE`, '%m/%d/%Y %r'),
`RPT_DATE` = str_to_Date(@`RPT_DATE`, '%m/%d/%Y %r'),
`QUAL_DATE` = str_to_Date(@`QUAL_DATE`, '%m/%d/%Y %r'),
`SIG_DATE` = str_to_Date(@`SIG_DATE`, '%m/%d/%Y %r')
''')


## CVR2_CAMPAIGN_DISCLOSURE_CD
mysql.execute('DELETE FROM CVR2_CAMPAIGN_DISCLOSURE_CD;')
csv_cvr2 = clean_data_dir + 'cvr2_campaign_disclosure_cd.csv'
mysql.execute('''
LOAD DATA LOCAL INFILE '%s'
INTO TABLE CVR2_CAMPAIGN_DISCLOSURE_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILING_ID`,
`AMEND_ID`,
`LINE_ITEM`,
`REC_TYPE`,
`FORM_TYPE`,
`TRAN_ID`,
`ENTITY_CD`,
`TITLE`,
`MAIL_CITY`,
`MAIL_ST`,
`MAIL_ZIP4`,
`F460_PART`,
`CMTE_ID`,
`ENTY_NAML`,
`ENTY_NAMF`,
`ENTY_NAMT`,
`ENTY_NAMS`,
`ENTY_CITY`,
`ENTY_ST`,
`ENTY_ZIP4`,
`ENTY_PHON`,
`ENTY_FAX`,
`ENTY_EMAIL`,
`TRES_NAML`,
`TRES_NAMF`,
`TRES_NAMT`,
`TRES_NAMS`,
`CONTROL_YN`,
`OFFICE_CD`,
`OFFIC_DSCR`,
`JURIS_CD`,
`JURIS_DSCR`,
`DIST_NO`,
`OFF_S_H_CD`,
`BAL_NAME`,
`BAL_NUM`,
`BAL_JURIS`,
`SUP_OPP_CD`
);
''' % csv_cvr2)

## DEBT
mysql.execute('DELETE FROM DEBT_CD;')
debt_csv = clean_data_dir + 'debt_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % debt_csv
mysql.execute(first_line + '''
INTO TABLE DEBT_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`AMEND_ID`,
`AMT_INCUR`,
`AMT_PAID`,
`BAKREF_TID`,
`BEG_BAL`,
`CMTE_ID`,
`END_BAL`,
`ENTITY_CD`,
`EXPN_CODE`,
`EXPN_DSCR`,
`FILING_ID`,
`FORM_TYPE`,
`LINE_ITEM`,
`MEMO_CODE`,
`MEMO_REFNO`,
`PAYEE_ADR1`,
`PAYEE_ADR2`,
`PAYEE_CITY`,
`PAYEE_NAMF`,
`PAYEE_NAML`,
`PAYEE_NAMS`,
`PAYEE_NAMT`,
`PAYEE_ST`,
`PAYEE_ZIP4`,
`REC_TYPE`,
`TRAN_ID`,
`TRES_ADR1`,
`TRES_ADR2`,
`TRES_CITY`,
`TRES_NAMF`,
`TRES_NAML`,
`TRES_NAMS`,
`TRES_NAMT`,
`TRES_ST`,
`TRES_ZIP4`,
`XREF_MATCH`,
`XREF_SCHNM`
)
''')

## EXPN
mysql.execute('DELETE FROM EXPN_CD;')
expn_csv = clean_data_dir + 'expn_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % expn_csv
mysql.execute(first_line + '''
INTO TABLE EXPN_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(

`FILING_ID`,
`AMEND_ID`,
`LINE_ITEM`,
`REC_TYPE`,
`FORM_TYPE`,
`TRAN_ID`,
`ENTITY_CD`,
`PAYEE_NAML`,
`PAYEE_NAMF`,
`PAYEE_NAMT`,
`PAYEE_NAMS`,
`PAYEE_CITY`,
`PAYEE_ST`,
`PAYEE_ZIP4`,
@`EXPN_DATE`,
`AMOUNT`,
`CUM_YTD`,
`CUM_OTH`,
`EXPN_CHKNO`,
`EXPN_CODE`,
`EXPN_DSCR`,
`AGENT_NAML`,
`AGENT_NAMF`,
`AGENT_NAMT`,
`AGENT_NAMS`,
`CMTE_ID`,
`TRES_NAML`,
`TRES_NAMF`,
`TRES_NAMT`,
`TRES_NAMS`,
`TRES_CITY`,
`TRES_ST`,
`TRES_ZIP4`,
`CAND_NAML`,
`CAND_NAMF`,
`CAND_NAMT`,
`CAND_NAMS`,
`OFFICE_CD`,
`OFFIC_DSCR`,
`JURIS_CD`,
`JURIS_DSCR`,
`DIST_NO`,
`OFF_S_H_CD`,
`BAL_NAME`,
`BAL_NUM`,
`BAL_JURIS`,
`SUP_OPP_CD`,
`MEMO_CODE`,
`MEMO_REFNO`,
`BAKREF_TID`,
`G_FROM_E_F`,
`XREF_SCHNM`,
`XREF_MATCH`
)
SET
`EXPN_DATE` = str_to_Date(@`EXPN_DATE`, '%m/%d/%Y %r');
''')
#mysql.execute('''
#ALTER TABLE EXPN_CD
#ADD COLUMN current_filing CHAR(1)
#''')



## FILER_ACRONYMS_CD
mysql.execute('DELETE FROM FILER_ACRONYMS_CD;')
acro_csv = clean_data_dir + 'filer_acronyms_cd.csv'
mysql.execute('''
LOAD DATA LOCAL INFILE '%s'
INTO TABLE FILER_ACRONYMS_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
''' % acro_csv)


## FILER FILINGS
mysql.execute('DELETE FROM FILER_FILINGS_CD;')
filings_csv = clean_data_dir + 'filer_filings_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % filings_csv
mysql.execute(first_line + '''
INTO TABLE FILER_FILINGS_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILER_ID`,
`FILING_ID`,
`PERIOD_ID`,
`FORM_ID`,
`FILING_SEQUENCE`,
@`FILING_DATE`,
`STMNT_TYPE`,
`STMNT_STATUS`,
`SESSION_ID`,
`USER_ID`,
`SPECIAL_AUDIT`,
`FINE_AUDIT`,
@`RPT_START`,
@`RPT_END`,
@`RPT_DATE`,
`FILING_TYPE`
)
SET
`FILING_DATE` = str_to_date(@`FILING_DATE`, '%m/%d/%Y %r'),
`RPT_START` = str_to_date(@`RPT_START`, '%m/%d/%Y %r'),
`RPT_END` = str_to_date(@`RPT_END`, '%m/%d/%Y %r'),
`RPT_DATE` = str_to_date(@`RPT_DATE`, '%m/%d/%Y %r');
''')


## FILER INTERESTS
mysql.execute('DELETE FROM FILER_INTERESTS_CD;')
interests_csv = clean_data_dir + 'filer_interests_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % interests_csv
mysql.execute(first_line + '''
INTO TABLE FILER_INTERESTS_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILER_ID`,
`SESSION_ID`,
`INTEREST_CD`,
`EFFECT_DATE`
)
SET
`EFFECT_DATE` = str_to_date(@`EFFECT_DATE`, '%m/%d/%Y %r');
''')


## FILER LINKS
mysql.execute('DELETE FROM FILER_LINKS_CD;')
links_csv = clean_data_dir + 'filer_links_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % links_csv
mysql.execute(first_line + '''
INTO TABLE FILER_LINKS_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILER_ID_A`,
`FILER_ID_B`,
`ACTIVE_FLG`,
`SESSION_ID`,
`LINK_TYPE`,
`LINK_DESC`,
@`EFFECT_DT`,
`DOMINATE_FILER`,
@`TERMINATION_DT`
)
SET
`EFFECT_DT` = str_to_date(@`EFFECT_DT`, '%m/%d/%Y %r'),
`TERMINATION_DT` = str_to_date(@`TERMINATION_DT`, '%m/%d/%Y %r');
''')


## FILER STATUS TYPES
mysql.execute('DELETE FROM FILER_STATUS_TYPES_CD;')
status_csv = clean_data_dir + 'filer_status_types_cd.csv'
mysql.execute('''
LOAD DATA LOCAL INFILE '%s'
INTO TABLE FILER_STATUS_TYPES_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES;
''' % status_csv)

## FILER TYPE PERIODS -- Empty table so skipping


## FILER TO FILER TYPE
mysql.execute('DELETE FROM FILER_TO_FILER_TYPE_CD;')
lk_filer_type_csv = clean_data_dir + 'filer_to_filer_type_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % lk_filer_type_csv
mysql.execute(first_line + '''
INTO TABLE FILER_TO_FILER_TYPE_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILER_ID`,
`FILER_TYPE`,
`ACTIVE`,
`RACE`,
`SESSION_ID`,
`CATEGORY`,
`CATEGORY_TYPE`,
`SUB_CATEGORY`,
@`EFFECT_DT`,
`SUB_CATEGORY_TYPE`,
`ELECTION_TYPE`,
`SUB_CATEGORY_A`,
@`NYQ_DT`,
`PARTY_CD`,
`COUNTY_CD`,
`DISTRICT_CD`
)
SET
`EFFECT_DT` = str_to_date(@`EFFECT_DT`, '%m/%d/%Y %r'),
`NYQ_DT` = str_to_date(@`NYQ_DT`, '%m/%d/%Y %r');
''')


## FILER TYPES
mysql.execute('DELETE FROM FILER_TYPES_CD;')
filer_types = clean_data_dir + 'filer_types_cd.csv'
mysql.execute('''
LOAD DATA LOCAL INFILE '%s'
INTO TABLE FILER_TYPES_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES;
''' % filer_types)


## FILER XREF
mysql.execute('DELETE FROM FILER_XREF_CD;')
xref_csv = clean_data_dir + 'filer_xref_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % xref_csv
mysql.execute(first_line + '''
INTO TABLE FILER_XREF_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILER_ID`,
`XREF_ID`,
@`EFFECT_DT`,
`MIGRATION_SOURCE`
)
SET 
`EFFECT_DT`=str_to_date(@`EFFECT_DT`, '%m/%d/%Y %r');
''')


## FILERNAME_CD
mysql.execute('DELETE FROM FILERNAME_CD;')
filername_csv = clean_data_dir + 'filername_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % filername_csv
mysql.execute(first_line + '''
INTO TABLE FILERNAME_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
XREF_FILER_ID,
FILER_ID,
FILER_TYPE,
STATUS,
@EFFECT_DT,
NAML,
NAMF,
NAMT,
NAMS,
ADR1,
ADR2,
CITY,
ST,
ZIP4,
PHON,
FAX,
EMAIL
)
SET 
`EFFECT_DT`=str_to_date(@`EFFECT_DT`, '%m/%d/%Y %r');
''')


## FILERS
mysql.execute('DELETE FROM FILERS_CD;')
filers_csv = clean_data_dir + 'filers_cd.csv'
mysql.execute('''
LOAD DATA LOCAL INFILE '%s'
INTO TABLE FILERS_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES;
''' % filers_csv)


## FILINGS
mysql.execute('DELETE FROM FILINGS;')
filings_csv = clean_data_dir + 'filings.csv'
mysql.execute('''
LOAD DATA LOCAL INFILE '%s'
INTO TABLE FILINGS
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES;
''' % filings_csv)

## FILING PERIOD
mysql.execute('DELETE FROM FILING_PERIOD_CD;')
filing_period_csv = clean_data_dir + 'filing_period_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % filing_period_csv
mysql.execute(first_line + '''
INTO TABLE FILING_PERIOD_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`PERIOD_ID`,
@`START_DATE`,
@`END_DATE`,
`PERIOD_TYPE`,
`PER_GRP_TYPE`,
`PERIOD_DESC`,
@`DEADLINE`
)
SET 
`START_DATE`=str_to_date(@`START_DATE`, '%m/%d/%Y %r'),
`END_DATE`=str_to_date(@`END_DATE`, '%m/%d/%Y %r'),
`DEADLINE`=str_to_date(@`DEADLINE`, '%m/%d/%Y %r')
;
''')


## LEMP
mysql.execute('DELETE FROM LEMP_CD;')
lemp_csv = clean_data_dir + 'lemp_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % lemp_csv
mysql.execute(first_line + '''
INTO TABLE LEMP_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILING_ID`,
`AMEND_ID`,
`LINE_ITEM`,
`REC_TYPE`,
`FORM_TYPE`,
`CLIENT_ID`,
`CLI_NAML`,
`CLI_NAMF`,
`CLI_NAMT`,
`CLI_NAMS`,
`CLI_CITY`,
`CLI_ST`,
`CLI_ZIP4`,
`CLI_PHON`,
@`EFF_DATE`,
`CON_PERIOD`,
`AGENCYLIST`,
`DESCRIP`,
`SUBFIRM_ID`,
`SUB_NAME`,
`SUB_CITY`,
`SUB_ST`,
`SUB_ZIP4`,
`SUB_PHON`
)
SET 
`EFF_DATE`=str_to_date(@`EFF_DATE`, '%m/%d/%Y %r');
''')


## LEXP
mysql.execute('DELETE FROM LEXP_CD;')
lexp_cd_csv = clean_data_dir + 'lexp_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % lexp_cd_csv
mysql.execute(first_line + '''
INTO TABLE LEXP_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`AMEND_ID`,
`AMOUNT`,
`BAKREF_TID`,
`BENE_AMT`,
`BENE_NAME`,
`BENE_POSIT`,
`CREDCARDCO`,
`ENTITY_CD`,
@`EXPN_DATE`,
`EXPN_DSCR`,
`FILING_ID`,
`FORM_TYPE`,
`LINE_ITEM`,
`MEMO_CODE`,
`MEMO_REFNO`,
`PAYEE_ADR1`,
`PAYEE_ADR2`,
`PAYEE_CITY`,
`PAYEE_NAMF`,
`PAYEE_NAML`,
`PAYEE_NAMS`,
`PAYEE_NAMT`,
`PAYEE_ST`,
`PAYEE_ZIP4`,
`REC_TYPE`,
`RECSUBTYPE`,
`TRAN_ID`
)
SET 
`EXPN_DATE`=str_to_date(@`EXPN_DATE`, '%m/%d/%Y %r');
''')


## LOAN
mysql.execute('DELETE FROM LOAN_CD;')
loan_csv = clean_data_dir + 'loan_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % loan_csv
mysql.execute(first_line + '''
INTO TABLE LOAN_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`AMEND_ID`,
`BAKREF_TID`,
`CMTE_ID`,
`ENTITY_CD`,
`FILING_ID`,
`FORM_TYPE`,
`INTR_ADR1`,
`INTR_ADR2`,
`INTR_CITY`,
`INTR_NAMF`,
`INTR_NAML`,
`INTR_NAMS`,
`INTR_NAMT`,
`INTR_ST`,
`INTR_ZIP4`,
`LINE_ITEM`,
`LNDR_NAMF`,
`LNDR_NAML`,
`LNDR_NAMS`,
`LNDR_NAMT`,
`LOAN_ADR1`,
`LOAN_ADR2`,
`LOAN_AMT1`,
`LOAN_AMT2`,
`LOAN_AMT3`,
`LOAN_AMT4`,
`LOAN_AMT5`,
`LOAN_AMT6`,
`LOAN_AMT7`,
`LOAN_AMT8`,
`LOAN_CITY`,
@`LOAN_DATE1`,
@`LOAN_DATE2`,
`LOAN_EMP`,
`LOAN_OCC`,
`LOAN_RATE`,
`LOAN_SELF`,
`LOAN_ST`,
`LOAN_TYPE`,
`LOAN_ZIP4`,
`MEMO_CODE`,
`MEMO_REFNO`,
`REC_TYPE`,
`TRAN_ID`,
`TRES_ADR1`,
`TRES_ADR2`,
`TRES_CITY`,
`TRES_NAMF`,
`TRES_NAML`,
`TRES_NAMS`,
`TRES_NAMT`,
`TRES_ST`,
`TRES_ZIP4`,
`XREF_MATCH`,
`XREF_SCHNM`
)
SET 
`LOAN_DATE1`=str_to_date(@`LOAN_DATE1`, '%m/%d/%Y %r'),
`LOAN_DATE2`=str_to_date(@`LOAN_DATE2`, '%m/%d/%Y %r');
''')


## LOBBY AMENDMENTS
mysql.execute('DELETE FROM LOBBY_AMENDMENTS_CD;')
lobby_amends_csv = clean_data_dir + 'lobby_amendments_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % lobby_amends_csv
mysql.execute(first_line + '''
INTO TABLE LOBBY_AMENDMENTS_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILING_ID`,
`AMEND_ID`,
`REC_TYPE`,
`FORM_TYPE`,
`EXEC_DATE`,
@`FROM_DATE`,
@`THRU_DATE`,
`ADD_L_CB`,
@`ADD_L_EFF`,
`A_L_NAML`,
`A_L_NAMF`,
`A_L_NAMT`,
`A_L_NAMS`,
`DEL_L_CB`,
@`DEL_L_EFF`,
`D_L_NAML`,
`D_L_NAMF`,
`D_L_NAMT`,
`D_L_NAMS`,
`ADD_LE_CB`,
@`ADD_LE_EFF`,
`A_LE_NAML`,
`A_LE_NAMF`,
`A_LE_NAMT`,
`A_LE_NAMS`,
`DEL_LE_CB`,
@`DEL_LE_EFF`,
`D_LE_NAML`,
`D_LE_NAMF`,
`D_LE_NAMT`,
`D_LE_NAMS`,
`ADD_LF_CB`,
@`ADD_LF_EFF`,
`A_LF_NAME`,
`DEL_LF_CB`,
@`DEL_LF_EFF`,
`D_LF_NAME`,
`OTHER_CB`,
@`OTHER_EFF`,
`OTHER_DESC`,
`F606_YES`,
`F606_NO`
)
SET 
`FROM_DATE`=str_to_date(@`FROM_DATE`, '%m/%d/%Y %r'),
`THRU_DATE`=str_to_date(@`THRU_DATE`, '%m/%d/%Y %r'),
`ADD_L_EFF`=str_to_date(@`ADD_L_EFF`, '%m/%d/%Y %r'),
`DEL_L_EFF`=str_to_date(@`DEL_L_EFF`, '%m/%d/%Y %r'),
`ADD_LE_EFF`=str_to_date(@`ADD_LE_EFF`, '%m/%d/%Y %r'),
`DEL_LE_EFF`=str_to_date(@`DEL_LE_EFF`, '%m/%d/%Y %r'),
`ADD_LF_EFF`=str_to_date(@`ADD_LF_EFF`, '%m/%d/%Y %r'),
`DEL_LF_EFF`=str_to_date(@`DEL_LF_EFF`, '%m/%d/%Y %r'),
`OTHER_EFF`=str_to_date(@`OTHER_EFF`, '%m/%d/%Y %r');
''')


## LOTH
mysql.execute('DELETE FROM LOTH_CD;')
loth_csv = clean_data_dir + 'loth_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % loth_csv
mysql.execute(first_line + '''
INTO TABLE LOTH_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`AMEND_ID`,
`AMOUNT`,
`CUM_AMT`,
`FILING_ID`,
`FIRM_ADR1`,
`FIRM_ADR2`,
`FIRM_CITY`,
`FIRM_NAME`,
`FIRM_PHON`,
`FIRM_ST`,
`FIRM_ZIP4`,
`FORM_TYPE`,
`LINE_ITEM`,
`MEMO_CODE`,
`MEMO_REFNO`,
@`PMT_DATE`,
`REC_TYPE`,
`SUBJ_NAMF`,
`SUBJ_NAML`,
`SUBJ_NAMS`,
`SUBJ_NAMT`,
`TRAN_ID`
)
SET 
`PMT_DATE`=str_to_date(@`PMT_DATE`, '%m/%d/%Y %r');
''')


## LPAY
mysql.execute('DELETE FROM LPAY_CD;')
lpay_csv = clean_data_dir + 'lpay_cd.csv'
mysql.execute('''
LOAD DATA LOCAL INFILE '%s'
INTO TABLE LPAY_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES;
''' % lpay_csv)


## NAMES
mysql.execute('DELETE FROM NAMES;')
names_csv = clean_data_dir + 'names.csv'
mysql.execute('''
LOAD DATA LOCAL INFILE '%s'
INTO TABLE NAMES
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES;
''' % names_csv)

## SMRY
mysql.execute('DELETE FROM SMRY_CD;')
smry_csv = clean_data_dir + 'smry_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % smry_csv
mysql.execute(first_line + '''
INTO TABLE SMRY_CD
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(
`FILING_ID`,
`AMEND_ID`,
`LINE_ITEM`,
`REC_TYPE`,
`FORM_TYPE`,
`AMOUNT_A`,
`AMOUNT_B`,
`AMOUNT_C`,
@`ELEC_DT`
)
SET 
`ELEC_DT`=str_to_date(@`ELEC_DATE`, '%m/%d/%Y %r');
''')

## RCPT
mysql.execute('DELETE FROM `RCPT_CD`')
rcpt_csv = clean_data_dir + 'rcpt_cd.csv'
first_line = "LOAD DATA LOCAL INFILE '%s'" % rcpt_csv
mysql.execute(first_line + '''
INTO TABLE `RCPT_CD`
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
IGNORE 1 LINES
(

`FILING_ID`,
`AMEND_ID`,
`LINE_ITEM`,
`REC_TYPE`,
`FORM_TYPE`,
`TRAN_ID`,
`ENTITY_CD`,
`CTRIB_NAML`,
`CTRIB_NAMF`,
`CTRIB_NAMT`,
`CTRIB_NAMS`,
`CTRIB_CITY`,
`CTRIB_ST`,
`CTRIB_ZIP4`,
`CTRIB_EMP`,
`CTRIB_OCC`,
`CTRIB_SELF`,
`TRAN_TYPE`,
@`RCPT_DATE`,
@`DATE_THRU`,
`AMOUNT`,
`CUM_YTD`,
`CUM_OTH`,
`CTRIB_DSCR`,
`CMTE_ID`,
`TRES_NAML`,
`TRES_NAMF`,
`TRES_NAMT`,
`TRES_NAMS`,
`TRES_CITY`,
`TRES_ST`,
`TRES_ZIP4`,
`INTR_NAML`,
`INTR_NAMF`,
`INTR_NAMT`,
`INTR_NAMS`,
`INTR_CITY`,
`INTR_ST`,
`INTR_ZIP4`,
`INTR_EMP`,
`INTR_OCC`,
`INTR_SELF`,
`CAND_NAML`,
`CAND_NAMF`,
`CAND_NAMT`,
`CAND_NAMS`,
`OFFICE_CD`,
`OFFIC_DSCR`,
`JURIS_CD`,
`JURIS_DSCR`,
`DIST_NO`,
`OFF_S_H_CD`,
`BAL_NAME`,
`BAL_NUM`,
`BAL_JURIS`,
`SUP_OPP_CD`,
`MEMO_CODE`,
`MEMO_REFNO`,
`BAKREF_TID`,
`XREF_SCHNM`,
`XREF_MATCH`,
`INT_RATE`,
`INTR_CMTEID`
)
SET
`DATE_THRU` = str_to_date(@`DATE_THRU`, '%m/%d/%Y %r'),
`RCPT_DATE` = str_to_date(@`RCPT_DATE`, '%m/%d/%Y %r')
''')





###  DATA IS LOADED UP NOW GET IT READY FOR ANALYSIS

## Smash together a filer lookup that's easier to comprehend
mysql.execute('DROP TABLE IF EXISTS lk_filers')
mysql.execute('''
CREATE TABLE `lk_filers` (
  `FILER_ID` int(11) NOT NULL,
  `filername_name` varchar(255),
  `type` varchar(255),
  `prik` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`prik`),
  KEY `1` (`FILER_ID`)
) 
''')
mysql.execute('''
INSERT INTO lk_filers(FILER_ID, filername_name, type)
SELECT FILERNAME_CD.FILER_ID, CONCAT(
	FILERNAME_CD.NAML, ' ',
	FILERNAME_CD.NAMF, ' ', 
	FILERNAME_CD.NAMT,  ' ',
	FILERNAME_CD.NAMS
) AS name,
FILERNAME_CD.FILER_TYPE
FROM FILER_FILINGS_CD INNER JOIN FILERNAME_CD ON FILERNAME_CD.FILER_ID = FILER_FILINGS_CD.FILER_ID
WHERE FILERNAME_CD.FILER_ID<>0
GROUP BY 1, 2
''')


## Smash together a list of current filings. Forget the rest
mysql.execute('DROP TABLE IF EXISTS lk_current_filings')
mysql.execute('''
CREATE TABLE `lk_current_filings` (
  `FILER_ID` int(11) NOT NULL,
  `FILING_ID` int(11) NOT NULL,
  `amend_id` int(11),
  `SESSION_ID` int(11) NOT NULL,
  `FORM_ID` varchar(50),
  `total_raised` Decimal(16,2),
  `total_spent` Decimal(16,2),
  KEY `1` (`FILER_ID`),
  KEY `2` (`FILING_ID`),
  KEY `3` (`amend_id`)
)
''')
## I'm taking the MIN(SESSION_ID) since it seems that's the session the form belongs too even if an amendment is filed in a later session.
## Obviously we take the newer amendment, but don't lump the form's disclosure data with whatever session the latest amendment appears in.
mysql.execute('''
INSERT INTO lk_current_filings (FILER_ID, FILING_ID, amend_id, SESSION_ID)
SELECT 
	FILER_FILINGS_CD.FILER_ID, 
	FILER_FILINGS_CD.FILING_ID,
	MAX(FILER_FILINGS_CD.FILING_SEQUENCE) AS AMEND_ID, 
	MIN(FILER_FILINGS_CD.SESSION_ID)
FROM FILER_FILINGS_CD
GROUP BY 1,2
''')
## now take whatever form ID goes with the latest amendment.
mysql.execute('''
UPDATE lk_current_filings INNER JOIN FILER_FILINGS_CD ON FILER_FILINGS_CD.FILER_ID = lk_current_filings.FILER_ID AND
                                                         FILER_FILINGS_CD.FILING_ID = lk_current_filings.FILING_ID AND
                                                         FILER_FILINGS_CD.FILING_SEQUENCE = lk_current_filings.AMEND_ID
SET lk_current_filings.FORM_ID = FILER_FILINGS_CD.FORM_ID
''')
mysql.execute('''
    UPDATE lk_current_filings INNER JOIN SMRY_CD ON lk_current_filings.FILING_ID = SMRY_CD.FILING_ID AND lk_current_filings.amend_id = SMRY_CD.AMEND_ID
    SET lk_current_filings.total_raised = SMRY_CD.AMOUNT_A
    WHERE SMRY_CD.FORM_TYPE='F460' AND SMRY_CD.REC_TYPE = 'SMRY' AND SMRY_CD.LINE_ITEM='5'
''')

mysql.execute('''
    UPDATE lk_current_filings INNER JOIN SMRY_CD ON lk_current_filings.FILING_ID = SMRY_CD.FILING_ID AND lk_current_filings.amend_id = SMRY_CD.AMEND_ID
    SET lk_current_filings.total_spent = SMRY_CD.AMOUNT_A
    WHERE SMRY_CD.FORM_TYPE='F460' AND SMRY_CD.REC_TYPE = 'SMRY' AND SMRY_CD.LINE_ITEM='11'
''')


"""

mysql.execute("UPDATE EXPN_CD SET current_filing='n'")
mysql.execute('''
UPDATE EXPN_CD INNER JOIN (
SELECT filing_id, MAX(filing_sequence) AS Amend
FROM FILER_FILINGS_CD
GROUP BY 1
) w on EXPN_CD.FILING_ID = w.filing_id AND EXPN_CD.AMEND_ID = w.amend
SET current_filing='y'
''')


mysql.execute("UPDATE SMRY_CD SET current_filing='n'")
mysql.execute('''
UPDATE SMRY_CD INNER JOIN (
SELECT filing_id, MAX(filing_sequence) AS Amend
FROM FILER_FILINGS_CD
GROUP BY 1
) w on SMRY_CD.FILING_ID = w.filing_id AND SMRY_CD.AMEND_ID = w.amend
SET current_filing='y'
''')





## Get a list of everyone we have a filing for. Forget the rest.

CREATE TABLE lk_filers
SELECT FILER_FILINGS_CD.FILER_ID
FROM FILER_FILINGS_CD
GROUP BY 1




## Grab their names & types from FILERNAMES_CD
## I have no idea what the NAMES table is all about
## It only "kinda" matches up to FILERNAMES_CD
## The documentation indicates that FILERNAME is where to look and my own comparisons to the live CAL-ACCESS version seem to bear this out.

UPDATE lk_filers INNER JOIN (

SELECT FILERNAME_CD.FILER_ID,
CONCAT(
	FILERNAME_CD.NAML, ' ',
	FILERNAME_CD.NAMF, ' ', 
	FILERNAME_CD.NAMT,  ' ',
	FILERNAME_CD.NAMS
) AS name
FROM FILERNAME_CD
GROUP BY 1

) w ON lk_filers.filer_id = w.filer_id
SET lk_filers.filername_name = w.name




## Each filer appears to have only one filer type associated with it

UPDATE lk_filers INNER JOIN
(

SELECT FILERNAME_CD.FILER_ID, 
	FILERNAME_CD.FILER_TYPE
FROM FILERNAME_CD
GROUP BY 1,2

) w ON lk_filers.FILER_ID = w.FILER_ID
SET lk_filers.type = w.FILER_TYPE




## You can find all of the committees run by a candidate using FILER_LINKS_CD
## Candidate Filer Types can be linked to all of their committees using the FILER_LINKS_CD table WHERE FILER_ID_A = 'Candidate FILER_ID'
## The status types come from FILER_STATUS_TYPES_CD

SELECT *
FROM FILER_LINKS_CD
WHERE FILER_ID_A='1304250' # These are all Speaker John A Perez committees

http://cal-access.ss.ca.gov/Campaign/Candidates/Detail.aspx?id=1304250&session=2013


### separate out all the current expenditures
CREATE TABLE current_expn
SELECT EXPN_CD.*
FROM lk_filers INNER JOIN lk_current_filings ON lk_filers.FILER_ID = lk_current_filings.FILER_ID
	 INNER JOIN EXPN_CD ON lk_current_filings.amend_id = EXPN_CD.AMEND_ID AND lk_current_filings.FILING_ID = EXPN_CD.FILING_ID
WHERE
lk_filers.type='MAJOR DONOR/INDEPENDENT EXPENDITURE COMMITTEE' OR
lk_filers.type='RECIPIENT COMMITTEE'










"""