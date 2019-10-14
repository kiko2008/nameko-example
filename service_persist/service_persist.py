from pymongo import MongoClient
from nameko.rpc import rpc
from dynaconf import settings
# import pdb


def get_bd():
    host = settings.HOST
    puerto = settings.PORT
    bbdd = "personas"
    client = MongoClient("mongodb://{}:{}".format(host, puerto))
    return client[bbdd]


class Persons(object):
    name = "persons"
    @rpc
    def save_family(self, name, age):
        bbdd = get_bd()
        # pdb.set_trace()
        result = bbdd.familiares.insert_one({
            "nombre": name,
            "edad": age
        }).inserted_id
