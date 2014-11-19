from django.db import models

class Donor(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)

class Donation(models.Model):
	date = models.DateTimeField()
	amount = models.FloatField(default=0)
	donor = models.ForeignKey(Donor, default=1)

class Item(models.Model):
	name = models.CharField(max_length=50)
	label = models.CharField(max_length=30)
	
	CATEGORIES = (
		('SP', "Soup"),
		('GR', "Grain"),
		('MT', "Meat"),
		('FRUIT', "Fruit"),
		('VEG', "Vegetable"),
		('BEV', "Beverage"),
		('P', "Pasta"),
		('O', "Other"),
	)
	
	UNIT = (
		('OZ', "ounces"),
		('LB', "pounds"),
		('G', "grams"),
		('FL OZ', "fluid ounces"),
		('L', "liter"),
		('G', "gallon"),
		('Q', "quarts"),
		('NA', "unknown"),
	)
	
	category = models.CharField(max_length=5, choices=CATEGORIES, default='O')
	unit = models.CharField(max_length=5, choices=UNIT, default='NA')
	donation = models.ForeignKey(Donation, default=1)


