# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 50
		  cast(nc.[seq] as varchar) as RsId
		, nc.[GUID] as NewsId
		, convert(varchar(30), nc.MTIME, 126) as UpdateDateTime
		, '' AS AttachmentUrl
		, '' AS AttachmentPath
		, '' AS AttachmentPathMd5
		, cast(nc.TXT_CONTENT as nvarchar(max)) as ContentText
		, cast(nc.HTML_TXT as nvarchar(max)) as ContentHtml
	from NEWS_CONTENT nc with(nolock)
    where nc.ISVALID = 1 -- and nc.MTIME > cast('2016-08-01' as datetime)
      and ((nc.MTIME = '{UpdateDateTime}' and nc.[seq] > '{RsId}') or (nc.MTIME > '{UpdateDateTime}'))
  order by nc.MTIME, nc.[seq]"""
