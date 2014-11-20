from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from foodbank.models import Item

def login(request):
	return render(request,"foodbank/login.html")
	
def hello(request):
	user = User.objects.filter(username=request.GET['username'])
	if check_password(request.GET['password'], user[0].password):
		return HttpResponse("Welcome!")
	else:
		return HttpResponse("Incorrect username or password")

class Inventory(ListView):
	model = Item
