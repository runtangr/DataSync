# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """select top 500
		  cast(rrm.[Seq] as varchar(20)) as RsId
		, convert(varchar(30), rrm.MTIME, 126) as UpdateDateTime
    	, rrm.[RES_ID] as YanBaoId
    	,cast (rrm.rpt_type as varchar(20))       as  ClassNo
    	,rrm.RPT_TYPE_NAME  as ClassName
    from RES_REPORT_MAIN rrm with(nolock)
    where  rrm.ISVALID=1
      and ((rrm.MTIME = '{UpdateDateTime}' and rrm.[Seq] > '{RsId}') or (rrm.MTIME > '{UpdateDateTime}'))
    order by rrm.MTIME, rrm.[Seq]"""
