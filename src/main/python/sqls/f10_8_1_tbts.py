# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
SELECT TOP 500 a.SEQ AS RsId, a.MTIME AS UpdateDateTime,
       QKTZ20160429.dbo.Date2Str( a.MTIME ) AS II_Mtime, CASE x.TRADE_MKT_REF
                                                             WHEN 1 THEN 'SZ'
                                                             WHEN 2 THEN 'SH'
                                                             ELSE ''
                                                         END + x.STOCKCODE AS Obj,
       CASE x.TRADE_MKT_REF
           WHEN 1 THEN 'SZ'
           WHEN 2 THEN 'SH'
           ELSE ''
       END MarketCode, x.STOCKCODE StockCode,
       CAST(x.STOCKSNAME AS NVARCHAR(MAX)) AS StockName,
       a.HINT_TYPE_CODE AS HintTypeCode,
       CAST(a.HINT_TYPE_NAME AS NVARCHAR(MAX)) AS HintTypeName, a.HINT_DT AS HintDt,
       QKTZ20160429.dbo.Date2Str( a.HINT_DT ) AS II_HintDt,
       CAST(a.ESP_HINT AS NVARCHAR(MAX)) AS EspHint, a.DECLAREDATE DeclareDate,
       QKTZ20160429.dbo.Date2Str( a.DECLAREDATE ) AS II_DeclareDate
  FROM NEWS_ESP_HINT AS a
  INNER JOIN STK_CODE AS x
          ON a.INNER_CODE = x.INNER_CODE
         AND a.ISVALID = 1
         AND x.ISVALID = 1
 WHERE x.TRADE_MKT_REF IN (
                              1, 2
                          )
   AND ( (   a.MTIME = '{UpdateDateTime}'
       AND   a.SEQ > '{RsId}'
        )
      OR ( a.MTIME > '{UpdateDateTime}' )
       )
 ORDER BY a.MTIME, a.SEQ
"""
