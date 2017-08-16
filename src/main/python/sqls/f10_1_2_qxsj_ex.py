# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
select top 500
     case when b.MarketID = 10 then 'SH' when b.MarketID = 11 then 'SZ' else '' end + b.StockCode as Obj
   , b.StockShortName  
   , convert(varchar(8), a.[DRDate], 112) as [Date]
   , cast(a.[Coefficient_01] as decimal(20,6)) as HouChuQuanChengShu
   , cast(a.[Coefficient_02] as decimal(20,6)) as HouQianChuQuanPianYi
   , cast(a.[Coefficient_11] as decimal(20,6)) as QianChuQuanChengShu
   , cast(a.[Coefficient_12] as decimal(20,6)) as QianChuQuanPianYi
   , a.[BonusIssue_Note] as FhkgXinXi
   , convert(varchar(10), a.[DRDate], 120) as cqcxr
   , convert(varchar(8), a.[QxDjr], 112) as gqdjr
   , '' as zhjyr
   , convert(varchar(26), a.rsDateTime, 121) as UpdateDateTime
   , convert(varchar(8), a.[QxBgq], 112) as qxbgq,
   a.rsstatus,a.rsMainkeyid
from stocksoftdata.dbo.[sidbStockCoefficient] a with(nolock)
inner join stocksoftdata.dbo.[commStockCode] b with(nolock) on a.[StockCodeID] = b.rsMainkeyID
where b.MarketID in(10, 11) and a.rsDateTime > cast('{UpdateDateTime}' as datetime)
order by a.rsDateTime"""