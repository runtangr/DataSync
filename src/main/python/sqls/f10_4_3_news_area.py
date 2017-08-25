# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 500
		  cast(nar.[Seq] as varchar) as RsId
    	, nm.[GUID] as NewsId
		, convert(varchar(30), nar.MTIME, 126) as UpdateDateTime
		, fai.AREACODE as AreaCode
		, fai.AREAName as AreaName
	from NEWS_AREA nar with(nolock)
	inner join news_main nm with(nolock) on nm.ISVALID = 1 and nm.[GUID] = nar.[GUID]
	inner join FUT_AREA_INFO fai with(nolock) on fai.ISVALID = 1 and fai.AreaCode = nar.AREACODE
	where nar.ISVALID = 1 -- and nar.MTIME > cast('2016-08-01' as datetime)
	  and ((nar.MTIME = '{UpdateDateTime}' and nar.[Seq] > '{RsId}') or (nar.MTIME > '{UpdateDateTime}'))
  order by nar.MTIME asc, nar.[Seq]asc"""
