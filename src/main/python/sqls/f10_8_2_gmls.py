# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT *
  FROM (
           SELECT TOP 500 a.SEQ Seq, a.MTIME Mtime,dbo.Date2Str( a.MTIME ) AS II_Mtime, CASE x.TRADE_MKT_REF
                                                  WHEN 1 THEN 'SZ'
                                                  WHEN 2 THEN 'SH'
                                                  ELSE ''
                                              END + x.STOCKCODE AS Obj,
                  CASE x.TRADE_MKT_REF
                      WHEN 1 THEN 'SZ'
                      WHEN 2 THEN 'SH'
                      ELSE ''
                  END MarketCode, x.STOCKCODE StockCode, a.STOCKSNAME StockName,
                  a.CHANGEDATE ChangeDate,dbo.Date2Str( a.CHANGEDATE ) AS II_ChangeDate,
                  (   SELECT TOP 1 STOCKSNAME
                        FROM STK_SNAME_CHNG
                       WHERE ISVALID = 1
                         AND INNER_CODE = a.INNER_CODE
                         AND CHANGEDATE < a.CHANGEDATE
                       ORDER BY CHANGEDATE DESC
                  ) AS OldStockName
             FROM STK_SNAME_CHNG AS a
             INNER JOIN STK_CODE AS x
                     ON a.INNER_CODE = x.INNER_CODE
                    AND a.ISVALID = 1
                    AND x.ISVALID = 1
                    AND x.TRADE_MKT_REF IN (
                                               1, 2
                                           )
                    AND ( (   a.MTIME = '{UpdateDateTime}'
                        AND   a.SEQ > '{RsId}'
                         )
                       OR ( a.MTIME > '{UpdateDateTime}' )
                        )
            ORDER BY a.MTIME, a.SEQ
       ) AS aa
 WHERE aa.StockNameLat IS NOT NULL
 ORDER BY MTIME, Seq"""
