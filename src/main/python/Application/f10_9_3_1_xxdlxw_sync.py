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
        max_rsid = ""
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

        return results, max_update_datetime, max_rsid


class TableSaveData(SyncBase.SaveDataToDB):

    def SaveData(self,table_name=None, data=None):
      #select
      while True:
          try:
            count = self.db[table_name].find({"RsId":data["RsId"]}).count()
            break
          except pymongo.errors.AutoReconnect, e:
            logging.error('AutoReconnect fail\n')
            time.sleep(2)
      if str(data["Status"]) == -1:

        self.db[table_name].remove({"RsId":data["RsId"]})
      else:

          if count > 0:
            #edit
            try:
                #logging
                print("Edit ：RsId = {0} Timestamp = {1}".format(data["RsId"], data["UpdateDateTime"]))
                logging.info("Edit ：RsId = {0} Timestamp = {1}".format(data["RsId"],data["UpdateDateTime"]))
                self.db[table_name].update({"RsId":data["RsId"]},{"$set":data})
            except pymongo.errors.AutoReconnect, e:
                logging.error('AutoReconnect fail\n')
                time.sleep(2)
          else:
            #add
            # logging
            try:
                print("Add ：RsId = {0} Timestamp = {1}".format(data["RsId"], data["UpdateDateTime"]))
                logging.info("Add ：RsId = {0} Timestamp = {1}".format(data["RsId"], data["UpdateDateTime"]))
                self.db[table_name].insert(data)
            except pymongo.errors.AutoReconnect, e:
                logging.error('AutoReconnect fail\n')
                time.sleep(2)


