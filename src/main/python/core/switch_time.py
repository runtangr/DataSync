import datetime

def local2utc(local_st):

     return local_st - datetime.timedelta(hours=8)