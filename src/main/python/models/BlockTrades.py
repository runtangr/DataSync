# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, ListField, DateTimeField, DecimalField, EmbeddedDocumentField


class SingleBlockTrades(QKEmbeddedDocument):
    jg = DecimalField(precision=6)  # 价格
    drspj = DecimalField(precision=6)  # 当日收盘价
    zjl = DecimalField(precision=6)  # 折价率( %)
    cjl = DecimalField(precision=6)  # 成交量
    cjje = DecimalField(precision=6)  # 成交金额
    mf = StringField()  # 买方
    mf2 = StringField()  # 卖方
    RsId = StringField()


class BlockTrades(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()  # 截止日期
    Data = ListField(EmbeddedDocumentField(SingleBlockTrades))

    meta = {
        "collection": "f10_2_8_5_dzjy",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            },
        ]
    }
