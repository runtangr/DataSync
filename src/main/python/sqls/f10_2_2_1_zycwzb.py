# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT  
    isnull(CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END,'') + X.STOCKCODE AS Obj,
    x.STOCKSNAME,
    x.STOCKCODE ,
    CONVERT(VARCHAR(12),A.ENDDATE,112) AS 'Date',QKTZ20160429.dbo.Date2Str( A.ENDDATE ) AS II_Date,
    ISNULL(C.DOM_AUDIT,'未审计') AS kjssjyj,  --会计师事务所审计意见
    A.EPSP AS jbmgsy,  --基本每股收益(元)
    A.EPSP_DED AS kchjbmgsy,--基本每股收益(扣除后)
    A.EPSNED AS tbmgsy, --摊薄每股收益(元)
    A.BPS AS mgjzc,  --每股净资产(元)
    A.PS_UP AS mgwfplr,  --每股未分配利润(元)
    A.PS_CR AS mggjj,  --每股公积金(元)
    A.SEL_RINT AS xsmll, --销售毛利率(%)
    A.TR_TP AS yylrl,  -- 营业利润率(%)
    A.SEL_NINT AS jlrl,  -- 净利润率(%)
    A.DU_ROE AS jzcsyl,  --净资产收益率(%)
    A.ROER AS jqjzcsyl,--加权净资产收益率(%)
    A.ROED AS tbjzcsyl,--摊薄净资产收益率%
    B.B300000/10000 AS gdqy,--股东权益(%)
    A.LAB_FLO AS ldbl,--流动比率
    A.LAB_SLO AS sdbl,--速动比率
    A.PS_NET_VAL AS mgjyxjll,--每股经营现金流量(元)
    CONVERT(VARCHAR(10),B.DECLAREDATE,120) AS bbgbr,--报表公布日
    A.ROA AS zzcbcl,--总资产报酬率ROA
    a.EPSFD AS  xsmgsy,   --稀释每股收益
    CASE WHEN a.RPT_TAG =1 THEN 10   --1季度
         WHEN a.RPT_TAG =5 THEN 20   --2季度（半年报）
         WHEN a.RPT_TAG =6 THEN 30   --三季度
         WHEN a.RPT_TAG =7 THEN 40   --四季度（年报）
         ELSE 90 END  AS bgfldm      --其他    报告分类代码
    ,A.SEL_NINT  AS  xsjll	--销售净利率 %
    ,A.SEL_COST   AS  xscbl		--销售成本率 %
    ,A.ROA       AS zzcsyl		--总资产收益率%
    ,a.RIS_EPS  AS  jbsyzzl		--基本每股收益同比增长率
    ,a.RIS_EPSD	AS	xxsyzzl		--稀释每股收益同比增长率
    ,a.RIS_OP   AS  yylrzzl     --营业利润(同比增长率)
    ,a.RIS_OR   AS  yysyzzl		--营业收入(同比增长率)
    ,a.RIS_TP  AS	lrzezzl		--利润总额(同比增长率)
    ,a.RIS_TR  AS   yyzsrzzl	--营业总收入(同比增长率)
    ,a.RIS_MNP AS	jlrzzl		--净利润(同比增长率)
	,A.OPE_PER AS  yyzq--营业周期		
	,A.OPE_STC AS  chzzts--存货周转天数	
	,A.OPE_STCI AS chzzl--存货周转率		
	,A.OPE_ACI AS  yszkzzl--应收账款周转率 
	,A.OPE_TAI AS  zzczzl--总资产周转率  
	,A.OPE_FAI AS   ldzczzl--流动资产周转率  
	,A.OPE_APR AS   yfzkzzl--应付账款周转率 
	,A.OPE_FCI AS   gdzczzl--固定资产周转率				 		        			
FROM STK_CODE X with(nolock)
  INNER JOIN ANA_STK_FIN_IDX A with(nolock) ON X.COMCODE=A.COMCODE AND X.STOCKCODE='{STOCKCODE}'
     AND X.ISVALID=1 AND A.ISVALID=1 AND A.ENDDATE>=CAST(YEAR(GETDATE())-3 AS VARCHAR) +'-01-01'
  INNER JOIN STK_BALA_GEN B with(nolock) ON X.COMCODE=B.COMCODE AND A.ENDDATE=B.ENDDATE AND B.RPT_TYPE='合并'
    AND B.RPT_DATE = (SELECT MAX(RPT_DATE) FROM STK_BALA_GEN WHERE COMCODE = X.COMCODE AND ENDDATE = B.ENDDATE AND RPT_TYPE = B.RPT_TYPE)    
  LEFT JOIN STK_AUDIT_OPINON C with(nolock) ON X.COMCODE=C.COMCODE AND A.ENDDATE=C.PeriodDate
ORDER BY A.ENDDATE DESC """
