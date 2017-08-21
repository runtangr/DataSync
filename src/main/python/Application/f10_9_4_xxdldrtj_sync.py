
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

            RsId = result[headers.index("RsID")]
            UpdateDateTime = result[headers.index("UpdateDateTime")]
            ZxDate = result[headers.index("ZxDate")]
            CountNum = result[headers.index("CountNum")]

            Obj = result[headers.index("Obj")]

            ZxType = result[headers.index("ZxType")]

            if Obj is not None:
                result = {"RsId": RsId, "UpdateDateTime": UpdateDateTime, "ZxDate": ZxDate, "CountNum": CountNum,
                          "ZxType": ZxType, "Obj": Obj}
                results.append(result)

        return results, max_update_datetime, max_rsid

class TableSaveData(SyncBase.SaveDataToDB):
    pass
