import random

from model import db, Donor, Donation 

db.connect()
db.execute_sql('PRAGMA foreign_keys = ON;')

# This line will allow you "upgrade" an existing database by
# dropping all existing tables from it.
db.drop_tables([Donor, Donation])
#
db.create_tables([Donor, Donation])

alice = Donor.create(name="Alice")
# alice.save()

bob = Donor.create(name="Bob")
# bob.save()

charlie = Donor.create(name="Charlie")
# charlie.save()

donors = [alice, bob, charlie]

for x in range(30):
    Donation.create(donor=random.choice(donors), value=random.randint(100, 10000))


