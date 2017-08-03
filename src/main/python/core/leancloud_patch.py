# -*- coding: utf-8 -*-
__author__ = "AllenC"


def _deep_save(self, unsaved_children, unsaved_files, exclude=None, ignore_failed=True):
    import leancloud
    from leancloud import client
    if exclude:
        # unsaved_children = [x for x in unsaved_children if x != exclude]
        unsaved_children = filter(lambda x: x != exclude, unsaved_children)

    for f in unsaved_files:
        f.save()

    if not unsaved_children:
        return
    dumped_objs = []
    for obj in unsaved_children:
        method = ('PUT', 'POST')[obj.id is None]
        path = '/{0}/classes/{1}'.format(client.SERVER_VERSION, obj._class_name)
        path += ("/{}".format(obj.id), "")[obj.id is None]
        body = obj._dump_save()
        dumped_obj = {
            'method': method,
            'path': path,
            'body': body,
        }
        dumped_objs.append(dumped_obj)

    response = client.post('/batch', params={'requests': dumped_objs}).json()

    errors = []
    for idx, obj in enumerate(unsaved_children):
        content = response[idx]
        if not content.get('success'):
            errors.append(leancloud.LeanCloudError(content.get('code'), content.get('error')))
        else:
            obj._update_data(content['success'])

        if errors:
            # TODO: how to raise list of errors?
            # raise MultipleValidationErrors(errors)
            # add test
            if ignore_failed:
                continue

            raise errors[0]


def _get_base_url():
    import os
    from leancloud.app_router import AppRouter
    from leancloud.client import SERVER_URLS
    from leancloud.client import REGION
    from leancloud.client import APP_ID
    from leancloud.client import USE_HTTPS
    from leancloud.client import SERVER_VERSION
    from leancloud.client import app_router

    # try to use the base URL from environ
    url = os.environ.get('LC_API_SERVER') or os.environ.get('LEANCLOUD_API_SERVER')
    if url:
        return '{}/{}'.format(url, SERVER_VERSION)

    if REGION == 'US':
        # use the hard coded base URL if region is US
        host = SERVER_URLS[REGION]
    elif REGION == 'MC':
        USE_HTTPS = False
        host = SERVER_URLS[REGION]
    else:
        # use base URL from app router
        # global app_router
        if app_router is None:
            app_router = AppRouter(APP_ID)
        host = app_router.get()
    r = {
        'schema': 'https' if USE_HTTPS else 'http',
        'version': SERVER_VERSION,
        'host': host,
    }
    return '{schema}://{host}/{version}'.format(**r)

from leancloud.client import  need_init
from leancloud.client import  region_redirect
from leancloud.client import  check_error
from leancloud._compat import iteritems
from leancloud.client import get_base_url
from leancloud.client import TIMEOUT_SECONDS
import requests
import json
@need_init
@region_redirect
@check_error
def get(url, params=None, headers=None):
    if not params:
        params = {}
    else:
        for k, v in iteritems(params):
            if isinstance(v, dict):
                params[k] = json.dumps(v, separators=(',', ':'))
    #print(headers)
    #print(params)
    #print(_get_base_url() + url)
    response = requests.get(_get_base_url() + url, headers=headers, params=params, timeout=TIMEOUT_SECONDS)
    #print(response)
    #print(response.json())
    return response

@need_init
@region_redirect
@check_error
def post(url, params, headers=None):
    #print(headers)
    #print(params)
    #print(_get_base_url() + url)
    response = requests.post(_get_base_url() + url, headers=headers, data=json.dumps(params, separators=(',', ':')), timeout=TIMEOUT_SECONDS)
    #print(response)
    #print(response.json())
    return response


@need_init
@region_redirect
@check_error
def put(url, params, headers=None):
    # print(headers)
    # print(params)
    # print(_get_base_url() + url)
    response = requests.put(_get_base_url() + url, headers=headers, data=json.dumps(params, separators=(',', ':')), timeout=TIMEOUT_SECONDS)
    # print(response)
    # print(response.json())
    return response

@classmethod
def create_or_get(cls, object_id=None):
    import leancloud
    """
    If object_id is not None, use create_without_data method, else use create
    :param cls:
    :param id:
    :return:
    """
    return cls() if object_id is None else leancloud.Query(cls._class_name).get(object_id=object_id)


from leancloud.object_ import Object

Object._deep_save = _deep_save
setattr(Object, "create_or_get", create_or_get)

from leancloud.client import SERVER_URLS
import os

# mc_url = os.environ.get("MC_URL", "10.9.2.191:5000")
# mc_url = os.environ.get("MC_URL", "10.30.0.128:7000")
mc_url = os.environ.get("MC_URL", "10.30.0.12:8002")#10.30.0.12:6000或10.30.0.12
# mc_url = os.environ.get("MC_URL", "api.qkzhi.com")
SERVER_URLS.update({"MC": mc_url})

from leancloud import client

client.get_base_url = _get_base_url
client.get = get
client.post = post
client.put = put

@classmethod
def become(cls, session_token):
    response = post('/users/me', params={'session_token': session_token})
    content = response.json()
    user = cls()
    user._update_data(content)
    user._handle_save_result(True)
    if 'smsCode' not in content:
        user._attributes.pop('smsCode', None)
    return user

from leancloud.user import User
User.become = become

import arrow
import leancloud
from dateutil import tz
from datetime import datetime
from werkzeug import LocalProxy
from leancloud import operation
from collections import OrderedDict
from leancloud._compat import iteritems


def get_dumpable_types():
    return (
        leancloud.ACL,
        leancloud.File,
        leancloud.GeoPoint,
        leancloud.Relation,
        operation.BaseOp,
    )


def encode(value, disallow_objects=False):
    if isinstance(value, LocalProxy):
        value = value._get_current_object()

    if isinstance(value, datetime):
        tzinfo = value.tzinfo
        if tzinfo is None:
            tzinfo = tz.tzlocal()

        result = OrderedDict()
        result["__type"] = "Date"
        result["iso"] = arrow.get(value, tzinfo).to('utc').format('YYYY-MM-DDTHH:mm:ss.SSS') + 'Z'
        return result

    if isinstance(value, leancloud.Object):
        if disallow_objects:
            raise ValueError('leancloud.Object not allowed')
        return value._to_pointer()

    if isinstance(value, leancloud.File):
        if not value.url and not value.id:
            raise ValueError('Tried to save an object containing an unsaved file.')
        return {
            '__type': 'File',
            'id': value.id,
            'name': value.name,
            'url': value.url,
        }

    if isinstance(value, get_dumpable_types()):
        return value.dump()

    if isinstance(value, (tuple, list)):
        return [encode(x, disallow_objects) for x in value]

    if isinstance(value, dict):
        return dict([(k, encode(v, disallow_objects)) for k, v in iteritems(value)])

    return value

from leancloud import utils

utils.encode = encode
