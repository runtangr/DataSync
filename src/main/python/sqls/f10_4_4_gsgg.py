# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """select top 500
		  cast(dmc.SEQ as varchar) as RsId
		, convert(varchar(30), dmc.MTime, 126) as UpdateDateTime
		, dmc.Disc_ID as GgggId
		, convert(varchar(30), dmc.DECLAREDATE, 112) + replace(convert(varchar(30), dmc.DECLAREDATE, 108), ':', '') as [DateTime]
		,QKTZ20160429.dbo.Date2Str( dmc.DECLAREDATE ) AS II_DateTime
		, dmc.Title
		, convert(varchar(30), dmc.EndDate, 112) as EndDate
		,QKTZ20160429.dbo.Date2Str( dmc.ENDDATE ) AS II_EndDate
		, cast(dmc.Is_Acce as varchar) as IsHaveAttach
		, cast(dmc.Is_Content as varchar) as IsHaveContent
		, dmc.[Source]
	from DISC_MAIN_COM dmc with(nolock)
	where dmc.ISVALID = 1 and dmc.DECLAREDATE >= cast(CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01' as datetime)
	  and ((dmc.MTime = '{UpdateDateTime}' and dmc.SEQ > '{RsId}') or (dmc.MTime > '{UpdateDateTime}'))
  order by dmc.MTime asc, dmc.SEQ asc"""
