# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select  top 500
		  cast(rrm.[Seq] as varchar(20))              as RsId
		, convert(varchar(30), rrm.MTIME, 126)        as UpdateDateTime
    	, rrm.[RES_ID]                                as YanBaoId
    	,cast(cc.ATTR_TYPE as varchar) as KeyId
    	,dd.REF_NAME    as   KeyName
    from RES_REPORT_MAIN rrm with(nolock)
    inner join RES_QUALIFICATION cc with(nolock) on  rrm.RES_ID=cc.RES_ID   and cc.ISVALID=1
    INNER join GEN_REF  dd with(nolock) on cc.ATTR_TYPE =dd.REF_CODE    and dd.ISVALID=1 and  dd.CLS_CODE =5081
    where   rrm.ISVALID=1
      and ((rrm.MTIME = '{UpdateDateTime}' and rrm.[Seq] > '{RsId}') or (rrm.MTIME > '{UpdateDateTime}'))
    order by rrm.MTIME, rrm.[Seq]"""
