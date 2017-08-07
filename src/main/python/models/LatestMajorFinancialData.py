# -*- coding: utf-8 -*-
__author__ = "Sommily"

from models.QKDocument import QKDocument
from mongoengine import StringField, DecimalField, DateTimeField, LongField


class LatestMajorFinancialData(QKDocument):
    Obj = StringField()  # 证券代码
    BaoGaoQi = StringField()  # 报告期
    ShangShiJia = DecimalField(precision=6)  # 上市价 ------------- 需要增加 ( 大智慧无 )
    ShangShiRiQi = DateTimeField()  # 上市日期
    MeiGuShouYi = DecimalField(precision=6)  # 每股收益 ( 元 )
    MeiGuJingZiChan = DecimalField(precision=6)  # 每股净资产 ( 元 )
    JingZiChanShouYiLv = DecimalField(precision=6)  # 净资产收益率
    MeiGuJingYingXianJin = DecimalField(precision=6)  # 每股经营现金 ( 元 )
    MeiGuGongJiJin = DecimalField(precision=6)  # 每股公niz积金 ( 元 )
    MeiGuWeiFenPei = DecimalField(precision=6)  # 每股未分配 ( 元 )
    GuDongQuanYiBi = DecimalField(precision=6)  # 股东权益比
    JingLiRunTongBi = DecimalField(precision=6)  # 净利润同比
    # ZhuYingShouRuTongBi = DecimalField(precision=6)  # 主营收入同比
    XiaoShouMaoLiLv = DecimalField(precision=6)  # 销售毛利率
    TiaoZhengMeiGuJingZi = DecimalField(precision=6)  # 调整每股净资 ( 元 )
    ZongZiChan = DecimalField(precision=6)  # 总资产 ( 万元 )
    LiuDongZiChan = DecimalField(precision=6)  # 流动资产 ( 万元 )
    GuDingZiChan = DecimalField(precision=6)  # 固定资产 ( 万元 )
    WuXingZiChan = DecimalField(precision=6)  # 无形资产 ( 万元 )
    LiuDongFuZhai = DecimalField(precision=6)  # 流动负债 ( 万元 )
    ChangQiFuZhai = DecimalField(precision=6)  # 长期负债 ( 万元 )
    ZongFuZhai = DecimalField(precision=6)  # 总负债 ( 万元 )
    GuDongQuanYi = DecimalField(precision=6)  # 股东权益 ( 万元 )
    ZiBenGongJiJin = DecimalField(precision=6)  # 资本公积金 ( 万元 )
    JingYingXianJinLiuLiang = DecimalField(precision=6)  # 经营现金流量 ( 万元 )
    TouZiXianJinLiuLiang = DecimalField(precision=6)  # 投资现金流量 ( 万元 )
    ChouZiXianJinLiuLiang = DecimalField(precision=6)  # 筹资现金流量 ( 万元 )
    XianJinZengJiaE = DecimalField(precision=6)  # 现金增加额 ( 万元 )
    ZhuYingShouRu = DecimalField(precision=6)  # 主营收入 ( 万元 )
    ZhuYingLiRun = DecimalField(precision=6)  # 主营利润 ( 万元 )
    YingYeLiRun = DecimalField(precision=6)  # 营业利润 ( 万元 )
    TouZiShouYi = DecimalField(precision=6)  # 投资收益 ( 万元 )
    YingYeWaiShouZhi = DecimalField(precision=6)  # 营业外收支 ( 万元 )
    LiRunZongE = DecimalField(precision=6)  # 利润总额 ( 万元 )
    JingLiRun = DecimalField(precision=6)  # 净利润 ( 万元 )
    WeiFenPeiLiRun = DecimalField(precision=6)  # 未分配利润 ( 万元 )
    ZongGuBen = DecimalField(precision=6)  # 总股本 ( 万股 )
    LiuTongGu = DecimalField(precision=6)  # 当前流通股 (A 股或 B 股 )( 万股 )------ 需要增加 ( 大智慧无 )
    LiuTongAGu = DecimalField(precision=6)  # 流通 A 股 ( 万股 )
    LiuTongBGu = DecimalField(precision=6)  # 流通 B 股 ( 万股 )
    JingWaiShangShiGu = DecimalField(precision=6)  # 境外上市股 ( 万股 )
    QiTaLiuTongGu = DecimalField(precision=6)  # 其他流通股 ( 万股 )
    WuXianShouGuHeJi = DecimalField(precision=6)  # 无限售股合计 ( 万股 )
    XianShouGuHeJi = DecimalField(precision=6)  # 限售股合计 ( 万股 )
    GuDongRenShu = LongField()  # 股东人数
    PingJunGuBen = DecimalField(precision=6)  # 平均股本 ( 万股 )
    UpdateDateTime = DateTimeField()

    # New
    YingYeShouRuTongBi = DecimalField(precision=6)
    Rpt_des = StringField()
    RPT_YEAR = LongField()
    RPT_TAG = LongField()
    stockcode = StringField()
    stocksname = StringField()
    LiuTongGuTota = DecimalField(precision=6)
    LiuTongGuTotal = DecimalField(precision=6)
    MeiGuShouYiJiSuan = DecimalField(precision=6)

    meta = {
        "collection": "f10_1_1_zxzycwsj",
        "indexes": [
            {
                "fields": ("Obj",),
                "unique": True
            }
        ]
    }
