# -*- coding: utf-8 -*-
__author__ = "Cyh"
sql = """SELECT RsID, UpdateDateTime, Obj, zxDate AS ZxDate, count_num AS CountNum,
       zxType AS ZxType
  FROM xxdllstj
 WHERE (   RsID > '{RsID}'
     AND   UpdateDateTime = '{UpdateDateTime}'
       )
    OR UpdateDateTime >= '{UpdateDateTime}'"""
