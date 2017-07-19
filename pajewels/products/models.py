# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from durationfield.db.models.fields.duration import DurationField

# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=100, default=False)
	primaryImage = models.ImageField(upload_to='products/images/')
	secondaryImage = models.ImageField(upload_to='products/images/')
	additionalImage = models.ImageField(upload_to='products/images/')
   
	def saveProduct(self):
		self.save()

   
  


class SpecialProduct(Product):
	timePeriod = DurationField()
	returnOnInvestment = models.DecimalField(decimal_places=2, max_digits=100, default=False)
	returnOnRefferal = models.DecimalField(decimal_places=2, max_digits=100, default=False)
	
	def saveSpecialProduct(self):
		self.save()    

	