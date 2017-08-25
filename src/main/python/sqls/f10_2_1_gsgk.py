# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT CASE X.TRADE_MKT_REF
           WHEN 1 THEN 'SZ'
           WHEN 2 THEN 'SH'
       END + X.STOCKCODE AS Obj, X.STK_TYPE AS zqlx, CAST(X.COMCODE AS VARCHAR) AS gsdm,
       CAST(A.CNAME AS NVARCHAR(MAX)) AS gsmc, CAST(A.ENAME AS NVARCHAR(MAX)) AS ywqc,
       CAST(A.REGI_ADDR AS NVARCHAR(MAX)) AS zcdz,
       CAST(A.OFFICE_ADDR AS NVARCHAR(MAX)) AS bgdz,
       CAST(A.REGION AS NVARCHAR(MAX)) AS ssqy,
       --B.CSRC_INDU_1 AS sshy,
       CAST(B.CF_INDU_NAME AS NVARCHAR(MAX)) AS sshy, A.WEB_SITE AS gswz,
       A.EMAIL AS dzxx, X.LIST_DATE AS ssrq, QKTZ20160429.dbo.Date2Str( X.LIST_DATE ) AS II_ssrq,
       G.INTRO_DCL_DATE AS zgrq, QKTZ20160429.dbo.Date2Str( G.INTRO_DCL_DATE ) AS II_zgrq,
       F.NEW_SHR AS fxl, F.ISS_PRC AS fxj, E.TOPEN AS srkpj,
       CAST(STUFF((   SELECT ',' + ORG_NAME
                        FROM STK_LIST_ORG
                       WHERE COMCODE = A.COMCODE
                         AND ORG_CLS_CODE = 4
                      FOR XML PATH( '' )
                  ),
                  1,
                  1,
                  ''
                 ) AS NVARCHAR(MAX)) AS sstjr,
       CAST(STUFF((   SELECT ',' + ORG_NAME
                        FROM STK_LIST_ORG
                       WHERE COMCODE = A.COMCODE
                         AND ORG_CLS_CODE = 1
                      FOR XML PATH( '' )
                  ),
                  1,
                  1,
                  ''
                 ) AS NVARCHAR(MAX)) AS zcxs,
       CAST(A.LEG_PERSON AS NVARCHAR(MAX)) AS frdb,
       CAST(H.INDI_NAME AS NVARCHAR(MAX)) AS dsz,
       CAST(A.GEN_MANAGER AS NVARCHAR(MAX)) AS zjl,
       CAST(A.BOARD_SECTRY AS NVARCHAR(MAX)) AS dm,
       CAST(A.REPR AS NVARCHAR(MAX)) AS zqdb, A.TEL AS dh, A.FAX AS cz, A.POSTCODE AS yb,
       CAST(( SELECT CNAME FROM ORG_PROFILE WHERE ORGCODE = A.ACC_ORGCODE ) AS NVARCHAR(MAX)) AS kjsws,
       CAST(A.PRI_BIZ AS NVARCHAR(MAX)) AS zyfw,
       CAST(A.BRIEF_INTRO AS NVARCHAR(MAX)) AS gsjs, A.SECTRY_TEL AS dmdh,
       A.SECTRY_FAX AS dmcz, A.SECTRY_EMAIL AS dmdzyx,
       CAST(A.CITY AS NVARCHAR(MAX)) AS RegionName
  FROM STK_CODE AS X WITH ( NOLOCK )
  INNER JOIN STK_COM_PROFILE AS A WITH ( NOLOCK )
          ON X.COMCODE = A.COMCODE
         AND X.STOCKCODE = '{STOCKCODE}'
         AND X.ISVALID = 1
         AND A.ISVALID = 1
  INNER JOIN STK_COM_INDU_REL AS B WITH ( NOLOCK )
          ON X.COMCODE = B.COMCODE
         AND B.ISVALID = 1
  INNER JOIN PUB_INDU_REF AS W WITH ( NOLOCK )
          ON B.SW_INDU_CODE_2014 = W.INDU_CODE
         AND W.INDU_SYS_MARK = 15
  LEFT JOIN STK_LIST_PERFORM AS E WITH ( NOLOCK )
         ON X.INNER_CODE = E.INNER_CODE
        AND E.ISVALID = 1
  LEFT JOIN STK_LIST_RESULT AS F WITH ( NOLOCK )
         ON X.COMCODE = F.COMCODE
        AND F.ISVALID = 1
        AND F.ITEM_ID = 1
  LEFT JOIN STK_LIST_PLAN AS G WITH ( NOLOCK )
         ON X.COMCODE = G.COMCODE
        AND G.ISVALID = 1
        AND G.ITEM_ID = 1
  LEFT JOIN STK_DS_POST AS H WITH ( NOLOCK )
         ON X.COMCODE = H.COMCODE
        AND H.ISVALID = 1
        AND H.POST_CODE = 1
        AND H.END_DATE >= CONVERT( VARCHAR(10), GETDATE(), 120 )"""
