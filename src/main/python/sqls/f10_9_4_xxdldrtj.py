# -*- coding: utf-8 -*-
# 库：stocksoftdata 
__author__ = "Cyh"
sql = """SELECT TOP 500 CAST(RsID AS NVARCHAR(MAX)) AS RsID, UpdateDateTime, Obj, ZxDate,
       CountNum, ZxType
  FROM stocksoftdata.dbo.F10_9_4_XXDLDRTJ
 WHERE (   RsID > '{RsId}'
     AND   UpdateDateTime = '{UpdateDateTime}'
       )
    OR UpdateDateTime > '{UpdateDateTime}'"""
