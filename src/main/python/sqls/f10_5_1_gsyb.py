# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 500
		  cast(rrm.[Seq] as varchar(20)) as RsId
		, convert(varchar(30), rrm.MTIME, 126) as UpdateDateTime
    	, rrm.[RES_ID] as YanBaoId
    	, convert(varchar(30), rrm.DECLAREDATE, 112) + replace(convert(varchar(30), rrm.DECLAREDATE, 108), ':', '')   as  BaoGaoRiQi
		,QKTZ20160429.dbo.Date2Str( rrm.DECLAREDATE ) AS II_BaoGaoRiQi
    	, rrm.ORGNAME      as  YanJiuJiGou
    	, rrm.ANALYST      as  YanJiuZuoZhe
    	, rrm.RPT_TITLE    as  YanBaoBiaoTi
    	, cast(rrm.RPT_ABSTRACT as nvarchar(max)) as Summary

    from RES_REPORT_MAIN rrm with(nolock)
    where rrm.ISVALID=1
      and ((rrm.MTIME = '{UpdateDateTime}' and rrm.[Seq] > '{RsId}') or (rrm.MTIME > '{UpdateDateTime}'))
    order by rrm.MTIME asc, rrm.[Seq] asc"""
