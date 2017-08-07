# -*- coding: utf-8 -*-
__author__ = "Tony"

from models.QKDocument import QKDocument, QKEmbeddedDocument
from mongoengine import LongField, StringField, ListField, DateTimeField, DecimalField, EmbeddedDocumentField

class OrganizationsLevelDetail(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    gpmc = StringField()
    jzrq = DateTimeField()
    jgdm = LongField()
    jgmc = StringField()
    jglxdm = DecimalField(precision=6)
    cgsz = DecimalField(precision=6)
    cgzs = DecimalField(precision=6)
    zzgbb = DecimalField(precision=6)
    cltgsl = DecimalField(precision=6)
    cltgsz = DecimalField(precision=6)
    ltgzb = DecimalField(precision=6)
    jdid = DecimalField(precision=6)
    jglxfldm = DecimalField(precision=6)
    cgbd = DecimalField(precision=6)

    # New
    jgsx = StringField()

    meta = {
        "collection": "f10_2_8_3_1_jgccmx",
        "indexes": [
            {
                "fields": ("Obj", "jgdm", "jzrq"),
                "unique": True
            }
        ]
    }
