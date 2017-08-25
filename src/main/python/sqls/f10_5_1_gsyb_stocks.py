# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select  top 500
		  cast(rrm.[Seq] as varchar(20)) as RsId
		, convert(varchar(30), rrm.MTIME, 126) as UpdateDateTime
    	, rrm.[RES_ID]  as YanBaoId
    	, case when dd.MKT_TYPE = 1 then 'SZ'
		       when dd.MKT_TYPE = 2 then 'SH'
			   else cast(dd.MKT_TYPE as varchar(20)) + '-'
			   end + dd.SEC_CODE    as StockCode
    	, dd.SEC_SNAME  AS StockName
    from RES_REPORT_MAIN rrm with(nolock)
    inner join RES_SEC_CODE cc with(nolock)  on rrm.RES_ID =cc.RES_ID  and  cc.ISVALID=1
    inner join PUB_SEC_CODE dd with(nolock) on cc.INNER_CODE=dd.INNER_CODE  and dd.ISVALID=1  and dd.SEC_SNAME is not null
    where  rrm.ISVALID=1
      and ((rrm.MTIME = '{UpdateDateTime}' and rrm.[Seq] > '{RsId}') or (rrm.MTIME > '{UpdateDateTime}'))
    order by rrm.MTIME, rrm.[Seq]"""
