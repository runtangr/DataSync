# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select top 500 * from
(
   select
     case when stkcode.TRADE_MKT = '深圳证券交易所' then 'SZ' when stkcode.TRADE_MKT = '上海证券交易所' then 'SH' else '' end + stkfin.a_stockcode as Obj
--   , stkfin.a_stocksname as stocksname
--   , stkfin.Rpt_des
--   , stkfin.RPT_YEAR, stkfin.RPT_TAG
   , stkfin.RPT_YEAR + case when stkfin.RPT_TAG = 1 then '-03-31' when stkfin.RPT_TAG = 5 then '-06-30' when stkfin.RPT_TAG = 6 then '-09-30' when stkfin.RPT_TAG = 7 then '-12-31' end as BaoGaoQi
   , stklist.ISS_PRC as ShangShiJia--上市价//发行价
   , stkcode.LIST_DATE as ShangShiRiQi--上市日期
   , stkfin.EPSP as MeiGuShouYi--每股收益(元)-每股收益EPS-最新股本摊薄
   , COALESCE(NULLIF(stkfin.EPSNED,0),NULLIF(stkfin.EPSP_DED,0), NULLIF(stkfin.EPSP,0),0)  
   * case stkfin.RPT_TAG when 1 then 4.0 when 5 then 2.0 when 6 then 1.3333 when 7 then 1.0 else 0 end as MeiGuShouYiJiSuan--每股收益EPS-最新股本摊薄-乘上系数，不适合展示，只用于计算
   , stkfin.BPS as MeiGuJingZiChan--每股净资产(元)
   , stkfin.DU_ROE as JingZiChanShouYiLv   --净资产收益率
   , stkfin.PS_CN as MeiGuJingYingXianJin   --每股经营现金(元)--每股现金流量净额 PS_CN
   , stkfin.PS_CR as MeiGuGongJiJin   --每股公积金(元)--每股资本公积 PS_CR
   , stkfin.PS_UP as MeiGuWeiFenPei   --每股未分配(元)
   , stkfin.RIS_MSHR as GuDongQuanYiBi   --股东权益比 --归属母公司股东的权益(相对年初增长率)  RIS_MSHR
   , stkfin.RIS_MNP as JingLiRunTongBi   --净利润同比 --归属母公司股东的净利润(同比增长率)   RIS_MNP
--   , 0 as ZhuYingShouRuTongBi   --主营收入同比
   , stkfin.RIS_OR as YingYeShouRuTongBi   ----营业收入(同比增长率)  RIS_OR
   , stkfin.SEL_RINT as XiaoShouMaoLiLv   --销售毛利率
   , stkfin.BPSNED as TiaoZhengMeiGuJingZi   --调整每股净资(元)
   , stkfin.BAL_O as ZongZiChan   --总资产(万元)--资产总计  BAL_O
   , stkfin.BAL_M as LiuDongZiChan   --流动资产(万元)
   , stkfin.BAL_D as GuDingZiChan   --固定资产(万元)--有形资产  BAL_D
   , stkbala.B140101 / 10000 as WuXingZiChan   --无形资产(万元)
   , stkfin.BAL_N as LiuDongFuZhai   --流动负债(万元)
   , stkbala.B220001 / 10000 as ChangQiFuZhai   --长期负债(万元)
   , stkfin.BAL_P as ZongFuZhai   --总负债(万元)
   , stkbala.B300000 / 10000 as GuDongQuanYi   --股东权益(万元)
   , stkbala.B310201 / 10000 as ZiBenGongJiJin   --资本公积金(万元)
   , stkcash.C100000 / 10000 as JingYingXianJinLiuLiang   --经营现金流量(万元)
   , stkcash.C200000 / 10000 as TouZiXianJinLiuLiang   --投资现金流量(万元)
   , stkcash.C300000 / 10000 as ChouZiXianJinLiuLiang   --筹资现金流量(万元)
   , stkcash.C410201 / 10000 as XianJinZengJiaE   --现金增加额(万元)
   , stkincome.P110121 / 10000 as ZhuYingShouRu   --主营收入(万元)
   , stkincome.P120101 / 10000 as ZhuYingLiRun   --主营利润(万元)
   , stkincome.P130101 / 10000 as YingYeLiRun   --营业利润(万元)
   , stkincome.P130201 / 10000 as TouZiShouYi   --投资收益(万元)
   , stkincome.P130801 / 10000 as YingYeWaiShouZhi   --营业外收支(万元)--净额
   , stkincome.P140101 / 10000 as LiRunZongE   --利润总额(万元)
   , stkincome.P150101 / 10000 as JingLiRun   --净利润(万元)
   , stkincome.P240101 / 10000 as WeiFenPeiLiRun   --未分配利润(万元)
   , stkshr.TOTAL / 10000 as ZongGuBen   --总股本(万股)
   , stkshr.FL_ASHR / 10000 as LiuTongGu   --当前流通股(A股或B股)(万股)------需要增加(大智慧无)
   , stkshr.FL_ASHR / 10000 as LiuTongAGu   --流通A股(万股)
   , stkshr.B_SHR / 10000 as LiuTongBGu   --流通B股(万股)
   , stkshr.OTH_ABROAD / 10000 as JingWaiShangShiGu   --境外上市股(万股)
   , stkshr.OTH_FL / 10000 as QiTaLiuTongGu   --其他流通股(万股)
--   , stkshr.FL_SHR / 10000 as WuXianShouGuHeJi   --无限售股合计(万股)
   , stkshr.FL_SHR / 10000 as LiuTongGuTotal   --流通股合计(万股)
   , stkshr.TOT_LTDFL / 10000 as XianShouGuHeJi   --限售股合计(万股)
   , stkholder.TOT_HLD as GuDongRenShu   --股东人数
   , stkshr.FL_ASHR / 10000 / stkholder.TOT_HLD as PingJunGuBen   --平均股本(万股)
   , UpdateDateTime = (select convert(varchar(26), max(mtime), 121) from
                     (select stkfin.MTIME union select stkcode.MTIME       union select stkbala.MTIME
                                     union select stkcash.MTIME         union select stkincome.MTIME
                                     union select stkshr.MTIME       union select stkholder.MTIME
                                     union select stklist.MTIME         union select stklistplan.MTIME) a)

from ANA_STK_FIN_IDX_LAT stkfin WITH(NOLOCK)
inner join STK_CODE stkcode WITH(NOLOCK) on stkfin.a_stockcode = stkcode.STOCKCODE and stkcode.ISVALID = 1
                              and stkcode.Status_Type_Ref in (1, 4) and stkcode.TRADE_MKT in ('深圳证券交易所', '上海证券交易所')
left join STK_BALA_GEN stkbala WITH(NOLOCK) ON stkcode.COMCODE = stkbala.COMCODE AND stkbala.RPT_TYPE = '合并' and stkbala.ISVALID = 1
                              and stkbala.RPT_DATE = (SELECT MAX(RPT_DATE) FROM STK_BALA_GEN WITH(NOLOCK) WHERE COMCODE = stkbala.COMCODE AND ENDDATE = stkbala.ENDDATE AND RPT_TYPE = stkbala.RPT_TYPE)
                       --and stkbala.StartDate = cast( convert(varchar(4), stkbala.EndDate, 112) + '-01-01' as datetime)
                       and stkbala.EndDate = stkfin.EndDate--(SELECT MAX(EndDate) FROM STK_BALA_GEN WHERE COMCODE = stkbala.COMCODE AND RPT_TYPE = stkbala.RPT_TYPE)
left join STK_CASH_GEN stkcash WITH(NOLOCK) ON stkcode.COMCODE = stkcash.COMCODE AND stkcash.RPT_TYPE = '合并' and stkcash.ISVALID = 1
                              and stkcash.RPT_DATE = (SELECT MAX(RPT_DATE) FROM STK_CASH_GEN WITH(NOLOCK) WHERE COMCODE = stkcash.COMCODE AND ENDDATE = stkcash.ENDDATE AND RPT_TYPE = stkcash.RPT_TYPE)
                       and stkcash.StartDate = cast( convert(varchar(4), stkcash.EndDate, 112) + '-01-01' as datetime)
                       and stkcash.EndDate = stkfin.EndDate-- (SELECT MAX(EndDate) FROM STK_CASH_GEN WHERE COMCODE = stkcash.COMCODE AND RPT_TYPE = stkcash.RPT_TYPE)
left join STK_INCOME_GEN stkincome WITH(NOLOCK) ON stkcode.COMCODE = stkincome.COMCODE AND stkincome.RPT_TYPE = '合并' and stkincome.ISVALID = 1
                              and stkincome.RPT_DATE = (SELECT MAX(RPT_DATE) FROM STK_CASH_GEN WITH(NOLOCK) WHERE COMCODE = stkincome.COMCODE AND ENDDATE = stkincome.ENDDATE AND RPT_TYPE = stkincome.RPT_TYPE)
                       and stkincome.StartDate = cast( convert(varchar(4), stkincome.EndDate, 112) + '-01-01' as datetime)
                       and stkincome.EndDate = stkfin.EndDate--(SELECT MAX(EndDate) FROM STK_CASH_GEN WHERE COMCODE = stkincome.COMCODE AND RPT_TYPE = stkincome.RPT_TYPE)
left join STK_SHR_STRU stkshr with(nolock) on stkfin.a_stockcode = stkshr.a_stockcode and stkshr.ISVALID = 1
                       and stkshr.CHANGEDATE = (select max(CHANGEDATE) from STK_SHR_STRU with(nolock) where a_stockcode = stkshr.a_stockcode and ISVALID = 1)
left join STK_HOLDER_NUM stkholder with(nolock) on stkcode.COMCODE = stkholder.COMCODE and stkholder.ISVALID = 1
                       and stkholder.CHANGEDATE = (select max(CHANGEDATE) from STK_HOLDER_NUM with(nolock) where COMCODE = stkholder.COMCODE and ISVALID = 1)
left join STK_LIST_PLAN stklistplan with(nolock) on stklistplan.ISVALID = 1 and stkcode.STK_TYPE_REF=stklistplan.STK_CLS_CODE and stkcode.COMCODE = stklistplan.COMCODE
                             -- AND stklistplan.CSRC_RESULT = '通过'
left join STK_LIST_RESULT stklist with(nolock) on stklist.ISVALID = 1 and stklistplan.SEQ=stklist.P_SEQ and stkcode.COMCODE = stklist.COMCODE and stklist.LIST_DATE is not null
                              
where stkfin.ISVALID = 1 and stkfin.a_stockcode is not null and stklist.LIST_DATE is not null
) a where a.UpdateDateTime >= (cast('{UpdateDateTime}' as datetime))
order by a.UpdateDateTime"""

