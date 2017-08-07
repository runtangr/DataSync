# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, ListField, DateTimeField, DecimalField, LongField, EmbeddedDocumentField


class SubShareHolderInfo(QKEmbeddedDocument):
    cgs = DecimalField(precision=6)  # 持股数(万股)
    zzgs = DecimalField(precision=6)  # 占总股数( %)
    zjqk = DecimalField(precision=6)  # 增减情况(万股)
    gbxz = StringField()  # 股本性质

    def __eq__(self, other):
        return self.cgs == other.cgs \
               and self.zzgs == other.zzgs \
               and self.zjqk == other.zjqk \
               and self.gbxz == other.gbxz


class SingleShareHolder(QKEmbeddedDocument):
    xh = LongField()  # 序号
    gdmc = StringField()  # 股东名称
    gsdm = LongField()  # 公司代码
    DData = ListField(EmbeddedDocumentField(SubShareHolderInfo))

    def __eq__(self, other):
        return self.xh == other.xh \
               and self.gdmc == other.gdmc \
               and self.gsdm == other.gsdm


class TopTenShareHolder(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()  # 截止日期
    gdrs = LongField()  # 股东人数
    Data = ListField(EmbeddedDocumentField(SingleShareHolder))

    meta = {
        "collection": "f10_2_4_1_sdgd",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
