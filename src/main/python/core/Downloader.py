# -*- coding: utf-8 -*-
__author__ = "Sommily"
import os
import json
import time
import urllib
import urllib2
import pymssql
import importlib
from Converter import get_results


class Downloader(object):
    BASE_URL = "http://114.141.181.25:22280"
    MSSQL_SERVER = "114.141.181.24:6986"
    MSSQL_USER = "sa"
    MSSQL_PASSWORD = "cp_cd060906"
    MSSQL_DATABASE = "QKTZ20160429"
    MSSQL_DATABASE = "stocksoftdata"

    def __init__(self, base_url=None, mssql_server=None, mssql_user=None, mssql_password=None, mssql_database=None):
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

    def get_data(self, parse_url, action_name, parse_args=None):
        request_url = self.BASE_URL + parse_url
        if parse_args is not None:
            request_url += "?" + urllib.urlencode(parse_args)

        try:
            data = urllib2.urlopen(request_url, timeout=120).read()
        except Exception as e:
            print("Request {} failed, reason: {}".format(request_url, e))
            data = None

        try:
            response = json.loads(data)
        except ValueError:
            print("Time out, request url: {}".format(request_url))
            return None, None, None

        status_code = response["sys_status"]
        if status_code != 200:
            return None, None, None

        table = response.get("table", [])
        if len(table) <= 1:
            return None, None, None

        results, max_update_datetime, max_rsid = get_results(action_name, table)
        return results, max_update_datetime, max_rsid

    def get_data_from_mssql(self, action_name, parse_args=None):
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

        results, max_update_datetime, max_rsid = get_results(action_name, tables)
        cursor.close()
        return results, max_update_datetime, max_rsid


downloader = Downloader(base_url=os.environ.get("CadaTapBaseUrl", None),
                        mssql_server=os.environ.get("MSSQLServer", "10.3.131.87:6988"),
                        mssql_user=os.environ.get("MSSQLUser", "scott"),
                        mssql_password=os.environ.get("MSSQLPassword", "tiger"),
                        mssql_database=os.environ.get("MSSQLDataBase", "QKTZ20160429"))
                        # mssql_database = os.environ.get("MSSQLDataBase", "stocksoftdata"))
