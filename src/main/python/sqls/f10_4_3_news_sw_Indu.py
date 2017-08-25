# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 500
		  cast(nir.[Seq] as varchar) as RsId
    	, nm.[GUID] as NewsId
		, convert(varchar(30), nir.MTIME, 126) as UpdateDateTime
		, pir.Indu_Code as SwIndustryCode
		, pir.Indu_Name as SwIndustry
	from NEWS_INDU_RELA nir with(nolock)
	inner join news_main nm with(nolock) on nm.ISVALID = 1 and nm.[GUID] = nir.[GUID]
	inner join PUB_INDU_REF pir with(nolock) on pir.ISVALID = 1 and pir.INDU_SYS_MARK = 15 and pir.INNER_CODE = nir.SW_INNER_CODE_2014
	where nir.ISVALID = 1 -- and nir.MTIME > cast('2016-08-01' as datetime)
	  and ((nir.MTIME = '{UpdateDateTime}' and nir.[Seq] > '{RsId}') or (nir.MTIME > '{UpdateDateTime}'))
  order by nir.MTIME asc, nir.[Seq] asc"""
