
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
from core import switch_time

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
            Date = result[headers.index("Date")]
            QianChuQuanChengShu = float(result[headers.index("QianChuQuanChengShu")])
            QianChuQuanPianYi = float(result[headers.index("QianChuQuanPianYi")])
            HouChuQuanChengShu = float(result[headers.index("HouChuQuanChengShu")])

            HouQianChuQuanPianYi = float(result[headers.index("HouQianChuQuanPianYi")])
            FhkgXinXi = result[headers.index("FhkgXinXi")]
            gqdjr = result[headers.index("gqdjr")]

            cqcxr = result[headers.index("cqcxr")]
            zhjyr = result[headers.index("zhjyr")]
            qxbgq = result[headers.index("qxbgq")]
            rsStatus = result[headers.index("rsStatus")]
            RsId = long(result[headers.index("rsMainkeyID")])
            UpdateDateTime = parse(result[headers.index("UpdateDateTime")])

            II_Date = result[headers.index("II_Date")]
            II_cqcxr = result[headers.index("II_cqcxr")]
            II_gqdjr = result[headers.index("II_gqdjr")]
            II_qxbgq = result[headers.index("II_qxbgq")]

            if Obj is not None:
                result = {"Obj": Obj, "StockShortName": StockShortName, "Date": Date,
                          "QianChuQuanChengShu": QianChuQuanChengShu,
                          "QianChuQuanPianYi": QianChuQuanPianYi,
                          "HouChuQuanChengShu": HouChuQuanChengShu,
                          "HouQianChuQuanPianYi": HouQianChuQuanPianYi,
                          "FhkgXinXi": FhkgXinXi, "gqdjr": gqdjr,
                          "cqcxr": cqcxr, "zhjyr": zhjyr,
                          "qxbgq": qxbgq, "rsStatus": rsStatus,
                          "RsId": RsId,
                          "UpdateDateTime": UpdateDateTime,
                          "II_Date":II_Date,
                          "II_cqcxr":II_cqcxr,
                          "II_gqdjr":II_gqdjr,
                          "II_qxbgq":II_qxbgq
                          }
                results.append(result)

        return results, max_update_datetime, max_rsid

class TableSaveData(SyncBase.SaveDataToDB):
    pass

