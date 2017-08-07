# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField


class EconomicCalendar(QKDocument):
    RsId = StringField(required=True)
    UpdateDateTime = DateTimeField()  # 更新日期时间，日期时间类型
    NewsDate = DateTimeField()  # 新闻日期
    NewsSource = StringField()  # 新闻来源
    NewsTitle = StringField()  # 新闻标题
    NewsContent = StringField()  # 新闻内容
    NewsGNBK = StringField()  # 相关概念板块名称
    NewsTypeCode = StringField()  # 事件类型分类代码
    NewsTypeName = StringField()  # 事件类型分类名称

    meta = {
        "collection": "f10_4_8_caijingrili",
        "indexes": [
            {
                "fields": ("RsId",),
                "unique": True
            }
        ]
    }
