# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DecimalField, DateTimeField, LongField


class CapitalStockIntroduction(QKDocument):
    Obj = StringField()
    Date = DateTimeField()  # 最新日期
    zgb = DecimalField(precision=6)  # 总股本(万股)
    zltgb = DecimalField(precision=6)  # 总流通股本(万股)
    dqltgb = DecimalField(precision=6)  # 当前流通股本(万股)，A股则A股股本，B股则B股股本
    gdrs = LongField()  # 股东人数
    kggd = StringField()  # 控股股东
    qsdgdbl = DecimalField(precision=6)  # 前十大股东占股比例(非十大流通股东占比)

    meta = {
        "collection": "f10_2_5_4_gbgk",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
