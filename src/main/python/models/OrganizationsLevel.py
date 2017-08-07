# -*- coding: utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import LongField, StringField, ListField, DateTimeField, DecimalField, EmbeddedDocumentField

class OrganizationsLevel(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    gpmc = StringField()
    jzrq = DateTimeField()
    jglxdm = DecimalField(precision=6)
    cgsl = DecimalField(precision=6)
    qmltgs = DecimalField(precision=6)
    qmltgbl = DecimalField(precision=6)
    qmcgzsz = DecimalField(precision=6)
    qmcgzsl = DecimalField(precision=6)
    qmzcgbl = DecimalField(precision=6)
    jglxfldm = DecimalField(precision=6)
    cgbd = DecimalField(precision=6)
    
    meta = {
        "collection": "f10_2_8_3_jgcc",
        "indexes": [
            {
                "fields": ("Obj", "jglxfldm", "jzrq"),
                "unique": True
            }
        ]
    }
