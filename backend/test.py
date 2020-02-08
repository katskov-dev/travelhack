import aiohttp
import asyncio
import json

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
            print(resp.status)
            d = json.loads(await resp.text())

            print(json.dumps(d, indent=4))

    return res


async def req2(check_in, check_out, adults, destination):
    f = open("x.json", 'w')

    async with aiohttp.ClientSession() as session:
        data = {
            "page": "serp",
            "search_id": "",
            "params": {
                "check_in": check_in,#"2020-02-15",
                "check_out": check_out,#"2020-02-16",
                "marker": "171596.70000000000.$1489",
                "currency": "rub",
                "locale": "ru",
                "rooms": [
                    {
                        "adults": adults,#1,
                        "children": []
                    }
                ],
                "locations_ids": [
                    2764
                ],
                "hotels_ids": [],
                "destination": destination,#"Стамбул, Турция ",
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
        data = json.dumps(data).encode()
        print(data)
        async with session.post('https://s.travel.megafon.ru/api/wl_search/result', json=data) as resp:
            print(resp.status)
            d = json.loads(await resp.text())
            print(json.dumps(d, indent =4))
            search_id = d["search_id"]
            loc = []
            for key in d["locations"]:
                loc.append(key)


            stop = d["stop"]
            f.write(json.dumps(d, ))



        print(type(stop))
        for i in range(1):
            if stop != False:
                break
            async with aiohttp.ClientSession() as session:
                data = {
                        "page": "serp",
                        "search_id": search_id,
                        "params": {
                            "check_in": check_in,#"2020-03-29",
                            "check_out": check_out,#"2020-03-31",
                            "marker": "171596.70000000000.$1489",
                            "currency": "rub",
                            "locale": "ru",
                            "rooms": [
                                {
                                    "adults": adults,#2,
                                    "children": []
                                }
                            ],
                            "locations_ids": loc,
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
                        "limit": 100,
                        "offset": 0
                    }

                async with session.post('https://s.travel.megafon.ru/api/wl_search/result', json=data) as resp:
                    print(resp.status)
                    d = json.loads(await resp.text())
                    if not "stop" in d:
                        break
                    stop = d["stop"]
                    f.write(json.dumps(d))
                    # print(stop)
                    print(json.dumps(d, indent=4).encode())

def a1(depart_start, return_start, origin_iata, destination_iata):
    return asyncio.run(req1(depart_start, return_start, origin_iata, destination_iata))
def a2(check_in, check_out, adults, destination):
    return asyncio.run(req2(check_in, check_out, adults, destination))
