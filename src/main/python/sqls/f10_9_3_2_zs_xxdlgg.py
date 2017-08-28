# -*- coding: utf-8 -*-
__author__ = "Cyh"
sql = """SELECT TOP 500 CAST(dmc.SEQ AS NVARCHAR(MAX)) AS RsId,
       CONVERT( NVARCHAR(30), dmc.CTIME, 121 ) AS UpdateDateTime,
       CONVERT( NVARCHAR(30), dmc.CTIME, 120 ) AS ZxDate,
	   QKTZ20160429.dbo.Date2Str( dmc.CTIME ) AS II_ZxDate,
       CAST(dmc.DISC_ID AS NVARCHAR(30)) AS ZiXunId,
       CAST(dcr.CLS_NAME AS NVARCHAR(50)) AS ZiXunType, 'SH000001' AS Obj,
       '000001' AS StockCode, '指数' AS StockName,
       CAST(dmc.TITLE AS NVARCHAR(256)) AS Title
  FROM QKTZ20160429.dbo.DISC_CLS_COM AS dcc WITH ( NOLOCK )
  INNER JOIN QKTZ20160429.dbo.DISC_CLS_REF AS dcr WITH ( NOLOCK )
          ON dcr.ISVALID = 1
         AND dcc.CLS_CODE = dcr.CLS_CODE
  INNER JOIN QKTZ20160429.dbo.DISC_MAIN_COM AS dmc WITH ( NOLOCK )
          ON dmc.DISC_ID = dcc.DISC_ID
         AND dmc.ISVALID = 1
 WHERE dcc.ISVALID = 1
   AND LEFT(dcr.CLS_CODE, 3) IN (
                                    '007', '008'
                                )
   AND (   dmc.CTIME >= '{UpdateDateTime}'
     AND   dmc.SEQ > '{RsId}'
       )
 ORDER BY dmc.CTIME, dmc.SEQ"""
