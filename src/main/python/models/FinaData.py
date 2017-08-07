# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField


class FinaData(QKDocument):
    RsId = StringField()  # 记录号
    UpdateDateTime = DateTimeField()  # 更新日期时间，日期时间类型
    EventId = StringField()  # 事件ID
    EventDateTime = DateTimeField()  # 事件日期时间# 日期型
    EventTitle = StringField()  # 数据名称
    EventContent = StringField()
    EventAreaCode = StringField()  # 事件地区代码
    EventAreaName = StringField()  # 事件地区名称
    LastValue = StringField()  # 上期数值
    ExcepValue = StringField()  # 预测值
    RealValue = StringField()  # 公布值
    Unit = StringField()  # 单位
    Important = StringField()  # 事件重要性，低 / 中 / 高 /
    EventIndexId = StringField()  # 事件索引ID，用于确认事件历史数据

    meta = {
        "collection": "f10_4_8_2_fina_data",
        "indexes": [
            {
                "fields": ("RsId",),
                "unique": True
            }
        ]
    }
