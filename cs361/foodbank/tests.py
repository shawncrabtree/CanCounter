from django.test import TestCase
from foodbank.models import Donor
from foodbank.models import Donation

# Create your tests here.

class InventoryTest(TestCase):
    def setUp(self):
	Donor.objects.create(name="justin", email="lsdfkj@slfjkd.com")
	Donation.objects.create(donor=Donor.objects.get(name="justin"), amount=12, date="2012-11-11 00:00:00")
        Donation.objects.create(donor=Donor.objects.get(name="justin"), amount=14, date="2012-12-12 00:00:00")

    def testFunction(self):
	donor = Donor.objects.get(name="justin")
	donation = Donation.objects.get(amount=14)
	self.assertEquals(donation.donor, donor)

