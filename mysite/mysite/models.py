from mongoengine import *
from django.db import models

class Pharmacy(models.Model):
	pharmacy_id = models.AutoField(primary_key=True)
	address = models.CharField(max_length=200)
	name = models.CharField(max_length=128)

class Doctor(models.Model):
	doctor_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=200)
	specialty = models.CharField(max_length=128)

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=200)
	pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
	doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Prescription(models.Model):
	refills = models.IntegerField(default=0)
	dosage = models.CharField(max_length=128)
	warnings = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Event(models.Model):
	doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.CharField(max_length=128)
	time = models.CharField(max_length=128)