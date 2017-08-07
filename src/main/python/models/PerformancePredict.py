# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class PerformancePredict(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    gpmc = StringField()
    ggrq = DateTimeField()
    jzrq = DateTimeField()
    ycdm = LongField()
    yclx = StringField()
    ggly = StringField()
    yzzy = StringField()
    jtnr = StringField()
    yysm = StringField()
    jlytbsx = DecimalField(precision=6)
    jlytbxx = DecimalField(precision=6)
    qntqsy = DecimalField(precision=6)
    qntqlr = DecimalField(precision=6)
    yjmgsysx = DecimalField(precision=6)
    yjmgsyxx = DecimalField(precision=6)

    meta = {
        "collection": "f10_2_3_5_yjyg",
        "indexes": [
            {
                "fields": ("RsId", ),
                "unique": True
            }
        ]
    }
