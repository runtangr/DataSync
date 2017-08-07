# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class CashFlowTracing(QKDocument):    
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    yybdm = LongField() 
    yybmc = StringField()
    yzsbcs = LongField()
    yzmrzs = DecimalField(precision=6)
    yzljmr = DecimalField(precision=6)
    yzmczs = DecimalField(precision=6)
    yzljmc = DecimalField(precision=6)
    flfs = LongField()    

    meta = {
        "collection": "f10_2_6_3_3_yzgz",
        "indexes": [
            {
                "fields": ("yybdm","flfs" ),
                "unique": True
            }
        ]
    }    
