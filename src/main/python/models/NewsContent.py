# -*- coding: utf-8 -*-
__author__ = "Sommily"

from mongoengine import signals
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField
from News import News
from StockNewsAnnouncementResearchReport import StockNewsAnnouncementResearchReport


class NewsContent(QKDocument):
    NewsId = StringField(required=True, unique=True)  # 新闻ID
    AttachmentUrl = StringField()
    AttachmentPath = StringField()
    AttachmentPathMd5 = StringField()
    ContentText = StringField()  # 新闻内容
    ContentHtml = StringField()

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    meta = {
        "collection": "f10_4_3_1_news_content"
    }

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        news_id = document.NewsId
        try:
            query_set = News.objects(NewsId=news_id)
            if len(query_set) == 0:
                news = News()
                news.NewsId = news_id
                news.IntegrityValue = 10
                news.save()
            else:
                news = query_set.get()
                if news.IntegrityValue / 10 % 10 == 0:
                    news.IntegrityValue += 10
                    news.save()

            query_set = StockNewsAnnouncementResearchReport.objects(ZiXunId=news_id, ZiXunType="XW")
            if len(query_set) == 0:
                stock_info = StockNewsAnnouncementResearchReport()
                stock_info.ZiXunId = news_id
                stock_info.ZiXunType = "XW"
                stock_info.IntegrityValue = 10
                stock_info.save()
            else:
                stock_info = query_set.get()
                if stock_info.IntegrityValue / 10 % 10 == 0:
                    stock_info.IntegrityValue += 10
                    stock_info.save()

        except Exception as e:
            print("NewsContent post save failed: {}".format(e))


signals.post_save.connect(NewsContent.post_save, sender=NewsContent)
