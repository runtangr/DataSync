# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """SELECT CAST(seccode.SEQ AS VARCHAR) AS RsId, seccode.MTIME AS UpdateDateTime,
       CASE
           WHEN seccode.MKT_TYPE = 1 THEN 'SZ'
           WHEN seccode.MKT_TYPE = 2 THEN 'SH'
           ELSE ''
       END + seccode.SEC_CODE AS Obj, CASE
                                          WHEN seccode.MKT_TYPE = 1 THEN 'SZ'
                                          WHEN seccode.MKT_TYPE = 2 THEN 'SH'
                                          ELSE ''
                                      END AS MarketCode, seccode.SEC_CODE AS StockCode,
       seccode.SEC_SNAME AS StockName, seccode.SEC_NAME AS StockFullName,
       seccode.SEC_CHI_SPEL AS ShortCode, CASE
                                              WHEN seccode.SEC_TYPE = 1
                                               AND seccode.SEC_STYPE = 101 THEN '10' --A股
                                              WHEN seccode.SEC_TYPE = 1
                                               AND seccode.SEC_STYPE = 102 THEN '15' --B股
                                              WHEN seccode.SEC_TYPE = 2 THEN '35' --债券
                                              WHEN seccode.SEC_TYPE = 3 THEN '25' --封闭式基金
                                              WHEN seccode.SEC_TYPE = 4 THEN '40' --权证
                                              WHEN seccode.SEC_TYPE = 5
                                               AND seccode.SEC_STYPE = 501 THEN '5' --指数
                                              ELSE ''
                                          END AS TypeValue,
       CASE
           WHEN seccode.SEC_TYPE = 1
            AND seccode.SEC_STYPE = 101 THEN 'A股'
           WHEN seccode.SEC_TYPE = 1
            AND seccode.SEC_STYPE = 102 THEN 'B股'
           WHEN seccode.SEC_TYPE = 2 THEN '债券'
           WHEN seccode.SEC_TYPE = 3 THEN '基金'
           WHEN seccode.SEC_TYPE = 4 THEN '权证'
           WHEN seccode.SEC_TYPE = 5 THEN '指数'
           ELSE ''
       END AS TypeName,
       CAST(ISNULL( seccode.LIST_SECTOR, 1 ) AS VARCHAR) AS SubMarketType,
       ISNULL( seccode.LIST_SECTOR_NAME, '主板' ) AS SubMarketTypeName,
       CASE
           WHEN seccode.LIST_STATUS = '正常上市' THEN '1'
           WHEN seccode.LIST_STATUS = '发行配售期间' THEN '4'
           WHEN seccode.LIST_STATUS = '终止上市' THEN '-10'
           ELSE CASE
                    WHEN seccode.SEC_TYPE = 5
                     AND indx.IS_MKT = 1
                     AND indx.END_DATE IS NULL THEN '1'
                    WHEN seccode.SEC_TYPE = 5
                     AND indx.END_DATE <= GETDATE() THEN '-10'
                    WHEN seccode.SEC_TYPE = 5
                     AND indx.IS_MKT = 2 THEN '-10'
                    WHEN seccode.SEC_TYPE = 5
                     AND indx.IS_MKT = 1
                     AND indx.END_DATE > GETDATE() THEN '1'
                    ELSE '0'
                END
       END AS StatusValue, seccode.LIST_STATUS AS StatusName,
       CONVERT( VARCHAR(8), seccode.LIST_DATE, 112 ) AS StartDate,
       QKTZ20160429.dbo.Date2Str( seccode.LIST_DATE ) AS II_StartDate,
       CONVERT( VARCHAR(8), seccode.LIST_ENDDATE, 112 ) AS EndDate,
       QKTZ20160429.dbo.Date2Str( seccode.LIST_ENDDATE ) AS II_EndDate
  --, * 
  FROM PUB_SEC_CODE AS seccode WITH ( NOLOCK )
  LEFT JOIN INDX_GEN_INFO AS indx WITH ( NOLOCK )
         ON seccode.SEC_CODE = indx.INDX_CODE
        AND indx.ISVALID = 1
 WHERE seccode.MKT_TYPE IN (
                               1, 2
                           )
   AND seccode.SEC_TYPE IN (
                               1, 5
                           )
   AND seccode.SEC_SNAME IS NOT NULL
   AND seccode.ISVALID = 1
--and (indx.END_DATE is null or indx.END_DATE > getdate())
--and seccode.LIST_STATUS is not null -- and sec_code = '000001'
UNION ALL
SELECT CAST(rsMainkeyID AS VARCHAR) AS RsId, rsDateTime AS UpdateDateTime,
       'BK' + PlateCode AS PlateCode, 'BK' AS MarketCode, PlateCode AS PlateCode,
       SECTION_NAME_H AS SectionNameH, SECTION_NAME AS SectionName, ShortCode,
       '5' AS SysCode, '指数代码' AS TypeName, CAST(SYS_CODE AS VARCHAR) AS SysCode,
       CASE SYS_CODE
           WHEN 3 THEN '行政地域'
           WHEN 4 THEN '指数成分'
           WHEN 5 THEN '概念板块'
           WHEN 16 THEN '行业板块'
           WHEN 17 THEN '细分行业'
           ELSE '其它'
       END AS TypeName, '1' AS StatusValue, '正常上市' AS StatusName,
       '20000101' AS StartDate, QKTZ20160429.dbo.Date2Str( '20000101' ) AS II_StartDate,
       '' AS EndDate, '' AS II_EndDate
  FROM stocksoftdata..ViewStockSoft_commStockSection WITH ( NOLOCK )
 WHERE ( (   SYS_CODE = 3
       AND   SECTION_LEVEL = 1
         )
      OR (   SYS_CODE = 4
       AND   SECTION_LEVEL = 2
         )
      OR (   SYS_CODE = 5
       AND   SECTION_LEVEL = 1
         )
      OR (   SYS_CODE = 16
       AND   SECTION_LEVEL = 2
         )
      OR (   SYS_CODE = 17
       AND   SECTION_LEVEL = 3
        )
       )
 ORDER BY 2, 1"""
