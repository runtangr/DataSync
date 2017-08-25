# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 1000 a.SEQ AS RsId, a.MTIME AS UpdateDateTime,
       CONVERT( VARCHAR(10), ISNULL( a.ONL_APL_DATE, a.ONL_BUY_DATE ), 112 ) AS ShenGouDate, --申购日期
       QKTZ20160429.dbo.Date2Str( ISNULL( a.ONL_APL_DATE, a.ONL_BUY_DATE )) AS II_ShenGouDate,
       ( CASE X.TRADE_MKT_REF
             WHEN 1 THEN 'SZ'
             WHEN 2 THEN 'SH'
         END
       ) + ISNULL( a.BUY_CODE1, a.BUY_CODE2 ) AS ShenGouDaiMa, --申购代码
       ISNULL( X.STOCKSNAME, ISNULL( a.BUY_NAME1, a.BUY_NAME2 )) AS ShenGouMingCheng, --申购名称
       ISNULL( b.TTL_SHR, ISNULL( a.SHR_FLOR, a.SHR_CEIL )) AS FaXingLiang, --发行量
       CONVERT( VARCHAR(10), ISNULL( b.LIST_DATE, a.LIST_DATE ), 120 ) AS ShangShiDate, --上市时间
       QKTZ20160429.dbo.Date2Str( ISNULL( b.LIST_DATE, a.LIST_DATE )) AS II_ShangShiDate,
       ( CASE X.TRADE_MKT_REF
             WHEN 1 THEN 'SZ'
             WHEN 2 THEN 'SH'
         END
       ) + X.STOCKCODE AS GuPiaoDaiMa, --股票代码
       CASE X.TRADE_MKT_REF
           WHEN 1 THEN 500
           WHEN 2 THEN 1000
       END AS zyqgs, --中一签股数
       CONVERT( VARCHAR(10), a.PAY_DATE, 112 ) AS zqjkr, --中签缴款日
       QKTZ20160429.dbo.Date2Str( a.PAY_DATE ) AS II_zqjkr, a.LIST_CLS AS fxfs, --发行方法
       a.CSRC_RESULT AS sfshtg, --是否审核通过
       b.LOT_DCL_DT AS wszqgbr, ---网上中签号公布日
       QKTZ20160429.dbo.Date2Str( b.LOT_DCL_DT ) AS II_wszqgbr, b.LOT_NUM AS wszqsl, --网上中签数量
       b.LOT_RESULT AS wszqjg, --网上中签结果
       b.ONL_LOT_RATE AS ZhongQianLu, --网上中签率   %
       b.OFL_LOT_DT AS wxzqgbr, --网下中签公布日
       QKTZ20160429.dbo.Date2Str( b.OFL_LOT_DT ) AS II_wxzqgbr, b.OFL_LOT_NUM AS wxzqsj, --网下中签数量
       b.OFL_LOT_RESULT AS wxzqjg, --网下中签结果
       b.OFL_LOT_RATE AS wxzql, --网下中签率
       b.ONL_FREEZE_CAP AS wsdjzj, --网上冻结资金   万元
       b.OFL_FREEZE_CAP AS wxdjzj, --网下冻结资金  万元
       b.ONL_REFUND_DT AS wszjjdr, --网上资金解冻日
       QKTZ20160429.dbo.Date2Str( b.ONL_REFUND_DT ) AS II_wszjjdr,
       b.OFL_REFUND_DT AS wxzjjdr, --网下资金解冻日
       QKTZ20160429.dbo.Date2Str( b.OFL_REFUND_DT ) AS II_wxzjjdr,
       b.PER_SHR_CAP AS zyqsxzj, --每中一签所需资金  万元
       b.OFL_LOT_RATE AS wxyxsgbl, --网下有效申购比例
       b.OFL_TIMES AS wxcepsbs, --网下超额配售倍数
       b.OFL_VLD_APL AS wxsghs, --网下申购户数
       b.OFL_VLD_SHR AS wxyxsggs, --网下有效申购股数
       b.ONL_VLD_APL AS wssghs, --网上申购户数
       b.ONL_VLD_SHR AS wsyxsggs, --网上有效申购股数
       a.STK_CLS AS gplx, -- 股票类型//A股 B股
       b.LIST_EXCHANGE AS ssdd, --上市地点
       ISS_CLS AS fxff, --发行方式
       b.ISS_PRC AS FaXingJia, --发行价格  元
       b.PE AS FaXingShiYingLu, --发行后摊博市盈率  年
       b.CAP AS sjmjje, --实际募集资金  万元
       a.ONL_APL_DATE AS wssgksr, --网上申购开始日
       QKTZ20160429.dbo.Date2Str( a.ONL_APL_DATE ) AS II_wssgksr, a.ONL_BUY_DATE AS wssgjzr, --网上申购截止
       QKTZ20160429.dbo.Date2Str( a.ONL_BUY_DATE ) AS II_wssgjzr, a.OFL_APL_DATE AS wxsgksr, --网下申购开始日
       QKTZ20160429.dbo.Date2Str( a.OFL_APL_DATE ) AS II_wxsgksr, a.OFL_BUY_DATE AS wxsgjzr, --网下申购截止日
       QKTZ20160429.dbo.Date2Str( a.OFL_BUY_DATE ) AS II_wxsgjzr, b.ONL_SHR AS wsfxl, --网上发行数量  万股
       b.OFL_APL_SHR AS wxgkpssggs, --网下公开配售申购股数 万股
       a.BUY_CEIL AS ShenGouShangXian, --单一账户申购数量上限
       b.NEW_SHR AS fxxggs, -- 发行新股股数 万股
       b.PER_SHR_CAP AS zqzj, --每中一签所需资金  万元
       a.BUY_CEIL * 10 AS sxsz, --顶格申购所需市值 万元
       STUFF((   SELECT ',' + ORG_NAME
                   FROM STK_LIST_ORG
                  WHERE P_SEQ = a.SEQ
                    AND ORG_CLS_CODE = 1
                    AND ISVALID = 1
                 FOR XML PATH( '' )
             ),
             1,
             1,
             ''
            ) AS zcxs, --主承销商              
       a.DIST_CLS AS cxfs, --承销方式
       a.NAPS AS qmgjzc, --发行前每股净资产
       b.NAPS AS hmgjzc, --发行后每股净资产
       X.STATUS_TYPE_REF AS FxStatus, --发行状态
       ref1092.REF_NAME AS FxStatusName, --发行状态名
       c.ORGCODE AS jgdm, --机构代码
       c.CNAME AS gsmc, --公司名称
       a.APLY_DCL_DATE AS sbplrq, --申报披露日期
       QKTZ20160429.dbo.Date2Str( a.APLY_DCL_DATE ) AS II_sbplrq, a.CSRC_DATE AS shrq, --上会日期
       QKTZ20160429.dbo.Date2Str( a.CSRC_DATE ) AS II_shrq
  FROM STK_LIST_PLAN AS a WITH ( NOLOCK )
  INNER JOIN ORG_PROFILE AS c WITH ( NOLOCK )
          ON a.COMCODE = c.ORGCODE
         AND c.ISVALID = 1
  LEFT JOIN STK_LIST_RESULT AS b WITH ( NOLOCK )
         ON a.SEQ = b.P_SEQ
        AND b.ISVALID = 1
  LEFT JOIN STK_CODE AS X WITH ( NOLOCK )
         ON a.COMCODE = X.COMCODE
        AND X.STK_TYPE_REF = a.STK_CLS_CODE
        AND X.ISVALID = 1
  LEFT JOIN GEN_REF AS ref1092 WITH ( NOLOCK )
         ON X.STATUS_TYPE_REF = ref1092.REF_CODE
        AND ref1092.CLS_CODE = 1092
        AND ref1092.ISVALID = 1
 WHERE a.ITEM_ID = (   SELECT MAX( ITEM_ID )
                         FROM STK_LIST_PLAN
                        WHERE COMCODE = a.COMCODE
                          AND ISVALID = 1
                          AND STK_CLS_CODE = a.STK_CLS_CODE
                   )
   AND a.ISVALID = 1
   AND a.STK_CLS_CODE = 1
   AND ( (   a.MTIME = '{UpdateDateTime}'
       AND   a.SEQ > '{RsId}'
        )
      OR ( a.MTIME > '{UpdateDateTime}' )
       )
 ORDER BY a.MTIME, a.SEQ"""