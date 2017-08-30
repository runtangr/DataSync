
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
import decimal
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import SyncBase

class TableGetData(SyncBase.GetDataFromMssql):
    def get_results(self, action_name, tables):
        object_mapping = {}
        headers = tables.pop(0)
        max_update_datetime = datetime.datetime(year=1970, month=1, day=1)
        max_RsID = ""
        results = []
        for result in tables:

            tmp = {}
            for i, header in enumerate(headers):
                if result[i] != "" and result[i] is not None:
                    if type(result[i]) == type(decimal.Decimal('1314')):
                        tmp[headers[i]] = float(result[i])
                    else:
                        tmp[headers[i]] = result[i]
            results.append(tmp)

        return results, max_update_datetime, max_RsID


class TableSaveData(SyncBase.SaveDataToDB):
    pass