# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class LivelyStocks(QKDocument):    
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    cjlx = DecimalField(precision=6)
    ljmr = DecimalField(precision=6)
    ljmc = DecimalField(precision=6)
    flfs = LongField()
    sbcs = DecimalField(precision=6)
    
    meta = {
        "collection": "f10_2_6_3_1_hygg",
        "indexes": [
            {
                "fields": ("Obj","cjlx","flfs" ),
                "unique": True
            }
        ]
    }    
