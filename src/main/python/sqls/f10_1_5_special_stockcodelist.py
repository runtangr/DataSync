# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT  CASE TRADE_MKT_REF
          WHEN 1 THEN 'SZ'
          WHEN 2 THEN 'SH'
          ELSE ''
        END + STOCKCODE AS Obj, CASE TRADE_MKT_REF
                                  WHEN 1 THEN 'SZ'
                                  WHEN 2 THEN 'SH'
                                  ELSE ''
                                END MarketCode, STOCKCODE StockCode, STOCKSNAME StockName, CASE WHEN SPECIAL_TYPE_REF IN ( 2, 3 ) THEN 'FXTS'
                                                                                                ELSE 'TSYJ'
                                                                                           END AS SpecialType
FROM    STK_CODE
WHERE   ISVALID = 1
        AND SPECIAL_TYPE_REF IN ( 2, 3, 6 )
        AND STATUS_TYPE_REF = 1
        AND TRADE_MKT_REF IN ( 1, 2 )"""
