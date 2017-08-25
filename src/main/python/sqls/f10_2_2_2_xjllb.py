# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT 
      CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,
      CONVERT(VARCHAR(12),A.ENDDATE,112) AS 'Date',QKTZ20160429.dbo.Date2Str( A.ENDDATE ) AS II_Date,
      A.C410201 AS xjjzje,  --现金等的净增加额
      '元' AS dw,
      A.C110000 AS jyxjlr,--经营现金流入小计
      A.C120000 AS jyxjlc, --经营现金流出小计
      A.C100000 AS jyxjje,--经营现金流量净额
      A.C210000 AS tzxjlr,--投资现金流入小计
      A.C220000 AS tzxjlc,--投资现金流出小计
      A.C200000 AS tzxjje, --投资现金流量净额
      A.C310000 AS czxjlr,--筹资现金流入小计
      A.C320000 AS czxjlc, --筹资现金流出小计
      A.C300000 AS czxjje,   --筹资现金流量净额
      A.C410101 AS hlbdyx,    --汇率变动影响
      a.C110101 AS xxsdxj,     --销售所得现金
      CASE RPT_SRC WHEN '第一季度报' THEN 10
				   WHEN '中报' THEN 20
				   WHEN '第三季度报' THEN 30
				   WHEN '年报' THEN 40
				   WHEN '申报稿' THEN 50
				   WHEN '招股说明书' THEN 60
				   WHEN '上市公告书' THEN 70
				   WHEN '第一季度报' THEN 90
				   ELSE 90 END AS bgfldm --  报告分类代码			          
FROM STK_CODE X with(nolock)
  INNER JOIN STK_CASH_GEN A with(nolock) ON X.COMCODE = A.COMCODE AND X.STOCKCODE = '{STOCKCODE}' AND X.ISVALID=1
WHERE A.ISVALID=1 AND A.RPT_TYPE = '合并'
  AND A.ENDDATE>=CAST(YEAR(GETDATE())-3 AS VARCHAR) +'-01-01'
  AND A.RPT_DATE = (SELECT MAX(RPT_DATE) FROM STK_CASH_GEN
                    WHERE COMCODE = A.COMCODE AND ENDDATE = A.ENDDATE AND RPT_TYPE = A.RPT_TYPE)
ORDER BY A.ENDDATE DESC"""
