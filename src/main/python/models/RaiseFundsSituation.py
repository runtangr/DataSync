#-*-coding:utf-8 -*-
__author__ = "Tony"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField

class RaiseFundsSituation(QKDocument):
    RsId = StringField()
    UpdateDateTime = DateTimeField()
    Obj = StringField()
    gpmc = StringField()
    zjly = StringField()
    yksymjzj = DecimalField(precision=6)
    zjtx = StringField()
    xmmc = StringField()
    xmkgnd = DecimalField(precision=6)
    xmjsq = DecimalField(precision=6)
    xmscq = DecimalField(precision=6)
    kgwcn = DecimalField(precision=6)
    jhtre = DecimalField(precision=6)
    jdzctz = DecimalField(precision=6)
    pdldzjtz = DecimalField(precision=6)       
    yjsymjzj = DecimalField(precision=6)
    mjzjdyntre = DecimalField(precision=6)
    yjsyzyzj = DecimalField(precision=6)       
    xmspqk = StringField()
    xmnr = StringField()          
    nzcb = DecimalField(precision=6)
    tzlrl = DecimalField(precision=6)
    tzlsl = DecimalField(precision=6)
    tzhsq = DecimalField(precision=6)          
    cwnbsyl = DecimalField(precision=6)
    sfxxm = StringField()         
    zjtxgs = StringField()
    zjlydm = LongField()
    xmzjly_sjyj = DateTimeField()

    meta = {
        "collection": "f10_2_10_4_mjzjqk",
        "indexes": [
            {
                "fields": ("RsId",),
                "unique": True
            }
        ]
    }
