# -*- coding: utf-8 -*-
__author__ = "Cyh"
sql = """SELECT TOP 500 CAST(RsID AS VARCHAR) AS RsID, UpdateDateTime, Obj, zxDate AS ZxDate,stocksoftdata.dbo.Date2Str( zxDate ) AS II_ZxDate,
       count_num AS CountNum, zxType AS ZxType
  FROM xxdllstj
 WHERE (   RsID > '{RsId}'
     AND   UpdateDateTime >= '{UpdateDateTime}'
       )"""
