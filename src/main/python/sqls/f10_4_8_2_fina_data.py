# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 1000
       cast(a.SEQ as varchar) AS RsId,
       a.MTIME AS UpdateDateTime,
       cast(a.EVENT_ID as varchar) AS EventId,
       a.DECLAREDATE AS EventDateTime,QKTZ20160429.dbo.Date2Str( a.DECLAREDATE ) AS II_EventDateTime,
       a.EVENT EventTitle,
       '' AS EventContent,
       cast(a.AREA_CODE as varchar) AS EventAreaCode,
       dd.NATION_NAME AS EventAreaName,
       a.Last_Value AS LastValue,
       a.EXCEP_VALUE AS ExcepValue,
       a.Real_Value AS RealValue,
       ISNULL(a.Unit, '元') AS Unit,
       '中' AS Important,
       '123' AS EventIndexId
FROM [Genius2].[dbo].[FINA_DATA_CALENDAR] a
INNER JOIN PUB_NATION_CODE_REF dd ON a.AREA_code = dd.CODE
WHERE dd.ISVALID = 1
  AND ( ( a.MTime = '{UpdateDateTime}'
         AND a.SEQ > '{RsId}' )
       OR (a.MTime > '{UpdateDateTime}') )"""
