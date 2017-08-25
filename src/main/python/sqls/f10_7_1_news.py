# -*- coding: utf-8 -*-
__author__ = "Sommily"

sql = """select  top 5000
        cast(B.SEQ as varchar) AS RsId,
        B.MTIME AS UpdateDateTime,
        B.GUID AS ZiXunId,
        'XW' AS ZiXunType ,
        convert(varchar(30), B.DECLAREDATE, 112) + replace(convert(varchar(30), b.DECLAREDATE, 108), ':', '') as ZiXunDateTime,
		QKTZ20160429.dbo.Date2Str(b.DECLAREDATE) AS II_ZiXunDateTime,
        cast(B.TITLE_MAIN as nvarchar(max)) AS ZiXunBiaoTi,
		cast(IsNull(B.Summary,'') as nvarchar(max)) AS Summary,
		/*
        case when ISNULL(cast (B.SUMMARY as nvarchar(max)) ,'')=''
             then cast(LEFT(cast(e.TXT_CONTENT as nvarchar(max)),100) as nvarchar(max))
        else cast(B.SUMMARY as nvarchar(max)) end  AS Summary,
		*/
        F.SRC_NAME AS ZiXunJiGou,
        b.AUTOR  AS ZiXunZuoZhe
from NEWS_MAIN B with(nolock)
INNER JOIN PUB_INFOR_SRC F with(nolock) ON B.SRC_CODE = F.SRC_CODE  and f.ISVALID =1
--INNER JOIN NEWS_CONTENT E with(nolock) ON B.GUID = E.GUID and e.ISVALID =1
where b.ISVALID =1 and ((B.MTIME='{UpdateDateTime}' AND B.SEQ>'{RsId}') OR (B.MTIME>'{UpdateDateTime}'))
--where b.ISVALID =1 and ((B.MTIME='2014-01-7 13:25:21.890' AND B.SEQ>13691776) OR (B.MTIME>'2014-01-7 13:25:21.890'))
ORDER BY B.MTIME ASC, B.SEQ ASC"""