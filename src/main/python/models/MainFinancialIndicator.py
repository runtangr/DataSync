# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import StringField, DateTimeField, DecimalField, EmbeddedDocumentField, LongField


class SingleFinancialIndicator(QKEmbeddedDocument):
    kjssjyj = StringField()  # 会计师事务所审计意见
    jbmgsy = DecimalField(precision=6)  # 基本每股收益(元)
    kchjbmgsy = DecimalField(precision=6)  # 基本每股收益(扣除后)
    tbmgsy = DecimalField(precision=6)  # 摊薄每股收益(元)
    mgjzc = DecimalField(precision=6)  # 每股净资产(元)
    mgwfplr = DecimalField(precision=6)  # 每股未分配利润(元)
    mggjj = DecimalField(precision=6)  # 每股公积金(元)
    xsmll = DecimalField(precision=6)  # 销售毛利率( %)
    yylrl = DecimalField(precision=6)  # 营业利润率( %)
    jlrl = DecimalField(precision=6)  # 净利润率( %)
    jzcsyl = DecimalField(precision=6) #  净资产收益率( %)
    jqjzcsyl = DecimalField(precision=6)  # 加权净资产收益率( %)
    tbjzcsyl = DecimalField(precision=6)  # 摊薄净资产收益率( %)
    gdqy = DecimalField(precision=6)  # 股东权益( %)
    ldbl = DecimalField(precision=6)  # 流动比率
    sdbl = DecimalField(precision=6)  # 速动比率
    mgjyxjll = DecimalField(precision=6)  # 每股经营现金流量(元)
    bbgbr = DateTimeField()  # 报表公布日
    zzcbcl = DecimalField(precision=6)
    xsmgsy = DecimalField(precision=6)  # 稀释每股收益(元)
    bgfldm = LongField()  # 报告分类代码 10一季度...
    xsjll = DecimalField(precision=6)  # 销售净利率
    xscbl = DecimalField(precision=6)  # 销售成本率
    zzcsyl = DecimalField(precision=6)  # 总资产收益率
    jbsyzzl = DecimalField(precision=6)  # 基本每股收益同比增长率
    xxsyzzl = DecimalField(precision=6)  # 稀释每股收益同比增长率
    yylrzzl = DecimalField(precision=6)  # 营业利润(同比增长率)
    yysyzzl = DecimalField(precision=6)  # 营业收入(同比增长率)
    lrzezzl = DecimalField(precision=6)  # 利润总额(同比增长率)
    yyzsrzzl = DecimalField(precision=6)  # 营业总收入(同比增长率)
    jlrzzl = DecimalField(precision=6)  # 净利润(同比增长率)
    yyzq = DecimalField(precision=6)  # 营业周期
    chzzts = DecimalField(precision=6)  # 存货周转天数
    chzzl = DecimalField(precision=6)  # 存货周转率
    yszkzzl = DecimalField(precision=6)  # 应收账款周转率
    zzczzl = DecimalField(precision=6)  # 总资产周转率
    ldzczzl = DecimalField(precision=6)  # 流动资产周转率
    yfzkzzl = DecimalField(precision=6)  # 应付账款周转率
    gdzczzl = DecimalField(precision=6)  # 固定资产周转率
    xxjll = DecimalField(precision=6)
    xxcbl = DecimalField(precision=6)
    sshy = StringField()
    STOCKSNAME = StringField()
    STOCKCODE = StringField()

             
class MainFinancialIndicator(QKDocument):
    Date = DateTimeField()  # 截止日期
    Data = EmbeddedDocumentField(SingleFinancialIndicator)
    Obj = StringField()

    meta = {
        "collection": "f10_2_2_1_zycwzb",
        "indexes": [
            {
                "fields": ("Obj", "Date"),
                "unique": True
            }
        ]
    }
