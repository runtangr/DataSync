# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 500
		  cast(nm.[Seq] as varchar) as RsId
    , nm.[GUID] as NewsId
		, convert(varchar(30), nm.MTIME, 126) as UpdateDateTime
		, convert(varchar(30), nm.DECLAREDATE, 112) + replace(convert(varchar(30), nm.DECLAREDATE, 108), ':', '') as [DateTime]
		,QKTZ20160429.dbo.Date2Str( nm.DECLAREDATE ) AS II_DateTime
		, cast(nm.TITLE_MAIN as nvarchar(max)) as TitleMain
		, cast(nm.TITLE_SUB as nvarchar(max)) as TitleSub
		, cast(nm.TITLE_APP as nvarchar(max)) as TitleApp
		, cast(nm.AUTOR as nvarchar(max)) as Author
		, cast(nm.AUTOR_UNIT as nvarchar(max)) as AuthorUnit
		, cast(pis.Src_Name as nvarchar(max)) as [Source]
		, nm.CONTENT_URL as SourceUrl
		, cast(nm.SUMMARY as nvarchar(max)) as Summary
		, IsNull(nm.IS_HAND, '') as SummaryStatus
		, nm.IS_HEADLINE as IsHeadLine
		, ngm.Ref_Name as NegaPosiMark
	from news_main nm with(nolock)
	left join PUB_INFOR_SRC pis with(nolock) on pis.ISVALID = 1 and nm.SRC_CODE = pis.SRC_CODE
	left join GEN_REF ngm with(nolock) on ngm.ISVALID = 1 and ngm.CLS_CODE = 140
									  and cast(nm.NEGA_POSI_MARK as varchar) = ngm.REF_CODE
    where nm.ISVALID = 1 --and nm.MTIME > cast('2016-08-01' as datetime)
      and ((nm.MTIME = '{UpdateDateTime}' and nm.[Seq] > '{RsId}') or (nm.MTIME > '{UpdateDateTime}'))
    order by nm.MTIME asc, nm.[Seq] asc"""