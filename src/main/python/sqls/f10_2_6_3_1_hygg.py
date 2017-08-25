# -*- coding: utf-8 -*-
__author__ = "Sommily"
sql = """SELECT top 5000  RsId
,UpdateDateTime
,Obj
,cjlx
,ljmr
,ljmc
,TimeGroup AS flfs
,sbcs FROM  stocksoftdata.dbo.tmdbLHB_HYGG
WHERE ( ( UpdateDateTime = '{UpdateDateTime}'  AND RsId > '{RsId}' ) OR ( UpdateDateTime > '{UpdateDateTime}'  ) )
ORDER BY  UpdateDateTime ,RsId"""
