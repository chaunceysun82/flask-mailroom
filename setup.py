import random
from peewee import DoesNotExist
from passlib.hash import pbkdf2_sha256
from model import db, Donor, Donation, Admin

db.connect()
# db.execute_sql('PRAGMA foreign_keys = ON;')

# This line will allow you "upgrade" an existing database by
# dropping all existing tables from it.
db.drop_tables([Donor, Donation, Admin])
#
db.create_tables([Donor, Donation, Admin])

alice = Donor.create(name="Alice")
# alice.save()

bob = Donor.create(name="Bob")
# bob.save()

charlie = Donor.create(name="Charlie")
# charlie.save()

donors = [alice, bob, charlie]

for x in range(30):
    Donation.create(donor=random.choice(donors), value=random.randint(100, 10000))

user1 = Admin.create(user="admin", password=pbkdf2_sha256.hash("password"))
user2 = Admin.create(user="Chauncey", password=pbkdf2_sha256.hash("123456"))


# try:
#     user = Admin.get(Admin.user == 'admin')
# except DoesNotExist:
#     user = None
# print(user)
