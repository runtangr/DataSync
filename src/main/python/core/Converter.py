# -*- coding: utf-8 -*-
__author__ = "Sommily"
from datetime import datetime
import dateutil.parser


def get_update_datetime(result, headers):
    try:
        if isinstance(result[headers.index("UpdateDateTime")], datetime):
            update_datetime = result[headers.index("UpdateDateTime")]
        else:
            update_datetime = dateutil.parser.parse(timestr=result[headers.index("UpdateDateTime")])
    except Exception as e:
        update_datetime = datetime(year=1970, month=1, day=1)
    return update_datetime


def get_rsid(result, headers):
    try:
        if "RsId" in headers:
            rsid = result[headers.index("RsId")]
        else:
            rsid = ""
    except Exception as e:
        rsid = ""
    return rsid


def _incremental_mode_data(table):
    results = []
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""

    for result in table:
        update_datetime = get_update_datetime(result=result, headers=headers)
        rsid = get_rsid(result=result, headers=headers)
        if update_datetime > max_update_datetime:
            max_update_datetime = update_datetime
            max_rsid = rsid
        elif update_datetime == max_update_datetime:
            try:
                max_rsid = str(max(int(rsid), int(max_rsid)))
            except Exception:
                max_rsid = str(rsid)

        tmp = {}
        for i, header in enumerate(headers):
            if result[i] != "" and result[i] is not None:
                tmp[headers[i]] = result[i]
        results.append(tmp)

    return results, max_update_datetime, max_rsid


def _full_mode_data(table):
    object_mapping = {}
    headers = table.pop(0)
    obj_index = headers.index("Obj")
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = 0

    for result in table:
        try:
            obj = result[obj_index]
            update_datetime = get_update_datetime(result=result, headers=headers)
            rsid = get_rsid(result=result, headers=headers)
            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if obj not in object_mapping.keys():
                object_mapping[obj] = []
            tmp = {}
            for i, header in enumerate(headers):
                if header != "Obj" and result[i] != "" and result[i] is not None:
                    tmp[headers[i]] = result[i]
            object_mapping[obj].append(tmp)
        except Exception as e:
            print(e)
    results = []
    for obj, data in object_mapping.items():
        if obj is not None:
            results.append({"Obj": obj, "Data": data})

    return results, max_update_datetime, max_rsid


def _full_mode_data_v2(table):
    object_mapping = {}
    headers = table.pop(0)
    obj_index = headers.index("Obj")
    date_index = headers.index("Date")
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = 0

    for result in table:
        try:
            date = result[date_index]
            obj = result[obj_index]
            update_datetime = get_update_datetime(result=result, headers=headers)
            rsid = get_rsid(result=result, headers=headers)
            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime and update_datetime != datetime(year=1970, month=1, day=1):
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if (obj, date) not in object_mapping.keys():
                object_mapping[(obj, date)] = None
            tmp = {}
            for i, header in enumerate(headers):
                if header not in ["Obj", "Date"] and result[i] != "" and result[i] is not None:
                    tmp[headers[i]] = result[i]
            object_mapping[(obj, date)] = tmp
        except Exception as e:
            print(e)
    results = []
    for (obj, date), data in object_mapping.items():
        if (obj, date) is not None and data is not None:
            results.append({"Obj": obj, "Date": date, "Data": data})

    return results, max_update_datetime, max_rsid


def _f10_2_4_1_sdgd_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            obj = result[headers.index("Obj")]
            Date = result[headers.index("Date")]
            gdrs = result[headers.index("gdrs")]
            xh = result[headers.index("xh")]
            gdmc = result[headers.index("gdmc")]
            cgs = result[headers.index("cgs")]
            zzgs = result[headers.index("zzgs")]
            zjqk = result[headers.index("zjqk")]
            gbxz = result[headers.index("gbxz")]
            gsdm = result[headers.index("gsdm")]
            if (obj, Date, gdrs) not in object_mapping.keys():
                object_mapping[(obj, Date, gdrs)] = {}
            if (xh, gdmc, gsdm) not in object_mapping[(obj, Date, gdrs)].keys():
                object_mapping[(obj, Date, gdrs)][(xh, gdmc, gsdm)] = []
            object_mapping[(obj, Date, gdrs)][(xh, gdmc, gsdm)].append(
                {
                    "cgs": cgs,
                    "zzgs": zzgs,
                    "zjqk": zjqk,
                    "gbxz": gbxz,
                }
            )
        except Exception as e:
            print(e)

    results = []
    for (obj, Date, gdrs), data in object_mapping.items():
        if obj is not None:
            result = {"Obj": obj, "Date": Date, "gdrs": gdrs, "Data": []}
            for (xh, gdmc, gsdm), ddata in object_mapping[(obj, Date, gdrs)].items():
                result["Data"].append({"xh": xh, "gdmc": gdmc, "gsdm": gsdm, "DData": ddata})
            results.append(result)

    return results, max_update_datetime, max_rsid


def _f10_2_4_3_sdltggd_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            obj = result[headers.index("Obj")]
            Date = result[headers.index("Date")]
            gdrs = result[headers.index("gdrs")]
            xh = result[headers.index("xh")]
            gdmc = result[headers.index("gdmc")]
            cgs = result[headers.index("cgs")]
            zzgs = result[headers.index("zzgs")]
            zjqk = result[headers.index("zjqk")]
            zjsm = result[headers.index("zjsm")]
            gbxz = result[headers.index("gbxz")]
            gsdm = result[headers.index("gsdm")]

            if (obj, Date, gdrs) not in object_mapping.keys():
                object_mapping[(obj, Date, gdrs)] = []
            object_mapping[(obj, Date, gdrs)].append(
                {
                    "xh": xh,
                    "gdmc": gdmc,
                    "cgs": cgs,
                    "zzgs": zzgs,
                    "zjqk": zjqk,
                    "zjsm": zjsm,
                    "gbxz": gbxz,
                    "gsdm": gsdm
                }
            )
        except Exception as e:
            print(e)

    results = []
    for (obj, Date, gdrs), data in object_mapping.items():
        if obj is not None:
            result = {"Obj": obj, "Date": Date, "gdrs": gdrs, "Data": data}
            results.append(result)

    return results, max_update_datetime, max_rsid


def _f10_2_6_3_cjhb_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            obj = result[headers.index("Obj")]
            Date = result[headers.index("Date")]
            ZdlxCode = result[headers.index("ZdlxCode")]
            ZdlxName = result[headers.index("ZdlxName")]
            cjl = result[headers.index("cjl")]
            cjje = result[headers.index("cjje")]
            yybmc = result[headers.index("yybmc")]
            yybdm = result[headers.index("yybdm")]
            mrje = result[headers.index("mrje")]
            mcje = result[headers.index("mcje")]
            gpmc = result[headers.index("gpmc")]
            jgmrze = result[headers.index("jgmrze")]
            jgmcze = result[headers.index("jgmcze")]
            yzmrze = result[headers.index("yzmrze")]
            yzmcze = result[headers.index("yzmcze")]
            cjlx = result[headers.index("cjlx")]
            mcze = result[headers.index("mcze")]
            mrze = result[headers.index("mrze")]
            CHNG = result[headers.index("CHNG")]
            CHNG_PCT = result[headers.index("CHNG_PCT")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if (obj, Date, ZdlxCode, ZdlxName, cjl, cjje, gpmc, jgmrze, jgmcze, yzmrze,
                yzmcze, mcze, mrze, CHNG, CHNG_PCT) not in object_mapping.keys():
                object_mapping[
                    (obj, Date, ZdlxCode, ZdlxName, cjl, cjje, gpmc, jgmrze, jgmcze, yzmrze, yzmcze, mcze, mrze, CHNG, CHNG_PCT)] = []
            object_mapping[
                (obj, Date, ZdlxCode, ZdlxName, cjl, cjje, gpmc, jgmrze, jgmcze, yzmrze, yzmcze, mcze, mrze, CHNG, CHNG_PCT)].append({
                "yybmc": yybmc,
                "yybdm": yybdm,
                "mrje": mrje,
                "mcje": mcje,
                "cjlx": cjlx
            })
        except Exception as e:
            print(e)

    results = []
    for (obj, Date, ZdlxCode, ZdlxName, cjl, cjje, gpmc, jgmrze, jgmcze, yzmrze, yzmcze, mcze,
         mrze, CHNG, CHNG_PCT), data in object_mapping.items():
        if obj is not None:
            result = {"Obj": obj, "Date": Date, "ZdlxCode": ZdlxCode, "ZdlxName": ZdlxName, "cjl": cjl, "cjje": cjje,
                      "gpmc": gpmc, "jgmrze": jgmrze, "jgmcze": jgmcze, "yzmrze": yzmrze, "yzmcze": yzmcze,
                      "mcze": mcze, "mrze": mrze, "Data": data, "CHNG": CHNG, "CHNG_PCT": CHNG_PCT}
            results.append(result)

    return results, max_update_datetime, max_rsid


def _f10_2_8_5_dzjy_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            obj = result[headers.index("Obj")]
            Date = result[headers.index("Date")]
            jg = result[headers.index("jg")]
            drspj = result[headers.index("drspj")]
            zjl = result[headers.index("zjl")]
            cjl = result[headers.index("cjl")]
            cjje = result[headers.index("cjje")]
            mf = result[headers.index("mf")]
            mf2 = result[headers.index("mf2")]
            RsId = result[headers.index("RsId")]

            if (obj, Date) not in object_mapping.keys():
                object_mapping[(obj, Date)] = []
            object_mapping[(obj, Date)].append(
                {
                    "jg": jg,
                    "drspj": drspj,
                    "zjl": zjl,
                    "cjl": cjl,
                    "cjje": cjje,
                    "mf": mf,
                    "mf2": mf2,
                    "RsId": RsId

                }
            )
        except Exception as e:
            print(e)

    results = []
    for (obj, Date), data in object_mapping.items():
        if obj is not None:
            result = {"Obj": obj, "Date": Date, "Data": data}
            results.append(result)

    return results, max_update_datetime, max_rsid


def _f10_4_3_news_class_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            news_id = result[headers.index("NewsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            cls_code = result[headers.index("CLS_CODE")]
            cls_name = result[headers.index("CLS_NAME")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if news_id not in object_mapping.keys():
                object_mapping[news_id] = []
            object_mapping[news_id].append(
                {
                    "ClassNo": cls_code,
                    "ClassName": cls_name
                }
            )
        except Exception as e:
            print(e)

    results = [{"NewsId": news_id, "NewsClass": data} for news_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_4_3_news_stocks_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            news_id = result[headers.index("NewsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            stock_code = result[headers.index("StockCode")]
            stock_name = result[headers.index("StockName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if news_id not in object_mapping.keys():
                object_mapping[news_id] = []
            object_mapping[news_id].append(
                {
                    "StockCode": stock_code,
                    "StockName": stock_name
                }
            )
        except Exception as e:
            print(e)

    results = [{"NewsId": news_id, "NewsStocks": data} for news_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_4_3_news_csrc_Indu_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            news_id = result[headers.index("NewsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            CsrcIndustryCode = result[headers.index("CsrcIndustryCode")]
            CsrcIndustry = result[headers.index("CsrcIndustry")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if news_id not in object_mapping.keys():
                object_mapping[news_id] = []
            object_mapping[news_id].append(
                {
                    "CsrcIndustryCode": CsrcIndustryCode,
                    "CsrcIndustry": CsrcIndustry
                }
            )
        except Exception as e:
            print(e)

    results = [{"NewsId": news_id, "NewsCsrcIndustry": data} for news_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_4_3_news_sw_Indu_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            news_id = result[headers.index("NewsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            SwIndustryCode = result[headers.index("SwIndustryCode")]
            SwIndustry = result[headers.index("SwIndustry")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if news_id not in object_mapping.keys():
                object_mapping[news_id] = []
            object_mapping[news_id].append(
                {
                    "SwIndustryCode": SwIndustryCode,
                    "SwIndustry": SwIndustry
                }
            )
        except Exception as e:
            print(e)

    results = [{"NewsId": news_id, "NewsSwIndustry": data} for news_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_4_3_news_keys_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            news_id = result[headers.index("NewsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            KeyId = result[headers.index("KeyId")]
            KeyName = result[headers.index("KeyName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if news_id not in object_mapping.keys():
                object_mapping[news_id] = []
            object_mapping[news_id].append(
                {
                    "KeyId": KeyId,
                    "KeyName": KeyName
                }
            )
        except Exception as e:
            print(e)

    results = [{"NewsId": news_id, "NewsKeys": data} for news_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_4_3_news_area_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            news_id = result[headers.index("NewsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            AreaCode = result[headers.index("AreaCode")]
            AreaName = result[headers.index("AreaName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if news_id not in object_mapping.keys():
                object_mapping[news_id] = []
            object_mapping[news_id].append(
                {
                    "AreaCode": AreaCode,
                    "AreaName": AreaName
                }
            )
        except Exception as e:
            print(e)

    results = [{"NewsId": news_id, "NewsArea": data} for news_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_4_4_gsgg_class_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            gggg_id = result[headers.index("GgggId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            class_no = result[headers.index("ClassNo")]
            class_name = result[headers.index("ClassName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if gggg_id not in object_mapping.keys():
                object_mapping[gggg_id] = []
            object_mapping[gggg_id].append(
                {
                    "ClassNo": class_no,
                    "ClassName": class_name
                }
            )
        except Exception as e:
            print(e)

    results = [{"GgggId": gggg_id, "GgggClass": data} for gggg_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_4_4_gsgg_stocks_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            gggg_id = result[headers.index("GgggId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            stock_code = result[headers.index("StockCode")]
            stock_name = result[headers.index("StockName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if gggg_id not in object_mapping.keys():
                object_mapping[gggg_id] = []
            object_mapping[gggg_id].append(
                {
                    "StockCode": stock_code,
                    "StockName": stock_name
                }
            )
        except Exception as e:
            print(e)

    results = [{"GgggId": gggg_id, "GgggStocks": data} for gggg_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_4_4_1_gsgg_content_attach_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            gggg_id = result[headers.index("GgggId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            attachment_url = result[headers.index("AttachmentUrl")]
            attachment_path = result[headers.index("AttachmentPath")]
            attachment_path_md5 = result[headers.index("AttachmentPathMd5")]
            attachment_title = result[headers.index("AttachmentTitle")]
            attachment_type = result[headers.index("AttachmentType")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if gggg_id not in object_mapping.keys():
                object_mapping[gggg_id] = []
            object_mapping[gggg_id].append(
                {
                    "AttachmentUrl": attachment_url,
                    "AttachmentPath": attachment_path,
                    "AttachmentPathMd5": attachment_path_md5,
                    "AttachmentTitle": attachment_title,
                    "AttachmentType": attachment_type
                }
            )
        except Exception as e:
            print(e)

    results = [{"GgggId": gggg_id, "Attachment": data} for gggg_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_5_1_gsyb_class_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            yan_bao_id = result[headers.index("YanBaoId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            class_no = result[headers.index("ClassNo")]
            class_name = result[headers.index("ClassName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if yan_bao_id not in object_mapping.keys():
                object_mapping[yan_bao_id] = []
            object_mapping[yan_bao_id].append(
                {
                    "ClassNo": class_no,
                    "ClassName": class_name
                }
            )
        except Exception as e:
            print(e)

    results = [{"YanBaoId": yan_bao_id, "YbClass": data} for yan_bao_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_5_1_gsyb_YbStocks_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            yan_bao_id = result[headers.index("YanBaoId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            StockCode = result[headers.index("StockCode")]
            StockName = result[headers.index("StockName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if yan_bao_id not in object_mapping.keys():
                object_mapping[yan_bao_id] = []
            object_mapping[yan_bao_id].append(
                {
                    "StockCode": StockCode,
                    "StockName": StockName
                }
            )
        except Exception as e:
            print(e)

    results = [{"YanBaoId": yan_bao_id, "YbStocks": data} for yan_bao_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_5_1_gsyb_YbCsrcIndustry_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            yan_bao_id = result[headers.index("YanBaoId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            CsrcIndustry = result[headers.index("CsrcIndustry")]
            CsrcIndustryCode = result[headers.index("CsrcIndustryCode")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if yan_bao_id not in object_mapping.keys():
                object_mapping[yan_bao_id] = []
            object_mapping[yan_bao_id].append(
                {
                    "CsrcIndustry": CsrcIndustry,
                    "CsrcIndustryCode": CsrcIndustryCode
                }
            )
        except Exception as e:
            print(e)

    results = [{"YanBaoId": yan_bao_id, "YbCsrcIndustry": data} for yan_bao_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_5_1_gsyb_YbSwIndustry_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            yan_bao_id = result[headers.index("YanBaoId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            SwIndustry = result[headers.index("SwIndustry")]
            SwIndustryCode = result[headers.index("SwIndustryCode")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if yan_bao_id not in object_mapping.keys():
                object_mapping[yan_bao_id] = []
            object_mapping[yan_bao_id].append(
                {
                    "SwIndustry": SwIndustry,
                    "SwIndustryCode": SwIndustryCode
                }
            )
        except Exception as e:
            print(e)

    results = [{"YanBaoId": yan_bao_id, "YbSwIndustry": data} for yan_bao_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_5_1_gsyb_YbKeys_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            yan_bao_id = result[headers.index("YanBaoId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            KeyId = result[headers.index("KeyId")]
            KeyName = result[headers.index("KeyName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if yan_bao_id not in object_mapping.keys():
                object_mapping[yan_bao_id] = []
            object_mapping[yan_bao_id].append(
                {
                    "KeyId": KeyId,
                    "KeyName": KeyName
                }
            )
        except Exception as e:
            print(e)

    results = [{"YanBaoId": yan_bao_id, "YbKeys": data} for yan_bao_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_5_1_gsyb_area_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            yan_bao_id = result[headers.index("YanBaoId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            AreaCode = result[headers.index("AreaCode")]
            AreaName = result[headers.index("AreaName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if yan_bao_id not in object_mapping.keys():
                object_mapping[yan_bao_id] = []
            object_mapping[yan_bao_id].append(
                {
                    "AreaCode": AreaCode,
                    "AreaName": AreaName
                }
            )
        except Exception as e:
            print(e)

    results = [{"YanBaoId": yan_bao_id, "YbArea": data} for yan_bao_id, data in object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_5_1_1_gsyb_content_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            YanBaoId = result[headers.index("YanBaoId")]
            BaoGaoRiQi = result[headers.index("BaoGaoRiQi")]
            YanJiuJiGou = result[headers.index("YanJiuJiGou")]
            YanJiuZuoZhe = result[headers.index("YanJiuZuoZhe")]
            YanBaoBiaoTi = result[headers.index("YanBaoBiaoTi")]
            Summary = result[headers.index("Summary")]
            YanBaoNeiRong = result[headers.index("YanBaoNeiRong")]
            AttachmentUrl = result[headers.index("AttachmentUrl")]
            AttachmentType = result[headers.index("AttachmentType")]
            AttachmentPath = result[headers.index("AttachmentPath")]
            AttachmentPathMd5 = result[headers.index("AttachmentPathMd5")]

            UpdateDateTime = result[headers.index("UpdateDateTime")]
            update_datetime = get_update_datetime(result=result, headers=headers)
            rsid = get_rsid(result=result, headers=headers)

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if YanBaoId not in object_mapping.keys():
                object_mapping[
                    (YanBaoId, BaoGaoRiQi, YanJiuJiGou, YanJiuZuoZhe, YanBaoBiaoTi, Summary, YanBaoNeiRong, UpdateDateTime)] = []
            object_mapping[
                (YanBaoId, BaoGaoRiQi, YanJiuJiGou, YanJiuZuoZhe, YanBaoBiaoTi, Summary, YanBaoNeiRong, UpdateDateTime)].append(
                {
                    "AttachmentUrl": AttachmentUrl,
                    "AttachmentType": AttachmentType,
                    "AttachmentPath": AttachmentPath,
                    "AttachmentPathMd5": AttachmentPathMd5
                }
            )
        except Exception as e:
            print(e)

    results = [{
                   "YanBaoId": YanBaoId,
                   "BaoGaoRiQi": BaoGaoRiQi,
                   "YanJiuJiGou": YanJiuJiGou,
                   "YanJiuZuoZhe": YanJiuZuoZhe,
                   "YanBaoBiaoTi": YanBaoBiaoTi,
                   "Summary": Summary,
                   "YanBaoNeiRong": YanBaoNeiRong,

                   "UpdateDateTime": UpdateDateTime,

                   "Attachment": data
               } for (YanBaoId, BaoGaoRiQi, YanJiuJiGou, YanJiuZuoZhe, YanBaoBiaoTi, Summary, YanBaoNeiRong,UpdateDateTime), data in
               object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_7_123_stocks_data(table):
    object_mapping = {}
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    for result in table:
        try:
            rsid = result[headers.index("RsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            ZiXunId = result[headers.index("ZiXunId")]
            ZiXunType = result[headers.index("ZiXunType")]
            StockCode = result[headers.index("StockCode")]
            StockName = result[headers.index("StockName")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            if (ZiXunId, ZiXunType) not in object_mapping.keys():
                object_mapping[(ZiXunId, ZiXunType)] = []
            object_mapping[(ZiXunId, ZiXunType)].append(
                {
                    "StockCode": StockCode,
                    "StockName": StockName
                }
            )
        except Exception as e:
            print(e)

    results = [{"ZiXunId": ZiXunId, "ZiXunType": ZiXunType, "ZiXunStocks": data} for (ZiXunId, ZiXunType), data in
               object_mapping.items()]

    return results, max_update_datetime, max_rsid


def _f10_2_10_4_mjzjqk_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            zjly = result[headers.index("zjly")]
            yksymjzj = result[headers.index("yksymjzj")]
            zjtx = result[headers.index("zjtx")]
            xmmc = result[headers.index("xmmc")]
            xmkgnd = result[headers.index("xmkgnd")]
            xmjsq = result[headers.index("xmjsq")]
            xmscq = result[headers.index("xmscq")]
            kgwcn = result[headers.index("kgwcn")]
            jhtre = result[headers.index("jhtre")]
            jdzctz = result[headers.index("jdzctz")]
            pdldzjtz = result[headers.index("pdldzjtz")]
            yjsymjzj = result[headers.index("yjsymjzj")]
            mjzjdyntre = result[headers.index("mjzjdyntre")]
            yjsyzyzj = result[headers.index("yjsyzyzj")]
            xmspqk = result[headers.index("xmspqk")]
            xmnr = result[headers.index("xmnr")]
            nzcb = result[headers.index("nzcb")]
            tzlrl = result[headers.index("tzlrl")]
            tzlsl = result[headers.index("tzlsl")]
            tzhsq = result[headers.index("tzhsq")]
            cwnbsyl = result[headers.index("cwnbsyl")]
            sfxxm = result[headers.index("sfxxm")]
            zjtxgs = result[headers.index("zjtxgs")]
            zjlydm = result[headers.index("zjlydm")]

            gpmc = result[headers.index("gpmc")]
            xmzjly_sjyj = result[headers.index("xmzjly_sjyj")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = str(rsid)

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "zjly": zjly,
                "yksymjzj": yksymjzj,
                "zjtx": zjtx,
                "xmmc": xmmc,
                "xmkgnd": xmkgnd,
                "xmjsq": xmjsq,
                "xmscq": xmscq,
                "kgwcn": kgwcn,
                "jhtre": jhtre,
                "jdzctz": jdzctz,
                "pdldzjtz": pdldzjtz,
                "yjsymjzj": yjsymjzj,
                "mjzjdyntre": mjzjdyntre,
                "yjsyzyzj": yjsyzyzj,
                "xmspqk": xmspqk,
                "xmnr": xmnr,
                "nzcb": nzcb,
                "tzlrl": tzlrl,
                "tzlsl": tzlsl,
                "tzhsq": tzhsq,
                "cwnbsyl": cwnbsyl,
                "sfxxm": sfxxm,
                "zjtxgs": zjtxgs,
                "zjlydm": zjlydm,

                "xmzjly_sjyj":xmzjly_sjyj,
                "gpmc":gpmc
            })
        except Exception as e:
            print("_f10_2_10_4_mjzjqk_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_2_8_6_ggcgbd_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            gpmc = result[headers.index("gpmc")]
            jgdm = result[headers.index("jgdm")]
            zjcrmc = result[headers.index("zjcrmc")]
            zjcsl = result[headers.index("zjcsl")]
            zjczb = result[headers.index("zjczb")]
            zjcfs = result[headers.index("zjcfs")]
            zjyfsmc = result[headers.index("zjyfsmc")]
            zjclb = result[headers.index("zjclb")]
            zjylbmc = result[headers.index("zjylbmc")]
            zjcjj = result[headers.index("zjcjj")]
            qcgs = result[headers.index("qcgs")]
            qczb = result[headers.index("qczb")]
            yzxdr = result[headers.index("yzxdr")]
            ggrq = result[headers.index("ggrq")]
            ggid = result[headers.index("ggid")]
            hcgs = result[headers.index("hcgs")]
            hczb = result[headers.index("hczb")]
            zjcjzr = result[headers.index("zjcjzr")]
            sfdydgd = result[headers.index("sfdydgd")]
            jz = result[headers.index("jz")]

            rsid = result[headers.index("RsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "gpmc": gpmc,
                "jgdm": jgdm,
                "zjcrmc": zjcrmc,
                "zjcsl": zjcsl,
                "zjczb": zjczb,
                "zjcfs": zjcfs,
                "zjyfsmc": zjyfsmc,
                "zjclb": zjclb,
                "zjylbmc": zjylbmc,
                "zjcjj": zjcjj,
                "qcgs": qcgs,
                "qczb": qczb,
                "yzxdr": yzxdr,
                "ggrq": ggrq,
                "ggid": ggid,
                "hcgs": hcgs,
                "hczb": hczb,
                "zjcjzr": zjcjzr,
                "sfdydgd": sfdydgd,
                "jz": jz
            })
        except Exception as e:
            print("_f10_2_8_6_ggcgbd_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_4_7_3_ssbx_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            gpmc = result[headers.index("gpmc")]
            ssrq = result[headers.index("ssrq")]
            srsssl = result[headers.index("srsssl")]
            srkpj = result[headers.index("srkpj")]
            srzgj = result[headers.index("srzgj")]
            srzdj = result[headers.index("srzdj")]
            ssspj = result[headers.index("ssspj")]
            srcjjj = result[headers.index("srcjjj")]
            srcjl = result[headers.index("srcjl")]
            srcje = result[headers.index("srcje")]
            srzdf = result[headers.index("srzdf")]
            srhsl = result[headers.index("srhsl")]
            dxsyl = result[headers.index("dxsyl")]
            lxztts = result[headers.index("lxztts")]
            zhztspj = result[headers.index("zhztspj")]
            zhztsyl = result[headers.index("zhztsyl")]
            Obj = result[headers.index("Obj")]

            rsid = result[headers.index("RsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "gpmc": gpmc,
                "ssrq": ssrq,
                "srsssl": srsssl,
                "srkpj": srkpj,
                "srzgj": srzgj,
                "srzdj": srzdj,
                "ssspj": ssspj,
                "srcjjj": srcjjj,
                "srcjl": srcjl,
                "srcje": srcje,
                "srzdf": srzdf,
                "srhsl": srhsl,
                "dxsyl": dxsyl,
                "lxztts": lxztts,
                "zhztspj": zhztspj,
                "zhztsyl": zhztsyl,
                "Obj": Obj
            })
        except Exception as e:
            print("_f10_4_7_3_ssbx_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_2_8_1_jjlt_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            gpmc = result[headers.index("gpmc")]
            jjrq = result[headers.index("jjrq")]
            jjsl = result[headers.index("jjsl")]
            jjsz = result[headers.index("jjsz")]
            jjzb = result[headers.index("jjzb")]
            gddm = result[headers.index("gddm")]
            gdmc = result[headers.index("gdmc")]
            zxsp = result[headers.index("zxsp")]
            xxyydm = result[headers.index("xxyydm")]
            xxyy = result[headers.index("xxyy")]

            rsid = result[headers.index("RsId")]
            update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "gpmc": gpmc,
                "jjrq": jjrq,
                "jjsl": jjsl,
                "jjsz": jjsz,
                "jjzb": jjzb,
                "gddm": gddm,
                "gdmc": gdmc,
                "zxsp": zxsp,
                "xxyydm": xxyydm,
                "xxyy": xxyy
            })
        except Exception as e:
            print("_f10_2_8_1_jjlt_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_2_8_3_jgcc_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            gpmc = result[headers.index("gpmc")]
            jzrq = result[headers.index("jzrq")]
            jglxdm = result[headers.index("jglxdm")]
            cgsl = result[headers.index("cgsl")]
            qmltgs = result[headers.index("qmltgs")]
            qmltgbl = result[headers.index("qmltgbl")]
            qmcgzsz = result[headers.index("qmcgzsz")]
            qmcgzsl = result[headers.index("qmcgzsl")]
            qmzcgbl = result[headers.index("qmzcgbl")]
            jglxfldm = result[headers.index("jglxfldm")]
            cgbd = result[headers.index("cgbd")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "gpmc": gpmc,
                "jzrq": jzrq,
                "jglxdm": jglxdm,
                "cgsl": cgsl,
                "qmltgs": qmltgs,
                "qmltgbl": qmltgbl,
                "qmcgzsz": qmcgzsz,
                "qmcgzsl": qmcgzsl,
                "qmzcgbl": qmzcgbl,
                "jglxfldm": jglxfldm,
                "cgbd": cgbd
            })
        except Exception as e:
            print("_f10_2_8_3_jgcc_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_2_8_3_1_jgccmx_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            gpmc = result[headers.index("gpmc")]
            jzrq = result[headers.index("jzrq")]
            jgdm = result[headers.index("jgdm")]
            jgmc = result[headers.index("jgmc")]
            jglxdm = result[headers.index("jglxdm")]
            jgsx = result[headers.index("jgsx")]
            cgsz = result[headers.index("cgsz")]
            cgzs = result[headers.index("cgzs")]
            zzgbb = result[headers.index("zzgbb")]
            cltgsl = result[headers.index("cltgsl")]
            cltgsz = result[headers.index("cltgsz")]
            ltgzb = result[headers.index("ltgzb")]
            jdid = result[headers.index("jdid")]
            jglxfldm = result[headers.index("jglxfldm")]
            cgbd = result[headers.index("cgbd")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "gpmc": gpmc,
                "jzrq": jzrq,
                "jgdm": jgdm,
                "jgmc": jgmc,
                "jglxdm": jglxdm,
                "jgsx": jgsx,
                "cgsz": cgsz,
                "cgzs": cgzs,
                "zzgbb": zzgbb,
                "cltgsl": cltgsl,
                "cltgsz": cltgsz,
                "ltgzb": ltgzb,
                "jdid": jdid,
                "jglxfldm": jglxfldm,
                "cgbd": cgbd
            })
        except Exception as e:
            print("_f10_2_8_3_1_jgccmx_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_5_4_ylyc_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            gpmc = result[headers.index("gpmc")]
            ycnd = result[headers.index("ycnd")]
            mgsy1 = result[headers.index("mgsy1")]
            mgsy2 = result[headers.index("mgsy2")]
            mgsy3 = result[headers.index("mgsy3")]
            yysy1 = result[headers.index("yysy1")]
            yysy2 = result[headers.index("yysy2")]
            yysy3 = result[headers.index("yysy3")]
            jly1 = result[headers.index("jly1")]
            jly2 = result[headers.index("jly2")]
            jly3 = result[headers.index("jly3")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "gpmc": gpmc,
                "ycnd": ycnd,
                "mgsy1": mgsy1,
                "mgsy2": mgsy2,
                "mgsy3": mgsy3,
                "yysy1": yysy1,
                "yysy2": yysy2,
                "yysy3": yysy3,
                "jly1": jly1,
                "jly2": jly2,
                "jly3": jly3
            })
        except Exception as e:
            print("_f10_5_4_ylyc_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_5_5_jgpj_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            gpmc = result[headers.index("gpmc")]
            fbrq = result[headers.index("fbrq")]
            tzpj = result[headers.index("tzpj")]
            qtzpj = result[headers.index("qtzpj")]
            sfscpj = result[headers.index("sfscpj")]
            pjbh = result[headers.index("pjbh")]
            mbjg = result[headers.index("mbjg")]
            mbjgqx = result[headers.index("mbjgqx")]
            yspj = result[headers.index("yspj")]
            hymc = result[headers.index("hymc")]
            yjjcdm = result[headers.index("yjjcdm")]
            yjjgmc = result[headers.index("yjjgmc")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "gpmc": gpmc,
                "fbrq": fbrq,
                "tzpj": tzpj,
                "qtzpj": qtzpj,
                "sfscpj": sfscpj,
                "pjbh": pjbh,
                "mbjg": mbjg,
                "mbjgqx": mbjgqx,
                "yspj": yspj,
                "hymc": hymc,
                "yjjcdm": yjjcdm,
                "yjjgmc": yjjgmc
            })
        except Exception as e:
            print("_f10_5_5_jgpj_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_5_6_jgpjdf_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            tzpj = result[headers.index("tzpj")]
            pjsl = result[headers.index("pjsl")]
            zscr = result[headers.index("zscr")]
            mrpj = result[headers.index("mrpj")]
            zjs = result[headers.index("zjs")]

            rsid = result[headers.index("RsId")]
            # update_datetime = dateutil.parser.parse(result[headers.index("UpdateDateTime")])
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = str(rsid)
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = str(rsid)

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "tzpj": tzpj,
                "pjsl": pjsl,
                "zscr": zscr,
                "mrpj": mrpj,
                "zjs": zjs
            })
        except Exception as e:
            print("_f10_5_6_jgpjdf_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_2_6_3_1_hygg_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            cjlx = result[headers.index("cjlx")]
            ljmr = result[headers.index("ljmr")]
            ljmc = result[headers.index("ljmc")]
            flfs = result[headers.index("flfs")]
            sbcs = result[headers.index("sbcs")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "cjlx": cjlx,
                "ljmr": ljmr,
                "ljmc": ljmc,
                "flfs": flfs,
                "sbcs": sbcs
            })
        except Exception as e:
            print("_f10_2_6_3_1_hygg_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid


def _f10_2_6_3_2_jgzc_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            cjlx = result[headers.index("cjlx")]
            jgljmr = result[headers.index("jgljmr")]
            jgljmc = result[headers.index("jgljmc")]
            flfs = result[headers.index("flfs")]
            jgcys = result[headers.index("jgcys")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "cjlx": cjlx,
                "jgljmr": jgljmr,
                "jgljmc": jgljmc,
                "flfs": flfs,
                "jgcys": jgcys
            })

        except Exception as e:
            print("_f10_2_6_3_2_jgzc_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid

def _f10_2_6_3_3_yzgz_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            yybdm = result[headers.index("yybdm")]
            yybmc = result[headers.index("yybmc")]
            yzsbcs = result[headers.index("yzsbcs")]
            yzmrzs = result[headers.index("yzmrzs")]
            yzljmr = result[headers.index("yzljmr")]
            yzmczs = result[headers.index("yzmczs")]
            yzljmc = result[headers.index("yzljmc")]
            flfs = result[headers.index("flfs")]    

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "yybdm": yybdm,
                "yybmc": yybmc,
                "yzsbcs": yzsbcs,
                "yzmrzs": yzmrzs,
                "yzljmr": yzljmr,
                "yzmczs": yzmczs,
                "yzljmc": yzljmc,
                "flfs": flfs
            })

        except Exception as e:
            print("_f10_2_6_3_3_yzgz_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid

def _f10_2_3_5_yjyg_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            gpmc = result[headers.index("gpmc")]
            ggrq = result[headers.index("ggrq")]
            jzrq = result[headers.index("jzrq")]
            ycdm = result[headers.index("ycdm")]
            yclx = result[headers.index("yclx")]
            ggly = result[headers.index("ggly")]
            yzzy = result[headers.index("yzzy")]
            jtnr = result[headers.index("jtnr")]
            yysm = result[headers.index("yysm")]
            jlytbsx = result[headers.index("jlytbsx")]
            jlytbxx = result[headers.index("jlytbxx")]
            qntqsy = result[headers.index("qntqsy")]
            qntqlr = result[headers.index("qntqlr")]
            yjmgsysx = result[headers.index("yjmgsysx")]
            yjmgsyxx = result[headers.index("yjmgsyxx")]    

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "gpmc": gpmc,
                "ggrq": ggrq,
                "jzrq": jzrq,
                "ycdm": ycdm,
                "yclx": yclx,
                "ggly": ggly,
                "yzzy": yzzy,
                "jtnr": jtnr,
                "yysm": yysm,
                "jlytbsx": jlytbsx,
                "jlytbxx": jlytbxx,
                "qntqsy": qntqsy,
                "qntqlr": qntqlr,
                "yjmgsysx": yjmgsysx,
                "yjmgsyxx": yjmgsyxx
            })

        except Exception as e:
            print("_f10_2_3_5_yjyg_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid

def _f10_5_7_qgqp_data(table):
    headers = table.pop(0)
    max_update_datetime = datetime(year=1970, month=1, day=1)
    max_rsid = ""
    results = []
    for result in table:
        try:
            Obj = result[headers.index("Obj")]
            gpmc = result[headers.index("gpmc")]
            ggrq = result[headers.index("ggrq")]
            pjnr = result[headers.index("pjnr")]
            ly = result[headers.index("ly")]

            rsid = result[headers.index("RsId")]
            update_datetime = result[headers.index("UpdateDateTime")]

            if update_datetime > max_update_datetime:
                max_update_datetime = update_datetime
                max_rsid = rsid
            elif update_datetime == max_update_datetime:
                try:
                    max_rsid = str(max(int(rsid), int(max_rsid)))
                except Exception:
                    max_rsid = rsid

            results.append({
                "RsId": str(rsid),
                "UpdateDateTime": update_datetime,
                "Obj": Obj,
                "gpmc": gpmc,
                "ggrq": ggrq,
                "pjnr": pjnr,
                "ly": ly
            })

        except Exception as e:
            print("_f10_5_7_qgqp_data failed: {}".format(e))

    return results, max_update_datetime, max_rsid

def get_results(action_name, table):
    converter_mapping = {
        "f10_0_2_code_list": _incremental_mode_data,
        "f10_1_1_zxzycwsj_ag": _incremental_mode_data,
        "f10_1_1_zxzycwsj_bg": _incremental_mode_data,
        "f10_1_2_qxsj": _incremental_mode_data,
        "f10_1_3_gbls": _full_mode_data,
        "f10_2_1_gsgk": _incremental_mode_data,
        "f10_2_2_1_zycwzb": _full_mode_data_v2,
        "f10_2_2_2_xjllb": _full_mode_data_v2,
        "f10_2_2_3_lrfpb": _full_mode_data_v2,
        "f10_2_2_4_zcfzb": _full_mode_data_v2,
        "f10_2_4_1_sdgd": _f10_2_4_1_sdgd_data,
        "f10_2_4_2_gdhs": _full_mode_data_v2,
        "f10_2_4_3_sdltggd": _f10_2_4_3_sdltggd_data,
        "f10_2_4_4_kggd": _incremental_mode_data,
        "f10_2_4_5_sjkzr": _incremental_mode_data,
        "f10_2_5_1_gbjg": _full_mode_data_v2,
        "f10_2_5_4_gbgk": _incremental_mode_data,
        "f10_2_6_3_cjhb": _f10_2_6_3_cjhb_data,
        "f10_2_8_2_rzrq": _full_mode_data_v2,
        "f10_2_8_5_dzjy": _f10_2_8_5_dzjy_data,
        "f10_4_1_stocknews": _incremental_mode_data,
        "f10_4_1_1_stocknews_content": _incremental_mode_data,
        "f10_4_2_stockgggg": _incremental_mode_data,
        "f10_4_2_1_stockgggg_content": _incremental_mode_data,
        "f10_4_7_1_xingushengou": _incremental_mode_data,
        "f10_6_1_block_section": _incremental_mode_data,
        "f10_6_2_block_section_stock": _incremental_mode_data,
        "f10_7_1_stock_news": _incremental_mode_data,
        "f10_7_2_stock_gg": _incremental_mode_data,
        "f10_7_3_stock_yb": _incremental_mode_data,
        "f10_4_3_news": _incremental_mode_data,
        "f10_4_3_news_class": _f10_4_3_news_class_data,
        "f10_4_3_news_top_class": _f10_4_3_news_class_data,
        "f10_4_3_news_stocks_a": _f10_4_3_news_stocks_data,
        "f10_4_3_news_stocks_b": _f10_4_3_news_stocks_data,
        "f10_4_3_news_csrc_Indu": _f10_4_3_news_csrc_Indu_data,
        "f10_4_3_news_sw_Indu": _f10_4_3_news_sw_Indu_data,
        "f10_4_3_news_keys": _f10_4_3_news_keys_data,
        "f10_4_3_news_area": _f10_4_3_news_area_data,
        "f10_4_3_1_news_content": _incremental_mode_data,
        "f10_4_4_gsgg": _incremental_mode_data,
        "f10_4_4_gsgg_class": _f10_4_4_gsgg_class_data,
        "f10_4_4_gsgg_stocks": _f10_4_4_gsgg_stocks_data,
        "f10_4_4_1_gsgg_content": _incremental_mode_data,
        "f10_4_4_1_gsgg_content_attach": _f10_4_4_1_gsgg_content_attach_data,
        "f10_5_1_gsyb": _incremental_mode_data,
        "f10_5_1_gsyb_class": _f10_5_1_gsyb_class_data,
        "f10_5_1_gsyb_stocks": _f10_5_1_gsyb_YbStocks_data,
        "f10_5_1_gsyb_csIndu": _f10_5_1_gsyb_YbCsrcIndustry_data,
        "f10_5_1_gsyb_swIndu": _f10_5_1_gsyb_YbSwIndustry_data,
        "f10_5_1_gsyb_keys": _f10_5_1_gsyb_YbKeys_data,
        "f10_5_1_gsyb_area": _f10_5_1_gsyb_area_data,
        "f10_5_1_1_gsyb_content": _f10_5_1_1_gsyb_content_data,
        "f10_7_1_news": _incremental_mode_data,
        "f10_7_1_news_stocks_a": _f10_7_123_stocks_data,
        "f10_7_1_news_stocks_b": _f10_7_123_stocks_data,
        "f10_7_2_gsgg": _incremental_mode_data,
        "f10_7_2_gsgg_stocks": _f10_7_123_stocks_data,
        "f10_7_3_gsyb": _incremental_mode_data,
        "f10_7_3_gsyb_stocks": _f10_7_123_stocks_data,
        "f10_1_4_stockcodelist": _incremental_mode_data,
        "f10_4_8_caijingrili": _incremental_mode_data,
        "f10_4_8_1_fina_event": _incremental_mode_data,
        "f10_4_8_2_fina_data": _incremental_mode_data,
        "f10_4_7_3_ssbx": _f10_4_7_3_ssbx_data,
        "f10_2_10_4_mjzjqk": _f10_2_10_4_mjzjqk_data,
        "f10_2_8_6_ggcgbd": _f10_2_8_6_ggcgbd_data,
        "f10_2_8_1_jjlt": _f10_2_8_1_jjlt_data,
        "f10_2_8_3_jgcc": _f10_2_8_3_jgcc_data,
        "f10_2_8_3_1_jgccmx": _f10_2_8_3_1_jgccmx_data,
        "f10_5_4_ylyc": _f10_5_4_ylyc_data,
        "f10_5_5_jgpj": _f10_5_5_jgpj_data,
        "f10_5_6_jgpjdf": _f10_5_6_jgpjdf_data,
        "f10_2_6_3_1_hygg": _f10_2_6_3_1_hygg_data,
        "f10_2_6_3_2_jgzc": _f10_2_6_3_2_jgzc_data,
        "f10_2_6_3_3_yzgz": _f10_2_6_3_3_yzgz_data,
        "f10_2_3_5_yjyg": _f10_2_3_5_yjyg_data,
        "f10_5_7_qgqp": _f10_5_7_qgqp_data
    }
    return converter_mapping[action_name](table)
