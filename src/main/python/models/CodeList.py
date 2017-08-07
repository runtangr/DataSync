# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, LongField


class CodeList(QKDocument):
    MarketCode = StringField(required=True, choices=["SH", "SZ", "BK"])
    TypeCode = LongField()
    Code = StringField(required=True, max_length=6)
    ShortcutCode = StringField(required=True)
    ShortName = StringField(required=True)
    UpdateDateTime = DateTimeField()

    meta = {
        "collection": "f10_0_2_code_list",
        "indexes": [
            {
                "fields": ("MarketCode", "Code"),
                "unique": True
            }
        ]
    }
