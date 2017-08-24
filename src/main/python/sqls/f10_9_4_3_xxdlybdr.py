# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 500 CAST(rrm.SEQ AS VARCHAR(20)) AS RsId,
       CONVERT( VARCHAR(30), rrm.MTIME, 120 ) AS ZxDate,
       dbo.Date2Str( rrm.MTIME ) AS II_ZxDate,
       CONVERT( VARCHAR(30), rrm.MTIME, 126 ) AS UpdateDateTime, rrm.RES_ID AS ZiXunId,
       'YB' AS ZiXunType, CASE
                              WHEN dd.MKT_TYPE = 1 THEN 'SZ'
                              WHEN dd.MKT_TYPE = 2 THEN 'SH'
                              ELSE CAST(dd.MKT_TYPE AS VARCHAR(20)) + '-'
                          END + dd.SEC_CODE AS Obj, dd.SEC_CODE StockCode,
       dd.SEC_SNAME AS StockName, rrm.RPT_TITLE AS Title
  FROM RES_REPORT_MAIN AS rrm WITH ( NOLOCK )
  INNER JOIN RES_SEC_CODE AS cc WITH ( NOLOCK )
          ON rrm.RES_ID = cc.RES_ID
         AND cc.ISVALID = 1
  INNER JOIN PUB_SEC_CODE AS dd WITH ( NOLOCK )
          ON cc.INNER_CODE = dd.INNER_CODE
         AND dd.ISVALID = 1
         AND dd.SEC_SNAME IS NOT NULL
 WHERE rrm.ISVALID = 1
   AND rrm.MTIME > CAST(GETDATE() AS DATE)
   AND ( (   rrm.MTIME = '{UpdateDateTime}'
       AND   rrm.SEQ > '{RsId}'
        )
      OR ( rrm.MTIME > '{UpdateDateTime}' )
       )
 ORDER BY rrm.MTIME, rrm.SEQ"""
