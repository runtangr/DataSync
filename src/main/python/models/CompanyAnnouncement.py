# -*- coding: utf-8 -*-
__author__ = "Sommily"

from mongoengine import signals
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, ListField, EmbeddedDocumentField, DateTimeField, IntField


class AnnouncementClass(QKEmbeddedDocument):
    ClassNo = StringField()
    ClassName = StringField()


class AnnouncementStocks(QKEmbeddedDocument):
    StockCode = StringField()
    StockName = StringField()


class CompanyAnnouncement(QKDocument):
    GgggId = StringField()  # 个股公告ID
    DateTime = StringField()  # 公告日期时间
    Title = StringField()  # 公告标题
    Summary = StringField()  # 内容摘要(如果没有摘要字段，则取内容的前100个字符)，如果是附件类型，则为 > 空
    EndDate = StringField()  # 业绩报告日期
    IsHaveAttach = StringField()  # 是否附带附件，1为是，0为否
    IsHaveContent = StringField()  # 是否有全文内容，1 为是，0 为否
    Source = StringField()  # 数据来源
    GgggClass = ListField(EmbeddedDocumentField(AnnouncementClass))
    GgggStocks = ListField(EmbeddedDocumentField(AnnouncementStocks))

    IntegrityValue = IntField(default=0)  # 数据完整性，1标题是进入，11标题内容均进入，10内容进入标题未进入

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    meta = {
        "collection": "f10_4_4_gsgg",
        "indexes": [
            {
                "fields": ("GgggId", ),
                "unique": True
            }
        ]
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if document.IntegrityValue % 10 == 1:
            return

        if document.Title is not None:
            document.IntegrityValue += 1


signals.pre_save.connect(CompanyAnnouncement.pre_save, sender=CompanyAnnouncement)
