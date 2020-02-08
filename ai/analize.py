import ujson
import datetime

data = ujson.loads(open('users.json', 'r').read())
user_checked = []
analized = {}
print(data["users"][0])
for user in data["users"]:
    id = user["id"]
    ### COUNTRIES
    if not id in analized:
        analized[id] = {
            "countries": {}
        }

    countries = user["countries_in_trip"]
    if isinstance(countries, int):
        countries = [countries]
    else:
        countries = list(map(int, countries.split('; ')))

    for country in countries:
        code = country
        if not code in analized[id]["countries"]:
            analized[id]["countries"][code] = 0
        analized[id]["countries"][code] += 1
    code = user["trip_main_country"]
    if not code in analized[id]["countries"]:
        analized[id]["countries"][code] = 0
    analized[id]["countries"][code] += 1
    if "" in analized[id]["countries"]:
        del analized[id]["countries"][""]

    ### DATES
    if not "dates" in analized[id]:
        analized[id]["dates"] = []
    start_trip = user["start_trip"]
    start_trip = datetime.date.fromtimestamp(start_trip)
    end_trip = user["end_trip"]
    end_trip = datetime.date.fromtimestamp(end_trip)
    trip_dates = (start_trip.day, start_trip.month, end_trip.day, end_trip.month)
    if not trip_dates in analized[id]["dates"]:
        analized[id]["dates"].append(trip_dates)


    ## PRICE_LEVEL
    # level 1:  < 35k
    # level 2:  < 50k
    # level 3:  < 100k
    # level 4:  > 100k

    arpu_level = 1
    arpu = int(user["arpu_m3"])
    if arpu < 1500:
        arpu_level = 1
    elif arpu < 3000:
        arpu_level = 2
    elif arpu < 6000:
        arpu_level = 3
    else:
        arpu_level = 4

with open('analized.json', 'w') as f:
    f.write(ujson.dumps(analized))
