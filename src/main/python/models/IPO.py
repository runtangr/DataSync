# -*- coding: utf-8 -*-
__author__ = "Sommily"
from models.QKDocument import QKDocument
from mongoengine import StringField, DateTimeField, DecimalField, LongField


class IPO(QKDocument):
    ShenGouDate = DateTimeField()  # 申购日期
    ShenGouDaiMa = StringField()  # 申购代码
    ShenGouMingCheng = StringField()  # 申购名称
    FaXingJia = DecimalField(precision=6)  # 发行价
    FaXingLiang = DecimalField(precision=6)  # 发行量(万)
    FaXingShiYingLu = DecimalField(precision=6)  # 发行市盈率
    ShenGouShangXian = DecimalField(precision=6)  # 购上限
    ShangShiDate = DateTimeField()  # 上市日期
    GuPiaoDaiMa = StringField()  # 股票代码
    ZhongQianLu = DecimalField(precision=6)  # 中签率
    zyqgs = LongField()
    zqjkr = DateTimeField()  # 中签缴款日
    wsfxl = DecimalField()  # 网上发行量(万股)
    fxfs = StringField()  # 发行方式
    FxStatus = LongField() # 发行状态
    FxStatusName = StringField() # 发行状态名称
    wszqsl = DecimalField(precision=6)
    wszqjg = StringField()
    wxzqgbr = DateTimeField()
    wxzqsj = DecimalField()
    wxzqjg = StringField()
    wxzql = DecimalField(precision=6)
    wsdjzj = DecimalField(precision=6)
    wxdjzj = DecimalField(precision=6)
    wszjjdr = DateTimeField()
    wxzjjdr = DateTimeField()
    zyqsxzj = DecimalField(precision=6)       
    wxyxsgbl = DecimalField(precision=6)      
    wxcepsbs = DecimalField(precision=6)      
    wxsghs = LongField()
    wxyxsggs = DecimalField(precision=6)      
    wssghs = LongField()
    wsyxsggs = DecimalField(precision=6)
    gplx = StringField()          
    ssdd = StringField()          
    fxff = StringField()
    sjmjje = DecimalField(precision=6)        
    wssgksr = DateTimeField()       
    wssgjzr = DateTimeField()       
    wxsgksr = DateTimeField()
    wxsgjzr = DateTimeField()       
    wxgkpssggs = DecimalField(precision=6)    
    fxxggs = DecimalField(precision=6)        
    zqzj = DecimalField(precision=6)          
    sxsz = DecimalField(precision=6)
    zcxsdm = LongField()
    zcxs = StringField()          
    cxfs = StringField()          
    qmgjzc = DecimalField(precision=6)
    hmgjzc = DecimalField(precision=6)        

    UpdateDateTime = DateTimeField()
    RsId = StringField()

    # New!! at 20161127
    sfshtg = StringField()
    jgdm = LongField()
    gsmc = StringField()
    wszqgbr = DateTimeField()

    #New!! at 20161129
    sbplrq = DateTimeField() 
    shrq = DateTimeField()

    meta = {
        "collection": "f10_4_7_1_xingushengou",
        "indexes": [
            {
                "fields": ("RsId",),
                "unique": True
            }
        ]
    }
