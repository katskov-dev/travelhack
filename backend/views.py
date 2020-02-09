from sanic.response import json as jsons
import uuid
from models import *
from test import *
import datetime


packages_tours = {}

def fromisoz(time):

    time = str(time).replace('Z', '')
    time = str(time).split('T')[0]
    time = datetime.datetime.strptime(time, "%Y-%m-%d") + datetime.timedelta(hours=12)

    return time



def access_control(func):
    def control(request, *args, **kwargs):
        access_key = request.json["access_key"]
        session = session.get_or_none(access_key=access_key)
        if session != None:
            person = Person.get_or_none(id=session.person)
            if person != None:
                func(request, person)

    return control


async def test2(request):
    print("dadaa")
    # return "access_token"
    access_token = uuid.uuid4()
    print(access_token)
    return jsons({'access_token': ''})


async def sign_in(request):
    data = request.json
    person = Person.get_or_none(Person.name == data['name'])
    if (person != None or person.password == data["password"]):
        access_key = uuid.uuid4()
        session = Session(person=person.id,
                          access_key=access_key)
        session.save()
        return jsons({"access_token": str(access_key),
                      "code": "0"})
    return jsons({"code": "1"})


async def sign_up(request):
    data = request.json
    name = data["name"]
    password = data["password"]
    email = data["email"]
    person = Person.get_or_none(Person.name == name)
    if person == None:
        person = Person.get_or_none(Person.email == email)
        if person == None:
            person = Person(email=email,
                            name=name,
                            password=password)
            person.save()
            return jsons({"code": "0"})

    return jsons({"code": "1"})


async def sign_out(request):
    data = request.json
    person = Person.get_or_none(Person.name == data['name'])
    if (person != None or person.password == data["password"]):
        access_key = uuid.uuid4()
        session = Session(person=person.id,
                          access_key=access_key)
        session.save()
        return jsons({"access_token": str(access_key)})


async def get_tours_by_api(request):
    # {
    #     "date_start": "",
    #     "city_from": "ser@bud.ru",
    #     "city_in": "ser@bud.ru",
    #     "count_days": "123",
    #     "count_peoples": "123"
    # }
    data = request.json
    date_start = data["date_start"]
    city_from = data["city_from"]
    city_in = data["city_in"]
    count_days = data["count_days"]
    count_peoples = data["count_peoples"]
    # date_start = datetime.datetime.strptime(date_start, "%d/%m/%y %H:%M")
    date_start = fromisoz(date_start)
    date_finish = date_start + datetime.timedelta(days=int(count_days))
    tours = Tour.select().where(
        Tour.city_home == city_from and Tour.city_travel == city_in and Tour.kol_vzr == int(count_peoples))
    tours = list(tours)
    res = []
    for tour in tours:
        # date_start_tour = datetime.datetime.strptime(tour.plane_start_in, "%d/%m/%y %H:%M")
        date_start_tour = fromisoz(tour.plane_start_in)

        # date_finish_tour = datetime.datetime.strftime(tour.plane_finish_out, "%d/%m/%y %H:%M")

        date_finish_tour = fromisoz(tour.plane_finish_out)

        if (date_start < date_finish_tour and date_finish > date_finish_tour):
            res.append(
                {
                    "plane_start_in": tour.plane_start_in,
                    "plane_finish_in": tour.plane_finish_in,
                    "plane_start_out": tour.plane_start_out,
                    "plane_finish_out": tour.plane_finish_out,
                    "city_home": tour.city_home,
                    "city_travel": tour.city_travel,
                    "hotel": tour.hotel,
                    "date_in": tour.date_in,
                    "date_out": tour.date_out,
                    "count_peoples": tour.kol_vzr
                }
            )
    return jsons({"tours": res})


async def get_tours(request):
    # {
    #     "date_start": "01/03/20 12:00",
    #     "city_from": "MOW",
    #     "city_in": "TYO",
    #     "count_days": 5,
    #     "count_peoples": "2"
    # }
    hu = 'hu' in request.args
    tu = 'tu' in request.args
    data = request.json
    date_start = data["date_start"]
    city_from = data["city_from"]
    city_in = data["city_in"]
    count_days = data["count_days"]
    count_peoples = data["count_peoples"]
    # date_start = datetime.datetime.strptime(date_start, "%d/%m/%Y %H:%M")

    date_start = fromisoz(date_start)

    date_finish = date_start + datetime.timedelta(days=count_days)
    month = str(date_start.month)
    if len(month) == 1:
        month = "0" + month
    day = str(date_start.day)
    if len(day) == 1:
        day = "0" + day

    date_start = f"{str(date_start.year)}-{month}-{day}"

    month = str(date_finish.month)
    if len(month) == 1:
        month = "0" + month
    day = str(date_finish.day)
    if len(day) == 1:
        day = "0" + day
    date_finish = f"{str(date_finish.year)}-{month}-{day}"

    res0 = await a3(city_in)
    # print(res0)
    res0 = res0[0]
    ids = res0["id"]
    iata_in = res0["iata"]
    iata_in = iata_in[0]

    res01 = await a3(city_from)
    res01 = res01[0]
    iata_from = res01["iata"]
    iata_from = iata_from[0]

    res1 = await a1(date_start, date_finish, iata_from, iata_in)
    res2, hotels_amenties = await a2(date_start, date_finish, count_peoples, ids)
    package_tours = {}
    tours = []
    use_tickets = []
    use_hotels = []

    for hotel in res2:
        # if hu and hotel["id"] in use_hotels:
        #     continue
        for ticket in res1["prices"]:
            uuiid = str(uuid.uuid4())

        #     if tu and ticket in use_tickets:
        #         continue
            if int(hotel["median_minprice"]) != 0:
                photos_ids = []
                for photos_id in hotel["photos_ids"]:
                    photos_ids.append(f"https://photo.hotellook.com/image_v2/crop/{photos_id}/620/400.auto")
                amenties = []
                for amenty in hotel["amenities"]:
                    amenties.append(hotels_amenties[str(amenty)])
                tour = {

                    "id": uuiid,
                    "sum": ticket["value"]*int(count_peoples) + hotel["median_minprice"] * 70 * int(count_peoples) * int(count_days),

                    "ticket":
                        {
                            "origin_iata": iata_from,
                            "dest_iata": iata_in,
                            "depart_date": ticket["depart_date"],
                            "return_date": ticket["return_date"],
                            "value": ticket["value"],
                            "num_of_changes": ticket["number_of_changes"]
                        },
                    "hotel":
                        {
                            "distance_to_center": hotel["distance_to_center"],
                            "address": hotel["address"],
                            "name": hotel["name"],
                            "location_id": hotel["location_id"],
                            "photos_urls": photos_ids,
                            "median_price": hotel["median_minprice"],
                            "rating": hotel["rating"],
                            "stars": hotel["stars"],
                            "location": hotel["location"],
                            "id": hotel["id"],
                            "popularity": hotel["popularity"],
                            "amenities": amenties
                        }
                }
            package_tours[uuiid] = tour
            tours.append(tour)
            if hu:
                break
    uuiid = str(uuid.uuid4())
    print(uuiid)
    packages_tours[uuiid] = package_tours
    return jsons({
        "id": uuiid,
        "tours": tours
    })
    # return jsons({
    #                "id": str(uuiid),
    #                "tours": tours
    #               })



async def get_package(request, package):
    return jsons(packages_tours[package])



async def get_package_tour(request, package, tour):
    return jsons(packages_tours[package][tour])

