# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField


class StockNews(QKDocument):
    Obj = StringField()  # 证券代码
    Date = DateTimeField()  # 新闻日期
    zqmc = StringField()  # 证券名称
    NewsId = StringField()  # 新闻 ID
    Title = StringField()  # 新闻标题
    Source = StringField()  # 新闻来源
    UpdateDateTime = DateTimeField()
    Summary = StringField()
    RsId = StringField()

    meta = {"collection": "f10_4_1_stocknews"}
