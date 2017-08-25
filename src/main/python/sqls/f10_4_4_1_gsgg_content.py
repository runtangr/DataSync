# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 100
		  cast(dcc.SEQ as varchar) as RsId
		, cast(convert(varchar(30), dcc.MTime, 126) as datetime) as UpdateDateTime
		, dcc.Disc_ID as GgggId
--		, convert(varchar(30), dmc.DECLAREDATE, 112) + replace(convert(varchar(30), dmc.DECLAREDATE, 108), ':', '') as [DateTime]
--		, dmc.Title
		, case when datalength(dcc.TXT_CONTENT) > 1024 * 1024 then cast(dcc.TXT_CONTENT as nvarchar(4000))
		       else cast(dcc.TXT_CONTENT as nvarchar(max))
		       end as ContentText
--		, cast(dcc.TXT_CONTENT as nvarchar(100)) as Summary
	from DISC_CONTENT_COM dcc with(nolock)
--	inner join DISC_MAIN_COM dmc with(nolock) on dmc.ISVALID = 1 and dmc.Disc_ID = dcc.Disc_ID
	where dcc.ISVALID = 1 -- and dmc.DECLAREDATE >= cast(CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01' as datetime)
	  and ((dcc.MTime = '{UpdateDateTime}' and dcc.SEQ > '{RsId}') or (dcc.MTime > '{UpdateDateTime}'))
	order by dcc.MTime asc, dcc.SEQ asc"""
