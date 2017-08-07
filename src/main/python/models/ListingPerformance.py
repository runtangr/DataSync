# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class ListingPerformance(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    gpmc = StringField()
    ssrq = DateTimeField()
    srsssl = LongField()
    srkpj = DecimalField(precision=6)
    srzgj = DecimalField(precision=6)
    srzdj = DecimalField(precision=6)
    ssspj = DecimalField(precision=6)
    srcjjj = DecimalField(precision=6)
    srcjl = DecimalField(precision=6)
    srcje = DecimalField(precision=6)
    srzdf = DecimalField(precision=6)
    srhsl = DecimalField(precision=6)
    dxsyl = DecimalField(precision=6)
    lxztts = DecimalField(precision=6)
    zhztspj = DecimalField(precision=6) 
    zhztsyl = DecimalField(precision=6) 
    Obj = StringField()

    meta = {
        "collection": "f10_4_7_3_ssbx",
        "indexes": [
            {
                "fields": ("RsId", ),
                "unique": True
            }
        ]
    }
