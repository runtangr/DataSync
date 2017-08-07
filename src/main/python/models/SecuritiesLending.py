# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, DecimalField, EmbeddedDocumentField


class SingleSecuritiesLending(QKEmbeddedDocument):
    rzmrje = DecimalField(precision=6)  # 融资买入额(万元)
    rzchje = DecimalField(precision=6)  # 融资偿还额(万元)
    rzye = DecimalField(precision=6)  # 融资余额(万元)
    rqmcl = DecimalField(precision=6)  # 融券卖出量(万股)
    rqchl = DecimalField(precision=6)  # 融券偿还量(万股)
    rqyl = DecimalField(precision=6)  # 融券余量(万股)
    rqmcje = DecimalField(precision=6)  # 融券卖出额(万元)
    rqchje = DecimalField(precision=6)  # 融券偿还额(万元)
    rqye = DecimalField(precision=6)  # 融券余额(万元)
    rzrqye = DecimalField(precision=6)  # 融资融券余额(万元)
    ltgb = DecimalField(precision=6)  # 流通股本(万股)
    spj = DecimalField(precision=6)  # 收盘价(元)
    rzyezs = DecimalField(precision=6)  # 融资余额增速( %)
    rzyezltszb = DecimalField(precision=6)  # 融资余额占流通市值比( %)

    UpdateDateTime = DateTimeField()
    RsId = StringField()


class SecuritiesLending(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()  # 截止日期
    Data = EmbeddedDocumentField(SingleSecuritiesLending)

    meta = {
        "collection": "f10_2_8_2_rzrq",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
