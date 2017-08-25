#-*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 2000
		a.SEQ AS RsId,
		a.MTIME  AS UpdateDateTime,
		CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,--股票代码
		X.StocksName as gpmc,
        a.DECLAREDATE ggrq,  --公告日期
		QKTZ20160429.dbo.Date2Str( a.DECLAREDATE ) AS II_ggrq,
        a.ENDDATE jzrq,      --截止日期
		 QKTZ20160429.dbo.Date2Str( a.ENDDATE ) AS II_jzrq,
        a.FORE_CLS_CODE ycdm,--预测代码
        a.FORE_CLS yclx,   --预测类型
        a.SRC ggly,       --公告来源
        a.SUMMARY yzzy,   --预测摘要
        a.CONTENT jtnr,   --具体内容
        a.REASON yysm,     --原因说明      
        a.NTINC_GR_CEIL jlytbsx,--净利润同比增长上限 %
        a.NTINC_GR_FLOR jlytbxx,--净利润同比增长下限 %
        a.PREVIOUS_EPS qntqsy, --去年同期每股收益
        a.PREVIOUS_NET_PROFIT qntqlr,--去年同期净利润
        a.EPS_CEIL yjmgsysx, --预计每股收益上限
        a.EPS_FLOR yjmgsyxx--预计每股收益下限
FROM  STK_ACHIEVE_FORECAST a
INNER JOIN STK_CODE x ON a.comcode=X.comcode AND x.ISVALID=1 and X.STK_TYPE_REF = 1  
WHERE a.ISVALID=1
AND a.CHNG='否'
AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > '{RsId}' ) OR ( a.MTime > '{UpdateDateTime}'  ) )
ORDER BY a.MTIME,a.SEQ"""
