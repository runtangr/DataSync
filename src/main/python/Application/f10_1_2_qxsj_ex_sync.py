
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

            Obj = result[headers.index("Obj")]

            StockShortName = result[headers.index("StockShortName")]
            Date = parse(result[headers.index("Date")])
            QianChuQuanChengShu = float(result[headers.index("QianChuQuanChengShu")])
            QianChuQuanPianYi = float(result[headers.index("QianChuQuanPianYi")])
            HouChuQuanChengShu = float(result[headers.index("HouChuQuanChengShu")])

            HouQianChuQuanPianYi = float(result[headers.index("HouQianChuQuanPianYi")])
            FhkgXinXi = result[headers.index("FhkgXinXi")]
            gqdjr = parse(result[headers.index("gqdjr")])

            cqcxr = parse(result[headers.index("cqcxr")])
            zhjyr = result[headers.index("zhjyr")]
            qxbgq = parse(result[headers.index("qxbgq")])
            rsstatus = result[headers.index("rsstatus")]
            RsId = long(result[headers.index("rsMainkeyid")])
            UpdateDateTime = parse(result[headers.index("UpdateDateTime")])

            if Obj is not None:
                result = {"Obj": Obj, "StockShortName": StockShortName, "Date": Date,
                          "QianChuQuanChengShu": QianChuQuanChengShu,
                          "QianChuQuanPianYi": QianChuQuanPianYi,
                          "HouChuQuanChengShu": HouChuQuanChengShu,
                          "HouQianChuQuanPianYi": HouQianChuQuanPianYi,
                          "FhkgXinXi": FhkgXinXi, "gqdjr": gqdjr,
                          "cqcxr": cqcxr, "zhjyr": zhjyr,
                          "qxbgq": qxbgq, "rsstatus": rsstatus,
                          "RsId": RsId,
                          "UpdateDateTime": UpdateDateTime
                          }
                results.append(result)

        return results, max_update_datetime, max_rsid

class TableSaveData(SyncBase.SaveDataToDB):
    pass

