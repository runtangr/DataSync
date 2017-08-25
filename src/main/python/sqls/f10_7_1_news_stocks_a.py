# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """select top 500
		  cast(nsk.[Seq] as varchar) as RsId
    	, nm.[GUID] as ZiXunId
    	, 'XW' as ZiXunType
		, convert(varchar(30), nsk.MTIME, 126) as UpdateDateTime
		, case when stk.Trade_mkt_ref = 1 then 'SZ'
		       when stk.Trade_mkt_ref = 2 then 'SH'
			   else cast(stk.Trade_mkt_ref as varchar) + '-'
			   end + stk.StockCode as StockCode
		, stk.StocksName as StockName
	from NEWS_STK nsk with(nolock)
	inner join news_main nm with(nolock) on nm.ISVALID = 1 and nm.[GUID] = nsk.[GUID]
	inner join STK_CODE stk with(nolock) on stk.ISVALID = 1 and stk.INNER_CODE = nsk.A_Inner_Code
	where nsk.ISVALID = 1 -- and nsk.MTIME > cast('2016-08-01' as datetime)
	  and ((nsk.MTIME = '{UpdateDateTime}' and nsk.[Seq] > '{RsId}') or (nsk.MTIME > '{UpdateDateTime}'))
  order by nsk.MTIME asc, nsk.[Seq] asc"""
