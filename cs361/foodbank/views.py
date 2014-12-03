from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from foodbank.models import Item, Donation

def login(request):
	return render(request,"foodbank/login.html")

class Inventory(ListView):
	model = Item

class DonationCreate(CreateView):
    model = Donation
