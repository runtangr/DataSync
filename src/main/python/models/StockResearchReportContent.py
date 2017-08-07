# -*- coding: utf-8 -*-
__author__ = "Sommily"

from mongoengine import signals
from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, ListField, EmbeddedDocumentField
from StockResearchReport import StockResearchReport
from StockNewsAnnouncementResearchReport import StockNewsAnnouncementResearchReport


class Attachment(QKEmbeddedDocument):
    AttachmentUrl = StringField()  # 附件URL
    AttachmentType = StringField()  # 内容类型,/word/excel/pdf/.../
    AttachmentPath = StringField()  # 附件路径
    AttachmentPathMd5 = StringField()  # 附件路径MD5


class StockResearchReportContent(QKDocument):
    YanBaoId = StringField()  # 研报ID
    BaoGaoRiQi = DateTimeField()  # 报告日期
    YanJiuJiGou = StringField()  # 研究机构
    YanJiuZuoZhe = StringField()  # 研究作者
    YanBaoBiaoTi = StringField()  # 研报标题
    Summary = StringField()  # 内容摘要(如果没有摘要字段，则取内容的前100个字符)，如果是附件类型，则为空
    YanBaoNeiRong = StringField()  # 研报内容
    Attachment = ListField(EmbeddedDocumentField(Attachment))

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    meta = {
        "collection": "f10_5_1_1_gsyb_content",
        "indexes": [
            {
                "fields": ("YanBaoId", ),
                "unique": True
            }
        ]
    }

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        report_id = document.YanBaoId
        print("{}".format(report_id))
        try:
            query_set = StockResearchReport.objects(YanBaoId=report_id)
            if len(query_set) == 0:
                report = StockResearchReport()
                report.YanBaoId = report_id
                report.IntegrityValue = 10
                report.save()
            else:
                report = query_set.get()
                if report.IntegrityValue / 10 % 10 == 0:
                    report.IntegrityValue += 10
                    report.save()

            query_set = StockNewsAnnouncementResearchReport.objects(ZiXunId=report_id, ZiXunType="YB")
            if len(query_set) == 0:
                stock_info = StockNewsAnnouncementResearchReport()
                stock_info.ZiXunId = report_id
                stock_info.ZiXunType = "YB"
                stock_info.IntegrityValue = 10
                stock_info.save()
            else:
                stock_info = query_set.get()
                if stock_info.IntegrityValue / 10 % 10 == 0:
                    stock_info.IntegrityValue += 10
                    stock_info.save()

        except Exception as e:
            print("StockResearchReportContent post save failed: {}".format(e))


signals.post_save.connect(StockResearchReportContent.post_save, sender=StockResearchReportContent)
