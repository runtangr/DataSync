# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 500
		  cast(rrm.[Seq] as varchar(20))              as RsId
		, convert(varchar(30), rrm.MTIME, 126)        as UpdateDateTime
    	, rrm.[RES_ID]                                as YanBaoId
    	, cast(cc.AREA as varchar)  as   AreaCode
    	, dd.NATION_NAME    as   AreaName
    from RES_REPORT_MAIN rrm with(nolock)
    inner join RES_AREA cc with(nolock) on  rrm.RES_ID=cc.RES_ID and cc.ISVALID=1
    INNER join PUB_NATION_CODE_REF dd with(nolock) on cc.AREA =dd.CODE and dd.ISVALID=1
    where rrm.ISVALID=1
      and ((rrm.MTIME = '{UpdateDateTime}' and rrm.[Seq] > '{RsId}') or (rrm.MTIME > '{UpdateDateTime}'))
    order by rrm.MTIME, rrm.[Seq]"""
