# -*- coding: utf-8 -*-
__author__ = "Sommily"

# sql = """SELECT  TOP 100
#         B.DISC_ID AS ZiXunId,
#         CASE X.TRADE_MKT_REF WHEN 1 THEN 'SZ' WHEN 2 THEN 'SH' END + X.STOCKCODE AS Obj,
#         X.STOCKSNAME AS zqmc,
#         CONVERT(VARCHAR(12),B.DECLAREDATE,112) AS ZiXunDateTime,
#         B.TITLE AS ZiXunBiaoTi,
#         '' AS Summary,
#         '' AS AttachmentUrl,
#         D.ACCE_ROUTE AS AttachmentPath,
#         D.ACCE_ROUTE_MD5 AS AttachmentPathMd5,
#         D.ACCE_TYPE AS AttachmentType,
#         '' AS ZiXunJiGou,
#         '' AS ZiXunZuoZhe,
#         B.MTIME AS UpdateDateTime,
#         cast(A.SEQ as varchar) AS RsId,
#         'GG' AS ZiXunType
# FROM DISC_MAIN_COM B with(nolock)
#   INNER JOIN DISC_CONTENT_COM C with(nolock) ON B.DISC_ID = C.DISC_ID AND B.DECLAREDATE>=CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01'
#   INNER JOIN DISC_COM A with(nolock) ON A.DISC_ID = B.DISC_ID
#   INNER JOIN STK_CODE X with(nolock) ON A.COMCODE = X.COMCODE AND X.ISVALID=1
#   LEFT JOIN DISC_ACCE_COM D with(nolock) ON B.DISC_ID = D.DISC_ID
# WHERE ((B.MTIME = '{UpdateDateTime}' AND A.SEQ >'{RsId}' OR B.MTIME > '{UpdateDateTime}'))
# ORDER BY B.MTIME ASC,A.SEQ ASC"""

sql = """select top 500
		  cast(dmc.SEQ as varchar) as RsId
		, convert(varchar(30), dmc.MTime, 126) as UpdateDateTime
		, dmc.Disc_ID as ZiXunId
		, 'GG' as ZiXunType
		, convert(varchar(30), dmc.DECLAREDATE, 112) + replace(convert(varchar(30), dmc.DECLAREDATE, 108), ':', '') as ZiXunDateTime
		,QKTZ20160429.dbo.Date2Str( dmc.DECLAREDATE ) AS II_ZiXunDateTime
		, dmc.Title as ZiXunBiaoTi
		, '' as Summary
		, dmc.[Source] as ZiXunJiGou
		, '' as ZiXunZuoZhe
	from DISC_MAIN_COM dmc with(nolock)
	where dmc.ISVALID = 1 and dmc.DECLAREDATE >= cast(CAST(YEAR(GETDATE())-2 AS VARCHAR) +'-01-01' as datetime)
	  and ((dmc.MTime = '{UpdateDateTime}' and dmc.SEQ> '{RsId}') or (dmc.MTime > '{UpdateDateTime}'))
    order by dmc.MTime asc, dmc.SEQ asc
"""