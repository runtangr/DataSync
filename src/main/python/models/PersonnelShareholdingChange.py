#-*- coding: utf-8 -*-
__author__ = "Tony"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class PersonnelShareholdingChange(QKDocument):
    Obj = StringField()
    gpmc = StringField()
    jgdm = LongField()
    zjcrmc = StringField()
    zjcsl = DecimalField(precision=6)
    zjczb = DecimalField(precision=6)
    zjcfs = LongField()
    zjyfsmc = StringField()
    zjclb = LongField()
    zjylbmc = StringField()
    zjcjj = DecimalField(precision=6)
    qcgs = DecimalField(precision=6)
    qczb = DecimalField(precision=6)
    yzxdr = StringField()
    ggrq = DateTimeField()
    ggid = StringField()
    hcgs = DecimalField(precision=6)
    hczb = DecimalField(precision=6)
    zjcjzr = DateTimeField()
    sfdydgd = StringField()
    jz = StringField()

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    meta = {
        "collection": "f10_2_8_6_ggcgbd",
        "indexes": [
            {
                "fields": ("RsId",),
                "unique": True
            }
        ]
    }
