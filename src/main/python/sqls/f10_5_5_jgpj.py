# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 1000  
		cast(a.SEQ as varchar) AS RsId,   --记录号
        a.MTIME  AS UpdateDateTime,  --更新日期时间
		CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,--股票代码
		x.STOCKSNAME AS gpmc, --股票名称		
        c.DECLAREDATE  AS fbrq,--发布日期 
		QKTZ20160429.dbo.Date2Str( c.DECLAREDATE ) AS II_fbrq,
        a.INVEST_RATING  AS tzpj,  --投资评级
        a.LAST_RATING AS qtzpj, --前一次评级
        a.ISFIRST AS sfscpj,  --是否首次评级
        a.RATING_CHG AS pjbh,--评级变化
        a.EXPECT_PRICE AS mbjg,    --目标价格
        a.EXPECT_PRICE_PERIOD AS mbjgqx,--目标价格期限
        a.INVEST_RATING_SRC  AS yspj, --原始评级
        c.INDU_NAME AS hymc,--行业名称
        c.ORGCODE  AS yjjcdm,--研究机构代码
        c.ORGNAME AS yjjgmc--研究机构名称
        FROM QKTZ20160429.dbo.RES_COM_INVEST_RATING a with(nolock)
        INNER JOIN  QKTZ20160429.dbo.STK_CODE x with(nolock) ON a.INNER_CODE=X.INNER_CODE and x.STK_TYPE_REF = 1
        INNER JOIN QKTZ20160429.dbo.res_report_main c with(nolock) ON  a.RES_ID=c.RES_ID
        WHERE  a.ISVALID=1
		AND YEAR(c.declaredate)>YEAR(GETDATE())-3
		AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > '{RsId}' ) OR ( a.MTime > '{UpdateDateTime}' ) )
        ORDER BY a.MTIME,a.SEQ"""