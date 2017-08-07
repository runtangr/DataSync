# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField


class FinaEvent(QKDocument):
    RsId = StringField()  # 记录号
    UpdateDateTime = DateTimeField()  # 更新日期时间，日期时间类型
    EventId = StringField()  # 事件ID
    NewsDateTime = DateTimeField()  # 新闻日期时间 #  日期型
    NewsSource = StringField()  # 新闻来源
    NewsTitle = StringField()  # 国军民融合发展暨国防光电子信息化装备展" #  新闻标题
    NewsContent = StringField()  # 新闻内容
    NewsGNBK = StringField()  # 相关概念板块名称
    NewsTypeCode = StringField()  # 事件类型分类代码
    NewsTypeName = StringField()  # 事件类型分类名称
    NewsAreaCode = StringField()  # 新闻地区代码
    NewsAreaName = StringField()  # 新闻地区名称

    meta = {
        "collection": "f10_4_8_1_fina_event",
        "indexes": [
            {
                "fields": ("RsId",),
                "unique": True
            }
        ]
    }
