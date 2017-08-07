# -*- coding: utf-8 -*-
__author__ = "Sommily"
from datetime import datetime
from mongoengine import Document, StringField, ComplexDateTimeField


class UpdateTimestamp(Document):
    Name = StringField(required=True)
    KeyValue = StringField(required=True)
    Timestamp = ComplexDateTimeField(default=datetime(year=1970, month=1, day=1))
    RsId = StringField(default="0")

    meta = {
        "collection": "f10_0_1_update_timestamp",
        "indexes": [
            {
                "fields": ("Name", "KeyValue"),
                "unique": True
            }
        ]
    }
