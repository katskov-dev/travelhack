import aiohttp
import asyncio
import json
from sanic.response import  json as jsons

async def req3(query):
    async with aiohttp.ClientSession() as session:
        params = {
                  'query': query,
                  'lang': "ru",
                  'lookFor': "both",
                  'limit': 1
                  }
        async with session.get('https://engine.hotellook.com/api/v2/lookup.json', params=params) as resp:
            d = json.loads(await resp.text())
            d = d["results"]
            # d = d[0]
            d = d["locations"]
            # print(json.dumps(d, indent=4))
            return d

    return {}



async def req1(depart_start, return_start, origin_iata, destination_iata):
    async with aiohttp.ClientSession() as session:
        params = {'origin_iata': origin_iata,#'MOW',
                  'destination_iata': destination_iata,#'TYO',
                  'depart_start': depart_start,#'2020-02-05',
                  'return_start': return_start,#'2020-02-12',
                  'depart_range': "2",
                  'return_range': "2",
                  'need_request': "True", }
        async with session.get('https://s.travel.megafon.ru/price_matrix', params=params) as resp:
            d = json.loads(await resp.text())

            return d

    return {}


async def req2(check_in, check_out, adults, ids):




    f = open("x.json", 'w')
    res = []
    async with aiohttp.ClientSession() as session:
        data = {
            "page": "serp",
            "search_id": "",
            "params": {
                "check_in": check_in,#"2020-02-15",
                # "check_in": "2020-02-15",
                # "check_out": "2020-02-16",
                "check_out": check_out,#"2020-02-16",
                "marker": "171596.70000000000.$1489",
                "currency": "rub",
                "locale": "ru",
                "rooms": [
                    {
                        # "adults": 1,
                        "adults": int(adults),#1,
                        "children": []
                    }
                ],
                "locations_ids": [
                    # 2764
                    int(ids)
                ],
                "hotels_ids": [],
                # "destination": "Стамбул, Турция ",
                "destination": "null",
                "host": "s.travel.megafon.ru",
                "flags": {
                    "auid": "null",
                    "ab": "null",
                    "deviceType": "desktop"
                },
                "popularity": "default"
            },
            "selected_hotels_ids": [],
            "filters": {
                "prices": {
                    "groups": [
                        0,
                        500,
                        1000,
                        1500,
                        2000,
                        2500,
                        3000,
                        4000,
                        5000,
                        6000,
                        7000,
                        8000,
                        9000,
                        12000,
                        15000,
                        20000,
                        30000,
                        50000,
                        100000,
                        2147483647
                    ]
                },
                "ratings": {
                    "groups": [
                        0,
                        0.5,
                        1,
                        1.5,
                        2,
                        2.5,
                        3,
                        3.5,
                        4,
                        4.5,
                        5,
                        5.5,
                        6,
                        6.5,
                        7,
                        7.5,
                        8,
                        8.5,
                        9,
                        9.5,
                        10
                    ]
                }
            },
            "sort": "popularity",
            "limit": 10,
            "offset": 0
        }
        # data = json.dumps(data).encode()
        async with session.post('https://s.travel.megafon.ru/api/wl_search/result', json=data) as resp:
            d = json.loads(await resp.text())
            # loc = d[ids]
            hotels = d["hotels"]
            # return d
            # hotels_amenties = d["filters"]
            # hotels_amenties = hotels_amenties["counters"]
            # hotels_amenties = hotels_amenties["prices"]
            # hotels_amenties = hotels_amenties["property_types"]
            hotels_amenties = d["hotels_amenities"]

            # search_id = d["search_id"]
            loc = []
            # print("locations" in d)
            # for key in d["locations"].keys():
            #     print(key)
            #     # print(type(key))
                # if key in d:
                #     k = d[key]
                #
                #     print(k["hotels"])
            # stop = d["stop"]
            # f.write(json.dumps(d, ))



        # print(type(stop))
        for i in range(3):


            if not ("stop" in d) or (d["stop"] != False):
                break
            # if stop != False:
            #     break
            async with aiohttp.ClientSession() as session:
                data = {
                        "page": "serp",
                        "search_id": "",
                        "params": {
                            "check_in": check_in,#"2020-03-29",
                            "check_out": check_out,#"2020-03-31",
                            "marker": "171596.70000000000.$1489",
                            "currency": "rub",
                            "locale": "ru",
                            "rooms": [
                                {
                                    "adults": int(adults),#2,
                                    "children": []
                                }
                            ],
                            "locations_ids": [int(ids)],
                            "destination": 'null',
                            "hotels_ids": [],
                            "host": "s.travel.megafon.ru",
                            "flags": {
                                "auid": 'null',
                                "ab": 'null',
                                "deviceType": "desktop"
                            },
                            "popularity": "default"
                        },
                        "selected_hotels_ids": [],
                        "filters": {
                            "prices": {
                                "groups": [
                                    0,
                                    500,
                                    1000,
                                    1500,
                                    2000,
                                    2500,
                                    3000,
                                    4000,
                                    5000,
                                    6000,
                                    7000,
                                    8000,
                                    9000,
                                    12000,
                                    15000,
                                    20000,
                                    30000,
                                    50000,
                                    100000,
                                    2147483647
                                ]
                            },
                            "ratings": {
                                "groups": [
                                    0,
                                    0.5,
                                    1,
                                    1.5,
                                    2,
                                    2.5,
                                    3,
                                    3.5,
                                    4,
                                    4.5,
                                    5,
                                    5.5,
                                    6,
                                    6.5,
                                    7,
                                    7.5,
                                    8,
                                    8.5,
                                    9,
                                    9.5,
                                    10
                                ]
                            }
                        },
                        "sort": "popularity",
                        "limit": 10,
                        "offset": 0
                    }

                async with session.post('https://s.travel.megafon.ru/api/wl_search/result', json=data) as resp:
                    d = json.loads(await resp.text())
                    # if not "stop" in d:
                    #     break

                    if "hotels" in d:
                        hotels.extend(d["hotels"])
                    # stop = d["stop"]
                    f.write(json.dumps(d))
    return hotels, hotels_amenties
async def a1(depart_start, return_start, origin_iata, destination_iata):
    return await req1(depart_start, return_start, origin_iata, destination_iata)

async def a2(check_in, check_out, adults, destination):
    return await req2(check_in, check_out, adults, destination)
    # event_loop = asyncio.new_event_loop()
    # event_loop.run_until_complete(req2(check_in, check_out, adults, destination))

async def a3(query):
    return await req3(query)
# f = asyncio.run(req1("2020-02-15", "2020-02-16", origin_iata, destination_iata))
# print(f)