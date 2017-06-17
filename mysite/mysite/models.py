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
	days_available = models.CharField(max_length=128)
	times_available = models.CharField(max_length=128)

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=200)
	pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Prescription(models.Model):
	refills = models.IntegerField(default=0)
	dosage = models.CharField(max_length=128)
	warnings = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Event(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.CharField(max_length=128)
	start_time = models.CharField(max_length=128)
	end_time = models.CharField(max_length=128)
	event_name = models.CharField(max_length=128)