# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, DecimalField, EmbeddedDocumentField, LongField


class SingleCashFlow(QKEmbeddedDocument):
    xjjzje = DecimalField(precision=6)  # 现金等的净增加额
    dw = StringField()  # 单位
    jyxjlr = DecimalField(precision=6)  # 经营现金流入小计
    jyxjlc = DecimalField(precision=6)  # 经营现金流出小计
    jyxjje = DecimalField(precision=6)  # 经营现金流量净额
    tzxjlr = DecimalField(precision=6)  # 投资现金流入小计
    tzxjlc = DecimalField(precision=6)  # 投资现金流出小计
    tzxjje = DecimalField(precision=6)  # 投资现金流量净额
    czxjlr = DecimalField(precision=6)  # 筹资现金流入小计
    czxjlc = DecimalField(precision=6)  # 筹资现金流出小计
    czxjje = DecimalField(precision=6)  # 筹资现金流量净额
    hlbdyx = DecimalField(precision=6)  # 汇率变动影响
    xxsdxj = DecimalField(precision=6)  # 销售所得现金
    bgfldm = LongField()  # 报告分类代码
    sshy = StringField()

class CashFlow(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()  # 截止日期
    Data = EmbeddedDocumentField(SingleCashFlow)

    meta = {
        "collection": "f10_2_2_2_xjllb",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
