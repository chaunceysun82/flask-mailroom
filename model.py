import os

from peewee import Model, CharField, IntegerField, ForeignKeyField
from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class Donor(Model):
    name = CharField(max_length=255, primary_key=True)

    class Meta:
        database = db


class Donation(Model):
    value = IntegerField()
    donor = ForeignKeyField(Donor, backref='donations')

    class Meta:
        database = db


class Admin(Model):
    user = CharField(max_length=255, primary_key=True, unique=True)
    password = CharField(max_length=255)

    class Meta:
        database = db
