# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, LongField


class StockAnnouncementContent(QKDocument):
    GgggId = StringField()  # 公告ID
    Obj = StringField()  # 证券代码
    zqmc = StringField()  # 证券名称
    Date = DateTimeField()  # 公告日期
    Title = StringField()  # 公告标题
    Summary = StringField()
    ContentText = StringField()  # 公告内容
    AttachmentUrl = StringField()
    AttachmentType = StringField()
    AttachmentPath = StringField()
    AttachmentPathMd5 = StringField()
    UpdateDateTime = DateTimeField()
    RsId = LongField()

    meta = {"collection": "f10_4_2_1_stockgggg_content"}
