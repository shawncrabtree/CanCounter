from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from foodbank.models import Item

def index(request):
	return HttpResponse("Hello, world")

class Inventory(ListView):
	model = Item
