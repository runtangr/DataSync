# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 1000
       cast(a.SEQ as varchar) AS RsId,
       a.MTIME AS UpdateDateTime,
       cast(a.EVENT_ID as varchar) AS EventId,
       a.DECLAREDATE AS NewsDateTime,QKTZ20160429.dbo.Date2Str( a.DECLAREDATE ) AS II_NewsDateTime,
       '' AS 'NewsSource',
       a.EVENT 'NewsTitle',
               '' AS NewsContent,
               '' AS 'NewsGNBK',
               'wfl' AS 'NewsTypeCode',
               '未分类' AS 'NewsTypeName',
               cast( a.AREA_CODE as varchar) AS NewsAreaCode,
               dd.NATION_NAME AS NewsAreaName
FROM [Genius2].[dbo].[FINA_EVEN_CALENDAR] a
INNER JOIN PUB_NATION_CODE_REF dd ON a.AREA_code = dd.CODE
WHERE dd.ISVALID = 1
  AND ( ( a.MTime = '{UpdateDateTime}'
         AND a.SEQ > '{RsId}' )
       OR (a.MTime > '{UpdateDateTime}') )"""
