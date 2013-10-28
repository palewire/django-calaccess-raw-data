/*
 Navicat Premium Data Transfer

 Source Server         : mysql localhost
 Source Server Type    : MySQL
 Source Server Version : 50142
 Source Host           : localhost
 Source Database       : cal_access_testing

 Target Server Type    : MySQL
 Target Server Version : 50142
 File Encoding         : UTF-8

 Date: 10/21/2013 15:39:09 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `CVR2_CAMPAIGN_DISCLOSURE_CD`
-- ----------------------------
DROP TABLE IF EXISTS `CVR2_CAMPAIGN_DISCLOSURE_CD`;
CREATE TABLE `CVR2_CAMPAIGN_DISCLOSURE_CD` (
  `AMEND_ID` int(11) NOT NULL,
  `BAL_JURIS` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NUM` varchar(7) COLLATE ascii_bin DEFAULT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CONTROL_YN` tinyint(1) DEFAULT NULL,
  `DIST_NO` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_EMAIL` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_FAX` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `ENTY_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `F460_PART` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `JURIS_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(9) NOT NULL,
  `MAIL_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `OFF_S_H_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OFFIC_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `OFFICE_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUP_OPP_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TITLE` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `CVR_CAMPAIGN_DISCLOSURE_CD`
-- ----------------------------
DROP TABLE IF EXISTS `CVR_CAMPAIGN_DISCLOSURE_CD`;
CREATE TABLE `CVR_CAMPAIGN_DISCLOSURE_CD` (
  `AMEND_ID` int(11) NOT NULL,
  `AMENDEXP_1` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `AMENDEXP_2` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `AMENDEXP_3` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `ASSOC_CB` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `ASSOC_INT` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `BAL_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `BAL_JURIS` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NUM` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `BRDBASE_YN` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `BUS_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `BUS_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `BUS_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `BUS_INTER` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BUS_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BUS_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `BUSACT_CB` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `BUSACTVITY` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `CAND_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CAND_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CAND_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `CAND_EMAIL` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `CAND_FAX` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `CAND_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CAND_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `CAND_ST` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `CAND_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CMTTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CMTTE_TYPE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `CONTROL_YN` tinyint(1) DEFAULT NULL,
  `DIST_NO` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `ELECT_DATE` date DEFAULT NULL,
  `EMPLBUS_CB` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `EMPLOYER` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `FILE_EMAIL` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `FILER_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `FILER_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `FILER_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `FILER_FAX` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `FILER_ID` int(9) NOT NULL,
  `FILER_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `FILER_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `FILER_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FILER_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FILER_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `FILER_ST` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `FILER_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(9) NOT NULL,
  `FORM_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `FROM_DATE` date DEFAULT NULL,
  `JURIS_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `LATE_RPTNO` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ST` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `OCCUPATION` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `OFF_S_H_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OFFIC_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `OFFICE_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `OTHER_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OTHER_INT` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `PRIMFRM_YN` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(3) COLLATE ascii_bin NOT NULL,
  `REPORT_NUM` varchar(3) COLLATE ascii_bin NOT NULL,
  `REPORTNAME` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `RPT_ATT_CB` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `RPT_DATE` date NOT NULL,
  `RPTFROMDT` date DEFAULT NULL,
  `RPTTHRUDT` date DEFAULT NULL,
  `SELFEMP_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `SPONSOR_YN` tinyint(1) DEFAULT NULL,
  `STMT_TYPE` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `SUP_OPP_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `THRU_DATE` date DEFAULT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_EMAIL` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `TRES_FAX` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  KEY `1` (`AMEND_ID`),
  KEY `2` (`FILER_ID`),
  KEY `3` (`FILING_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `CVR_LOBBY_DISCLOSURE_CD`
-- ----------------------------
DROP TABLE IF EXISTS `CVR_LOBBY_DISCLOSURE_CD`;
CREATE TABLE `CVR_LOBBY_DISCLOSURE_CD` (
  `AMEND_ID` int(11) NOT NULL,
  `CTRIB_N_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_Y_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `CUM_BEG_DT` date DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `FILER_ID` varchar(9) COLLATE ascii_bin NOT NULL,
  `FILER_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `FILER_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `FILER_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FILER_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FIRM_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FORM_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `FROM_DATE` date NOT NULL,
  `LBY_ACTVTY` varchar(400) COLLATE ascii_bin DEFAULT NULL,
  `LOBBY_N_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `LOBBY_Y_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `MAJOR_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `MAJOR_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `MAJOR_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `MAJOR_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `NOPART1_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `NOPART2_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `PART1_1_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `PART1_2_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `PRN_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `PRN_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `PRN_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PRN_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `RCPCMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `RCPCMTE_NM` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(3) COLLATE ascii_bin NOT NULL,
  `REPORT_NUM` varchar(3) COLLATE ascii_bin NOT NULL,
  `RPT_DATE` date NOT NULL,
  `SENDER_ID` varchar(9) COLLATE ascii_bin NOT NULL,
  `SIG_DATE` date NOT NULL,
  `SIG_LOC` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `SIG_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `SIG_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `SIG_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `SIG_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `SIG_TITLE` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `THRU_DATE` date NOT NULL,
  KEY `1` (`AMEND_ID`),
  KEY `2` (`FILER_ID`),
  KEY `3` (`FILING_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `CVR_REGISTRATION_CD`
-- ----------------------------
DROP TABLE IF EXISTS `CVR_REGISTRATION_CD`;
CREATE TABLE `CVR_REGISTRATION_CD` (
  `A_B_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `A_B_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `A_B_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `A_B_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `A_B_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `A_B_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `AMEND_ID` int(9) NOT NULL,
  `AUTH_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `AUTH_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `AUTH_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `AUTH_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `AUTH_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `AUTH_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `BUS_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `BUS_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `BUS_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `BUS_CITY` varchar(30) COLLATE ascii_bin NOT NULL,
  `BUS_CLASS` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `BUS_DESCR` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `BUS_EMAIL` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `BUS_FAX` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BUS_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BUS_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `BUS_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `C_LESS50` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `C_MORE50` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `COMPLET_DT` date DEFAULT NULL,
  `DESCRIP_1` varchar(300) COLLATE ascii_bin DEFAULT NULL,
  `DESCRIP_2` varchar(300) COLLATE ascii_bin DEFAULT NULL,
  `EFF_DATE` date DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `FILER_ID` varchar(9) COLLATE ascii_bin NOT NULL,
  `FILER_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `FILER_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `FILER_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FILER_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) DEFAULT NULL,
  `FIRM_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `FORM_TYPE` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `IND_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `IND_CLASS` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `IND_DESCR` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `INFLUEN_YN` tinyint(1) DEFAULT NULL,
  `L_FIRM_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `LBY_604_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `LBY_REG_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `LOBBY_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `LOBBY_INT` varchar(300) COLLATE ascii_bin DEFAULT NULL,
  `LS_BEG_YR` int(4) DEFAULT NULL,
  `LS_END_YR` int(4) NOT NULL,
  `MAIL_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `MAIL_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `NEWCERT_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OTH_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `PRN_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `PRN_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `PRN_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PRN_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `QUAL_DATE` date DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `RENCERT_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `REPORT_NUM` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `RPT_DATE` date NOT NULL,
  `SENDER_ID` varchar(9) COLLATE ascii_bin NOT NULL,
  `SIG_DATE` date DEFAULT NULL,
  `SIG_LOC` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `SIG_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `SIG_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `SIG_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `SIG_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `SIG_TITLE` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `ST_AGENCY` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `ST_LEG_YN` tinyint(1) DEFAULT NULL,
  `STMT_FIRM` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `TRADE_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  KEY `1` (`AMEND_ID`),
  KEY `2` (`FILING_ID`),
  KEY `3` (`FILER_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `DEBT_CD`
-- ----------------------------
DROP TABLE IF EXISTS `DEBT_CD`;
CREATE TABLE `DEBT_CD` (
  `AMEND_ID` int(11) NOT NULL,
  `AMT_INCUR` decimal(12,2) NOT NULL,
  `AMT_PAID` decimal(12,2) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BEG_BAL` decimal(12,2) NOT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `END_BAL` decimal(12,2) NOT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_CODE` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_DSCR` varchar(400) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(1) COLLATE ascii_bin NOT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `PAYEE_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMT` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `XREF_MATCH` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `XREF_SCHNM` varchar(2) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `EXPN_CD`
-- ----------------------------
DROP TABLE IF EXISTS `EXPN_CD`;
CREATE TABLE `EXPN_CD` (
  `AGENT_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `AMEND_ID` int(11) NOT NULL,
  `AMOUNT` decimal(12,2) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BAL_JURIS` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NUM` varchar(7) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CUM_OTH` decimal(12,2) DEFAULT NULL,
  `CUM_YTD` decimal(12,2) DEFAULT NULL,
  `DIST_NO` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_CHKNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_CODE` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_DATE` date DEFAULT NULL,
  `EXPN_DSCR` varchar(400) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(6) COLLATE ascii_bin NOT NULL,
  `G_FROM_E_F` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `OFF_S_H_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OFFIC_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `OFFICE_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUP_OPP_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `XREF_MATCH` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `XREF_SCHNM` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `current_filing` char(1) COLLATE ascii_bin DEFAULT NULL,
  KEY `1` (`AMEND_ID`),
  KEY `2` (`FILING_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILERNAME_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILERNAME_CD`;
CREATE TABLE `FILERNAME_CD` (
  `XREF_FILER_ID` varchar(7) COLLATE ascii_bin NOT NULL,
  `FILER_ID` int(11) NOT NULL,
  `FILER_TYPE` varchar(45) COLLATE ascii_bin NOT NULL,
  `STATUS` varchar(10) COLLATE ascii_bin NOT NULL,
  `EFFECT_DT` date NOT NULL,
  `NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `NAMF` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `NAMT` varchar(28) COLLATE ascii_bin DEFAULT NULL,
  `NAMS` varchar(32) COLLATE ascii_bin DEFAULT NULL,
  `ADR1` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `ADR2` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CITY` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `ST` varchar(4) COLLATE ascii_bin DEFAULT NULL,
  `ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PHON` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `FAX` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `EMAIL` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  KEY `1` (`XREF_FILER_ID`),
  KEY `2` (`FILER_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILERS_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILERS_CD`;
CREATE TABLE `FILERS_CD` (
  `FILER_ID` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILER_ACRONYMS_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILER_ACRONYMS_CD`;
CREATE TABLE `FILER_ACRONYMS_CD` (
  `acronym` varchar(32) NOT NULL,
  `filer_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii;

-- ----------------------------
--  Table structure for `FILER_FILINGS_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILER_FILINGS_CD`;
CREATE TABLE `FILER_FILINGS_CD` (
  `FILER_ID` int(11) NOT NULL,
  `FILING_ID` int(11) NOT NULL,
  `PERIOD_ID` int(11) DEFAULT NULL,
  `FORM_ID` varchar(7) COLLATE ascii_bin NOT NULL,
  `FILING_SEQUENCE` int(11) NOT NULL,
  `FILING_DATE` date NOT NULL,
  `STMNT_TYPE` int(11) NOT NULL,
  `STMNT_STATUS` int(11) NOT NULL,
  `SESSION_ID` int(11) NOT NULL,
  `USER_ID` varchar(12) COLLATE ascii_bin NOT NULL,
  `SPECIAL_AUDIT` int(11) DEFAULT NULL,
  `FINE_AUDIT` int(11) DEFAULT NULL,
  `RPT_START` date DEFAULT NULL,
  `RPT_END` date DEFAULT NULL,
  `RPT_DATE` date DEFAULT NULL,
  `FILING_TYPE` int(11) DEFAULT NULL,
  KEY `1` (`FILER_ID`),
  KEY `2` (`FILING_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILER_INTERESTS_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILER_INTERESTS_CD`;
CREATE TABLE `FILER_INTERESTS_CD` (
  `FILER_ID` int(11) NOT NULL,
  `SESSION_ID` int(11) NOT NULL,
  `INTEREST_CD` int(11) NOT NULL,
  `EFFECT_DATE` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILER_LINKS_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILER_LINKS_CD`;
CREATE TABLE `FILER_LINKS_CD` (
  `FILER_ID_A` int(11) NOT NULL,
  `FILER_ID_B` int(11) NOT NULL,
  `ACTIVE_FLG` varchar(1) COLLATE ascii_bin NOT NULL,
  `SESSION_ID` int(11) NOT NULL,
  `LINK_TYPE` int(11) NOT NULL,
  `LINK_DESC` varchar(255) COLLATE ascii_bin DEFAULT NULL,
  `EFFECT_DT` date NOT NULL,
  `DOMINATE_FILER` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TERMINATION_DT` date DEFAULT NULL,
  KEY `1` (`FILER_ID_A`),
  KEY `2` (`FILER_ID_B`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILER_STATUS_TYPES_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILER_STATUS_TYPES_CD`;
CREATE TABLE `FILER_STATUS_TYPES_CD` (
  `STATUS_TYPE` varchar(11) COLLATE ascii_bin NOT NULL,
  `STATUS_DESC` varchar(11) COLLATE ascii_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILER_TO_FILER_TYPE_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILER_TO_FILER_TYPE_CD`;
CREATE TABLE `FILER_TO_FILER_TYPE_CD` (
  `FILER_ID` int(11) NOT NULL,
  `FILER_TYPE` int(11) NOT NULL,
  `ACTIVE` varchar(1) COLLATE ascii_bin NOT NULL,
  `RACE` int(11) DEFAULT NULL,
  `SESSION_ID` int(11) NOT NULL,
  `CATEGORY` int(11) DEFAULT NULL,
  `CATEGORY_TYPE` int(11) DEFAULT NULL,
  `SUB_CATEGORY` int(11) DEFAULT NULL,
  `EFFECT_DT` date NOT NULL,
  `SUB_CATEGORY_TYPE` int(11) DEFAULT NULL,
  `ELECTION_TYPE` int(11) DEFAULT NULL,
  `SUB_CATEGORY_A` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `NYQ_DT` date DEFAULT NULL,
  `PARTY_CD` int(11) DEFAULT NULL,
  `COUNTY_CD` int(11) DEFAULT NULL,
  `DISTRICT_CD` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILER_TYPES_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILER_TYPES_CD`;
CREATE TABLE `FILER_TYPES_CD` (
  `FILER_TYPE` int(9) NOT NULL,
  `DESCRIPTION` varchar(255) COLLATE ascii_bin NOT NULL,
  `GRP_TYPE` int(9) DEFAULT NULL,
  `CALC_USE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `GRACE_PERIOD` varchar(12) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILER_XREF_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILER_XREF_CD`;
CREATE TABLE `FILER_XREF_CD` (
  `FILER_ID` int(11) NOT NULL,
  `XREF_ID` varchar(32) COLLATE ascii_bin NOT NULL,
  `EFFECT_DT` date NOT NULL,
  `MIGRATION_SOURCE` varchar(50) COLLATE ascii_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `FILINGS`
-- ----------------------------
DROP TABLE IF EXISTS `FILINGS`;
CREATE TABLE `FILINGS` (
  `FILING_ID` int(11) NOT NULL,
  `FILING_TYPE` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii;

-- ----------------------------
--  Table structure for `FILING_PERIOD_CD`
-- ----------------------------
DROP TABLE IF EXISTS `FILING_PERIOD_CD`;
CREATE TABLE `FILING_PERIOD_CD` (
  `PERIOD_ID` int(11) NOT NULL,
  `START_DATE` date NOT NULL,
  `END_DATE` date NOT NULL,
  `PERIOD_TYPE` int(11) NOT NULL,
  `PER_GRP_TYPE` int(11) NOT NULL,
  `PERIOD_DESC` varchar(255) COLLATE ascii_bin NOT NULL,
  `DEADLINE` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `LEMP_CD`
-- ----------------------------
DROP TABLE IF EXISTS `LEMP_CD`;
CREATE TABLE `LEMP_CD` (
  `AGENCYLIST` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `AMEND_ID` int(11) NOT NULL,
  `CLI_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CLI_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CLI_CITY` varchar(30) COLLATE ascii_bin NOT NULL,
  `CLI_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CLI_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `CLI_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CLI_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CLI_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `CLI_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `CLI_ZIP4` varchar(10) COLLATE ascii_bin NOT NULL,
  `CLIENT_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CON_PERIOD` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `DESCRIP` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `EFF_DATE` date DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(7) COLLATE ascii_bin NOT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUB_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `SUB_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `SUB_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `SUB_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `SUB_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `SUB_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `SUB_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `SUBFIRM_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `LEXP_CD`
-- ----------------------------
DROP TABLE IF EXISTS `LEXP_CD`;
CREATE TABLE `LEXP_CD` (
  `AMEND_ID` int(11) NOT NULL,
  `AMOUNT` decimal(12,2) DEFAULT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BENE_AMT` varchar(12) COLLATE ascii_bin DEFAULT NULL,
  `BENE_NAME` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `BENE_POSIT` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `CREDCARDCO` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin NOT NULL,
  `EXPN_DATE` date DEFAULT NULL,
  `EXPN_DSCR` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(7) COLLATE ascii_bin NOT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `RECSUBTYPE` varchar(1) COLLATE ascii_bin NOT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `LOAN_CD`
-- ----------------------------
DROP TABLE IF EXISTS `LOAN_CD`;
CREATE TABLE `LOAN_CD` (
  `AMEND_ID` int(11) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(2) COLLATE ascii_bin NOT NULL,
  `INTR_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `INTR_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `LNDR_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `LNDR_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `LNDR_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `LNDR_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_AMT1` decimal(12,2) DEFAULT NULL,
  `LOAN_AMT2` decimal(12,2) DEFAULT NULL,
  `LOAN_AMT3` decimal(12,2) DEFAULT NULL,
  `LOAN_AMT4` decimal(12,2) DEFAULT NULL,
  `LOAN_AMT5` decimal(12,2) DEFAULT NULL,
  `LOAN_AMT6` decimal(12,2) DEFAULT NULL,
  `LOAN_AMT7` decimal(12,2) DEFAULT NULL,
  `LOAN_AMT8` decimal(12,2) DEFAULT NULL,
  `LOAN_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_DATE1` date NOT NULL,
  `LOAN_DATE2` date DEFAULT NULL,
  `LOAN_EMP` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_OCC` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_RATE` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_SELF` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_TYPE` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `LOAN_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `XREF_MATCH` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `XREF_SCHNM` varchar(2) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `LOBBY_AMENDMENTS_CD`
-- ----------------------------
DROP TABLE IF EXISTS `LOBBY_AMENDMENTS_CD`;
CREATE TABLE `LOBBY_AMENDMENTS_CD` (
  `FILING_ID` varchar(9) COLLATE ascii_bin NOT NULL,
  `AMEND_ID` varchar(8) COLLATE ascii_bin NOT NULL,
  `REC_TYPE` varchar(8) COLLATE ascii_bin NOT NULL,
  `FORM_TYPE` varchar(9) COLLATE ascii_bin NOT NULL,
  `EXEC_DATE` varchar(22) COLLATE ascii_bin NOT NULL,
  `FROM_DATE` varchar(22) COLLATE ascii_bin NOT NULL,
  `THRU_DATE` varchar(22) COLLATE ascii_bin NOT NULL,
  `ADD_L_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `ADD_L_EFF` date DEFAULT NULL,
  `A_L_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `A_L_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `A_L_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `A_L_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `DEL_L_CB` varchar(8) COLLATE ascii_bin DEFAULT NULL,
  `DEL_L_EFF` varchar(22) COLLATE ascii_bin DEFAULT NULL,
  `D_L_NAML` varchar(56) COLLATE ascii_bin DEFAULT NULL,
  `D_L_NAMF` varchar(35) COLLATE ascii_bin DEFAULT NULL,
  `D_L_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `D_L_NAMS` varchar(8) COLLATE ascii_bin DEFAULT NULL,
  `ADD_LE_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `ADD_LE_EFF` date DEFAULT NULL,
  `A_LE_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `A_LE_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `A_LE_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `A_LE_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `DEL_LE_CB` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `DEL_LE_EFF` varchar(22) COLLATE ascii_bin DEFAULT NULL,
  `D_LE_NAML` varchar(160) COLLATE ascii_bin DEFAULT NULL,
  `D_LE_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `D_LE_NAMT` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `D_LE_NAMS` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `ADD_LF_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `ADD_LF_EFF` date DEFAULT NULL,
  `A_LF_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `DEL_LF_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `DEL_LF_EFF` date DEFAULT NULL,
  `D_LF_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `OTHER_CB` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OTHER_EFF` date DEFAULT NULL,
  `OTHER_DESC` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `F606_YES` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `F606_NO` varchar(1) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `LOTH_CD`
-- ----------------------------
DROP TABLE IF EXISTS `LOTH_CD`;
CREATE TABLE `LOTH_CD` (
  `AMEND_ID` int(11) NOT NULL,
  `AMOUNT` decimal(12,2) DEFAULT NULL,
  `CUM_AMT` decimal(12,2) DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FIRM_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `FIRM_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `FORM_TYPE` varchar(7) COLLATE ascii_bin NOT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `PMT_DATE` date DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUBJ_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `SUBJ_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `SUBJ_NAMS` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `SUBJ_NAMT` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `LPAY_CD`
-- ----------------------------
DROP TABLE IF EXISTS `LPAY_CD`;
CREATE TABLE `LPAY_CD` (
  `ADVAN_AMT` decimal(12,2) DEFAULT NULL,
  `ADVAN_DSCR` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `AMEND_ID` int(11) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `CUM_TOTAL` decimal(12,2) NOT NULL,
  `EMPLR_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `EMPLR_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `FEES_AMT` decimal(12,2) DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(7) COLLATE ascii_bin NOT NULL,
  `LBY_ACTVTY` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `PER_TOTAL` decimal(12,2) NOT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `REIMB_AMT` decimal(12,2) DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  KEY `1` (`FILING_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `NAMES`
-- ----------------------------
DROP TABLE IF EXISTS `NAMES`;
CREATE TABLE `NAMES` (
  `NAMID` int(11) NOT NULL,
  `NAML` varchar(200) NOT NULL,
  `NAMF` varchar(50) NOT NULL,
  `NAMT` varchar(100) DEFAULT NULL,
  `NAMS` varchar(30) DEFAULT NULL,
  `MONIKER` varchar(30) DEFAULT NULL,
  `MONIKER_POS` varchar(9) DEFAULT NULL,
  `NAMM` varchar(20) DEFAULT NULL,
  `FULLNAME` varchar(200) NOT NULL,
  `NAML_SEARCH` varchar(200) NOT NULL,
  KEY `1` (`NAMID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii;

-- ----------------------------
--  Table structure for `RCPT_CD`
-- ----------------------------
DROP TABLE IF EXISTS `RCPT_CD`;
CREATE TABLE `RCPT_CD` (
  `AMEND_ID` int(11) NOT NULL,
  `AMOUNT` decimal(12,2) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BAL_JURIS` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NUM` varchar(7) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_DSCR` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_EMP` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `CTRIB_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_OCC` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_SELF` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CUM_OTH` decimal(12,2) DEFAULT NULL,
  `CUM_YTD` decimal(12,2) DEFAULT NULL,
  `DATE_THRU` date DEFAULT NULL,
  `DIST_NO` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(9) COLLATE ascii_bin NOT NULL,
  `INT_RATE` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `INTR_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `INTR_CMTEID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `INTR_EMP` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `INTR_OCC` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `INTR_SELF` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `OFF_S_H_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OFFIC_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `OFFICE_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `RCPT_DATE` date NOT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUP_OPP_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRAN_TYPE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` int(10) DEFAULT NULL,
  `XREF_MATCH` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `XREF_SCHNM` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  KEY `1` (`AMEND_ID`),
  KEY `2` (`FILING_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `SMRY_CD`
-- ----------------------------
DROP TABLE IF EXISTS `SMRY_CD`;
CREATE TABLE `SMRY_CD` (
  `FILING_ID` int(11) NOT NULL,
  `AMEND_ID` int(11) NOT NULL,
  `LINE_ITEM` varchar(8) COLLATE ascii_bin NOT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `FORM_TYPE` varchar(8) COLLATE ascii_bin NOT NULL,
  `AMOUNT_A` decimal(12,2) DEFAULT NULL,
  `AMOUNT_B` decimal(12,2) DEFAULT NULL,
  `AMOUNT_C` decimal(12,2) DEFAULT NULL,
  `ELEC_DT` date DEFAULT NULL,
  `current_filing` char(1) COLLATE ascii_bin DEFAULT NULL,
  KEY `1` (`FILING_ID`),
  KEY `2` (`AMEND_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `current_expn`
-- ----------------------------
DROP TABLE IF EXISTS `current_expn`;
CREATE TABLE `current_expn` (
  `AGENT_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `AMEND_ID` int(11) NOT NULL,
  `AMOUNT` decimal(12,2) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BAL_JURIS` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NUM` varchar(7) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CUM_OTH` decimal(12,2) DEFAULT NULL,
  `CUM_YTD` decimal(12,2) DEFAULT NULL,
  `DIST_NO` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_CHKNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_CODE` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_DATE` date DEFAULT NULL,
  `EXPN_DSCR` varchar(400) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(6) COLLATE ascii_bin NOT NULL,
  `G_FROM_E_F` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `OFF_S_H_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OFFIC_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `OFFICE_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUP_OPP_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `XREF_MATCH` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `XREF_SCHNM` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `current_filing` char(1) COLLATE ascii_bin DEFAULT NULL,
  KEY `1` (`FILING_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `current_rcpt`
-- ----------------------------
DROP TABLE IF EXISTS `current_rcpt`;
CREATE TABLE `current_rcpt` (
  `AMEND_ID` int(11) NOT NULL,
  `AMOUNT` decimal(12,2) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BAL_JURIS` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NUM` varchar(7) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_DSCR` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_EMP` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `CTRIB_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_OCC` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_SELF` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CUM_OTH` decimal(12,2) DEFAULT NULL,
  `CUM_YTD` decimal(12,2) DEFAULT NULL,
  `DATE_THRU` date DEFAULT NULL,
  `DIST_NO` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(9) COLLATE ascii_bin NOT NULL,
  `INT_RATE` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `INTR_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `INTR_CMTEID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `INTR_EMP` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `INTR_OCC` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `INTR_SELF` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `OFF_S_H_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OFFIC_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `OFFICE_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `RCPT_DATE` date NOT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUP_OPP_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRAN_TYPE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` int(10) DEFAULT NULL,
  `XREF_MATCH` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `XREF_SCHNM` varchar(2) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `deloitte_all_time_no_dupe_filings`
-- ----------------------------
DROP TABLE IF EXISTS `deloitte_all_time_no_dupe_filings`;
CREATE TABLE `deloitte_all_time_no_dupe_filings` (
  `FILER_ID` int(11) NOT NULL,
  `filername_name` varchar(255) COLLATE ascii_bin NOT NULL,
  `type` varchar(255) COLLATE ascii_bin NOT NULL,
  `SESSION_ID` int(11) NOT NULL,
  `AMEND_ID` int(11) NOT NULL,
  `AMOUNT` decimal(12,2) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BAL_JURIS` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NUM` varchar(7) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_DSCR` varchar(90) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_EMP` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `CTRIB_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_OCC` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_SELF` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `CTRIB_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CUM_OTH` decimal(12,2) DEFAULT NULL,
  `CUM_YTD` decimal(12,2) DEFAULT NULL,
  `DATE_THRU` date DEFAULT NULL,
  `DIST_NO` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(9) COLLATE ascii_bin NOT NULL,
  `INT_RATE` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `INTR_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `INTR_CMTEID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `INTR_EMP` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `INTR_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `INTR_OCC` varchar(60) COLLATE ascii_bin DEFAULT NULL,
  `INTR_SELF` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `INTR_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `OFF_S_H_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OFFIC_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `OFFICE_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `RCPT_DATE` date NOT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUP_OPP_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRAN_TYPE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` int(10) DEFAULT NULL,
  `XREF_MATCH` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `XREF_SCHNM` varchar(2) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `deloitte_lobby_no_dupes`
-- ----------------------------
DROP TABLE IF EXISTS `deloitte_lobby_no_dupes`;
CREATE TABLE `deloitte_lobby_no_dupes` (
  `FILER_ID` int(11) NOT NULL,
  `filername_name` varchar(255) COLLATE ascii_bin NOT NULL,
  `type` varchar(255) COLLATE ascii_bin NOT NULL,
  `FORM_ID` varchar(50) COLLATE ascii_bin NOT NULL,
  `SESSION_ID` int(11) NOT NULL,
  `ADVAN_AMT` decimal(12,2) DEFAULT NULL,
  `ADVAN_DSCR` varchar(100) COLLATE ascii_bin DEFAULT NULL,
  `AMEND_ID` int(11) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `CUM_TOTAL` decimal(12,2) NOT NULL,
  `EMPLR_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_NAML` varchar(200) COLLATE ascii_bin NOT NULL,
  `EMPLR_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_PHON` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `EMPLR_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `FEES_AMT` decimal(12,2) DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(7) COLLATE ascii_bin NOT NULL,
  `LBY_ACTVTY` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `PER_TOTAL` decimal(12,2) NOT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `REIMB_AMT` decimal(12,2) DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `fine_dining_comparison`
-- ----------------------------
DROP TABLE IF EXISTS `fine_dining_comparison`;
CREATE TABLE `fine_dining_comparison` (
  `committee_name` varchar(255) COLLATE ascii_bin DEFAULT NULL,
  `FILER_ID` int(11) NOT NULL,
  `filername_name` varchar(255) COLLATE ascii_bin NOT NULL,
  `type` varchar(255) COLLATE ascii_bin NOT NULL,
  `FILER_ID_A` int(11) NOT NULL,
  `FILER_ID_B` int(11) NOT NULL,
  `ACTIVE_FLG` varchar(1) COLLATE ascii_bin NOT NULL,
  `SESSION_ID` int(11) NOT NULL,
  `LINK_TYPE` int(11) NOT NULL,
  `LINK_DESC` varchar(255) COLLATE ascii_bin DEFAULT NULL,
  `EFFECT_DT` date NOT NULL,
  `DOMINATE_FILER` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TERMINATION_DT` date DEFAULT NULL,
  `AGENT_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `AGENT_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `AMEND_ID` int(11) NOT NULL,
  `AMOUNT` decimal(12,2) NOT NULL,
  `BAKREF_TID` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `BAL_JURIS` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NAME` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `BAL_NUM` varchar(7) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CAND_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `CMTE_ID` varchar(9) COLLATE ascii_bin DEFAULT NULL,
  `CUM_OTH` decimal(12,2) DEFAULT NULL,
  `CUM_YTD` decimal(12,2) DEFAULT NULL,
  `DIST_NO` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `ENTITY_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_CHKNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_CODE` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `EXPN_DATE` date DEFAULT NULL,
  `EXPN_DSCR` varchar(400) COLLATE ascii_bin DEFAULT NULL,
  `FILING_ID` int(11) NOT NULL,
  `FORM_TYPE` varchar(6) COLLATE ascii_bin NOT NULL,
  `G_FROM_E_F` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `JURIS_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `LINE_ITEM` int(11) NOT NULL,
  `MEMO_CODE` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `MEMO_REFNO` varchar(20) COLLATE ascii_bin DEFAULT NULL,
  `OFF_S_H_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `OFFIC_DSCR` varchar(40) COLLATE ascii_bin DEFAULT NULL,
  `OFFICE_CD` varchar(3) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `PAYEE_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `REC_TYPE` varchar(4) COLLATE ascii_bin NOT NULL,
  `SUP_OPP_CD` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `TRAN_ID` varchar(20) COLLATE ascii_bin NOT NULL,
  `TRES_ADR1` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ADR2` varchar(55) COLLATE ascii_bin DEFAULT NULL,
  `TRES_CITY` varchar(30) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMF` varchar(45) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAML` varchar(200) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMS` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_NAMT` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ST` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `TRES_ZIP4` varchar(10) COLLATE ascii_bin DEFAULT NULL,
  `XREF_MATCH` varchar(1) COLLATE ascii_bin DEFAULT NULL,
  `XREF_SCHNM` varchar(2) COLLATE ascii_bin DEFAULT NULL,
  `current_filing` char(1) COLLATE ascii_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `lk_current_filings`
-- ----------------------------
DROP TABLE IF EXISTS `lk_current_filings`;
CREATE TABLE `lk_current_filings` (
  `FILER_ID` int(11) NOT NULL,
  `FILING_ID` int(11) NOT NULL,
  `amend_id` int(11),
  `SESSION_ID` int(11) NOT NULL,
  `FORM_ID` varchar(50) COLLATE ascii_bin NOT NULL,
  KEY `1` (`FILER_ID`),
  KEY `2` (`FILING_ID`),
  KEY `3` (`amend_id`)
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `lk_current_filings_copy`
-- ----------------------------
DROP TABLE IF EXISTS `lk_current_filings_copy`;
CREATE TABLE `lk_current_filings_copy` (
  `FILER_ID` int(11) NOT NULL,
  `FILING_ID` int(11) NOT NULL,
  `amend_id` int(11) DEFAULT NULL,
  `SESSION_ID` int(11) NOT NULL,
  `FORM_ID` varchar(50) COLLATE ascii_bin NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=ascii COLLATE=ascii_bin;

-- ----------------------------
--  Table structure for `lk_filers`
-- ----------------------------
DROP TABLE IF EXISTS `lk_filers`;
CREATE TABLE `lk_filers` (
  `FILER_ID` int(11) NOT NULL,
  `filername_name` varchar(255) COLLATE ascii_bin NOT NULL,
  `type` varchar(255) COLLATE ascii_bin NOT NULL,
  `prik` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`prik`),
  KEY `1` (`FILER_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=146235 DEFAULT CHARSET=ascii COLLATE=ascii_bin;

