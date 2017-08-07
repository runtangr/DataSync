# -*- coding: utf-8 -*-
__author__ = "tangr"
import pymssql
import sys,os
import importlib
import time
import datetime
import pymongo
import dateutil
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.Utils import get_all_stock_codes, get_last_update_info, check_action_config, save_last_update_info, \
    is_continue

class SyncSys(object):

  """docstring for Sync"""

  def __init__(self, db):
    super(SyncSys, self).__init__()
    db = db


class GetDataFromMssql(SyncSys):
  """ get data from sqlserver"""

  def __init__(self, base_url=None, mssql_server=None, mssql_user=None, mssql_password=None, mssql_database=None):

      # super(GetDataFromMssql, self).__init__()

      if base_url is not None:
          self.BASE_URL = base_url
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
          last_request_update_datetime = datetime.datetime.strptime(QueryObj["Timestamp"], "%Y,%m,%d,%H,%M,%S,%f")
          last_request_rsid =  QueryObj["RsId"]
      else:
          #创建时间
          pass


      return last_request_update_datetime, last_request_rsid

  def GetArgs(self,DBObj):

      last_update_time = datetime.datetime.now()
      parse_args = []

      last_update_time, last_rsid = self.get_last_update_info(DBObj=DBObj,action_name="f10_9_3_1_xxdlxw", key_value="all")
      parse_args.append(("RsId", last_rsid))

      parse_args.append(("UpdateDateTime", last_update_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]))
      parse_args.append(("ENDDATE", last_update_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]))

      # last_update_datetime = datetime.datetime.now()
      return parse_args

  def get_results(self,action_name, tables):
      object_mapping = {}
      headers = tables.pop(0)
      max_update_datetime = datetime.datetime(year=1970, month=1, day=1)
      max_rsid = ""
      results = []
      for result in tables:


          RsId = result[headers.index("RsId")]
          UpdateDateTime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
          ZxDate = dateutil.parser.parse(result[headers.index("ZxDate")])
          ZiXunId = result[headers.index("ZiXunId")]
          ZiXunType = result[headers.index("ZiXunType")]
          Obj = result[headers.index("Obj")]
          StockCode = result[headers.index("StockCode")]
          StockName = result[headers.index("StockName")]
          Title = result[headers.index("Title")]

          if Obj is not None:
              result = {"RsId": RsId, "UpdateDateTime": UpdateDateTime, "ZxDate": ZxDate, "ZiXunId": ZiXunId,
                        "ZiXunType":ZiXunType, "Obj":Obj, "StockCode":StockCode, "StockName":StockName, "Title":Title}
              results.append(result)

      return results, max_update_datetime, max_rsid

  def GetData(self, action_name = "f10_9_3_1_xxdlxw", parse_args=None):
          try:
              cursor = self.get_cursor()
          except Exception as e:
              print("Open mssql connection failed: {}".format(e))
              return None, None, None

          if cursor is None:
              return None, None, None

          try:
              sql = getattr(importlib.import_module("sqls.{}".format(action_name), action_name), "sql", None)
          except Exception as e:
              print("Import {} failed, reason: {}".format(action_name, e))
              return None, None, None

          if sql is None:
              print("Can not find sql script: {}".format(action_name))
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

          results, max_update_datetime, max_rsid = self.get_results(action_name, tables)
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
      self.db = client.F10Data3

      # super(SaveDataToDB, self).__init__(db =self.db)

  @classmethod
  def get_db(cls):
      client = pymongo.MongoClient("10.3.131.51", 27019)
      db = client.F10Data3
      return db

  def SaveData(self,MssqlData):

    mssql_data =  MssqlData[0]
    Colection = self.db.f10_9_3_1_xxdlxw.find().count()
    AllColection = self.db.collection_names()
    if Colection == 0:
        #create
        map(lambda data:self.db.f10_9_3_1_xxdlxw.insert(data) , mssql_data)
    else:
        #add
        pass

    


if __name__ == '__main__':
    MssqlObj = GetDataFromMssql(
                            mssql_server=os.environ.get("MSSQLServer", "10.3.131.87:6988"),
                            mssql_user=os.environ.get("MSSQLUser", "scott"),
                            mssql_password=os.environ.get("MSSQLPassword", "tiger"),
                            mssql_database=os.environ.get("MSSQLDataBase", "QKTZ20160429"))

    DBObj = SaveDataToDB(
                  db_host=os.environ.get("DBHost", "10.3.131.51"),
                  db_port=os.environ.get("DBPort", 27019),
                  db_name=os.environ.get("DBName", "F10Data3")
                  )

    parse_args = MssqlObj.GetArgs(DBObj =DBObj)

    MssqlData = MssqlObj.GetData(parse_args=parse_args)

    DBObj.SaveData(MssqlData)