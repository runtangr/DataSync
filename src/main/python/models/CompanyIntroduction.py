# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField


class CompanyIntroduction(QKDocument):
    Obj = StringField(required=True)
    zqlx = StringField()  # 证券类型
    gsdm = LongField()  # 公司代码
    gsmc = StringField()  # 公司名称
    ywqc = StringField()  # 英文全称
    zcdz = StringField()  # 注册地址
    bgdz = StringField()  # 办公地址
    ssqy = StringField()  # 所属区域
    sshy = StringField()  # 所属行业
    gswz = StringField()  # 公司网址
    dzxx = StringField()  # 电子信箱
    ssrq = DateTimeField()  # 上市日期
    zgrq = DateTimeField()  # 招股日期
    fxl = DecimalField(precision=6)  # 发行量 ( 万股 )
    fxj = DecimalField(precision=6)  # 发行价(元)
    srkpj = DecimalField(precision=6)  # 首日开盘价(元)
    sstjr = StringField()  # 上市推荐人
    zcxs = StringField()  # 主承销商
    frdb = StringField()  # 法人代表
    dsz = StringField()  # 董事长
    zjl = StringField()  # 总经理
    dm = StringField()  # 董秘
    zqdb = StringField()  # 证券代表
    dh = StringField()  # 电话
    cz = StringField()  # 传真
    yb = StringField()  # 邮编
    kjsws = StringField()  # 会计事务所
    zyfw = StringField()  # 主营范围
    gsjs = StringField()  # 公司简史
    dmdh = StringField()  # 董秘电话
    dmcz = StringField()  # 董秘传真
    dmdzyx = StringField()  # 董秘电子邮箱
    RegionName = StringField()  # 地区

    meta = {
        "collection": "f10_2_1_gsgk",
        "indexes": [
            {
                "fields": ("Obj",),
                "unique": True
            }
        ]
    }
