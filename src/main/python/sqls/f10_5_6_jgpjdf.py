# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT   TOP 5000
	 RsId
	,UpdateDateTime
	,Obj
	,tzpj
	,pjsl
	,zjs
	,zscr
	,mrpj
 FROM  stocksoftdata.dbo.tmdbRES_COM_INVEST_RATING 
 WHERE ( ( UpdateDateTime = '{UpdateDateTime}'  AND RsId > {RsId} ) OR ( UpdateDateTime > '{UpdateDateTime}'  ) )
ORDER BY  UpdateDateTime ,RsId"""
