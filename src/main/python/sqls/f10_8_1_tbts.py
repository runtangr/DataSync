# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 500 a.SEQ AS Seq, a.MTIME AS Mtime, CASE x.TRADE_MKT_REF
                                                   WHEN 1 THEN 'SZ'
                                                   WHEN 2 THEN 'SH'
                                                   ELSE ''
                                               END + x.STOCKCODE AS Obj,
       CASE x.TRADE_MKT_REF
           WHEN 1 THEN 'SZ'
           WHEN 2 THEN 'SH'
           ELSE ''
       END MarketCode, x.STOCKCODE StockCode, x.STOCKSNAME StockName,
       a.HINT_TYPE_CODE AS HintTypeCode, a.HINT_TYPE_NAME AS HintTypeName,
       a.HINT_DT HintDt, a.ESP_HINT EspHint, a.DECLAREDATE DeclareDate
  FROM QKTZ20160429.dbo.NEWS_ESP_HINT AS a
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
 ORDER BY a.MTIME, a.SEQ"""
