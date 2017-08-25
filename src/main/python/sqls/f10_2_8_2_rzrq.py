# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
SELECT TOP 100
      A.GPSC+A.GPDM AS Obj
    , A.JZRQ AS 'Date'
	,QKTZ20160429.dbo.Date2Str( A.JZRQ ) AS II_Date
    , ROUND(A.rzmrje/10000.0,4) AS rzmrje
    , ROUND(A.rzchje/10000.0,4) AS rzchje
    , ROUND(A.rzye/10000.0,4) AS rzye
    , ROUND(A.rqmcl/10000.0,4) AS rqmcl
    , ROUND(A.rqchl/10000.0,4) AS rqchl
    , ROUND(A.rqyl/10000.0,4) AS rqyl
    , ROUND(A.rqmcje/10000.0,4) AS rqmcje
    , ROUND(A.rqchje/10000.0,4) AS rqchje
    , ROUND(A.rqye/10000.0,4) AS rqye
    , ROUND(A.rzrqye/10000.0,4) AS rzrqye
    , ROUND(A.ltgb/10000.0,4) AS ltgb
    , ROUND(A.spj, 4) as spj
    , ROUND(A.rzyezs, 4) as rzyezs
    , ROUND(A.rzyezltszb, 4) as rzyezltszb
    , A.UpdateTime AS UpdateDateTime
    -- , A.ID as RsId
    , cast(A.ID as varchar) as RsId
FROM StockStaticData..T_RZRQ_JYMX A with(nolock)
WHERE ((UpdateTime='{UpdateDateTime}' and A.ID > '{RsId}') or (UpdateTime>'{UpdateDateTime}'))
order by A.UpdateTime, A.ID


/*

SELECT  TOP 100 
        CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,
        CONVERT(VARCHAR(12),A.TRADEDATE,112) AS 'Date',
        ROUND(A.BUY_BALANCE/10000,4) AS rzje,
        ROUND(A.BUY_VALUE/10000,4) AS rzmre,
        ROUND(A.SELL_BALANCE_VOL/10000,4) AS rqyl,        
        ROUND(A.SELL_BALANCE_VAL/10000,4) AS rqye,
        ROUND(A.SELL_VALUE/10000,4) AS rqmcl,
        A.MTIME AS UpdateDateTime
FROM STK_CODE X
  INNER JOIN Genius2..MARGIN_TRD_DTL A ON X.INNER_CODE=A.INNER_CODE
    AND X.ISVALID=1 AND A.ISVALID=1
WHERE A.MTIME>=@UpdateDateTime
ORDER BY A.MTIME ASC
*/"""
