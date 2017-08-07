# -*- coding: utf-8 -*-
__author__ = "Sommily"
import sys
from datetime import datetime

from models.CodeList import CodeList
from models.UpdateTimestamp import UpdateTimestamp


def get_all_stock_codes():
    """
    从f10_0_2_code_list获取所有的股票代码列表
    :return: 股票代码列表
    """
    code_list = list(CodeList.objects.distinct("Code"))
    return code_list


def get_last_update_info(action_name, key_value):
    """
    从f10_0_1_update_timestamp获取上一次请求的UpdateDateTime和RsId,如果取不到，就返回默认值
    :param action_name:
    :param key_value:
    :return: last_request_update_datetime, last_request_rsid
    """
    last_request_update_datetime = datetime(year=1970, month=1, day=1)
    last_request_rsid = "0"
    query_set = self.db .objects(Name=action_name, KeyValue=key_value)
    if query_set.count() == 1:
        last_request_update_datetime = query_set.get().Timestamp
        last_request_rsid = query_set.get().RsId
    elif query_set.count() > 1:
        print("Error, f10_0_1_update_timestamp multi results, Name: {}, keyValue:{}".format(action_name, key_value))
        sys.exit(1)

    return last_request_update_datetime, last_request_rsid


def save_last_update_info(action_name, key_value, update_datetime=None, rsid=None):
    """
    保存UpdateDateTime和RsId到f10_0_1_update_timestamp
    :param action_name:
    :param key_value:
    :param update_datetime:
    :param rsid:
    :return: True or False
    """
    query_set = UpdateTimestamp.objects.filter(Name=action_name, KeyValue=key_value)
    if query_set.count() == 0:
        update_timestamp = UpdateTimestamp(Name=action_name, KeyValue=key_value)
        if update_datetime is not None:
            update_timestamp.Timestamp = update_datetime
        if rsid is not None:
            # force make rsid as string
            update_timestamp.RsId = str(rsid)
        update_timestamp.save()
        return True
    elif query_set.count() == 1:
        if update_datetime is not None:
            query_set.update(set__Timestamp=update_datetime, full_result=True)
        if rsid is not None:
            # force make rsid as string
            query_set.update(set__RsId=str(rsid), full_result=True)
        return True
    else:
        return False


def check_action_config(action_config):
    """
    判断action name是否存在
    :param action_config:
    :return: True or False
    """
    if action_config is None:
        print("Error, check_action_config, Action name not found")
        return False

    if action_config.is_use_mssql is False and action_config.url is None:
        print("Error, check_action_config, url not found")
        return False

    if action_config.is_merge_mode and action_config.key_field_list is None:
        print("Error, check_action_config, key field_list not found")
        return False

    return True


def check_update_datetime(last_update_datetime, action_name, key_value="all"):
    """
    Check Update Datetime is Done
    :param last_update_datetime:
    :param action_name:
    :param key_value:
    :return:
    """
    if last_update_datetime is None:
        return True

    db_max_update_datetime, _ = get_last_update_info(action_name=action_name, key_value=key_value)
    if db_max_update_datetime > last_update_datetime:
        print("request_time less than last_update_time_in_mongo")
        print("request time: {}, last update datetime: {}".format(last_update_datetime, db_max_update_datetime))
        return False

    return True


def is_continue(action_name, key_value, max_update_datetime=None, max_rsid=None):
    """
    根据上一次的请求的UpdateDateTime和RsId，判断是否继续请求
    :param action_name:
    :param key_value:
    :param max_update_datetime:
    :param max_rsid:
    :return: True/ False
    """
    if max_update_datetime is None:
        return True

    # last_request_update_datetime, last_request_rsid = get_last_update_info(action_name=action_name, key_value=key_value)
    # return (True, False)[last_request_update_datetime >= max_update_datetime]

    return True


if __name__ == "__main__":
    import os
    from mongoengine.connection import connect, disconnect
    # Connect to mongoDB and use environment
    db_name = os.environ.get("DBName", "F10Data2")
    db_host = os.environ.get("DBHost", "10.30.0.102")
    db_port = int(os.environ.get("DBPort", "27017"))
    connect(db_name, host=db_host, port=db_port)

    last_request_update_datetime, last_request_rsid = get_last_update_info("f10_0_2_code_list", key_value="all")
    disconnect()
    assert last_request_rsid
    assert last_request_update_datetime
