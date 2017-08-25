# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 500
		  cast(nke.[Seq] as varchar) as RsId
    	, nm.[GUID] as NewsId
		, convert(varchar(30), nke.MTIME, 126) as UpdateDateTime
		, cast(nkr.[KEY_ID] as varchar) as KeyId
		, nkr.[key_name] as KeyName
	from NEWS_KEY nke with(nolock)
	inner join news_main nm with(nolock) on nm.ISVALID = 1 and nm.[GUID] = nke.[GUID]
	inner join NEWS_KEY_REF nkr with(nolock) on nkr.ISVALID = 1 and nkr.[Key_ID] = nke.[Key_ID]
	where nke.ISVALID = 1 -- and nke.MTIME > cast('2016-08-01' as datetime)
	  and ((nke.MTIME = '{UpdateDateTime}' and nke.[Seq] > '{RsId}') or (nke.MTIME > '{UpdateDateTime}'))
  order by nke.MTIME asc, nke.[Seq] asc"""
