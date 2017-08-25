# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """select ssc.Class_id AS ClassId,
        ssc.classfatherid AS ClassfatherId,
        ssc.SYS_CODE AS SysCode,
        ssc.SECTION_NAME_H AS SectionNameH,
        ssc.SECTION_NAME AS SectionName,
        ltrim(rtrim(ssc.PlateCode)) AS PlateCode,
        ltrim(rtrim(ssc.MarketCode)) AS MarketCode,
        ltrim(rtrim(ssc.StockCode)) AS StockCode,
        ltrim(rtrim(ssc.StockShortName)) AS StockShortName,
		ltrim(rtrim(ssc.MarketCode)) + ltrim(rtrim(ssc.StockCode)) AS Obj,
		css.SECTION_LEVEL AS SectionLevel,
        ssc.bzzb AS bzzb,
        ssc.rsDatetime AS UpdateDateTime,
        cast(ssc.RsId as varchar) as RsId
FROM stocksoftdata..ViewStockSoft_sidbStockClass ssc with(nolock)
inner join stocksoftdata..ViewStockSoft_commStockSection css with(nolock) on ssc.Class_id = css.rsMainkeyID
AND  (	( css.SYS_CODE = 3  and css.Section_Level = 1)or
		( css.SYS_CODE = 4  and css.Section_Level = 2)or
		(css.SYS_CODE = 5  and css.Section_Level = 1)or
		(css.SYS_CODE = 16  and css.Section_Level = 2)or
		(css.SYS_CODE = 17  and css.Section_Level = 3)
	)
INNER JOIN stk_code x ON x.STOCKCODE = ssc.StockCode AND x.ISVALID=1
AND  x.STATUS_TYPE_REF !=2	 AND  x.STATUS_TYPE_REF !=3 AND  x.STATUS_TYPE_REF !=5
WHERE  css.SYS_CODE=(SELECT MAX(SYS_CODE)     
     FROM   stocksoftdata..ViewStockSoft_commStockSection with(nolock)    
     WHERE PlateCode =css.PlateCode AND  ISNUMERIC(SECTION_NAME_H)=0       
)    
    
AND css.rsMainkeyID= (SELECT MAX(rsMainkeyID)     
     FROM   stocksoftdata..ViewStockSoft_commStockSection with(nolock)    
     WHERE SECTION_NAME_H =css.SECTION_NAME_H AND  ISNUMERIC(SECTION_NAME_H)=0       
AND css.SECTION_LEVEL=SECTION_LEVEL AND ssc.SYS_CODE=Sys_Code) ORDER BY ssc.rsDatetime ASC, ssc.RsId ASC"""