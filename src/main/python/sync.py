# -*- coding: utf-8 -*-
__author__ = "tangr"
import pymssql
import sys,os
import importlib
import time
import datetime
import pymongo
from dateutil.parser import parse
import logging
from core import SyncBase

if __name__ == '__main__':

    sync_name = sys.argv[1]
    table_name = sync_name[:-5]
    sync_table = importlib.import_module("Application.{0}".format(sync_name),sync_name)
    MssqlObj = sync_table.TableGetData(
                            table_name = table_name,
                            mssql_server=os.environ.get("MSSQLServer", "10.3.131.87:6988"),
                            mssql_user=os.environ.get("MSSQLUser", "scott"),
                            mssql_password=os.environ.get("MSSQLPassword", "tiger"),
                            mssql_database=os.environ.get("MSSQLDataBase", "QKTZ20160429"))

    DBObj = sync_table.TableSaveData(

                  db_host=os.environ.get("DBHost", "10.3.131.51"),
                  db_port=int(os.environ.get("DBPort", "27019")),
                  db_name=os.environ.get("DBName", "F10Data3")
                  )

    parse_args = MssqlObj.GetArgs(table_name =table_name,DBObj =DBObj)

    MssqlData = MssqlObj.GetData(table_name = table_name, parse_args=parse_args)

    DBObj.Save(table_name=table_name , MssqlData=MssqlData)