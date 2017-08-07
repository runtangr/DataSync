# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, DecimalField, EmbeddedDocumentField, LongField


class SingleInComeStatement(QKEmbeddedDocument):
    dw = StringField()  # 单位
    yysr = DecimalField(precision=6)  # 营业收入
    yycb = DecimalField(precision=6)  # 营业成本
    yylr = DecimalField(precision=6)  # 营业利润
    tzsy = DecimalField(precision=6)  # 投资收益
    yywszje = DecimalField(precision=6)  # 营业外收支净额
    lrze = DecimalField(precision=6)  # 利润总额
    jlr = DecimalField(precision=6)  # 净利润
    wfplr = DecimalField(precision=6)  # 未分配利润
    bgfldm = LongField()  # 报告分类代码

class InComeStatement(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()  # 截止日期
    Data = EmbeddedDocumentField(SingleInComeStatement)

    meta = {
        "collection": "f10_2_2_3_lrfpb",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
