# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class InstitutionsHeavilyHeld(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    cjlx = LongField()
    jgljmr = DecimalField(precision=6)
    jgljmc = DecimalField(precision=6)
    flfs = DecimalField(precision=6)
    jgcys = DecimalField(precision=6)

    meta = {
        "collection": "f10_2_6_3_2_jgzc",
        "indexes": [
            {
                "fields": ("Obj","cjlx","flfs" ),
                "unique": True
            }
        ]
    }
