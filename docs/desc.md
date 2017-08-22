###9.1.信息地雷-历史统计###
###更新频率说明###
MsSql每日凌晨09:00:00更新统计上一日数据
###更新方式###
增量更新
####存储集合名####
f10_9_1_xxdllstj
####主键####
RsId
####输出数据####
      RsID				自增ID
	  UpdateDateTime	默认时间
	  Obj				股票代码
	  ZxDate            资讯日期
	  CountNum         数量
	  ZxType            资讯类型
	  
###1.1、最新主要财务数据###
--这部分数据需要进入StockHanding相关的Redis/mongdb，客户端从行情接口取大行情时进行下载
###更新频率说明###
MsSql每日08:00:00更新数据
###更新方式###
全量更新
####存储集合名####
"f10_1_1_zxzycwsj"
####主键组合####
Obj  

####存储数据####
	[
	    {
            "Obj":"SH600000",//证券代码
            "BaoGaoQi": "20150930", //报告期
            "ShangShiJia": 18.12,//上市价-------------需要增加(大智慧无)
            "ShangShiRiQi": "20091225", //上市日期
            "MeiGuShouYi": 0.9102,	//每股收益(元)收入
			"MeiGuShouYiJiSuan":3.6408,//--每股收益(元)--乘上系数，不适合展示，只用于计算
            "MeiGuJingZiChan": 3.0864,	//每股净资产(元)
            "JingZiChanShouYiLv": 29.4899,	//净资产收益率
            "MeiGuJingYingXianJin": 1.7779, //每股经营现金(元)
            "MeiGuGongJiJin": 0.6636, //每股公积金(元)
            "MeiGuWeiFenPei": 1.3733, //每股未分配(元)
            "GuDongQuanYiBi": 59.0188,	//股东权益比
            "JingLiRunTongBi": 2179.6632, //净利润同比
            ----"ZhuYingShouRuTongBi": 378.8595,	//主营收入同比  ----删除字段
			"YingYeShouRuTongBi":29.59,   ----营业收入(同比增长率)	RIS_OR----增加字段
            "XiaoShouMaoLiLv": 84.2389, //销售毛利率
            "TiaoZhengMeiGuJingZi": 3.0291, //调整每股净资(元)
            "ZongZiChan": 281137.4462,	//总资产(万元)
            "LiuDongZiChan": 243946.7482, //流动资产(万元)
            "GuDingZiChan": 14928.2858, //固定资产(万元)
            "WuXingZiChan": 2688.5318,	//无形资产(万元)
            "LiuDongFuZhai": 114239.7458, //流动负债(万元)
            "ChangQiFuZhai": 973.8254,	//长期负债(万元)
            "ZongFuZhai": 115213.5712,	//总负债(万元)
            "GuDongQuanYi": 165923.875, //股东权益(万元)
            "ZiBenGongJiJin": 35677.5876, //资本公积金(万元)
            "JingYingXianJinLiuLiang": 95581.4774,	//经营现金流量(万元) 
            "TouZiXianJinLiuLiang": -18257.3101,	//投资现金流量(万元)
            "ChouZiXianJinLiuLiang": -2150.4, //筹资现金流量(万元)
            "XianJinZengJiaE": 75176.046, //现金增加额(万元)
            "ZhuYingShouRu": 76795.1913,	//主营收入(万元)
            "ZhuYingLiRun": 63036.5085, //主营利润(万元)
            "YingYeLiRun": 56806.2889,	//营业利润(万元)
            "TouZiShouYi": 17663.857, //投资收益(万元)
            "YingYeWaiShouZhi": 1643.1879,	//营业外收支(万元)
            "LiRunZongE": 58449.4768, //利润总额(万元)
            "JingLiRun": 48930.8767,	//净利润(万元)
            "WeiFenPeiLiRun": 73828.984,	//未分配利润(万元)
            "ZongGuBen": 53760, //总股本(万股)
            "LiuTongGu": 26199.8076, //当前流通股(A股或B股)(万股)------需要增加(大智慧无)
            "LiuTongAGu": 26199.8076, //流通A股(万股)
            "LiuTongBGu": 0,	//流通B股(万股)
            "JingWaiShangShiGu": 0, //境外上市股(万股)
            "QiTaLiuTongGu": 0, //其他流通股(万股)
            ----"WuXianShouGuHeJi": 26199.8076, //无限售股合计(万股)  ----删除字段
			"LiuTongGuTotal": 26199.8076   --流通股合计(万股)----增加字段
            "XianShouGuHeJi": 27560.1924, //限售股合计(万股)
            "GuDongRenShu":119988,//股东人数
            "PingJunGuBen":234.1942,//平均股本(万股)
        },
	    {...},
	    {...}
	]