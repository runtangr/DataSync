# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql ="""select
      cast(cjrl.rsMainkeyID as varchar) as RsId
    , cjrl.rsDateTime as UpdateDateTime
	, cjrl.NewsDate,QKTZ20160429.dbo.Date2Str( cjrl.NewsDate ) AS II_NewsDate, cjrl.NewsSource, cjrl.NewsTitle, cjrl.NewsContent
	, cjrl.OtherDefine1 as NewsGNBK
	, case when cjrl.NewsTitle like '%新股申购%' then 'xgsg'
	       else 'wfl' end as NewsTypeCode
	, case when cjrl.NewsTitle like '%新股申购%' then '新股申购'
	       else '未分类' end as NewsTypeName
from stocksoftdata.dbo.CommNewsCJRL cjrl
order by cjrl.rsMainkeyID"""
