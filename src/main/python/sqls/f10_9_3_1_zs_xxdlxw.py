# -*- coding: utf-8 -*-
__author__ = "Cyh"
sql = """SELECT TOP 500 CAST(nm.SEQ AS NVARCHAR(MAX)) AS Rsid,
       CONVERT( VARCHAR(30), nm.CTIME, 121 ) AS UpdateDateTime,
       CONVERT( VARCHAR(30), nm.CTIME, 120 ) AS ZxDate,
	   dbo.Date2Str( nm.CTIME ) AS II_ZxDate,
       CAST(nm.GUID AS NVARCHAR(20)) AS ZiXunId,
       CAST(ncr.CLS_NAME AS NVARCHAR(50)) AS ZiXunType, 'SH000001' AS Obj,
       '000001' AS StockCode, '指数' AS StockName,
       CAST(nm.TITLE_MAIN AS NVARCHAR(300)) AS Title
  FROM QKTZ20160429.dbo.NEWS_CLS AS ncs WITH ( NOLOCK )
  INNER JOIN QKTZ20160429.dbo.NEWS_MAIN AS nm WITH ( NOLOCK )
          ON nm.ISVALID = 1
         AND nm.GUID = ncs.GUID
  INNER JOIN QKTZ20160429.dbo.NEWS_CLS_REF AS ncr WITH ( NOLOCK )
          ON ncr.ISVALID = 1
         AND ncs.CLS_CODE = ncr.CLS_CODE
 WHERE ncs.ISVALID = 1
   AND LEFT(ncr.CLS_CODE, 3) IN (
                                    '001', '002', '003', '004'
                                )
   AND (   nm.SEQ > '{@RsId}'
     AND   nm.CTIME >= '{@UpdateDateTime}'
       )
 ORDER BY nm.MTIME, nm.SEQ"""
