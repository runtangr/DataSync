# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 500 CAST(nsk.SEQ AS VARCHAR) AS RsId,
       CONVERT( VARCHAR(30), nsk.MTIME, 126 ) AS UpdateDateTime,
       CONVERT( VARCHAR(30), nm.MTIME, 120 ) AS ZxDate,QKTZ20160429.dbo.Date2Str( nm.MTIME ) AS II_ZxDate,nm.GUID AS ZiXunId,
       'XW' AS ZiXunType, CASE
                              WHEN stk.TRADE_MKT_REF = 1 THEN 'SZ'
                              WHEN stk.TRADE_MKT_REF = 2 THEN 'SH'
                              ELSE CAST(stk.TRADE_MKT_REF AS VARCHAR) + '-'
                          END + stk.STOCKCODE AS Obj, stk.STOCKCODE StockCode,
       stk.STOCKSNAME AS StockName, nm.TITLE_MAIN AS Title
  FROM NEWS_STK AS nsk WITH ( NOLOCK )
  INNER JOIN NEWS_MAIN AS nm WITH ( NOLOCK )
          ON nm.ISVALID = 1
         AND nm.GUID = nsk.GUID
  INNER JOIN STK_CODE AS stk WITH ( NOLOCK )
          ON stk.ISVALID = 1
         AND stk.INNER_CODE = nsk.A_INNER_CODE
 WHERE nsk.ISVALID = 1
   AND ( (   nsk.MTIME = '{UpdateDateTime}'
       AND   nsk.SEQ > '{RsId}'
        )
      OR ( nsk.MTIME > '{UpdateDateTime}' )
       )
 ORDER BY nsk.MTIME, nsk.SEQ"""
