# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 1000
	  cast(a.seq as varchar) AS RsId            --记录号
	, a.MTIME AS UpdateDateTime --更新日期时间
    , (CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END ) + x.STOCKCODE AS Obj  --股票代码     
    , x.STOCKSNAME AS gpmc --股票名称     
	, a.ENDDATE AS jzrq --截止日期
	,QKTZ20160429.dbo.Date2Str( a.ENDDATE ) AS II_jzrq
	, a.ORG_TYPE AS jglxdm--机构类型代码
	, HLD_ORG_NUM AS cgsl--持股机构数量
	, HLD_FL_NUM_END AS qmltgs--期末持流通股数量 股
	, HLD_FL_PCT_END AS qmltgbl --期末持流通股比例
	, HLD_TCAP_END AS qmcgzsz--期末持股总市值
	, HLD_TOT_NUM_END AS qmcgzsl--期末持股总数量
	, HLD_TOT_PCT_END AS qmzcgbl--期末总持股比例
	, CASE WHEN  a.ORG_TYPE  IN (007,007001,007002,007003,007050,021002,021003,025,027,704,705,715,703) THEN 1--基金 
		 WHEN  a.ORG_TYPE  IN (001009,026,701,702)THEN 2--社保
		 WHEN  a.ORG_TYPE  IN (005,005001,005002,712)THEN 3 --信托
		 WHEN  a.ORG_TYPE  IN (006,006001,006050,013,014,711) THEN 4--证券
		 WHEN  a.ORG_TYPE  IN (003,003001,003002,004,714) THEN 5 --保险
		 WHEN  a.ORG_TYPE  IN (1,17) THEN 6--QFII
		 WHEN  a.ORG_TYPE  =100 THEN 10 --合计项
		 ELSE  9 END  jglxfldm--其他   机构类型分类代码 
	, a.HLD_TOT_NUM_END-ISNULL((SELECT HLD_TOT_NUM_END FROM QKTZ20160429.dbo.ANA_STK_ORG_HOLD
									WHERE ISVALID=1  
									AND ORG_TYPE=a.ORG_TYPE 
									AND INNER_CODE=a.INNER_CODE 
									AND ENDDATE=(SELECT MAX(ENDDATE) FROM QKTZ20160429.dbo.ANA_STK_ORG_HOLD
												  WHERE  QTR_ID=a.QTR_ID-1  and DAY(ENDDATE) IN (30,31) )),0) cgbd --持股变动   
FROM  QKTZ20160429.dbo.ANA_STK_ORG_HOLD a
INNER JOIN QKTZ20160429.dbo.STK_CODE x ON a.INNER_CODE=X.INNER_CODE AND x.ISVALID=1
LEFT JOIN   QKTZ20160429.dbo.GEN_REF c  ON a.ORG_TYPE=c.REF_CODE  AND CLS_CODE IN (101,104)
WHERE a.ISVALID=1
AND YEAR(a.ENDDATE)>=YEAR(GETDATE())-1
AND DAY(a.ENDDATE) IN (30,31)
AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > '{RsId}' ) OR ( a.MTime > '{UpdateDateTime}' ) )
ORDER BY a.MTIME,a.SEQ"""