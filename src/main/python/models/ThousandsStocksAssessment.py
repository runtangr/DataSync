# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class ThousandsStocksAssessment(QKDocument):    
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    gpmc = StringField()
    ggrq = DateTimeField()
    pjnr = StringField()
    ly = StringField()    

    meta = {
        "collection": "f10_5_7_qgqp",
        "indexes": [
            {
                "fields": ("Obj","ggrq" ),
                "unique": True
            }
        ]
    }    

