# -*- coding: utf-8 -*-
__author__ = "Cyh"
sql = """SELECT TOP 500
        RsID, syncDate UpdateDateTime, Obj, zxDate AS ZxDate, count_num AS CountNum, UpdateDateTime zxTime, zxType AS ZxType
FROM    xxdllstj
WHERE   ( RsID > '{RsID}'
          AND syncDate = '{UpdateDateTime}'
        )
        OR syncDate >= '{UpdateDateTime}'
ORDER BY syncDate, RsID"""
