# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument
from mongoengine import StringField, LongField, DateTimeField


class StockCodeList(QKDocument):
    Obj = StringField(required=True, unique=True)
    MarketCode = StringField()
    StockCode = StringField()
    StockName = StringField()
    StockFullName = StringField()
    ShortCode = StringField()
    TypeValue = StringField()
    TypeName = StringField()
    SubMarketType = StringField()
    SubMarketTypeName = StringField()
    StatusValue = StringField()
    StatusName = StringField()
    StartDate = DateTimeField()
    EndDate = DateTimeField()

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    meta = {
        "collection": "f10_1_4_stockcodelist"
    }
