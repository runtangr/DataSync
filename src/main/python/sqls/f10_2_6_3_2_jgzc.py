# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT  
	 RsId
	,UpdateDateTime
	,Obj 
	,cjlx  
	,jgljmr
	,jgljmc
	,TimeGroup AS flfs
	,jgcys 
FROM stocksoftdata.dbo.tmdbLHB_JGZC
WHERE  ( ( UpdateDateTime = '{UpdateDateTime}' AND RsId > '{RsId}' ) OR ( UpdateDateTime > '{UpdateDateTime}' ) )   
ORDER  BY UpdateDateTime,RsId"""