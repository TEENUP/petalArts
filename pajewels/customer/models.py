# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from products.models import Product
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


# Create your models here.

class User(models.Model):
	firstName= models.CharField(max_length=100,default="Blank")
	lastName=models.CharField(max_length=100,default="Blank")
	phoneNo = PhoneNumberField()
	password = models.CharField(max_length=1000,blank=True)
	address = models.TextField()
	joiningDate = models.DateTimeField(default=timezone.now,blank=True)
	email = models.EmailField()

	def saveDetails(self):
		# self.published_date = timezone.now()
		self.save()

class UserAccount(models.Model):
	userId = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
	accountNo = models.CharField(max_length=200)
	IFSCCode = models.CharField(max_length=200)
	accountHolderName = models.CharField(max_length=100)
	bankName = models.CharField(max_length=200)
	branchName = models.CharField(max_length=200,default="Blank")
	accountType = models.BooleanField()
	panNo = models.CharField(max_length=200,default="Blank")
	aadhaarNo = models.CharField(max_length=200,default="Blank")
	panCard = models.BinaryField(default="Blank")
	aadhaarCard = models.BinaryField(default="Blank")
	photo = models.BinaryField(default="Blank")

	def saveAccountDetails(self):
		# self.published_date = timezone.now()
		self.save()

class UserRelation(models.Model):
	sponserId = models.CharField(max_length=10)
	parentId = models.CharField(max_length=10)
	userId = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
	productId = models.ForeignKey(Product, on_delete=models.CASCADE, default=False)

	def saveRelation(self):
		# self.published_date = timezone.now()
		self.save()
