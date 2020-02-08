import aiohttp
import asyncio
import json
import pprint
async def req1():
    async with aiohttp.ClientSession() as session:
        params = {'origin_iata': 'MOW',
                  'destination_iata': 'TYO',
                  'depart_start': '2020-02-05',
                  'return_start': '2020-02-12',
                  'depart_range': "6",
                  'return_range': "6",
                  'need_request': "True", }
        async with session.get('https://s.travel.megafon.ru/price_matrix', params = params) as resp:
            print(resp.status)
            d = json.loads(await resp.text())
            print(json.dumps(d, indent=4))

async def req2():
    async with aiohttp.ClientSession() as session:
        {
            "page": "serp",
            "search_id": "",
            "params": {
                "check_in": "2020-03-29",
                "check_out": "2020-03-31",
                "marker": "171596.70000000000.$1489",
                "currency": "rub",
                "locale": "ru",
                "rooms": [
                    {
                        "adults": 2,
                        "children": []
                    }
                ],
                "locations_ids": [
                    25666
                ],
                "destination": "null",
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
        async with session.post('https://s.travel.megafon.ru/api/wl_search/result',data=b'data') as resp:
            print(resp.status)
            d = json.loads(await resp.text())
            print(json.dumps(d, indent=4))

asyncio.run(req2())

