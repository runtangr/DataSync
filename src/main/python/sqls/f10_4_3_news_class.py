# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql="""select top 500
		  cast(ncs.[Seq] as varchar) as RsId
    	, nm.[GUID] as NewsId
		, convert(varchar(30), ncs.MTIME, 126) as UpdateDateTime
		, ncr.CLS_CODE
		, ncr.CLS_NAME
	from NEWS_CLS ncs with(nolock)
	inner join news_main nm with(nolock) on nm.ISVALID = 1 and nm.[GUID] = ncs.[GUID]
	inner join NEWS_CLS_REF ncr with(nolock) on ncr.ISVALID = 1 and ncs.CLS_CODE = ncr.CLS_CODE
	where ncs.ISVALID = 1 -- and ncs.MTIME > cast('2016-08-01' as datetime)
	  and ((ncs.MTIME = '{UpdateDateTime}' and ncs.[Seq]> '{RsId}') or (ncs.MTIME > '{UpdateDateTime}'))
  order by ncs.MTIME asc, ncs.[Seq] asc"""
