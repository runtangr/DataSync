# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField


class StockInterest(QKDocument):
    Obj = StringField(required=True)
    Date = DateTimeField()  # 时间
    StockShortName = StringField()
    QianChuQuanChengShu = DecimalField(precision=6)  # 前除权乘数
    QianChuQuanPianYi = DecimalField(precision=6)  # 前除权偏移
    HouChuQuanChengShu = DecimalField(precision=6)  # 后除权乘数
    HouQianChuQuanPianYi = DecimalField(precision=6)  # 后除权偏移
    FhkgXinXi = StringField()
    gqdjr = DateTimeField()  # 股权登记日
    cqcxr = DateTimeField()  # 除权除息日
    zhjyr = DateTimeField()  # 最后交易日
    qxbgq = DateTimeField()  # 权息报告期
    UpdateDateTime = DateTimeField()

    meta = {
        "collection": "f10_1_2_qxsj",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
