# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT
      CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,
      CONVERT(VARCHAR(12),A.CHANGEDATE,112) AS 'Date',QKTZ20160429.dbo.Date2Str( A.CHANGEDATE ) AS II_Date,
      A.TOTAL/10000 AS zgb,
      (CASE X.STK_TYPE_REF WHEN 1 THEN A.FL_ASHR WHEN 2 THEN A.B_SHR END)/10000 AS ltgbdq,
      A.FL_SHR/10000 AS ltgf,
      A.FL_ASHR/10000 AS ltag,
      A.B_SHR/10000 AS ltbg,
      A.H_SHR/10000 AS lthg,
      A.OTH_FL/10000 AS qtltgf,
      A.TOT_LTDFL/10000 AS xsltg,
      (A.FL_ASHR-A.LIST_FL_ASHR)/10000 AS xsltag,
      NULL AS xsltbg,
      NULL AS xslthg,
      A.STATE/10000 AS xsgjcg,
      A.STATE_LEG/10000 AS xsgyfrcg,
      A.DOM_LEG/10000 AS xsjnfrcg,
      A.DOM_NATURAL/10000 AS xsjnzrrcg,
      A.MNG_NONFL/10000 AS xsggcg,
      A.FRGN_LEG/10000 AS xsjwfrcg,
      A.FRGN_NATURAL/10000 AS xsjwzrrcg,
      A.TOT_NONFL/10000 AS wltg,
      A.STATE/10000 AS gjg,
      A.STATE_LEG/10000 AS gyfrg,
      A.DOM_LEG/10000 AS jnfgyfr,
      A.TRANS/10000 AS zpg,
      A.INNER_EMPL/10000 AS nbzgg,
      A.PREF/10000 AS yxg,
      A.FRGN_LEG/10000 AS jwfrg,
      A.OTH_NONFL/10000 AS qtwltgf
FROM STK_CODE X with(nolock)
  INNER JOIN STK_SHR_STRU A with(nolock) ON X.COMCODE=A.COMCODE AND X.STOCKCODE='{STOCKCODE}'
    AND X.ISVALID=1 AND A.ISVALID=1
WHERE A.CHANGEDATE>=CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01'"""
