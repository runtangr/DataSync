# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import LongField, StringField, ListField, DateTimeField, DecimalField, EmbeddedDocumentField


class SingleDealReturn(QKEmbeddedDocument):
    cjlx = LongField()
    yybdm = LongField()
    yybmc = StringField()  # 营业部名称
    mrje = DecimalField(precision=6)  # 买入金额(万)
    mcje = DecimalField(precision=6)  # 卖出金额(万)

class DealReturn(QKDocument):
    cjl = DecimalField(precision=6)
    cjje = DecimalField(precision=6)
    Obj = StringField(required=True)
    gpmc = StringField()
    Date = DateTimeField()  # 日期
    ZdlxCode = LongField()
    ZdlxName = StringField()
    mrze = DecimalField(precision=6)
    mcze = DecimalField(precision=6)
    jgmrze = DecimalField(precision=6)
    jgmcze = DecimalField(precision=6)
    yzmrze = DecimalField(precision=6)
    yzmcze = DecimalField(precision=6)
    CHNG = DecimalField(precision=6)
    CHNG_PCT = DecimalField(precision=6)
    cjlx = LongField()
    Data = ListField(EmbeddedDocumentField(SingleDealReturn))
    UpdateDateTime = DateTimeField()
    RsId = LongField()

    meta = {
        "collection": "f10_2_6_3_cjhb",
        "indexes": [
            {
                "fields": ("Obj", "Date", "ZdlxCode"),
                "unique": True
            }
        ]
    }
