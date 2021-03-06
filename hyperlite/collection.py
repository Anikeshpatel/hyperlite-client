import json
from .object import Object
from .cursor import Cursor
from .event import Event
from . import generateReadRequestSchema, generateReadByIdRequestSchema, generateReadOneRequestSchema, generateInsertRequestSchema, generateDeleteRequestSchema, generateUpdateRequestSchema
from . import DATABASE


class Collection(object):
    def __init__(self, name: str):
        self.name = name
        self.objects: Cursor

    def insert(self, obj):
        insertSchema = generateInsertRequestSchema()
        insertSchema["Insert"]["data"] = obj
        insertSchema["Insert"]["meta"]["Database"] = DATABASE
        insertSchema["Insert"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(insertSchema))

    def execHyperQl(self, query):
        readSchema = generateReadRequestSchema()
        readSchema["Read"]["meta"]["Query"] = query
        readSchema["Read"]["meta"]["Database"] = DATABASE
        readSchema["Read"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(readSchema))

    def readAll(self):
        readSchema = generateReadRequestSchema()
        readSchema["Read"]["meta"]["Query"] = None
        readSchema["Read"]["meta"]["Database"] = DATABASE
        readSchema["Read"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(readSchema))

    def readOne(self):
        readSchema = generateReadOneRequestSchema()
        readSchema["ReadOne"]["meta"]["Query"] = None
        readSchema["ReadOne"]["meta"]["Database"] = DATABASE
        readSchema["ReadOne"]["meta"]["Collection"] = self.name
        Event.emmit('request', json.dumps(readSchema))

    def readById(self, objectId: str):
        readSchema = generateReadByIdRequestSchema()
        readSchema["ReadById"]["meta"]["Database"] = DATABASE
        readSchema["ReadById"]["meta"]["Collection"] = self.name
        readSchema["ReadById"]["meta"]["id"] = objectId
        Event.emmit('request', json.dumps(readSchema))
