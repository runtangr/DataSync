# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DecimalField, LongField, DateTimeField


class BlockSectionStock(QKDocument):
    ClassId = LongField()  # 板块ID
    ClassfatherId = LongField()  # 板块的父级Id
    SysCode = LongField()  # 板块分类
    SectionNameH = StringField()  # 板块简称
    SectionName = StringField()  # 板块名称
    PlateCode = StringField()  # 板块代码
    SectionLevel = LongField() # 板块级别
    MarketCode = StringField()  # 股票的市场代码
    StockCode = StringField()  # 股票代码
    StockShortName = StringField()  # 股票简称
    Obj = StringField() # 市场代码+股票代码
    bzzb = DecimalField(precision=6)  # 市值占比
    UpdateDateTime = DateTimeField()
    RsId = LongField()

    meta = {
        "collection": "f10_6_2_block_section_stock",
        "indexes": [
            {
                "fields": ("ClassId", "MarketCode", "StockCode"),
                "unique": True
            }
        ]

    }
