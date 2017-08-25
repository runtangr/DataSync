# -*- coding: utf-8 -*-
__author__ = "Cyh"
sql = """SELECT TOP 500 CAST(rrm.SEQ AS NVARCHAR(MAX)) AS RsId,
       CONVERT( VARCHAR(30), rrm.CTIME, 121 ) AS UpdateDateTime,
       CONVERT( VARCHAR(30), rrm.CTIME, 120 ) AS ZxDate,
	   QKTZ20160429.dbo.Date2Str(rrm.CTIME) AS II_ZxDate,
       CAST(rrm.RES_ID AS NVARCHAR(18)) AS ZiXunId,
       CAST(rrm.RPT_TYPE_NAME AS NVARCHAR(60)) AS ZiXunType, 'SH000001' AS Obj,
       '000001' AS StockCode, '指数' AS StockName,
       CAST(rrm.RPT_TITLE AS NVARCHAR(200)) AS Title
  FROM RES_REPORT_MAIN AS rrm WITH ( NOLOCK )
 WHERE rrm.ISVALID = 1
   AND LEFT(rrm.RPT_TYPE, 1) IN (
                                    '1', '2', '3', '8', '9'
                                )
   AND (   rrm.CTIME >= '{@UpdateDateTime}'
     AND   rrm.SEQ > '{@RsId}'
       )
 ORDER BY rrm.CTIME, rrm.SEQ"""
