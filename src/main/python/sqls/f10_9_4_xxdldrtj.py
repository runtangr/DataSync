# -*- coding: utf-8 -*-
# 库：stocksoftdata 
__author__ = "Cyh"
sql = """SELECT TOP 500 CAST(RsID AS NVARCHAR(MAX)) AS RsId, UpdateDateTime, Obj, ZxDate,stocksoftdata.dbo.Date2Str( ZxDate ) AS II_ZxDate,
       CountNum, ZxType
  FROM stocksoftdata.dbo.F10_9_4_XXDLDRTJ
 WHERE (   RsId > '{RsId}'
     AND   UpdateDateTime = '{UpdateDateTime}'
       )
    OR UpdateDateTime > '{UpdateDateTime}'"""
