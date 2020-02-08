from sanic.response import json
import uuid
from models import *
import datetime



def access_control(func):
     def control(request, *args, **kwargs):
         access_key = request.json["access_key"]
         session = session.get_or_none(access_key = access_key)
         if session != None:
            person = Person.get_or_none(id = session.person)
            if person != None:
                func(request, person)
     return control

async def test2(request):
    print("dadaa")
    # return "access_token"
    access_token = uuid.uuid4()
    print(access_token)
    return json({"access_token": "kamol_lox"})

async def sign_in(request):
    data = request.json
    person = Person.get_or_none(Person.name == data['name'])
    if (person != None or person.password == data["password"]):
            access_key = uuid.uuid4()
            session = Session(person=person.id,
                              access_key = access_key)
            session.save()
            return json({"access_token": str(access_key),
                         "code":"0"})
    return json({"code": "1"})

async def sign_up(request):
    data = request.json
    name = data["name"]
    password = data["password"]
    email = data["email"]
    person = Person.get_or_none(Person.name == name)
    if person == None:
        person = Person.get_or_none(Person.email == email)
        if person == None:
            person = Person(email = email,
                            name = name,
                            password = password)
            person.save()
            return json({"code":"0"})

    return json({"code":"1"})

async def sign_out(request):
    data = request.json
    person = Person.get_or_none(Person.name == data['name'])
    if (person != None or person.password == data["password"]):
            access_key = uuid.uuid4()
            session = Session(person=person.id,
                              access_key = access_key)
            session.save()
            return json({"access_token": str(access_key)})


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
    date_start = datetime.datetime.strptime(date_start, "%d/%m/%y %H:%M")
    date_finish = date_start + datetime.timedelta(days=int(count_days))
    tours = Tour.select().where(
        Tour.city_home == city_from and Tour.city_travel == city_in and Tour.kol_vzr == int(count_peoples))
    tours = list(tours)
    res = []
    for tour in tours:
        date_start_tour = datetime.datetime.strptime(tour.plane_start_in, "%d/%m/%y %H:%M")
        date_finish_tour = datetime.datetime.strftime(tour.plane_finish_out, "%d/%m/%y %H:%M")
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
    return {"tours": res}


async def get_tours(request):
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
    date_start = datetime.datetime.strptime(date_start, "%d/%m/%y %H:%M")
    date_finish = date_start + datetime.timedelta(days=int(count_days))
    tours = Tour.select().where(Tour.city_home == city_from and Tour.city_travel == city_in and Tour.kol_vzr == int(count_peoples))
    tours = list(tours)
    res = []
    for tour in tours:
        date_start_tour = datetime.datetime.strptime(tour.plane_start_in, "%d/%m/%y %H:%M")
        date_finish_tour = datetime.datetime.strftime(tour.plane_finish_out, "%d/%m/%y %H:%M")
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
    return {"tours":res}