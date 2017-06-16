from django.http import HttpResponse
import datetime
from models import *

def index(request):
	return HttpResponse("Hello from Apollo Health.")

'''
def populate_db(request):
	# Populate with Pharmacies.
	P1 = Pharmacy(address="300 W 19 Terrace, Kansas City, MO 64108", name="Walgreens Pharmacy")
	P1.save()

	P2 = Pharmacy(address="241 Linwood Blvd, Kansas City, MO 64111", name="Costco Pharmacy")
	P2.save()

	P3 = Pharmacy(address="3537 Broadway, Kansas City, MO 64111", name="Walgreens Pharmacy")
	P3.save()

	P4 = Pharmacy(address="3801 Independence Ave, Kansas City, MO 64124", name="Spalitto's Pharmacy")
	P4.save()

	P5 = Pharmacy(address="712 Westport Rd, Kansas City, MO 64111", name="Triad")
	P5.save()

	P6 = Pharmacy(address="4240 SW Trafficway, Kansas City, MO 64111", name="Rockhill Pharmacy")
	P6.save()

	# Populate with Doctors.
	D1 = Doctor(name="Doctor Seuss", address="2301 Holmes St, Kansas City, MO 64108", specialty="General", days_available="M-W-F", times_available="8:00:00-7:00:00")
	D1.save()

	D2 = Doctor(name="Doctor Miranda Bailey", address="6420 Prospect Ave #102, Kansas City, MO 64131", specialty="General", days_available="M-T-W-F", times_available="9:00:00-5:00:00")
	D2.save()

	D3 = Doctor(name="Doctor John Dorian", address="4320 Wornall Rd #610, Kansas City, MO 64111", specialty="General", days_available="M-T-W-TH-F", times_available="9:00:00-4:30:00")
	D3.save()

	# Populate with Users.
	U1 = User(name="John Doe", address="2401 Troost Ave, Kansas City, MO 64108", pharmacy=P1, doctor_id=D3)
	U1.save()

	U2 = User(name="Jane Doe", address="10236 Marion Park Dr, Kansas City, MO 64137", pharmacy=P6, doctor_id=D2)
	U2.save()

	# Populate with Prescriptions.
	S1 = Prescription(refills=4, dosage="5 mg", warnings="None.", name="Advil", user_id=U1)
	S1.save()

	# Populate with Events.
	E1 = Event(doctor_id= D3, user_id=U1, date="06/31/2017", time="09:30:00")
	E1.save()
	return HttpResponse("DB populated.")
'''

'''
Effects: Gets the schedule for a given doctor and patient.
Input: json object with doctor id and patient id. 
		{
			"doctor":"doctor_id",
			"user":"user_id"
		}
Output: json object with two arrays, one for doctor and one for patient.
		{
			"doctor_schedule": [
				{
					"date": "00/00/0000",
					"time": "00:00:00"
				}
			],
			"patient_schedule": [
				{
					"date": "00/00/0000",
					"time": "00:00:00",
					"event_name": "name"
				}
			]
		}
'''
def get_total_schedule(request):
	return 0

'''
Gets the schedule for a given patient.
Input: json object patient id. 
		{
			"user":"user_id"
		}
Output: json object with one array for patient schedule.
		{
			"patient_schedule": [
				{
					"date": "00/00/0000",
					"time": "00:00:00"
				}
			]
		}
'''
def get_patient_schedule(request):
	return 0

'''
Gets the schedule for a given doctor.
Input: json object patient id. 
		{
			"doctor":"doctor_id"
		}
Output: json object with one array for patient schedule.
		{
			"doctor_schedule": [
				{
					"date": "00/00/0000",
					"time": "00:00:00"
				}
			]
		}
'''
def get_doctor_schedule(request):
	return 0

'''
Queries every table for the given word and returns all matching things.
Input: json object containing the word being queried for.
		{
			"word": "this"
		}
Output: json object containing arrays for possible matches.
		{
			"doctors": [
				{
					"name": "John Doe",
					"id": "1234",
					"location": 
						{
							"lat:": "42.00",
							"long": "42.00"
						},
					"address": "123 Main St., Kansas City, MO 64108"
				}
			],
			"medications": [
				{
					"name": "Advil",
					"price": "13.99",
					"id": "1234"
				}
			],
			"pharmacies": [
				{
					"name": "KC CVS",
					"id": "1234",
					"location":
						{
							"lat:": "42.00",
							"long": "42.00"
						},
					"address": "123 Main St., Kansas City, MO 64108"
				}
			]
		}
'''
def get_word(request):
	return 0

'''
Takes in an address and returns the latitiude, longitude of the address.
Input: json object of an address.
		{
			"address": "123 Main St., Kansas City, MO 64108"
		}
Output: json object of latitude and longitude.
		{
			"latitude": "42.00",
			"longitude": "42.00"
		}
'''
def get_lat_long(request):
	return 0
