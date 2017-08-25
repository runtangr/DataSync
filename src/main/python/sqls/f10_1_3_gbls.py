# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """SELECT TOP 500 CASE X.TRADE_MKT_REF
                   WHEN 1 THEN 'SZ'
                   WHEN 2 THEN 'SH'
               END + X.STOCKCODE AS Obj, A.CHANGEDATE AS 'Date',
       QKTZ20160429.dbo.Date2Str( A.CHANGEDATE ) AS II_Date, A.NEW_TOT AS bdhzgb,
       A.NEW_A_SHR AS bdhltgb, A.MTIME AS UpdateDateTime
  FROM STK_CODE AS X WITH ( NOLOCK )
  INNER JOIN STK_SHR_STRU_CHNG AS A WITH ( NOLOCK )
          ON X.COMCODE = A.COMCODE
         AND X.ISVALID = 1
         AND X.STATUS_TYPE_REF IN (
                                      1, 4
                                  )
         AND X.TRADE_MKT_REF IN (
                                    1, 2
                                )
 WHERE A.ISVALID = 1
   AND A.CHNG_REAS_CODE NOT IN (
                                   10, 11, 12, 13
                               )
   AND A.MTIME >= '{UpdateDateTime}'
 ORDER BY A.MTIME ASC"""