# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, DecimalField, EmbeddedDocumentListField


class SingleCapitalStock(QKEmbeddedDocument):
    Date = DateTimeField()  # 变动日期
    bdhzgb = DecimalField(precision=6)  # 变动后总股本
    bdhltgb = DecimalField(precision=6)  # 变动后当前流通股本
    UpdateDateTime = DateTimeField()


class CapitalStockHistory(QKDocument):
    Obj = StringField(required=True, unique=True)
    Data = EmbeddedDocumentListField(SingleCapitalStock)

    meta = {"collection": "f10_1_3_gbls"}
