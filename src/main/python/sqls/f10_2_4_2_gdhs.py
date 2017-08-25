# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
SELECT 
      CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,
      CONVERT(VARCHAR(12),A.ENDDATE,112) AS 'Date',QKTZ20160429.dbo.Date2Str( A.ENDDATE ) AS II_Date,
      A.TOT_HOLDER AS gdzhs,
      A.AVG_NUM_QTR_GR AS hbzj,
      A.AVG_PCT_QTR_GR AS hbbh,
      A.AVG_NUM AS rjcg,
      (SELECT FL_HLD FROM STK_HOLDER_NUM WHERE COMCODE=X.COMCODE AND CHANGEDATE=A.ENDDATE) AS ltgdhs
FROM STK_CODE X with(nolock)
  INNER JOIN STK_HOLDER_NUM_IDX A with(nolock) ON X.COMCODE=A.COMCODE AND X.STOCKCODE='{STOCKCODE}'
    AND X.ISVALID=1 AND A.ISVALID=1
WHERE A.ENDDATE>=CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01'
ORDER BY ENDDATE DESC"""