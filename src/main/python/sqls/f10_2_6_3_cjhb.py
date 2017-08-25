# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT TOP 3000
	 cast(RsId as varchar) as RsId
	,UpdateDateTime 
	,Obj 
	,gpmc 
	,Date 
	QKTZ20160429.dbo.Date2Str( Date ) AS II_Date,
	,ZdlxCode 
	,ZdlxName 
	,cjl 
	,cjje 
	,mrze 
	,mcze 
	,jgmrze 
	,jgmcze 
	,yzmrze 
	,yzmcze 
	,cjlx 
	,yybdm 
	,yybmc 
	,mrje 
	,mcje
	,CHNG
	,CHNG_PCT
FROM  stocksoftdata..tmdbSTK_EXCRA_INFO
WHERE  ( ( UpdateDateTime = '{UpdateDateTime}' AND RsId > '{RsId}' ) OR ( UpdateDateTime > '{UpdateDateTime}' ) )   
ORDER BY  UpdateDateTime ,RsId"""
