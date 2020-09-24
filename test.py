from model import db, Donor, Donation
from peewee import *

name = "Bor"

try:
    donor = Donor.get(name=name)
except DoesNotExist:
    donor = Donor.create(name=name)
Donation.create(donor=donor, value=2000)

print(donor.name)

for donation in Donation.select():
    print(donation.value, donation.donor)
