import peewee

from main import database


class BaseModel(peewee.Model):
    class Meta:
        database = database
