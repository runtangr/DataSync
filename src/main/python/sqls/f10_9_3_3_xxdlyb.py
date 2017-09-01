# -*- coding: utf-8 -*-
__author__ = "Cyh"
sql = """
SELECT RsId, StockCode, Obj, StockName, ZiXunId, Title, ZiXunType, ZxDate, II_ZxDate,
       DECLAREDATE AS Declaredate, II_DECLAREDATE AS II_Declaredate,  MyDate, II_MyDate, UpdateDateTime, Status
  FROM stocksoftdata.dbo.F10_9_3_3_XXDLYB
 WHERE (   RsId > '{RsId}'
     AND   UpdateDateTime = '{UpdateDateTime}'
       )
    OR UpdateDateTime > '{UpdateDateTime}'
"""
