# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
SELECT 
      CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,
      CONVERT(VARCHAR(12),A.ENDDATE,112) AS 'Date',QKTZ20160429.dbo.Date2Str( A.ENDDATE ) AS II_Date,
      B.TOT_HLD AS gdrs,
      A.RANK AS xh,
      A.NAME AS gdmc,
      A.SHR_NUM/10000 AS cgs,
      ROUND(A.SHR_NUM*A.HOLD_PCT/A.HOLD_NUM,4) AS zzgs,
      ISNULL(A.ADD_NUM/10000,0) AS zjqk,
      A.SHR_CLS_NAME AS gbxz,
      A.COMCODE AS gsdm
FROM STK_CODE X with(nolock)
  INNER JOIN STK_SHR_CLS_DTL A with(nolock) ON X.COMCODE=A.COMCODE AND X.STOCKCODE='{STOCKCODE}'
    AND X.ISVALID=1 AND A.ISVALID=1
  INNER JOIN STK_HOLDER_NUM B with(nolock) ON X.COMCODE=B.COMCODE AND B.ISVALID=1
    AND A.ENDDATE=B.CHANGEDATE
WHERE A.ENDDATE>=CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01'
ORDER BY ENDDATE DESC,RANK ASC"""
