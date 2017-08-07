# -*- coding: utf-8 -*-
__author__ = "Sommily"
import hashlib
from bson import json_util
from datetime import datetime
from mongoengine import DateTimeField, ListField, StringField
from mongoengine import Document, EmbeddedDocument


class QKDocument(Document):
    CreatedDateTime = DateTimeField()
    UpdatedDateTime = DateTimeField()

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None,
             _refs=None, save_condition=None, **kwargs):
        if self.CreatedDateTime is None:
            self.CreatedDateTime = datetime.now()

        self.UpdateDateTime = datetime.now()

        list_fields = filter(lambda (k, v): isinstance(v, ListField), self._fields.items())
        for list_field in list_fields:
            values = filter(lambda x: isinstance(x, QKEmbeddedDocument), getattr(self, list_field[0]))
            map(lambda x: x.update_md5(), values)

        super(QKDocument, self).save(force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs,
                                     save_condition, **kwargs)

    meta = {
        "abstract": True
    }


class QKEmbeddedDocument(EmbeddedDocument):
    md5 = StringField()

    def update_md5(self):
        md = hashlib.md5()
        data = self.to_mongo()
        if "md5" in data.keys():
            data.pop("md5")
        md.update(json_util.dumps(data))
        self.md5 = md.hexdigest()
        return self.md5

    meta = {
        "abstract": True
    }
