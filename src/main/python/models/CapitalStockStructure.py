# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, DecimalField, EmbeddedDocumentField


class SingleCapitalStockStructure(QKEmbeddedDocument):
    zgb = DecimalField(precision=6)  # 总股本(万股)
    ltgbdq = DecimalField(precision=6)  # 变动后当前流通股本 - ---- 比大智慧多的,
    # 证券代码是A股, 就是流通A股, 证券代码是流通B股, 就是流通B股
    ltgf = DecimalField(precision=6)  # 流通股份(万股)
    ltag = DecimalField(precision=6)  # 流通A股(含高管)(万股)
    ltbg = DecimalField(precision=6)  # 流通B股(含高管)(万股)
    lthg = DecimalField(precision=6)  # 流通H股(含高管)(万股)
    qtltgf = DecimalField(precision=6)  # 其他流通股份(万股)
    xsltg = DecimalField(precision=6)  # 限售流通股(万股)
    xsltag = DecimalField(precision=6)  # 限售流通A股(万股)
    xsltbg = DecimalField(precision=6)  # 限售流通B股(万股)
    xslthg = DecimalField(precision=6)  # 限售流通H股(万股)
    xsgjcg = DecimalField(precision=6)  # 限售国家持股(万股)
    xsgyfrcg = DecimalField(precision=6)  # 限售国有法人持股(万股)
    xsjnfrcg = DecimalField(precision=6)  # 限售境内法人持股(万股)
    xsjnzrrcg = DecimalField(precision=6)  # 限售境内自然人持股(万股)
    xsggcg = DecimalField(precision=6)  # 限售高管持股(万股)
    xsjwfrcg = DecimalField(precision=6)  # 限售境外法人持股(万股)
    xsjwzrrcg = DecimalField(precision=6)  # 限售境外自然人持股(万股)
    wltg = DecimalField(precision=6)  # 未流通股(万股)
    gjg = DecimalField(precision=6)  # 国家股(万股)
    gyfrg = DecimalField(precision=6)  # 国有法人股(万股)
    jnfgyfr = DecimalField(precision=6)  # 境内非国有法人(万股)
    zpg = DecimalField(precision=6)  # 转配股(万股)
    nbzgg = DecimalField(precision=6)  # 内部职工股(万股)
    yxg = DecimalField(precision=6)  # 优先股(万股)
    jwfrg = DecimalField(precision=6)  # 境外法人股(万股)
    qtwltgf = DecimalField(precision=6)  # 其他未流通股份(万股)


class CapitalStockStructure(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()
    Data = EmbeddedDocumentField(SingleCapitalStockStructure)

    meta = {
        "collection": "f10_2_5_1_gbjg",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
