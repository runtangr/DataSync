# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField


class ActualShareHolder(QKDocument):
    Obj = StringField(required=True)
    mc = StringField()  # 名称
    frdb = StringField()  # 法人代表
    zczb = DecimalField(precision=6)  # 注册资本(万元)
    clrq = DateTimeField()  # 成立日期
    jyyw = StringField()  # 经营业务
    qylx = StringField()  # 企业类型

    meta = {
        "collection": "f10_2_4_4_kggd",
        "indexes": [
            {
                "fields": ("Obj",),
                "unique": True
            }
        ]
    }
