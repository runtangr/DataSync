# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select  top 500
		  cast(rrm.[Seq] as varchar(20))              as RsId
		, convert(varchar(30), rrm.MTIME, 126)        as UpdateDateTime
    	, rrm.[RES_ID]                                as YanBaoId
    	, cc.INDU_NAME                             as SwIndustry
    	, cast (rrm.SW_INDU_CODE_2014  as varchar(20))as  SwIndustryCode
    from RES_REPORT_MAIN rrm with(nolock)
    inner join PUB_INDU_REF cc with(nolock) on cast(rrm.SW_INDU_CODE_2014 as varchar(50)) = cast(cc.INDU_CODE as varchar(50)) and cc.INDU_SYS_MARK=15  and  cc.ISVALID=1
    where  rrm.ISVALID=1
      and ((rrm.MTIME = '{UpdateDateTime}' and rrm.[Seq] > '{RsId}') or (rrm.MTIME > '{UpdateDateTime}'))
    order by rrm.MTIME, rrm.[Seq]"""
