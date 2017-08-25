# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """ SELECT TOP 1000
	 a.seq AS RsId     --记录号
    , convert(varchar(30), a.MTIME, 126)  as UpdateDateTime
    -- a.MTIME AS UpdateDateTime ,
    ,(CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END ) + x.STOCKCODE AS Obj  --股票代码     
    , x.STOCKSNAME AS gpmc --股票名称 
    ,a.TRADEDATE  AS jjrq  --解禁日期
    ,a.UNLTD_VOL  AS  jjsl--解禁数量
    ,a.STK_VAL  AS jjsz--解禁股市值
    ,a.SHR_PCT  AS jjzb--占当前总股本比
    ,a.ORGCODE AS  gddm   --股东机构代码
    ,a.HOLDER_NAME AS gdmc --股东名称
    ,a.TCLOSE   AS zxsp --最新收盘价
    ,a.LTD_REAS_CODE AS xxyydm--限售原因代码
    ,a.LTD_REAS     AS xxyy --限售原因 
FROM  DERI_STK_LTD_DTL a 
INNER  JOIN STK_CODE X ON A.COMCODE = X.COMCODE AND X.ISVALID = 1
WHERE a.ISVALID=1
AND x.STATUS_TYPE_REF=1
AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > '{RsId}' ) OR ( a.MTime > '{UpdateDateTime}' ) )
ORDER BY a.MTIME,a.SEQ"""
