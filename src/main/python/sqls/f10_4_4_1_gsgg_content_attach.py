# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 500
		  cast(dcc.SEQ as varchar) as RsId
		, convert(varchar(30), dcc.MTime, 126) as UpdateDateTime
		, dcc.Disc_ID as GgggId
		, '' as AttachmentUrl
		, dcc.ACCE_ROUTE as AttachmentPath
		, dcc.ACCE_ROUTE_MD5 as AttachmentPathMd5
		, dcc.ACCE_TITLE as AttachmentTitle
		, dcc.ACCE_TYPE as AttachmentType
	from DISC_ACCE_COM dcc with(nolock)
	where dcc.ISVALID = 1
	  and ((dcc.MTime = '{UpdateDateTime}' and dcc.SEQ > '{RsId}') or (dcc.MTime > '{UpdateDateTime}'))
  order by dcc.MTime asc, dcc.SEQ asc"""
