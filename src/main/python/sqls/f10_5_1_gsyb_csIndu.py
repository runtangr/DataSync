# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """select  top 500
		  cast(rrm.[Seq] as varchar(20)) as RsId
		, convert(varchar(30), rrm.MTIME, 126) as UpdateDateTime
    	, rrm.[RES_ID] as YanBaoId
    	,cc.INDU_NAME    as CsrcIndustry
    	,cast (rrm.CSRC_INDU_CODE_2012  as varchar(20))       as  CsrcIndustryCode
    from RES_REPORT_MAIN rrm with(nolock)
    inner join PUB_INDU_REF cc with(nolock) on rrm.CSRC_INDU_CODE_2012=cc.INDU_CODE and  cc.ISVALID=1 and cc.INDU_SYS_MARK=14
    where rrm.ISVALID=1
      and ((rrm.MTIME = '{UpdateDateTime}' and rrm.[Seq] > '{RsId}') or (rrm.MTIME > '{UpdateDateTime}'))
    order by rrm.MTIME, rrm.[Seq]"""
