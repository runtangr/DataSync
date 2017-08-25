# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """select top 500
		  cast(dcc.SEQ as varchar) as RsId
		, convert(varchar(30), dcc.MTime, 126) as UpdateDateTime
		, dcc.Disc_ID as GgggId
		, dcr.CLS_CODE as ClassNo
		, dcr.CLS_NAME as ClassName
	from DISC_CLS_COM dcc with(nolock)
	inner join DISC_CLS_REF dcr with(nolock) on dcr.ISVALID = 1 and dcc.CLS_CODE = dcr.CLS_CODE
	where dcc.ISVALID = 1 and dcc.DECLAREDATE >= cast(CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01' as datetime)
	  and ((dcc.MTime = '{UpdateDateTime}' and dcc.SEQ > '{RsId}') or (dcc.MTime > '{UpdateDateTime}'))
  order by dcc.MTime asc, dcc.SEQ asc"""
