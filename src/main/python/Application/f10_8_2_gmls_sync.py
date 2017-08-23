
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
        max_Seq = ""
        results = []
        for result in tables:

            RsId = result[headers.index("Seq")]
            UpdateDateTime = result[headers.index("Mtime")]
            MarketCode = result[headers.index("MarketCode")]
            Obj = result[headers.index("Obj")]
            StockCode = result[headers.index("StockCode")]
            StockName = result[headers.index("StockName")]
            ChangeDate = result[headers.index("ChangeDate")]
            OldStockName = result[headers.index("OldStockName")]

            if Obj is not None:
                result = {"RsId": RsId, "UpdateDateTime": UpdateDateTime, "MarketCode": MarketCode,
                          "Obj": Obj,
                          "StockCode": StockCode, "StockName": StockName,
                          "ChangeDate": ChangeDate,
                          "OldStockName": OldStockName}
                results.append(result)

        return results, max_update_datetime, max_Seq


class TableSaveData(SyncBase.SaveDataToDB):
    pass