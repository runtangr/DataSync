# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
SELECT 
      CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj, 
      STUFF((SELECT ','+ CTRL_NAME FROM STK_ACT_CTRL_INFO 
       WHERE COMCODE=X.COMCODE AND ISVALID=1 
            AND ENDDATE=(SELECT MAX(ENDDATE) FROM STK_CTRL_HLD_INFO WHERE COMCODE=X.COMCODE AND ISVALID=1) 
       FOR XML PATH('')),1,1,'') AS mc,
       '' AS sm
FROM STK_CODE X with(nolock)
WHERE X.STOCKCODE='{STOCKCODE}' AND X.ISVALID=1"""
