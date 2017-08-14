# -*- coding: utf-8 -*-
# 库：QKTZ20160429
__author__ = "Cyh"
sql = """SELECT TOP 500 CAST(RsID AS VARCHAR) AS RsID, UpdateDateTime, Obj, ZxDate, CountNum,
       ZxType
  FROM F10_9_4_XXDLDRTJ
 WHERE (   RsID > '{RsId}'
     AND   UpdateDateTime >= '{UpdateDateTime}'
       )"""
