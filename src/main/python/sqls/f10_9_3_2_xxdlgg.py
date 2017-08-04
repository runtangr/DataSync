# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 500 CAST(dco.SEQ AS VARCHAR) AS RsId,
       CONVERT( VARCHAR(30), dco.MTIME, 126 ) AS UpdateDateTime,
       CONVERT( VARCHAR(30), dco.MTIME, 120 ) AS ZxDate, dco.DISC_ID AS ZiXunId,
       'GG' AS ZiXunType, CASE
                              WHEN stk.TRADE_MKT_REF = 1 THEN 'SZ'
                              WHEN stk.TRADE_MKT_REF = 2 THEN 'SH'
                              ELSE CAST(stk.TRADE_MKT_REF AS VARCHAR) + '-'
                          END + stk.STOCKCODE AS Obj, stk.STOCKCODE AS StockCode,
       stk.STOCKSNAME AS StockName, nm.TITLE AS Title
  FROM DISC_COM AS dco WITH ( NOLOCK )
  INNER JOIN STK_CODE AS stk WITH ( NOLOCK )
          ON stk.ISVALID = 1
         AND stk.COMCODE = dco.COMCODE
  INNER JOIN DISC_MAIN_COM AS nm
          ON nm.ISVALID = 1
         AND dco.DISC_ID = nm.DISC_ID
 WHERE dco.ISVALID = 1
   AND dco.DECLAREDATE >= CAST(CAST(YEAR( GETDATE()) - 2 AS VARCHAR) + '-01-01' AS DATETIME)
   AND ( (   dco.MTIME = '{UpdateDateTime}'
       AND   dco.SEQ > '{RsId}'
        )
      OR ( dco.MTIME > '{UpdateDateTime}' )
       )
 ORDER BY dco.MTIME, dco.SEQ"""
