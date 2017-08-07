# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, LongField


class StockNewsContent(QKDocument):
    NewsId = StringField()  # 新闻ID
    Obj = StringField()  # 证券代码
    Date = DateTimeField()  # 新闻日期
    zqmc = StringField()  # 证券名称
    Title = StringField()  # 新闻标题
    Summary = StringField()
    ContentUrl = StringField()
    ContentText = StringField()  # 新闻内容
    ContentHtml = StringField()
    AttachmentUrl = StringField()
    AttachmentPath = StringField()
    AttachmentPathMd5 = StringField()
    Source = StringField()  # 新闻来源
    UpdateDateTime = DateTimeField()
    RsId = LongField()

    meta = {"collection": "f10_4_1_1_stocknews_content"}
