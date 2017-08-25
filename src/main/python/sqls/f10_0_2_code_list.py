# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT  STOCKCODE AS Code,
        STOCKSNAME AS ShortName,
        CASE TRADE_MKT_REF
          WHEN 1 THEN 'SZ'
          WHEN 2 THEN 'SH'
        END AS MarketCode,
        CHI_SPEL AS ShortcutCode,
        10 AS TypeCode,
        MTIME AS UpdateDateTime
FROM STK_CODE with(nolock)
WHERE ISVALID=1 AND STK_TYPE_REF in (1,4) AND STK_TYPE_REF=1
  AND STOCKSNAME IS NOT NULL"""

headers = ["Code", "ShortName", "MarketCode", "ShortcutCode", "TypeCode", "UpdateDateTime"]
