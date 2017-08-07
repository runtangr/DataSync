# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class InstitutionsRatingGrade(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    tzpj = StringField()
    pjsl = DecimalField(precision=6)
    zscr = DecimalField(precision=6)
    mrpj = StringField()
    zjs = DecimalField(precision=6)

    meta = {
        "collection": "f10_5_6_jgpjdf",
        "indexes": [
            {
                "fields": ("Obj","tzpj" ),
                "unique": True
            }
        ]
    }
