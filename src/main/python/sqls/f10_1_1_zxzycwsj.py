# -*- coding: utf-8 -*-
__author__ = "Cyh"
sql = """
SELECT CAST(id AS NVARCHAR(MAX)) AS RsId, StockCode, Obj, BaoGaoQi,
       stocksoftdata.dbo.Date2Str( BaoGaoQi ) AS II_BaoGaoQi, ShangShiJia, ShangShiRiQi,
       stocksoftdata.dbo.Date2Str( ShangShiRiQi ) II_ShangShiRiQi, MeiGuShouYi,
       MeiGuShouYiJiSuan, MeiGuJingZiChan, JingZiChanShouYiLv, MeiGuJingYingXianJin,
       MeiGuGongJiJin, MeiGuWeiFenPei, GuDongQuanYiBi, JingLiRunTongBi,
       YingYeShouRuTongBi, XiaoShouMaoLiLv, TiaoZhengMeiGuJingZi, ZongZiChan,
       LiuDongZiChan, GuDingZiChan, WuXingZiChan, LiuDongFuZhai, ChangQiFuZhai,
       ZongFuZhai, GuDongQuanYi, ZiBenGongJiJin, JingYingXianJinLiuLiang,
       TouZiXianJinLiuLiang, ChouZiXianJinLiuLiang, XianJinZengJiaE, ZhuYingShouRu,
       ZhuYingLiRun, YingYeLiRun, TouZiShouYi, YingYeWaiShouZhi, LiRunZongE, JingLiRun,
       WeiFenPeiLiRun, ZongGuBen, LiuTongGu, LiuTongAGu, LiuTongBGu, JingWaiShangShiGu,
       QiTaLiuTongGu, LiuTongGuTotal, XianShouGuHeJi, GuDongRenShu, PingJunGuBen,
       UpdateDateTime
  FROM stocksoftdata.dbo.F10_1_1_ZXZYCWSJ
"""