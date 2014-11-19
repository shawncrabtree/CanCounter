from django.contrib import admin
from foodbank.models import Donor, Donation, Item

admin.site.register(Donor)
admin.site.register(Donation)
admin.site.register(Item)