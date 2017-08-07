# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, LongField


class StockAnnouncement(QKDocument):
    Obj = StringField()  # 证券代码
    zqmc = StringField()  # 证券名称
    GgggId = StringField()  # 公告ID
    Date = DateTimeField()  # 公告日期
    Title = StringField()  # 公告标题
    Content = StringField()  # 公告: 内容压缩文件下载url
    ContentType = StringField()  # 内容类型, / word / excel / pdf / ... /
    UpdateDateTime = DateTimeField()
    Summary = StringField()
    RsId = LongField()

    meta = {"collection": "f10_4_2_stockgggg"}
