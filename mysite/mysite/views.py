from django.http import HttpResponse
import datetime


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
