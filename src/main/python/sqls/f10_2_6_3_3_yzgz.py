# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT 
	RsId
	,UpdateDateTime
	,yybdm
	,yybmc
	,yzsbcs
	,yzmrzs
	,yzljmr
	,yzmczs
	,yzljmc
	,TimeGroup  as flfs 
FROM  stocksoftdata.dbo.tmdbLHB_YZGZ
WHERE  ( ( UpdateDateTime = '{UpdateDateTime}' AND RsId > '{RsId}' ) OR ( UpdateDateTime > '{UpdateDateTime}' ) )   
ORDER  BY UpdateDateTime,RsId"""