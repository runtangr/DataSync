# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
SELECT TOP 500 CASE
                   WHEN b.MarketID = 10 THEN 'SH'
                   WHEN b.MarketID = 11 THEN 'SZ'
                   ELSE ''
               END + b.StockCode AS Obj, b.StockShortName,
       CONVERT( VARCHAR(8), a.DRDate, 112 ) AS Date, QKTZ20160429.dbo.Date2Str( a.DRDate ) AS II_Date,
       CAST(a.Coefficient_01 AS DECIMAL(20, 6)) AS HouChuQuanChengShu,
       CAST(a.Coefficient_02 AS DECIMAL(20, 6)) AS HouQianChuQuanPianYi,
       CAST(a.Coefficient_11 AS DECIMAL(20, 6)) AS QianChuQuanChengShu,
       CAST(a.Coefficient_12 AS DECIMAL(20, 6)) AS QianChuQuanPianYi,
       a.BonusIssue_Note AS FhkgXinXi, CONVERT( VARCHAR(10), a.DRDate, 120 ) AS cqcxr,
       QKTZ20160429.dbo.Date2Str( a.DRDate ) AS II_cqcxr,
       CONVERT( VARCHAR(8), a.QxDjr, 112 ) AS gqdjr, QKTZ20160429.dbo.Date2Str( a.QxDjr ) AS II_gqdjr,
       '' AS zhjyr, CONVERT( VARCHAR(26), a.rsDateTime, 121 ) AS UpdateDateTime,
       CONVERT( VARCHAR(8), a.QxBgq, 112 ) AS qxbgq, QKTZ20160429.dbo.Date2Str( a.QxBgq ) AS II_qxbgq
  FROM stocksoftdata.dbo.sidbStockCoefficient AS a WITH ( NOLOCK )
  INNER JOIN stocksoftdata.dbo.commStockCode AS b WITH ( NOLOCK )
          ON a.StockCodeID = b.rsMainkeyID
 WHERE b.MarketID IN (
                         10, 11
                     )
   AND a.rsDateTime >= CAST('{UpdateDateTime}' AS DATETIME)
 ORDER BY a.rsDateTime"""