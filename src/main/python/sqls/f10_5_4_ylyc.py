# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """SELECT      
				CAST(a.SEQ AS VARCHAR(20)) AS RsId,--记录号
				a.MTIME  AS UpdateDateTime,--更新日期时间
				CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,--股票代码		
			    x.STOCKSNAME AS gpmc, --股票名称     
                a.FORECAST_YEAR AS ycnd,  --预测年度
                a.EPS_P1 AS mgsy1, --每股收益(首个预测年份)
                a.EPS_P2 AS  mgsy2 ,--每股收益(第二个预测年份)
                a.EPS_P3 AS mgsy3,--每股收益(第三个预测年份)
                a.SALES_P1 AS yysy1,--营业收入（首个预测年份）
                a.SALES_P2 AS yysy2 ,--营业收入（第二个预测年份）
                a.SALES_P3 AS yysy3,--营业收入（第三个预测年份）          
                a.NP_P1 AS jly1,--净利润(首个预测年份)
                a.NP_P2 AS jly2,--净利润(第二个预测年份)
                a.NP_P3 AS jly3--净利润(第三个预测年份)                 
                
FROM    QKTZ20160429.dbo.RES_COM_PFT_FCST a
        INNER JOIN QKTZ20160429.dbo.STK_CODE x ON a.INNER_CODE = X.INNER_CODE
WHERE  
       a.ISVALID = 1
AND a.FORECAST_YEAR=(SELECT MAX(FORECAST_YEAR) FROM  QKTZ20160429.dbo.RES_COM_PFT_FCST  WHERE INNER_CODE=a.INNER_CODE AND ISVALID=1)
AND a.MTIME=(SELECT MAX(MTIME) FROM  QKTZ20160429.dbo.RES_COM_PFT_FCST
			 WHERE INNER_CODE=a.INNER_CODE 
			 AND  ISVALID=1
			 AND SALES_P1 IS NOT NULL 
			 AND NP_P1 IS NOT null )
AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > '{RsId}' ) OR ( a.MTime > '{UpdateDateTime}' ) )
ORDER BY a.MTIME,a.SEQ"""


