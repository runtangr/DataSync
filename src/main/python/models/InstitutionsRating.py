# -*- coding = utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class InstitutionsRating(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    gpmc = StringField()
    fbrq = DateTimeField()
    tzpj = StringField()
    qtzpj = StringField()
    sfscpj = StringField()
    pjbh = StringField()
    mbjg = DecimalField(precision=6)
    # mbjgqx = DecimalField(precision=6)
    mbjgqx = StringField()
    yspj = StringField()
    hymc = StringField()
    yjjcdm = LongField()
    yjjgmc = StringField()

    meta = {
        "collection": "f10_5_5_jgpj",
        "indexes": [
            {
                "fields": ("RsId", ),
                "unique": True
            }
        ]
    }
