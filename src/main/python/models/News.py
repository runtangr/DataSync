# -*- coding: utf-8 -*-
__author__ = "Sommily"

from mongoengine import signals
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, EmbeddedDocumentField, ListField, IntField


class NewsClass(QKEmbeddedDocument):
    ClassNo = StringField()
    ClassName = StringField()


class NewsStocks(QKEmbeddedDocument):
    StockCode = StringField()
    StockName = StringField()


class NewsCsrcIndustry(QKEmbeddedDocument):
    CsrcIndustryCode = StringField()
    CsrcIndustry = StringField()


class NewsSwIndustry(QKEmbeddedDocument):
    SwIndustry = StringField()
    SwIndustryCode = StringField()


class NewsKeys(QKEmbeddedDocument):
    KeyId = StringField()
    KeyName = StringField()


class NewsArea(QKEmbeddedDocument):
    AreaCode = StringField()
    AreaName = StringField()


class News(QKDocument):
    DateTime = DateTimeField()  # 新闻发布日期时间
    NewsId = StringField()  # 新闻 ID
    TitleMain = StringField()  # 新闻主标题
    TitleSub = StringField()  # 新闻副标题
    TitleApp = StringField()  # 新闻引标题
    Summary = StringField()  # 内容摘要(如果没有摘要字段，则取内容的前100个字符)，如果是附件类型，则为空
    SummaryStatus = StringField()  # 摘要状态， / 自动 / 手动 / (空字符串) /，一般这个有值，摘要才有值
    Source = StringField()  # 新闻来源
    SourceUrl = StringField()  # 来源URL
    Author = StringField()  # 作者
    AuthorUnit = StringField()  # 作者单位
    IsHeadLine = StringField()  # 是否头条
    NegaPosiMark = StringField()  # 正负面标识， 中性 / 负面 / 正面
    NewsClass = ListField(EmbeddedDocumentField(NewsClass))
    NewsStocks = ListField(EmbeddedDocumentField(NewsStocks))
    NewsCsrcIndustry = ListField(EmbeddedDocumentField(NewsCsrcIndustry))
    NewsSwIndustry = ListField(EmbeddedDocumentField(NewsSwIndustry))
    NewsKeys = ListField(EmbeddedDocumentField(NewsKeys))
    NewsArea = ListField(EmbeddedDocumentField(NewsArea))

    IntegrityValue = IntField(default=0)  # 数据完整性，1标题是进入，11标题内容均进入，10内容进入标题未进入

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    meta = {
        "collection": "f10_4_3_news",
        "indexes": [
            {
                "fields": ("NewsId",),
                "unique": True
            }
        ]
    }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if document.IntegrityValue % 10 == 1:
            return

        if document.TitleMain is not None:
            document.IntegrityValue += 1


signals.pre_save.connect(News.pre_save, sender=News)
