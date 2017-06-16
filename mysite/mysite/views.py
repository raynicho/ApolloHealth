from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
import googlemaps

import json

def index(request):
	return HttpResponse("Hello from Apollo Health.")

'''
Effects: Gets the schedule for a given doctor and patient.
Input: doctor=<doctor_id>, user=<user_id>
Output: json object with two arrays, one for doctor and one for patient.
		{
			"doctor_schedule": [
				{
					"date": "00/00/0000",
					"start_time": "00:00:00",
					"end_time": "00:00:00"
				}
			],
			"patient_schedule": [
				{
					"date": "00/00/0000",
					"time": "00:00:00",
					"end_time": "00:00:00",
					"event_name": "name"
				}
			]
		}
'''
def get_total_schedule(request):
	return 0

'''
Gets the schedule for a given patient.
Input: user=<user_id>
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
Input: doctor=<doctor_id>
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
Input: word=<this>
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
Input: address=<123 Main St., Kansas City, MO 64108>
Output: json object of latitude and longitude.
		{
			"latitude": "42.00",
			"longitude": "42.00"
		}
'''
# maps api key = AIzaSyCCM6JhqOsTmEemINp5USl0DJ34RgI54yo
def get_lat_long(request):
	address = request.GET.get('address', '')
	gClient = googlemaps.Client(key="AIzaSyCCM6JhqOsTmEemINp5USl0DJ34RgI54yo")
	geocoded = gClient.geocode(address)
	data = {
		"lat": geocoded[0]["geometry"]["location"]["lat"],
		"long": geocoded[0]["geometry"]["location"]["lng"]
	}
	#if geocoded["geometry"] is None:
	#return HttpResponse("Error")
	#lat = geocoded["geometry"]["location"]["lat"]
	return HttpResponse(json.dumps(data), content_type= "application/json")

'''
Handles all CRED requests for pharmacy objects.
Request Types:
	GET (nil): All pharmacies.
	GET (pharmacy_id): Pharmacy with that pharmacy_id.

	PUT (address, name): Creates a pharmacy.

	DELETE (pharmacy_id): Deletes the pharmacy with the given pharmacy_id.

	POST (pharmacy_id, address, name): Edits the pharmacy.
'''
@csrf_exempt
def pharmacy(request):
	# GET 
	if request.method == "GET":
		if request.GET.get('pharmacy_id', '') == '':
			if not Pharmacy.objects.filter().exists():
				return HttpResponse(json.dumps({"error":"No pharmacies found."}), content_type="application/json", status=404)

			obj = Pharmacy.objects.filter()
			pharm_array = []
			for pharm in obj:
				data = {
        			"pharmacy_id": pharm.pharmacy_id,
        			"address": pharm.address,
        			"name":  pharm.name
    			}
    			print data
    			pharm_array.append(data)
			response_data = {
				"pharmacies": pharm_array
			}
			return HttpResponse(json.dumps(response_data), content_type="application/json")
		else:
			pharmacy_id = request.GET.get('pharmacy_id', '')

			if not Pharmacy.objects.filter(pharmacy_id=pharmacy_id).exists():
				return HttpResponse(json.dumps({"error":"No pharmacy found."}), content_type="application/json", status=404)

			obj = Pharmacy.objects.get(pk=pharmacy_id)
			response_data = {
        		"pharmacy_id": pharmacy_id,
        		"address": obj.address,
        		"name":  obj.name
    		}
    		return HttpResponse(json.dumps(response_data), content_type="application/json")
	# PUT
	elif request.method == "PUT":
		return HttpResponse("PUT")
	# DELETE
	elif request.method == "DELETE":
		return HttpResponse("DELETE")
	# POST
	elif request.method == "POST":
		return HttpResponse("POST")
	# UNIDENTIFIED
	return HttpResponse("Unidentified API request method.")


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
	U1 = User(name="John Doe", address="2401 Troost Ave, Kansas City, MO 64108", pharmacy=P1, doctor=D3)
	U1.save()

	U2 = User(name="Jane Doe", address="10236 Marion Park Dr, Kansas City, MO 64137", pharmacy=P6, doctor=D2)
	U2.save()

	# Populate with Prescriptions.
	S1 = Prescription(refills=4, dosage="5 mg", warnings="None.", name="Advil", user=U1)
	S1.save()

	# Populate with Events.
	E1 = Event(doctor= D3, user=U1, date="06/31/2017", start_time="09:30:00", end_time="10:15:00", event_name="Check Up")
	E1.save()
	return HttpResponse("DB populated.")
'''
