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
import switch_time

class SyncSys(object):

  """docstring for Sync"""

  def __init__(self, db):
    super(SyncSys, self).__init__()
    db = db


class GetDataFromMssql(SyncSys):
  """ get data from sqlserver"""

  def __init__(self, table_name=None, mssql_server=None, mssql_user=None, mssql_password=None, mssql_database=None):

      # super(GetDataFromMssql, self).__init__()

      if table_name is not None:
          self.TABLE_NAME = table_name
      if mssql_server is not None:
          self.MSSQL_SERVER = mssql_server
      if mssql_user is not None:
          self.MSSQL_USER = mssql_user
      if mssql_password is not None:
          self.MSSQL_PASSWORD = mssql_password
      if mssql_database is not None:
          self.MSSQL_DATABASE = mssql_database
      self.conn = None
      self._connect()

      # super(GetDataFromMssql, self).__init__()

  def _connect(self):
      try:
          self.conn = pymssql.connect(self.MSSQL_SERVER, self.MSSQL_USER, self.MSSQL_PASSWORD, self.MSSQL_DATABASE)
          print("Connect to MYSQL: {} {} {} ".format(self.MSSQL_SERVER, self.MSSQL_DATABASE, self.MSSQL_USER))
      except Exception as e:
          print("Error, Connect to MSSql, {}".format(e))

  def get_cursor(self):
      cursor = None
      while True:
          if self.conn is None:
              self._connect()

          try:
              cursor = self.conn.cursor()
              break
          except Exception as e:
              print("Error, Get cursor failed, try again: {}".format(e))
              self.conn = None
              time.sleep(2)

      return cursor

  def get_last_update_info(self,DBObj,action_name, key_value):
      """
      从f10_0_1_update_timestamp获取上一次请求的UpdateDateTime和RsId,如果取不到，就返回默认值
      :param action_name:
      :param key_value:
      :return: last_request_update_datetime, last_request_rsid
      """
      last_request_update_datetime = datetime.datetime(year=1970, month=1, day=1)
      last_request_rsid = "0"

      ###这里需要优化
      f10_db = SaveDataToDB.get_db()
      collection = f10_db.f10_0_1_update_timestamp
      QueryObj = collection.find_one({"Name":action_name})

      if QueryObj is not None:
          # last_request_update_datetime = datetime.datetime.strptime(QueryObj["Timestamp"], "%Y,%m,%d,%H,%M,%S,%f")
          last_request_update_datetime =QueryObj["Timestamp"]
          last_request_rsid =  QueryObj["RsId"]
      else:
          #创建时间
          collection.insert({"Name":action_name, "RsId":"0", "Timestamp":last_request_update_datetime})


      return last_request_update_datetime, last_request_rsid

  def GetArgs(self,table_name=None,DBObj=None):

      last_update_time = datetime.datetime.now()
      parse_args = []

      last_update_time, last_rsid = self.get_last_update_info(DBObj=DBObj,action_name=table_name, key_value="all")
      parse_args.append(("RsId", last_rsid))

      parse_args.append(("UpdateDateTime", last_update_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]))
      parse_args.append(("ENDDATE", last_update_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]))

      # last_update_datetime = datetime.datetime.now()
      return parse_args


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

                  if type(result[i]) == type(datetime.datetime.now()) and headers[i] != u"UpdateDateTime":
                      temp = switch_time.local2utc(result[i])
                      tmp[headers[i]] = temp

          results.append(tmp)

      return results, max_update_datetime, max_rsid

  def GetData(self, table_name=None, parse_args=None):
          try:
              cursor = self.get_cursor()
          except Exception as e:
              print("Open mssql connection failed: {}".format(e))
              return None, None, None

          if cursor is None:
              return None, None, None

          try:
              sql = getattr(importlib.import_module("sqls.{}".format(table_name), table_name), "sql", None)
          except Exception as e:
              print("Import {} failed, reason: {}".format(table_name, e))
              return None, None, None

          if sql is None:
              print("Can not find sql script: {}".format(table_name))
              return None, None, None
          if parse_args is not None:
              sql = sql.format(**dict((k, v) for k, v in parse_args))

          try:
              cursor.execute(sql)
          except Exception as e:
              print("Exec {} failed, reason: {}".format(sql, e))
              return None, None, None

          rows = cursor.fetchall()
          tables = [[x[0] for x in cursor.description]]
          tables.extend(rows)

          results, max_update_datetime, max_rsid = self.get_results(table_name, tables)
          cursor.close()
          return results, max_update_datetime, max_rsid




class SaveDataToDB(SyncSys):
  """save data to DB"""

  def __init__(self,db_host=None, db_port=None, db_name=None):

      #

      if db_host is not None:
          self.DB_HOST = db_host
      if db_host is not None:
          self.DB_PORT = db_port
      if db_name is not None:
          self.DB_NAME = db_name

      client = pymongo.MongoClient(self.DB_HOST, self.DB_PORT)
      self.db = client[db_name]

      # super(SaveDataToDB, self).__init__(db =self.db)

  @classmethod
  def get_db(cls):
      client = pymongo.MongoClient(os.environ.get("DBHost", "10.0.2.15"),
                                   int(os.environ.get("DBPort", "27017")))
      db = client[os.environ.get("DBName", "F10data3")]
      return db

  def Save(self,table_name=None,MssqlData=None):

    if len(MssqlData) == 0:
        logging.warning('data is null!\n')
        return
    mssql_data =  MssqlData[0]
    Colection = self.db[table_name].find().count()
    AllColection = self.db.collection_names()

    map(lambda data: self.SaveData(table_name=table_name,data=data), mssql_data)
    # 写入sync时间
    if len(mssql_data) == 0:
        logging.warning('data is null!\n')
        return
    last_data = mssql_data[-1]

    self.db.f10_0_1_update_timestamp.update({"Name":table_name},
                                            {"$set":{"RsId":last_data["RsId"], "Timestamp":last_data["UpdateDateTime"]}})

  def SaveData(self,table_name=None, data=None):
      #select
      while True:
          try:
            count = self.db[table_name].find({"RsId":data["RsId"]}).count()
            break
          except pymongo.errors.AutoReconnect, e:
            logging.error('AutoReconnect fail\n')
            time.sleep(2)

      if count > 0:
        #edit
        try:
            #logging
            print("Edit ：RsId = {0} Timestamp = {1}".format(data["RsId"], data["UpdateDateTime"]))
            logging.info("Edit ：RsId = {0} Timestamp = {1}".format(data["RsId"],data["UpdateDateTime"]))
            self.db[table_name].remove({"RsId": data["RsId"]})
            self.db[table_name].insert(data)
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