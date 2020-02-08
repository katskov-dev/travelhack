import openpyxl
import json
import ujson

wb = openpyxl.load_workbook('dataset.xlsx')


def convert_countries():
    countries = {
        "countries":
            []
    }
    countries_wb = wb["CountryDict"]
    for i in range(2, 249):
        country = {}
        code = countries_wb[f'A{i}'].value
        name = countries_wb[f'B{i}'].value
        name_r = countries_wb[f'C{i}'].value
        country["code"] = code if code is not "" else ""
        country["name"] = name if name is not "" else ""
        country["name_r"] = name_r if name_r is not "" else ""
        countries["countries"].append(country)

    with open('countries.json', 'w') as f:
        f.write(ujson.dumps(countries))


def convert_user():
    user_data = {
        "users": [

        ]
    }
    users_wb = wb["Data"]
    for i in range(2, 300000):
        user = {}
        id = users_wb[f'A{i}'].value
        gender = users_wb[f'B{i}'].value
        age = users_wb[f'C{i}'].value
        region = users_wb[f'D{i}'].value
        device_type = users_wb[f'E{i}'].value
        os = users_wb[f'F{i}'].value
        subsage_mf_segment = users_wb[f'G{i}'].value
        using_internet = users_wb[f'H{i}'].value
        start_trip = users_wb[f'I{i}'].value
        end_trip = users_wb[f'J{i}'].value
        trip_duration = users_wb[f'K{i}'].value
        trip_main_country = users_wb[f'L{i}'].value
        countries_in_trip = users_wb[f'M{i}'].value
        arpu_m3 = users_wb[f'N{i}'].value
        sms_in_cnt_m3 = users_wb[f'O{i}'].value
        sms_out_cnt_m3 = users_wb[f'P{i}'].value
        mou_in_revenue_m3 = users_wb[f'Q{i}'].value
        mou_out_revenue_m3 = users_wb[f'R{i}'].value
        dou_duration_m3 = users_wb[f'S{i}'].value

        user["id"] = id if id is not "" else ""
        user["gender"] = gender if gender is not "" else ""
        user["age"] = age if age is not "" else ""
        user["region"] = region if region is not "" else ""
        user["device_type"] = device_type if device_type is not "" else ""
        user["os"] = os if os is not "" else ""
        user["subsage_mf_segment"] = subsage_mf_segment if subsage_mf_segment is not "" else ""
        user["using_internet"] = using_internet if using_internet is not "" else ""
        user["start_trip"] = start_trip if start_trip is not "" else ""
        user["end_trip"] = end_trip if end_trip is not "" else ""
        user["trip_duration"] = trip_duration if trip_duration is not "" else ""
        user["trip_main_country"] = trip_main_country if trip_main_country is not "" else ""
        user["countries_in_trip"] = countries_in_trip if countries_in_trip is not "" else ""
        user["arpu_m3"] = arpu_m3 if arpu_m3 is not "" else ""
        user["sms_in_cnt_m3"] = sms_in_cnt_m3 if sms_in_cnt_m3 is not "" else ""
        user["sms_out_cnt_m3"] = sms_out_cnt_m3 if sms_out_cnt_m3 is not "" else ""
        user["mou_in_revenue_m3"] = mou_in_revenue_m3 if mou_in_revenue_m3 is not "" else ""
        user["mou_out_revenue_m3"] = mou_out_revenue_m3 if mou_out_revenue_m3 is not "" else ""
        user["dou_duration_m3"] = dou_duration_m3 if dou_duration_m3 is not "" else ""

        user_data["users"].append(user)

    with open('users.json', 'w') as f:
        f.write(ujson.dumps(user_data))
