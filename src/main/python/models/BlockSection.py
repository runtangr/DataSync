# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, LongField, DateTimeField


class BlockSection(QKDocument):
    ClassId = LongField(required=True)  # 板块ID
    ClassfatherId = LongField()  # 板块的父级
    SysCode = LongField()  # 板块分类
    SectionLevel = LongField()  # 板块级别
    PlateCode = StringField()  # 板块代码
    SectionNameH = StringField()  # 板块简称
    SectionName = StringField()  # 板块名称
    gps = LongField()  # 板块内股票数
    ComputerType = LongField()  # 计算方式，1：权重为1，涨跌幅计算；2：指数系数方式计算
    ShortCode = StringField()
    UpdateDateTime = DateTimeField()
    RsId = LongField()

    meta = {"collection": "f10_6_1_block_section"}
