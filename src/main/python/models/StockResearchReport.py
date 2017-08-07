# -*- coding: utf-8 -*-
__author__ = "Sommily"

from mongoengine import signals
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, EmbeddedDocumentField, ListField, IntField


class ResearchReportClass(QKEmbeddedDocument):
    ClassNo = StringField()
    ClassName = StringField()


class ResearchReportStocks(QKEmbeddedDocument):
    StockCode = StringField()
    StockName = StringField()


class ResearchReportCsrcIndustry(QKEmbeddedDocument):
    CsrcIndustry = StringField()
    CsrcIndustryCode = StringField()


class ResearchReportSwIndustry(QKEmbeddedDocument):
    SwIndustry = StringField()
    SwIndustryCode = StringField()


class ResearchReportKeys(QKEmbeddedDocument):
    KeyId = StringField()
    KeyName = StringField()


class ResearchReportArea(QKEmbeddedDocument):
    AreaCode = StringField()
    AreaName = StringField()


class StockResearchReport(QKDocument):
    YanBaoId = StringField()  # 研报ID
    BaoGaoRiQi = DateTimeField()  # 报告日期
    YanJiuJiGou = StringField()  # 研究机构
    YanJiuZuoZhe = StringField()  # 研究作者
    YanBaoBiaoTi = StringField()  # 研报标题
    Summary = StringField()  # 内容摘要(如果没有摘要字段，则取内容的前100个字符)，如果是附件类型，则为空
    YbClass = ListField(EmbeddedDocumentField(ResearchReportClass))
    YbStocks = ListField(EmbeddedDocumentField(ResearchReportStocks))
    YbCsrcIndustry = ListField(EmbeddedDocumentField(ResearchReportCsrcIndustry))
    YbSwIndustry = ListField(EmbeddedDocumentField(ResearchReportSwIndustry))
    YbKeys = ListField(EmbeddedDocumentField(ResearchReportKeys))
    YbArea = ListField(EmbeddedDocumentField(ResearchReportArea))

    IntegrityValue = IntField(default=0)  # 数据完整性，1标题是进入，11标题内容均进入，10内容进入标题未进入

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    meta = {
        "collection": "f10_5_1_gsyb",
        "indexes": [
            {
                "fields": ("YanBaoId", ),
                "unique": True
            }
        ]
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if document.IntegrityValue % 10 == 1:
            return

        if document.YanBaoBiaoTi is not None:
            document.IntegrityValue += 1


signals.pre_save.connect(StockResearchReport.pre_save, sender=StockResearchReport)

