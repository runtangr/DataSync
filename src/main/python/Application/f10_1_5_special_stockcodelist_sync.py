
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
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import SyncBase

class TableGetData(SyncBase.GetDataFromMssql):

    def get_results(self, action_name, tables):
        object_mapping = {}
        headers = tables.pop(0)
        max_update_datetime = datetime.datetime(year=1970, month=1, day=1)
        max_rsid = ""
        results = []
        for result in tables:

            MarketCode = result[headers.index("MarketCode")]
            StockCode = result[headers.index("StockCode")]
            StockName =result[headers.index("StockName")]
            SpecialType = result[headers.index("SpecialType")]

            Obj = result[headers.index("Obj")]

            if Obj is not None:
                result = {"MarketCode": MarketCode, "StockCode": StockCode, "StockName": StockName, "SpecialType": SpecialType,
                           "Obj": Obj,
                         }
                results.append(result)

        return results, max_update_datetime, max_rsid

class TableSaveData(SyncBase.SaveDataToDB):
    def Save(self, table_name=None, MssqlData=None):

        if len(MssqlData) == 0:
            logging.warning('data is null!\n')
            return
        mssql_data = MssqlData[0]
        Colection = self.db[table_name].find().count()
        AllColection = self.db.collection_names()
        #清除
        self.db[table_name].remove({})
        map(lambda data: self.SaveData(table_name=table_name, data=data), mssql_data)

    def SaveData(self, table_name=None, data=None):
            # add
            # logging
            try:
                # print("Add ：RsId = {0} Timestamp = {1}".format(data["RsId"], data["UpdateDateTime"]))
                # logging.info("Add ：RsId = {0} Timestamp = {1}".format(data["RsId"], data["UpdateDateTime"]))
                self.db[table_name].insert(data)
            except pymongo.errors.AutoReconnect, e:
                logging.error('AutoReconnect fail\n')
                time.sleep(2)
