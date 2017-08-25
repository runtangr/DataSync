# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """
SELECT  rsMainkeyID AS ClassId,
        classfatherid AS ClassfatherId,
        SYS_CODE AS SysCode,
        SECTION_LEVEL AS SectionLevel,
        PlateCode AS PlateCode,
        SECTION_NAME_H AS SectionNameH,
        SECTION_NAME AS SectionName,
        gps AS gps,
        ComputerType as ComputerType,
        rsDateTime AS UpdateDateTime,
        cast(rsMainkeyID as varchar) AS RsId,
        ShortCode 
FROM stocksoftdata..ViewStockSoft_commStockSection a with(nolock)
WHERE   ISNUMERIC(SECTION_NAME_H)=0
AND a.rsMainkeyID= (SELECT MAX(rsMainkeyID)     
     FROM   stocksoftdata..ViewStockSoft_commStockSection with(nolock)    
     WHERE SECTION_NAME_H =a.SECTION_NAME_H AND  ISNUMERIC(SECTION_NAME_H)=0       
AND a.SECTION_LEVEL=SECTION_LEVEL AND a.SYS_CODE=Sys_Code) 
        AND     a.SYS_CODE=(SELECT MAX(SYS_CODE)     
     FROM   stocksoftdata..ViewStockSoft_commStockSection with(nolock)    
     WHERE PlateCode =a.PlateCode AND  ISNUMERIC(SECTION_NAME_H)=0       
)   ORDER BY rsDateTime ASC,rsMainkeyID ASC"""