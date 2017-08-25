# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """ SELECT top 1000 
	a.seq AS RsId 
   , convert(varchar(30), a.MTIME, 126)  as UpdateDateTime
   -- a.MTIME AS UpdateDateTime ,
   ,(CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END ) + x.STOCKCODE AS Obj  --股票代码     
   , x.STOCKSNAME AS gpmc --股票名称
   , ADD_CODE     AS jgdm  --机构代码   
   ,ADD_NAME AS zjcrmc--增减持人名称
   ,ADD_NUM AS zjcsl--增减持数量   股
   ,ADD_PCT AS zjczb--增减持占比
   ,ADD_SUB_CLS AS  zjcfs  --增减持方式代码
   ,CASE  ADD_SUB_CLS WHEN 1 THEN '大宗交易'
					  WHEN 2 THEN '二级市场买卖'
					  WHEN 3 THEN  '大宗交易和二级市场买卖'
					  WHEN 4 THEN  '司法扣划' 
					  ELSE '其它' END AS  zjyfsmc --增减持方式 
   ,ADD_SUB_TYPE   AS zjclb              --增减持类别代码 
   ,CASE ADD_SUB_TYPE WHEN 1 THEN '增持'
					  WHEN 2 THEN '减持' 
					  ELSE '其他' END   AS zjylbmc   --增减持类别  
   ,AVG_PRC AS	 zjcjj    --增减持均价  元/股
   ,BEF_HOLD_NUM AS qcgs--前持有股数
   ,BEF_HOLD_PCT AS  qczb--前持有占比 %
   ,CAP_NAME   AS  yzxdr--一致行动人
   ,DECLAREDATE  AS ggrq--公告日期
   ,QKTZ20160429.dbo.Date2Str( DECLAREDATE ) AS II_ggrq
   ,DISC_ID   AS ggid  --公告ID
   ,END_HOLD_NUM  AS hcgs --后持股数
   ,END_HOLD_PCT  AS hczb --后持股比例
   ,ENDDATE       AS  zjcjzr --增减持截止日
   ,QKTZ20160429.dbo.Date2Str( ENDDATE ) AS II_zjcjzr
   ,CASE IS_FIRST_HOLDER WHEN 3  THEN '不详'
			             WHEN 1 THEN  '是'
			             WHEN 2 THEN  '否'
			             ELSE '不适用' END as sfdydgd --是否为第一大股东
    ,a.PRG    AS jz       --进展
FROM STK_ADD_HOLD a
INNER  JOIN STK_CODE X ON A.COMCODE = X.COMCODE AND X.ISVALID = 1
WHERE a.ISVALID=1
	AND X.STK_TYPE_REF=1
        AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > '{RsId}' ) OR ( a.MTime > '{UpdateDateTime}' ) )
ORDER BY a.MTIME,a.SEQ"""
