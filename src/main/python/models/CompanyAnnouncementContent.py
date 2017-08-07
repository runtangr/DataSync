# -*- coding: utf-8 -*-
__author__ = "Sommily"

from mongoengine import signals
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, ListField, EmbeddedDocumentField, DateTimeField
from CompanyAnnouncement import CompanyAnnouncement
from StockNewsAnnouncementResearchReport import StockNewsAnnouncementResearchReport

class Attachment(QKEmbeddedDocument):
    AttachmentUrl = StringField()
    AttachmentType = StringField()
    AttachmentPath = StringField()
    AttachmentPathMd5 = StringField()
    AttachmentTitle = StringField()


class CompanyAnnouncementContent(QKDocument):
    GgggId = StringField()  # 个股公告ID
    DateTime = StringField()  # 公告日期时间
    Title = StringField()  # 公告标题
    Attachment = ListField(EmbeddedDocumentField(Attachment))
    ContentText = StringField()

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    meta = {
        "collection": "f10_4_4_1_gsgg_content",
        "indexes": [
            {
                "fields": ("GgggId",),
                "unique": True
            }
        ]
    }

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        announcement_id = document.GgggId
        try:
            query_set = CompanyAnnouncement.objects(GgggId=announcement_id)
            if len(query_set) == 0:
                announcement = CompanyAnnouncement()
                announcement.GgggId = announcement_id
                announcement.IntegrityValue = 10
                announcement.save()
            else:
                announcement = query_set.get()
                if announcement.IntegrityValue / 10 % 10 == 0:
                    announcement.IntegrityValue += 10
                    announcement.save()

            query_set = StockNewsAnnouncementResearchReport.objects(ZiXunId=announcement_id, ZiXunType="GG")
            if len(query_set) == 0:
                stock_info = StockNewsAnnouncementResearchReport()
                stock_info.ZiXunId = announcement_id
                stock_info.ZiXunType = "GG"
                stock_info.IntegrityValue = 10
                stock_info.save()
            else:
                stock_info = query_set.get()
                if stock_info.IntegrityValue / 10 % 10 == 0:
                    stock_info.IntegrityValue += 10
                    stock_info.save()

        except Exception as e:
            print("CompanyAnnouncementContent post save failed: {}".format(e))


signals.post_save.connect(CompanyAnnouncementContent.post_save, sender=CompanyAnnouncementContent)
