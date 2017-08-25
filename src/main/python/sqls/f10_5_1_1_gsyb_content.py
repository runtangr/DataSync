# -*- coding: utf-8 -*-
__author__ = "Sommily"

# sql = """SELECT TOP 10
#         B.RES_ID AS YanBaoId,
# 		'' as Obj,
# 		'' as zqmc,
# --        CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,
# --        X.STOCKSNAME AS zqmc,
#         CONVERT(VARCHAR(12),B.WRITEDATE,112) AS 'BaoGaoRiQi',
#         B.ORGNAME AS YanJiuJiGou,
#         B.ANALYST AS YanJiuZuoZhe,
#         B.RPT_TITLE AS YanBaoBiaoTi,
#         CAST(B.RPT_ABSTRACT AS nvarchar(100)) AS Summary,
#         CAST(B.RPT_ABSTRACT AS nvarchar(max))  AS YanBaoNeiRong,
#         '' AS AttachmentUrl,
#         C.REF_NAME AS AttachmentType,
#         B.RPT_FILE AS AttachmentPath,
#         B.RPT_FILE_MD5 AS AttachmentPathMd5,
#         B.MTIME AS UpdateDateTime,
#         CAST(B.SEQ AS VARCHAR) AS RsId
# FROM RES_REPORT_MAIN B with(nolock)
# --  INNER JOIN STK_COM_INDU_REL A ON A.CF_INDU_CODE=B.CF_INDU_CODE
# --  INNER JOIN STK_CODE X  ON X.COMCODE=A.COMCODE AND X.ISVALID=1
#   LEFT JOIN GEN_REF C with(nolock) ON B.FILE_TYPE=C.REF_CODE AND C.CLS_CODE=121
# where
#     --AND
# 	B.WRITEDATE>=CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01'
# --    AND (B.MTIME='1980-01-01' AND A.SEQ>0 OR B.MTIME>'1980-01-01')
# 	    AND B.MTIME>='{UpdateDateTime}' AND b.SEQ>'{RsId}'
# ORDER BY B.MTIME ASC,b.SEQ ASC"""

sql = """SELECT TOP 50
        B.RES_ID AS YanBaoId,
        convert(varchar(30), B.DECLAREDATE, 112) + replace(convert(varchar(30), B.DECLAREDATE, 108), ':', '')   as  BaoGaoRiQi,
		QKTZ20160429.dbo.Date2Str(b.DECLAREDATE) AS II_BaoGaoRiQi,
        B.ORGNAME AS YanJiuJiGou,
        B.ANALYST AS YanJiuZuoZhe,
        B.RPT_TITLE AS YanBaoBiaoTi,
        CAST(B.RPT_ABSTRACT AS nvarchar(max)) AS Summary,
        CASE  WHEN datalength(B.RPT_ABSTRACT) < 10 then B.RPT_TITLE + '<br /><br />-------暂无内容-------' 
        ELSE CAST(B.RPT_ABSTRACT AS nvarchar(max)) end AS YanBaoNeiRong,
        '' AS AttachmentUrl,
        C.REF_NAME AS AttachmentType,
        B.RPT_FILE AS AttachmentPath,
        B.RPT_FILE_MD5 AS AttachmentPathMd5,
        B.MTIME AS UpdateDateTime,
        CAST(B.SEQ AS VARCHAR) AS RsId
FROM RES_REPORT_MAIN B with(nolock)
LEFT JOIN GEN_REF C with(nolock) ON B.FILE_TYPE=C.REF_CODE AND C.CLS_CODE=121
where ((B.MTIME='{UpdateDateTime}' AND b.SEQ>'{RsId}') or (B.MTIME > '{UpdateDateTime}'))
ORDER BY B.MTIME ASC,b.SEQ ASC"""
