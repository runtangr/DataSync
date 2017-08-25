# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT top 1000    
      a.seq AS RsId
    , convert(varchar(30), a.MTIME, 126)  as UpdateDateTime
    , ( CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END ) + a.STOCKCODE as Obj
	, a.STOCKSNAME as gpmc
	, a.LIST_DATE as ssrq
	,QKTZ20160429.dbo.Date2Str( a.LIST_DATE ) AS II_ssrq
	, a.FIR_VOL as srsssl  --首日上市数量
    , a.TOPEN as srkpj    --上市首日开盘价
    , a.THIGH as srzgj    --上市首日最高价
    , a.TLOW as srzdj      --上市首日最低价
    , a.TCLOSE as ssspj     --上市首日收盘价
    , a.FIR_AVG_PRC as srcjjj--上市首日成交均价
    , a.TVOLUME as srcjl    --上市首日成交量
    , a.TVALUE as srcje     --上市首日成交额
    , a.CHNG_PCT as srzdf   --上市首日涨跌幅
    , a.EXCHR as srhsl      --上市首日换手率
    , a.PLY_YIELD as dxsyl  --打新收益率
    , 0 as lxztts  --连续涨停天数
    , 11.11 as zhztspj	--最后涨停日收盘价
    , 22.22 as zhztsyl	--最后涨停日打新收益率
FROM  STK_LIST_PERFORM a with(nolock)
LEFT JOIN STK_CODE X with(nolock) ON A.INNER_CODE = X.INNER_CODE AND X.ISVALID = 1
WHERE a.ISVALID = 1
	AND x.STK_TYPE='A股'
        AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > {RsId} ) OR ( a.MTime > '{UpdateDateTime}' ) )
ORDER BY a.MTIME,a.SEQ"""
