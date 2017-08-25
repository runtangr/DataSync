# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT top 1000  
    cast(a.seq as varchar) AS RsId 
    , a.MTIME AS UpdateDateTime
    , (CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END ) + x.STOCKCODE AS Obj  --股票代码     
    , cast(x.STOCKSNAME as nvarchar(max)) AS gpmc --股票名称      
    , a.CAP_SRC AS zjly    --资金来源    
    , a.CLCT_PLAN AS yksymjzj    --预计使用募集资金  万元    
    , cast(a.IVST_INFO as nvarchar(max)) AS zjtx      --资金投向概述    
    , cast(PRJ_NAME as nvarchar(max)) AS xmmc     --项目名称    
    , BEGIN_YEAR AS xmkgnd   --项目开工年度 
    , case when b.DeclareDate is not null then b.DeclareDate else x.LIST_DATE end as xmzjly_sjyj   --项目资金来源-时间依据：/募集资金公告日/上市日/   
    , CSTR_YEAR AS xmjsq    --项目建设期    
    , PRDU_YEAR AS xmscq     --项目生成期    
    , CPLT_YEAR AS kgwcn    --开工后几年完成    
    , a.IVST_PLAN AS jhtre    --计划总投入额    --万元    
    , FIX_CAP AS jdzctz     --其中:建设/固定资产投资  万元    
    , FLOW_CAP AS pdldzjtz  --铺底流动资金投资 万元    
    , CLCT_CAP AS yjsymjzj     --预计使用募集资金    
    , FIR_YEAR_IVST AS mjzjdyntre   --募集资金第一年投入额    
    , SELF_CAP AS yjsyzyzj  --预计使用自有资金    
    , APRV_INFO AS xmspqk     --项目审批情况    
    , cast(PRJ_MAIN_INFO as nvarchar(max)) AS xmnr  --项目主要内容    
    , COST AS nzcb         --年总成本    
    , IVST_PRFT AS tzlrl --投资利润率    
    , IVST_PTR AS tzlsl   --投资利税率    
    , IVST_TP AS tzhsq   --投资回收期  年    
    , IRR AS cwnbsyl    --财务内部收益率    
    , NEW_PRJ AS sfxxm --是否为新项目
    , a.IVST_INFO AS zjtxgs  --资金投向概述
    , a.CAP_SRC_CODE AS    zjlydm --资金来源代码      
FROM    QKTZ20160429.dbo.STK_IVST_PRJ a
left join QKTZ20160429.dbo.STK_CAP_SRC b on a.P_SEQ = b.seq
LEFT JOIN QKTZ20160429.dbo.STK_CODE X ON A.COMCODE = X.COMCODE AND X.ISVALID = 1 and  x.STK_TYPE_REF = 1
WHERE a.ISVALID = 1
        AND a.CAP_SRC_CODE = 1
        AND case when b.DeclareDate is not null then b.DeclareDate else x.LIST_DATE END IS NOT null
        AND ( ( a.MTime = '{UpdateDateTime}' AND a.SEQ > {RsId} ) OR ( a.MTime > '{UpdateDateTime}' ) )
ORDER BY a.MTIME,a.SEQ"""
  