from peewee import *

db = SqliteDatabase('basa.db')

class Person(Model):
    name = CharField()
    password = CharField()
    email = CharField()
    class Meta:
        database = db

class Session(Model):
    person = IntegerField()
    access_key = CharField()
    class Meta:
        database = db

class Chat(Model):
    session = IntegerField()
    class Meta:
        database = db

class Messages(Model):
    chat = IntegerField()
    text = CharField()
    datetime = CharField()
    tour = IntegerField()
    class Meta:
        database = db


class Tour(Model):
    city_home = CharField()
    city_travel = CharField()
    plane_start_in = CharField()
    plane_finish_in = CharField()
    plane_start_out = CharField()
    plane_finish_out = CharField()
    hotel = CharField()
    date_in = CharField()
    date_out = CharField()
    kol_vzr = IntegerField()
    kol_chl = IntegerField()
    class Meta:
        database = db