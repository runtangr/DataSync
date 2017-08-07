# -*- coding: utf-8 -*-
__author__ = "Sommily"

from mongoengine import signals
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, ListField, EmbeddedDocumentField, IntField


class ZiXunStock(QKEmbeddedDocument):
    StockCode = StringField()
    StockName = StringField()


class StockNewsAnnouncementResearchReport(QKDocument):
    ZiXunId = StringField()  # 资讯ID
    ZiXunType = StringField()  # 资讯类型， / XW / GG / YB / / 新闻 / 公告 / 研报 /
    ZiXunDateTime = DateTimeField()  # 资讯日期时间
    ZiXunBiaoTi = StringField()  # 资讯标题
    ZiXunJiGou = StringField()  # 资讯机构(研究机构 / 新闻来源)
    ZiXunZuoZhe = StringField()  # 资讯作者
    Summary = StringField()  # 内容摘要(如果没有摘要字段，则取内容的前100个字符)，如果是附件类型，则为空
    ZiXunStocks = ListField(EmbeddedDocumentField(ZiXunStock))

    IntegrityValue = IntField(default=0)  # 数据完整性，1标题是进入，11标题内容均进入，10内容进入标题未进入

    RsId = StringField()
    UpdateDateTime = DateTimeField()

    meta = {
        "collection": "f10_7_123_stock_news_gg_yb",
        "indexes": [
            {
                "fields": ("ZiXunId", "ZiXunType"),
                "unique": True
            }
        ]
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if document.IntegrityValue % 10 == 1:
            return

        if document.ZiXunBiaoTi is not None:
            document.IntegrityValue += 1


signals.pre_save.connect(StockNewsAnnouncementResearchReport.pre_save, sender=StockNewsAnnouncementResearchReport)

