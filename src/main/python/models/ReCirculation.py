# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class ReCirculation(QKDocument):
    RsId = StringField()          
    UpdateDateTime = DateTimeField()
    Obj = StringField()          
    gpmc = StringField()         
    jjrq = DateTimeField()         
    jjsl = DecimalField(precision=6)
    jjsz = DecimalField(precision=6)	        
    jjzb = DecimalField(precision=6)         
    gddm = LongField()
    gdmc = StringField() 
    zxsp = DecimalField(precision=6) 
    xxyydm = LongField()
    xxyy = StringField() 

    meta = {
        "collection": "f10_2_8_1_jjlt",
        "indexes": [
            {
                "fields": ("RsId", ),
                "unique": True
            }
        ]
    }
