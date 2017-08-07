# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField


class ActualController(QKDocument):
    Obj = StringField(required=True)
    mc = StringField()  # 名称
    sm = StringField()  # 说明

    meta = {
        "collection": "f10_2_4_5_sjkzr",
        "indexes": [
            {
                "fields": ("Obj",),
                "unique": True
            }
        ]
    }
