# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, DecimalField, EmbeddedDocumentField, LongField


class SingleAssetLiability(QKEmbeddedDocument):
    dw = StringField()  # 单位
    zzc = DecimalField(precision=6)  # 总资产
    hbzj = DecimalField(precision=6)  # 货币资金
    jyxjrzc = DecimalField(precision=6)  # 交易性金融资产
    gdzcje = DecimalField(precision=6)  # 固定资产净额
    kgcsjrzc = DecimalField(precision=6)  # 可供出售金融资产
    wxzc = DecimalField(precision=6)  # 无形资产
    zfz = DecimalField(precision=6)  # 总负债
    gdqy = DecimalField(precision=6)  # 股东权益
    zbgjj = DecimalField(precision=6)  # 资本公积金
    bgfldm = LongField()  # 报告分类代码

    wfplr = DecimalField(precision=6)  # 未分配利润

class AssetLiability(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()  # 截止日期
    Data = EmbeddedDocumentField(SingleAssetLiability)

    meta = {
        "collection": "f10_2_2_4_zcfzb",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
