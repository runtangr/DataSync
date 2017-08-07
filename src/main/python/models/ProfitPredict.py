# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class ProfitPredict(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    gpmc = StringField()
    ycnd = LongField()
    mgsy1= DecimalField(precision=6)
    mgsy2= DecimalField(precision=6)
    mgsy3= DecimalField(precision=6)
    yysy1= DecimalField(precision=6)
    yysy2= DecimalField(precision=6)
    yysy3= DecimalField(precision=6)
    jly1= DecimalField(precision=6)
    jly2= DecimalField(precision=6)
    jly3= DecimalField(precision=6) 

    meta = {
        "collection": "f10_5_4_ylyc",
        "indexes": [
            {
                "fields": ("Obj", ),
                "unique": True
            }
        ]
    }
