# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 100
		  cast(rrm.[Seq] as varchar(20)) as RsId
		, convert(varchar(30), rrm.MTIME, 126) as UpdateDateTime
		, 'YB' as ZiXunType
    	, rrm.[RES_ID] as ZiXunId
    	, convert(varchar(30), rrm.DECLAREDATE, 112) + replace(convert(varchar(30), rrm.DECLAREDATE, 108), ':', '') as ZiXunDateTime
		,QKTZ20160429.dbo.Date2Str( rrm.DECLAREDATE ) AS II_ZiXunDateTime
    	, rrm.RPT_TITLE    as  ZiXunBiaoTi
    	, cast(rrm.RPT_ABSTRACT as nvarchar(max)) as Summary
    	, rrm.ORGNAME      as  ZiXunJiGou
    	, rrm.ANALYST      as  ZiXunZuoZhe
    from RES_REPORT_MAIN rrm with(nolock)
	where rrm.ISVALID=1
	  and ((rrm.MTIME = '{UpdateDateTime}' and rrm.[Seq] > '{RsId}') or (rrm.MTIME > '{UpdateDateTime}'))
    order by rrm.MTIME asc, rrm.[Seq] asc"""
