
# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """SELECT  TOP 1000
		a.seq AS RsId            --记录号
		, a.MTIME AS UpdateDateTime --更新日期时间
		, (CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END ) + x.STOCKCODE AS Obj  --股票代码     
		, x.STOCKSNAME AS gpmc --股票名称    
        ,a.ENDDATE AS jzrq--截止日期 
		,QKTZ20160429.dbo.Date2Str( a.ENDDATE ) AS II_jzrq
        ,a.ORGCODE AS jgdm--机构代码
        ,c.CName AS jgmc--机构名称
        ,d.REF_CODE AS jglxdm--机构类型代码
        ,d.REF_NAME AS jgsx--机构属性
        ,a.HLD_TCAP AS cgsz--持股市值 元
        ,HLD_TOT_NUM AS cgzs--持股总数 股
        ,HLD_TOT_PCT AS zzgbb--占总股本比 %
        ,HLD_FL_NUM AS cltgsl--持流通股数量
        ,HLD_MKTCAP AS cltgsz--持流通股市值 元
        ,HLD_FL_PCT AS ltgzb--流通股占比 %
        ,a.QTR_ID  AS jdid   --季度id
    	,CASE WHEN  d.REF_CODE  IN (007,007001,007002,007003,007050,021002,021003,025,027,704,705,715,703) THEN 1--基金 
			 WHEN  d.REF_CODE  IN (001009,026,701,702)THEN 2--社保
			 WHEN  d.REF_CODE  IN (005,005001,005002,712)THEN 3 --信托
			 WHEN  d.REF_CODE  IN (006,006001,006050,013,014,711) THEN 4--证券
			 WHEN  d.REF_CODE  IN (003,003001,003002,004,714) THEN 5 --保险
			 WHEN  d.REF_CODE  IN (1,17) THEN 6--QFII
			 WHEN  d.REF_CODE  =100 THEN 10 --合计项
			 ELSE  9 END  AS  jglxfldm--其他   机构类型分类代码 
		, a.HLD_TOT_NUM-ISNULL((SELECT HLD_TOT_NUM FROM ANA_STK_HOLD_DTL 
								WHERE ISVALID=1 
								AND ORGCODE=a.ORGCODE 
									AND INNER_CODE=a.INNER_CODE 
									AND ENDDATE=(SELECT MAX(ENDDATE) FROM ANA_STK_ORG_HOLD 
												  WHERE  QTR_ID=a.QTR_ID-1  and DAY(ENDDATE) IN (30,31) )),0) cgbd
                
FROM  ANA_STK_HOLD_DTL a
INNER JOIN STK_CODE x ON a.INNER_CODE=X.INNER_CODE AND x.ISVALID=1
INNER JOIN  ORG_PROFILE c ON a.ORGCODE=c.ORGCODE AND c.ISVALID=1
LEFT JOIN  GEN_REF d  ON c.ORG_TYPE=d.REF_CODE  AND CLS_CODE IN (101,104)
WHERE a.ISVALID=1
AND DAY(ENDDATE) IN (30,31)
AND YEAR(a.ENDDATE)>=YEAR(GETDATE())-3 
AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > '{RsId}' ) OR ( a.MTime > '{UpdateDateTime}' ) )
ORDER BY a.MTIME,a.SEQ"""