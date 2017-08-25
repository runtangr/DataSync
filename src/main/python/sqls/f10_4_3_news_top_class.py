# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 100
	RsId,NewsId,UpdateDateTime,CLS_CODE,CLS_NAME
from (
	select distinct
		  cast(ncs.[Seq] as varchar) as RsId
    	, nm.[GUID] as NewsId
		, convert(varchar(30), ncs.MTIME, 126) as UpdateDateTime
		, ncr.CLS_CODE
		, ncr.CLS_NAME
	from NEWS_CLS ncs with(nolock) 
	inner join news_main nm with(nolock) on nm.ISVALID = 1 and nm.[GUID] = ncs.[GUID]
	inner join NEWS_CLS_REF ncr with(nolock) on ncr.ISVALID = 1 and left(ncs.CLS_CODE, 3) = ncr.CLS_CODE
	where ncs.ISVALID = 1 and len(ncs.CLS_CODE) > 3 /* and ncs.MTIME > cast('2016-08-01' as datetime)*/
) a where ((a.UpdateDateTime = '{UpdateDateTime}' and a.RsId > '{RsId}') or (a.UpdateDateTime > '{UpdateDateTime}'))
order by a.UpdateDateTime asc, a.RsId asc"""
