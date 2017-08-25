# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 5000 
        a.SEQ AS RsId,
		a.MTIME  AS UpdateDateTime,
		CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,--股票代码
		X.StocksName as gpmc    --股票名称
		, A.DECLAREDATE    AS ggrq       --公告日期
		,QKTZ20160429.dbo.Date2Str(a.DECLAREDATE) AS II_ggrq
		, A.REVIEW_CONTENT   AS pjnr    --评价内容
		, A.SOURCE_NAME      AS ly   --来源
 FROM	 NEWS_COM_REVIEW a
INNER JOIN STK_CODE x ON a.STOCKCODE=X.STOCKCODE AND x.ISVALID=1 and X.STK_TYPE_REF = 1  
AND a.ISVALID=1 
 WHERE ( ( a.MTIME = '{UpdateDateTime}'  AND a.SEQ > {RsId} ) OR ( a.MTIME > '{UpdateDateTime}'  ) )
ORDER BY a.MTIME,a.SEQ"""
