#-*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
SELECT TOP 2000 a.SEQ AS RsId, a.MTIME AS UpdateDateTime,
       CASE x.TRADE_MKT_REF
           WHEN 1 THEN 'SZ'
           WHEN 2 THEN 'SH'
       END + x.STOCKCODE AS Obj, --股票代码
       x.STOCKSNAME AS gpmc, a.DECLAREDATE ggrq, --公告日期
       dbo.Date2Str( a.DECLAREDATE ) AS II_ggrq, a.ENDDATE jzrq, --截止日期
       dbo.Date2Str( a.ENDDATE ) AS II_jzrq, a.FORE_CLS_CODE ycdm, --预测代码
       a.FORE_CLS yclx, --预测类型
       a.SRC ggly, --公告来源
       a.SUMMARY yzzy, --预测摘要
       a.CONTENT jtnr, --具体内容
       a.REASON yysm, --原因说明      
       a.NTINC_GR_CEIL jlytbsx, --净利润同比增长上限 %
       a.NTINC_GR_FLOR jlytbxx, --净利润同比增长下限 %
       a.PREVIOUS_EPS qntqsy, --去年同期每股收益
       CASE
           WHEN a.PREVIOUS_NET_PROFIT IS NULL THEN t.jlr
           ELSE a.PREVIOUS_NET_PROFIT
       END qntqlr, --去年同期净利润
       a.EPS_CEIL yjmgsysx, --预计每股收益上限
       a.EPS_FLOR yjmgsyxx --预计每股收益下限
  FROM STK_ACHIEVE_FORECAST AS a
  INNER JOIN STK_CODE AS x
          ON a.COMCODE = x.COMCODE
         AND x.ISVALID = 1
         AND (   x.STK_TYPE_REF = 1
            OR   x.STK_TYPE_REF = 2
             )
  LEFT JOIN (   SELECT a.COMCODE, ROUND( P150101, 4 ) AS jlr
                  FROM STK_INCOME_GEN AS a
                  INNER JOIN (   SELECT COMCODE, MAX( ENDDATE ) edate
                                   FROM STK_INCOME_GEN
                                  WHERE RPT_TYPE = '合并'
                                    AND ISVALID = 1
                                  GROUP BY COMCODE
                             ) AS b
                          ON a.COMCODE = b.COMCODE
                         AND a.ISVALID = 1
                         AND a.ENDDATE = DATEADD( YEAR, -1, b.edate )
                         AND a.RPT_TYPE = '合并'
            ) AS t
         ON x.COMCODE = t.COMCODE
 WHERE a.ISVALID = 1
   AND a.CHNG = '否'
   AND ( (   a.MTIME = '{UpdateDateTime}'
       AND   a.SEQ > '{RsId}'
        )
      OR ( a.MTIME > '{UpdateDateTime}' )
       )
 ORDER BY a.MTIME, a.SEQ
"""
