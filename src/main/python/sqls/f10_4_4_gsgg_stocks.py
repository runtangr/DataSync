# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """select top 500
		  cast(dco.SEQ as varchar) as RsId
		, convert(varchar(30), dco.MTime, 126) as UpdateDateTime
		, dco.Disc_ID as GgggId
		, case when stk.Trade_mkt_ref = 1 then 'SZ'
		       when stk.Trade_mkt_ref = 2 then 'SH'
			   else cast(stk.Trade_mkt_ref as varchar) + '-'
			   end + stk.STOCKCODE as StockCode
		, stk.STOCKSNAME as StockName
	from DISC_COM dco with(nolock)
	inner join STK_CODE stk with(nolock) on stk.ISVALID = 1 and stk.COMCODE = dco.COMCODE
	where dco.ISVALID = 1 and dco.DECLAREDATE >= cast(CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01' as datetime)
	  and ((dco.MTime = '{UpdateDateTime}' and dco.SEQ > '{RsId}') or (dco.MTime > '{UpdateDateTime}'))
  order by dco.MTime asc, dco.SEQ asc"""
