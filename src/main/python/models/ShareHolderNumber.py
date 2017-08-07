# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField, EmbeddedDocumentField


class SingleShareHolderNumber(QKEmbeddedDocument):
    gdzhs = LongField()  # 股东总户数
    hbzj = DecimalField(precision=6)  # 环比增减
    hbbh = DecimalField(precision=6)  # 环比变化
    rjcg = DecimalField(precision=6)  # 人均持股
    ltgdhs = LongField()  # 流通股东户数


class ShareHolderNumber(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()  # 截止日期
    Data = EmbeddedDocumentField(SingleShareHolderNumber)

    meta = {
        "collection": "f10_2_4_2_gdhs",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
