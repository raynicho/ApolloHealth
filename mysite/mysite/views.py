from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import *
import copy
import json

def index(request):
	return HttpResponse("Hello from Apollo Health.")

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
def get_lat_long(request):
	return 0

'''
Handles getting pharmacies.
Request Types:
	GET (nil): All pharmacies.
	GET (pharmacy_id): Pharmacy with that pharmacy_id.
'''
@csrf_exempt
def get_pharmacy(request):
	if request.GET.get('pharmacy_id', '') == '':
		if not Pharmacy.objects.filter().exists():
			return HttpResponse(json.dumps({"error":"No pharmacies found."}), content_type="application/json", status=404)

		pharm_array = []
		i = -1
		for obj in Pharmacy.objects.all():
			i += 1
			pharm_array.append({
				"pharmacy_id": obj.pharmacy_id,
				"address": obj.address,
				"name":  obj.name,
				"long": str(obj.lon),
				"lat": str(obj.lat),
				"phone": obj.phone,
				"rating": str(obj.rating)
			})
		response_data = {
			"pharmacies": pharm_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		pharmacy_id = request.GET.get('pharmacy_id', '')

		if not Pharmacy.objects.filter(pk=pharmacy_id).exists():
			return HttpResponse(json.dumps({"error":"No pharmacy found."}), content_type="application/json", status=404)

		obj = Pharmacy.objects.get(pk=pharmacy_id)
		response_data = {
			"pharmacy_id": pharmacy_id,
			"address": obj.address,
			"name":  obj.name,
			"long": str(obj.lon),
			"lat": str(obj.lat),
			"phone": obj.phone,
			"rating": str(obj.rating)
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	return HttpResponse("Unidentified API request method or input parameters.")

'''
Handles creating pharmacies.
Request Types:
	GET (address, name): Creates a pharmacy.
'''
@csrf_exempt
def create_pharmacy(request):
	if request.GET.get('name', '') == '' or request.GET.get('address', '') == '' or request.GET.get('lon', '') == '' or request.GET.get('lat', '') == '' or request.GET.get('phone', '') == '' or request.GET.get('rating', '') == '':
		return HttpResponse(json.dumps({"error":"Missing name and/or address params."}), content_type="application/json", status=400)
	elif request.GET.get('address', '') != '' and request.GET.get('name', '') != '':
		P = Pharmacy(address=request.GET.get('address', ''), name=request.GET.get('name', ''), lon=request.GET.get('lon', ''), lat=request.GET.get('lat', ''), phone=request.GET.get('phone', ''), rating=request.GET.get('rating', '') == '')
		P.save()

		return HttpResponse(json.dumps({"status":"Pharmacy created."}), content_type="application/json")
	return HttpResponse("Unidentified API request method or input parameters.")

'''
Handles editing pharmacies.
Request Types:
	GET (pharmacy_id, address, name): Edits a pharmacy.
'''
@csrf_exempt
def edit_pharmacy(request):
	if request.GET.get('pharmacy_id', '') == '' or request.GET.get('name', '') == '' or request.GET.get('address', '') == '':
		return HttpResponse(json.dumps({"error":"One or more parameters mssing."}), content_type="application/json", status=400)
	
	pharmacy_id = request.GET.get('pharmacy_id', '')
	if not Pharmacy.objects.filter(pk=pharmacy_id).exists():
		return HttpResponse(json.dumps({"error":"No pharmacy found."}), content_type="application/json", status=404)

	Pharmacy.objects.filter(pk=pharmacy_id).update(address=request.GET.get('address', ''), name=request.GET.get('name', ''))
	return HttpResponse(json.dumps({"status":"Pharmacy updated."}), content_type="application/json")

'''
Handles deleting pharmacies.
Request Types:
	GET (pharmacy_id): Deletes a pharmacy.
'''
@csrf_exempt
def delete_pharmacy(request):
	if request.GET.get('pharmacy_id', '') == '':
		return HttpResponse(json.dumps({"error":"No parameters entered."}), content_type="application/json", status=400)
	pharmacy_id = request.GET.get('pharmacy_id', '')
	if not Pharmacy.objects.filter(pk=pharmacy_id).exists():
		return HttpResponse(json.dumps({"error":"No pharmacy found."}), content_type="application/json", status=404)

	Pharmacy.objects.filter(pk=pharmacy_id).delete()
	return HttpResponse(json.dumps({"status":"Pharmacy deleted."}), content_type="application/json")

'''
Handles getting doctors.
Request Types:
	GET (nil): All doctors.
	GET (pharmacy_id): Doctor with that doctor_id.
'''
@csrf_exempt
def get_doctor(request):
	if request.GET.get('doctor_id', '') == '' and request.GET.get('specialty', '') == '':
		if not Doctor.objects.filter().exists():
			return HttpResponse(json.dumps({"error":"No doctors found."}), content_type="application/json", status=404)

		doc_array = []
		i = -1
		for doc in Doctor.objects.all():
			i += 1
			doc_array.append({
				"doctor_id": doc.doctor_id,
				"address": doc.address,
				"name": doc.name,
				"specialty": doc.specialty,
				"days_available": doc.days_available,
				"times_available": doc.times_available,
				"lon": str(doc.lon),
				"lat": str(doc.lat)
			})
		response_data = {
			"doctors": doc_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif request.GET.get('specialty', '') != '':
		doc_array = []
		i = -1
		for doc in Doctor.objects.filter(specialty=request.GET.get('specialty', '')):
			i += 1
			doc_array.append({
				"doctor_id": doc.doctor_id,
				"address": doc.address,
				"name": doc.name,
				"specialty": doc.specialty,
				"days_available": doc.days_available,
				"times_available": doc.times_available,
				"lon": str(doc.lon),
				"lat": str(doc.lat)
			})
		response_data = {
			"doctors": doc_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		doctor_id = request.GET.get('doctor_id', '')

		if not Doctor.objects.filter(pk=doctor_id).exists():
			return HttpResponse(json.dumps({"error":"No doctor found."}), content_type="application/json", status=404)

		doc = Doctor.objects.get(pk=doctor_id)
		response_data = {
			"doctor_id": doc.doctor_id,
			"address": doc.address,
			"name": doc.name,
			"specialty": doc.specialty,
			"days_available": doc.days_available,
			"times_available": doc.times_available,
			"lon": str(doc.lon),
			"lat": str(doc.lat)
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	return HttpResponse("Unidentified API request method or input parameters.")

'''
Handles creating doctors.
Request Types:
	GET (address, name, specialty, days_available, times_available, lon, lat): Creates a doctor.
'''
@csrf_exempt
def create_doctor(request):
	if request.GET.get('lon', '') == '' or request.GET.get('lat', '') == '' or request.GET.get('name', '') == '' or request.GET.get('address', '') == '' or request.GET.get('specialty', '') == '' or request.GET.get('times_available', '') == '' or request.GET.get('days_available', '') == '':
		return HttpResponse(json.dumps({"error":"Missing params."}), content_type="application/json", status=400)
	
	D = Doctor(address=request.GET.get('address', ''), name=request.GET.get('name', ''), specialty=request.GET.get('specialty', ''), times_available=request.GET.get('times_available', ''), days_available=request.GET.get('days_available', ''), lon=request.GET.get('lon', ''), lat=request.GET.get('lat', ''))
	D.save()

	return HttpResponse(json.dumps({"status":"Doctor created."}), content_type="application/json")

'''
Handles editing doctors.
Request Types:
	GET (pharmacy_id, address, name): Edits a doctor.
'''
@csrf_exempt
def edit_doctor(request):
	if request.GET.get('name', '') == '' or request.GET.get('address', '') == '' or request.GET.get('specialty', '') == '' or request.GET.get('times_available', '') == '' or request.GET.get('days_available', '') == '' or request.GET.get('doctor_id', '') == '':
		return HttpResponse(json.dumps({"error":"One or more parameters mssing."}), content_type="application/json", status=400)
	
	doctor_id = request.GET.get('doctor_id', '')
	if not Doctor.objects.filter(pk=doctor_id).exists():
		return HttpResponse(json.dumps({"error":"No doctor found."}), content_type="application/json", status=404)

	Doctor.objects.filter(pk=doctor_id).update(address=request.GET.get('address', ''), name=request.GET.get('name', ''), specialty=request.GET.get('specialty', ''), times_available=request.GET.get('times_available', ''), days_available=request.GET.get('days_available', ''))
	return HttpResponse(json.dumps({"status":"Doctor updated."}), content_type="application/json")

'''
Handles deleting doctors.
Request Types:
	GET (doctor_id): Deletes a doctor.
'''
@csrf_exempt
def delete_doctor(request):
	if request.GET.get('doctor_id', '') == '':
		return HttpResponse(json.dumps({"error":"No parameters entered."}), content_type="application/json", status=400)
	doctor_id = request.GET.get('doctor_id', '')
	if not Doctor.objects.filter(pk=doctor_id).exists():
		return HttpResponse(json.dumps({"error":"No doctor found."}), content_type="application/json", status=404)

	Doctor.objects.filter(pk=doctor_id).delete()
	return HttpResponse(json.dumps({"status":"Doctor deleted."}), content_type="application/json")

'''
Handles getting users.
Request Types:
	GET (nil): All users.
	GET (user_id): User with that user_id.
'''
@csrf_exempt
def get_user(request):
	if request.GET.get('user_id', '') == '':
		if not User.objects.filter().exists():
			return HttpResponse(json.dumps({"error":"No users found."}), content_type="application/json", status=404)

		user_array = []
		i = -1
		for user in User.objects.all():
			i += 1
			user_array.append({
				"user_id": user.user_id,
				"address": user.address,
				"name": user.name,
				"user_pharmacy": user.pharmacy.pharmacy_id,
				"user_doctor": user.doctor_id
			})
		response_data = {
			"users": user_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		user_id = request.GET.get('user_id', '')

		if not User.objects.filter(pk=user_id).exists():
			return HttpResponse(json.dumps({"error":"No user found."}), content_type="application/json", status=404)

		user = User.objects.get(pk=user_id)
		response_data = {
			"user_id": user.user_id,
			"address": user.address,
			"name": user.name,
			"user_pharmacy": user.pharmacy.pharmacy_id,
			"user_doctor": user.doctor_id
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	return HttpResponse("Unidentified API request method or input parameters.")

'''
Handles creating users.
Request Types:
	GET (address, name, pharmacy, doctor): Creates a user.
'''
@csrf_exempt
def create_user(request):
	if request.GET.get('name', '') == '' or request.GET.get('address', '') == '' or request.GET.get('pharmacy_id', '') == '' or request.GET.get('doctor_id', '') == '':
		return HttpResponse(json.dumps({"error":"Missing params."}), content_type="application/json", status=400)
	
	U = User(address=request.GET.get('address', ''), name=request.GET.get('name', ''), doctor_id=request.GET.get('doctor_id', ''), pharmacy_id=request.GET.get('pharmacy_id', ''))
	U.save()

	return HttpResponse(json.dumps({"status":"User created."}), content_type="application/json")

'''
Handles editing user.
Request Types:
	GET (user_id, address, name, pharmacy_id, doctor_id): Edits a user.
'''
@csrf_exempt
def edit_user(request):
	if request.GET.get('user_id', '') == '' or request.GET.get('name', '') == '' or request.GET.get('address', '') == '' or request.GET.get('pharmacy_id', '') == '' or request.GET.get('doctor_id', '') == '':
		return HttpResponse(json.dumps({"error":"One or more parameters mssing."}), content_type="application/json", status=400)
	
	user_id = request.GET.get('user_id', '')
	if not User.objects.filter(pk=user_id).exists():
		return HttpResponse(json.dumps({"error":"No users found."}), content_type="application/json", status=404)

	User.objects.filter(pk=user_id).update(address=request.GET.get('address', ''), name=request.GET.get('name', ''), doctor=request.GET.get('doctor_id', ''), pharmacy=request.GET.get('pharmacy_id', ''))
	return HttpResponse(json.dumps({"status":"User updated."}), content_type="application/json")

'''
Handles deleting users.
Request Types:
	GET (user_id): Deletes a user.
'''
@csrf_exempt
def delete_user(request):
	if request.GET.get('user_id', '') == '':
		return HttpResponse(json.dumps({"error":"No parameters entered."}), content_type="application/json", status=400)
	user_id = request.GET.get('user_id', '')
	if not User.objects.filter(pk=user_id).exists():
		return HttpResponse(json.dumps({"error":"No user found."}), content_type="application/json", status=404)

	User.objects.filter(pk=user_id).delete()
	return HttpResponse(json.dumps({"status":"User deleted."}), content_type="application/json")

'''
Handles getting prescriptions.
Request Types:
	GET (nil): All prescriptions.
	GET (user_id): Prescription with that user_id.
	GET (prescription_id): Prescription with that prescription_id.
'''
@csrf_exempt
def get_script(request):
	if request.GET.get('prescription_id', '') == '' and request.GET.get('user_id', '') == '':
		if not Prescription.objects.filter().exists():
			return HttpResponse(json.dumps({"error":"No presscriptions found."}), content_type="application/json", status=404)

		script_array = []
		i = -1
		for script in Prescription.objects.all():
			i += 1
			script_array.append({
				"user_id": script.user_id,
				"refills": script.refills,
				"name": script.name,
				"dosage": script.dosage,
				"warnings": script.warnings,
				"prescription_id": script.id
			})
		response_data = {
			"prescriptions": script_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif request.GET.get('prescription_id', '') != '':
		script_id = request.GET.get('prescription_id', '')

		if not Prescription.objects.filter(pk=script_id).exists():
			return HttpResponse(json.dumps({"error":"No prescriptions found."}), content_type="application/json", status=404)

		script = Prescription.objects.get(pk=script_id)
		response_data = {
			"user_id": script.user_id,
			"refills": script.refills,
			"name": script.name,
			"dosage": script.dosage,
			"warnings": script.warnings,
			"prescription_id": script.id
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif request.GET.get('user_id', '') != '':
		user_id = request.GET.get('user_id', '')

		if not Prescription.objects.filter(user=user_id).exists():
			return HttpResponse(json.dumps({"error":"No prescriptions found."}), content_type="application/json", status=404)

		script_array = []
		i = -1
		for script in Prescription.objects.filter(user=user_id):
			i += 1
			script_array.append({
				"user_id": script.user_id,
				"refills": script.refills,
				"name": script.name,
				"dosage": script.dosage,
				"warnings": script.warnings,
				"prescription_id": script.id
			})
		response_data = {
			"prescriptions": script_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	return HttpResponse("Unidentified API request method or input parameters.")

'''
Handles creating scripts.
Request Types:
	GET (user_id, name, refills, dosage, warnings): Creates a script.
'''
@csrf_exempt
def create_script(request):
	if request.GET.get('name', '') == '' or request.GET.get('user_id', '') == '' or request.GET.get('refills', '') == '' or request.GET.get('dosage', '') == '' or request.GET.get('warnings', '') == '':
		return HttpResponse(json.dumps({"error":"Missing params."}), content_type="application/json", status=400)
	
	P = Prescription(user_id=request.GET.get('user_id', ''), name=request.GET.get('name', ''), refills=request.GET.get('refills', ''), dosage=request.GET.get('dosage', ''), warnings=request.GET.get('warnings', ''))
	P.save()

	return HttpResponse(json.dumps({"status":"Prescription created."}), content_type="application/json")

'''
Handles editing script.
Request Types:
	GET (prescription_id, user_id, name, refills, dosage, warnings): Edits a script.
'''
@csrf_exempt
def edit_script(request):
	if request.GET.get('prescription_id', '') == '' or request.GET.get('name', '') == '' or request.GET.get('user_id', '') == '' or request.GET.get('refills', '') == '' or request.GET.get('dosage', '') == '' or request.GET.get('warnings', '') == '':
		return HttpResponse(json.dumps({"error":"One or more parameters mssing."}), content_type="application/json", status=400)
	
	prescription_id = request.GET.get('prescription_id', '')
	if not Prescription.objects.filter(pk=prescription_id).exists():
		return HttpResponse(json.dumps({"error":"No scripts found."}), content_type="application/json", status=404)

	Prescription.objects.filter(pk=prescription_id).update(user=request.GET.get('user_id', ''), name=request.GET.get('name', ''), refills=request.GET.get('refills', ''), dosage=request.GET.get('dosage', ''), warnings=request.GET.get('warnings', ''))
	return HttpResponse(json.dumps({"status":"Script updated."}), content_type="application/json")

'''
Handles deleting prescriptions.
Request Types:
	GET (prescription_id): Deletes a prescription.
'''
@csrf_exempt
def delete_script(request):
	if request.GET.get('prescription_id', '') == '':
		return HttpResponse(json.dumps({"error":"No parameters entered."}), content_type="application/json", status=400)
	script_id = request.GET.get('prescription_id', '')
	if not Prescription.objects.filter(pk=script_id).exists():
		return HttpResponse(json.dumps({"error":"No scripts found."}), content_type="application/json", status=404)

	Prescription.objects.filter(pk=script_id).delete()
	return HttpResponse(json.dumps({"status":"Script deleted."}), content_type="application/json")

'''
Handles getting events.
Request Types:
	GET (nil): All events.
	GET (event_id): Event with that event_id.
	GET (doctor_id): All events for that doctor.
	GET (user_id): All events for that user.
	GET (doctor_id, user_id): All events for that doctor and all events for that user.
'''
@csrf_exempt
def get_event(request):
	if request.GET.get('event_id', '') == '' and request.GET.get('doctor_id', '') == '' and request.GET.get('user_id', '') == '':
		if not Event.objects.filter().exists():
			return HttpResponse(json.dumps({"events":[]}), content_type="application/json", status=200)

		event_array = []
		for event in Event.objects.all():
			event_array.append({
				"doctor_id": event.doctor_id,
				"user_id": event.user_id,
				"date": event.date,
				"start_time": event.start_time,
				"end_time": event.end_time,
				"name": event.event_name,
				"event_id": event.id
			})
		response_data = {
			"events": event_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif request.GET.get('doctor_id', '') != '' and request.GET.get('user_id', '') != '':
		doc_array = []
		for event in Event.objects.filter(doctor_id=request.GET.get('doctor_id', '')):
			doc_array.append({
				"doctor_id": event.doctor_id,
				"user_id": event.user_id,
				"date": event.date,
				"start_time": event.start_time,
				"end_time": event.end_time,
				"name": event.event_name,
				"event_id": event.id
			})

		user_array = []
		for event in Event.objects.filter(user_id=request.GET.get('user_id', '')):
			user_array.append({
				"doctor_id": event.doctor_id,
				"user_id": event.user_id,
				"date": event.date,
				"start_time": event.start_time,
				"end_time": event.end_time,
				"name": event.event_name,
				"event_id": event.id
			})

		response_data = {
			"doctor_events": doc_array,
			"user_events": user_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif request.GET.get('doctor_id', '') != '':
		doc_array = []
		for event in Event.objects.filter(doctor_id=request.GET.get('doctor_id', '')):
			doc_array.append({
				"doctor_id": event.doctor_id,
				"user_id": event.user_id,
				"date": event.date,
				"start_time": event.start_time,
				"end_time": event.end_time,
				"name": event.event_name,
				"event_id": event.id
			})
		response_data = {
			"doctor_events": doc_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif request.GET.get('user_id', '') != '':
		user_array = []
		for event in Event.objects.filter(user_id=request.GET.get('user_id', '')):
			user_array.append({
				"doctor_id": event.doctor_id,
				"user_id": event.user_id,
				"date": event.date,
				"start_time": event.start_time,
				"end_time": event.end_time,
				"name": event.event_name,
				"event_id": event.id
			})

		response_data = {
			"user_events": user_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		event_id = request.GET.get('event_id', '')

		if not Event.objects.filter(pk=event_id).exists():
			return HttpResponse(json.dumps({"error":"No event found."}), content_type="application/json", status=404)

		event = Event.objects.get(pk=event_id)
		response_data = {
			"doctor_id": event.doctor_id,
				"user_id": event.user_id,
				"date": event.date,
				"start_time": event.start_time,
				"end_time": event.end_time,
				"name": event.event_name,
				"event_id": event.id
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	return HttpResponse("Unidentified API request method or input parameters.")

'''
Handles creating events.
Request Types:
	GET (user_id, name, doctor_id, date, start_time, end_time): Creates an event.
'''
@csrf_exempt
def create_event(request):
	if request.GET.get('doctor_id', '') == '' or request.GET.get('user_id', '') == '' or request.GET.get('date', '') == '' or request.GET.get('start_time', '') == '' or request.GET.get('end_time', '') == '' or request.GET.get('name', '') == '':
		return HttpResponse(json.dumps({"error":"Missing params."}), content_type="application/json", status=400)
	
	E = Event(user_id=request.GET.get('user_id', ''), event_name=request.GET.get('name', ''), doctor_id=request.GET.get('doctor_id', ''), date=request.GET.get('date', ''), start_time=request.GET.get('start_time', ''), end_time=request.GET.get('end_time', ''))
	E.save()

	return HttpResponse(json.dumps({"status":"Event created."}), content_type="application/json")

'''
Handles editing events.
Request Types:
	GET (event_id, user_id, name, doctor_id, date, start_time, end_time): Edits an event.
'''
@csrf_exempt
def edit_event(request):
	if request.GET.get('event_id', '') == '' or request.GET.get('doctor_id', '') == '' or request.GET.get('user_id', '') == '' or request.GET.get('date', '') == '' or request.GET.get('start_time', '') == '' or request.GET.get('end_time', '') == '' or request.GET.get('name', '') == '':
		return HttpResponse(json.dumps({"error":"One or more parameters mssing."}), content_type="application/json", status=400)
	
	event_id = request.GET.get('event_id', '')
	if not Event.objects.filter(pk=event_id).exists():
		return HttpResponse(json.dumps({"error":"No events found."}), content_type="application/json", status=404)

	Event.objects.filter(pk=event_id).update(user=request.GET.get('user_id', ''), event_name=request.GET.get('name', ''), doctor=request.GET.get('doctor_id', ''), date=request.GET.get('date', ''), start_time=request.GET.get('start_time', ''), end_time=request.GET.get('end_time', ''))
	return HttpResponse(json.dumps({"status":"Event updated."}), content_type="application/json")

'''
Handles deleting an event.
Request Types:
	GET (event_id): Deletes an event.
'''
@csrf_exempt
def delete_event(request):
	if request.GET.get('event_id', '') == '':
		return HttpResponse(json.dumps({"error":"No parameters entered."}), content_type="application/json", status=400)
	event_id = request.GET.get('event_id', '')
	if not Event.objects.filter(pk=event_id).exists():
		return HttpResponse(json.dumps({"error":"No events found."}), content_type="application/json", status=404)

	Event.objects.filter(pk=event_id).delete()
	return HttpResponse(json.dumps({"status":"Event deleted."}), content_type="application/json")

'''
Handles getting pharmacy events.
Request Types:
	GET (nil): All pharmacy events.
	GET (pharm_event_id): Event with that pharm_event_id.
	GET (user_id): All events for that user.
'''
@csrf_exempt
def get_pharm_event(request):
	if request.GET.get('pharm_event_id', '') == '' and request.GET.get('user_id', '') == '':
		if not PharmacyEvent.objects.filter().exists():
			return HttpResponse(json.dumps({"pharmacy_events":[]}), content_type="application/json", status=200)

		event_array = []
		for event in PharmacyEvent.objects.all():
			event_array.append({
				"pharmacy_id": event.pharmacy_id,
				"user_id": event.user_id,
				"date": event.date,
				"pickup_time": event.pickup_time,
				"name": event.event_name,
				"pharm_event_id": event.pharm_event_id
			})
		response_data = {
			"events": event_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	elif request.GET.get('user_id', '') != '':
		event_array = []
		for event in PharmacyEvent.objects.filter(user_id=request.GET.get('user_id', '')):
			event_array.append({
				"pharmacy_id": event.pharmacy_id,
				"user_id": event.user_id,
				"date": event.date,
				"pickup_time": event.pickup_time,
				"name": event.event_name,
				"pharm_event_id": event.pharm_event_id
			})
		response_data = {
			"pharmacy_events": event_array
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		event_id = request.GET.get('pharm_event_id', '')

		if not PharmacyEvent.objects.filter(pk=event_id).exists():
			return HttpResponse(json.dumps({"error":"No event found."}), content_type="application/json", status=404)

		event = PharmacyEvent.objects.get(pk=event_id)
		response_data = {
			"pharmacy_id": event.pharmacy_id,
			"user_id": event.user_id,
			"date": event.date,
			"pickup_time": event.pickup_time,
			"name": event.event_name,
			"pharm_event_id": event.pharm_event_id
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	return HttpResponse("Unidentified API request method or input parameters.")

'''
Handles creating pharmacy events.
Request Types:
	GET (user_id, name, pharmacy_id, date, pickup_time): Creates a pharmacy event.
'''
@csrf_exempt
def create_pharm_event(request):
	if request.GET.get('pharmacy_id', '') == '' or request.GET.get('user_id', '') == '' or request.GET.get('date', '') == '' or request.GET.get('pickup_time', '') == '' or request.GET.get('name', '') == '':
		return HttpResponse(json.dumps({"error":"Missing params."}), content_type="application/json", status=400)
	
	E = PharmacyEvent(user_id=request.GET.get('user_id', ''), event_name=request.GET.get('name', ''), pharmacy_id=request.GET.get('pharmacy_id', ''), date=request.GET.get('date', ''), pickup_time=request.GET.get('pickup_time', ''))
	E.save()

	return HttpResponse(json.dumps({"status":"Event created."}), content_type="application/json")

'''
Handles editing events.
Request Types:
	GET (pharm_event_id, user_id, name, pharmacy_id, date, pickup_time): Edits an event.
'''
@csrf_exempt
def edit_pharm_event(request):
	if request.GET.get('pharm_event_id', '') == '' or request.GET.get('pharmacy_id', '') == '' or request.GET.get('user_id', '') == '' or request.GET.get('date', '') == ''  or request.GET.get('pickup_time', '') == '' or request.GET.get('name', '') == '':
		return HttpResponse(json.dumps({"error":"One or more parameters mssing."}), content_type="application/json", status=400)
	
	event_id = request.GET.get('pharm_event_id', '')
	if not PharmacyEvent.objects.filter(pk=event_id).exists():
		return HttpResponse(json.dumps({"error":"No events found."}), content_type="application/json", status=404)

	PharmacyEvent.objects.filter(pk=event_id).update(user=request.GET.get('user_id', ''), event_name=request.GET.get('name', ''), pharmacy=request.GET.get('pharmacy_id', ''), date=request.GET.get('date', ''), pickup_time=request.GET.get('pickup_time', ''))
	return HttpResponse(json.dumps({"status":"Event updated."}), content_type="application/json")

'''
Handles deleting a pharmacy event.
Request Types:
	GET (pharm_event_id): Deletes an event.
'''
@csrf_exempt
def delete_pharm_event(request):
	if request.GET.get('pharm_event_id', '') == '':
		return HttpResponse(json.dumps({"error":"No parameters entered."}), content_type="application/json", status=400)
	event_id = request.GET.get('pharm_event_id', '')
	if not PharmacyEvent.objects.filter(pk=event_id).exists():
		return HttpResponse(json.dumps({"error":"No events found."}), content_type="application/json", status=404)

	PharmacyEvent.objects.filter(pk=event_id).delete()
	return HttpResponse(json.dumps({"status":"Event deleted."}), content_type="application/json")

@csrf_exempt
def populate_pharmacies(request):
	clean = [{"name": "Spalitto's Pharmacy", "address": "3801 Independence Ave, Kansas City, MO 64124, United States", "long": "-94.5369394", "lat": "39.105483", "rating": "4.9", "phone": "816-395-4203"}, {"name": "Albers Medical Pharmacy", "address": "4400 Broadway #106, Kansas City, MO 64111, United States", "long": "-94.591771", "lat": "39.04716", "rating": "2.8", "phone": "816-313-1928"}, {"name": "Walmart Pharmacy", "address": "8551 N Boardwalk Ave, Kansas City, MO 64154, United States", "long": "-94.65450799999999", "lat": "39.250508", "rating": "2.3", "phone": "816-233-1277"}, {"name": "Costco Pharmacy", "address": "241 Linwood Blvd, Kansas City, MO 64111, United States", "long": "-94.5805424", "lat": "39.06762210000001", "rating": "2.3", "phone": "816-531-4889"}, {"name": "CVS Pharmacy", "address": "8509 State Line Rd, Kansas City, MO 64114, United States", "long": "-94.60718539999999", "lat": "38.97170310000001", "rating": "5", "phone": "816-497-7864"}, {"name": "Carondelet Pharmacy", "address": "1000 Carondelet Dr # 120, Kansas City, MO 64114, United States", "long": "-94.604709", "lat": "38.9358677", "rating": "3.6", "phone": "816-167-6224"}, {"name": "CVS Pharmacy", "address": "9040 N Skyview Ave, Kansas City, MO 64154, United States", "long": "-94.6557638", "lat": "39.2575422", "rating": "5", "phone": "816-891-7432"}, {"name": "Walmart Pharmacy", "address": "11601 E US Hwy 40, Kansas City, MO 64133, United States", "long": "-94.442639", "lat": "39.044854", "rating": "2", "phone": "816-995-8133"}, {"name": "CVS Pharmacy", "address": "11124 Holmes Rd, Kansas City, MO 64131, United States", "long": "-94.58412", "lat": "38.924715", "rating": "3.8", "phone": "816-713-1706"}, {"name": "Walmart Pharmacy", "address": "1701 W 133rd St, Kansas City, MO 64145, United States", "long": "-94.60485299999999", "lat": "38.885044", "rating": "4", "phone": "816-167-5125"}, {"name": "Hy-Vee Pharmacy", "address": "5330 NW 64th St, Kansas City, MO 64151, United States", "long": "-94.6417846", "lat": "39.21195609999999", "rating": "5", "phone": "816-817-1687"}, {"name": "Price Chopper Pharmacy", "address": "8430 Wornall Rd, Kansas City, MO 64114, United States", "long": "-94.59614189999999", "lat": "38.9751084", "rating": "5", "phone": "816-210-5597"}, {"name": "Cosentino's Price Chopper Pharmacy", "address": "1030 W 103rd St, Kansas City, MO 64114, United States", "long": "-94.6058063", "lat": "38.9436454", "rating": "5", "phone": "816-807-1158"}, {"name": "Hy-Vee Pharmacy", "address": "207 NW Englewood Rd, Kansas City, MO 64118, United States", "long": "-94.5798661", "lat": "39.1944879", "rating": "5", "phone": "816-442-7391"}, {"name": "Abrams' Pharmacy Inc", "address": "819 N 7th St, Kansas City, KS 66101, United States", "long": "-94.626634", "lat": "39.1144114", "rating": "5", "phone": "816-453-7903"}, {"name": "CVS Pharmacy", "address": "9220 NE barry Rd, Kansas City, MO 64157, United States", "long": "-94.4635093", "lat": "39.24789369999999", "rating": "5", "phone": "816-960-7691"}, {"name": "Sam's Club Pharmacy", "address": "5110 N Oak Trafficway, Kansas City, MO 64118, United States", "long": "-94.5792867", "lat": "39.1866467", "rating": "5", "phone": "816-739-3680"}, {"name": "Hen House Pharmacy", "address": "6238 N Chatham Ave, Kansas City, MO 64151, United States", "long": "-94.64431599999999", "lat": "39.208969", "rating": "4.8", "phone": "816-823-9200"}]
	for pharm in clean:
		P = Pharmacy(address=pharm["address"], name=pharm["name"], lon=pharm["long"], lat=pharm["lat"], phone=pharm["phone"], rating=pharm["rating"])
		P.save()
	return HttpResponse(json.dumps({"status":"Pharms populated."}), content_type="application/json")

@csrf_exempt
def populate_doctors(request):
	clean = [{"name": "HCA Midwest Physicians", "address": "903 E 104th St #500, Kansas City, MO 64131, United States", "specialty": "Orthopedic", "long": "-94.5810628", "lat": "38.9380067", "days_avalible": "MTWRF", "times_avail": "a59992f9-986e-39c5-9562-1495d08c4374"}, {"name": "Medical Group of Kansas City", "address": "6675 Holmes Rd #550, Kansas City, MO 64131, United States", "specialty": "Family", "long": "-94.577989", "lat": "39.0064874", "days_avalible": "MTWRF", "times_avail": "87e18e2f-c4af-308f-b86a-3fdc4fc7652f"}, {"name": "Midtown Family Medicine, Gary A. Thompson, MD", "address": "3406 Broadway, Kansas City, MO 64111, United States", "specialty": "Neurology", "long": "-94.59064629999999", "lat": "39.0662657", "days_avalible": "MTWRF", "times_avail": "a17cb649-27bc-3c33-810b-1d2bfe6f1e66"}, {"name": "Discover Vision Centers in North Kansas City", "address": "9401 N Oak Trafficway #200, Kansas City, MO 64155, United States", "specialty": "Anesthesiology", "long": "-94.57524400000001", "lat": "39.264681", "days_avalible": "MTWRF", "times_avail": "933385d1-5dcc-32a1-b3fb-12dd6f7c2b25"}, {"name": "Medical Group of Kansas City at Research Medical Center Main Campus", "address": "6420 Prospect Ave #102, Kansas City, MO 64131, United States", "specialty": "Pathology", "long": "-94.5562985", "lat": "39.0099747", "days_avalible": "MTWRF", "times_avail": "49a83bb7-ecbf-31f8-83b1-5b79a18608ac"}, {"name": "Consultants in Gastroenterology, P.C.", "address": "5330 N Oak Trafficway Suite 102, Kansas City, MO 64118, United States", "specialty": "Allergy", "long": "-94.5769832", "lat": "39.1912489", "days_avalible": "MTWRF", "times_avail": "adf97d16-172e-304b-91c2-e10aeb9a3f3c"}, {"name": "Goppert-Trinity Family Care", "address": "6675 Holmes Rd #360, Kansas City, MO 64131, United States", "specialty": "Anesthesiology", "long": "-94.5778717", "lat": "39.00707130000001", "days_avalible": "MTWRF", "times_avail": "08ddc5ff-939c-3cbb-b9b3-694451126917"}, {"name": "Erickson Neal A MD", "address": "1004 Carondelet Dr #300a, Kansas City, MO 64114, United States", "specialty": "Pathology", "long": "-94.60159589999999", "lat": "38.935677", "days_avalible": "MTWRF", "times_avail": "591a0bfe-5f84-35ae-84d4-138f9d8d6bfb"}, {"name": "Midwest Women's Healthcare Specialists - Kansas City", "address": "5330 N Oak Trafficway #203, Kansas City, MO 64118, United States", "specialty": "Pathology", "long": "-94.5770261", "lat": "39.1912957", "days_avalible": "MTWRF", "times_avail": "7936b5e4-a389-30cd-9903-4509e6b9a60a"}, {"name": "Brookside Family Medical Group", "address": "7130 Wornall Rd, Kansas City, MO 64114, United States", "specialty": "Psychiatry", "long": "-94.594257", "lat": "38.9987149", "days_avalible": "MTWRF", "times_avail": "47132712-d8f0-3edc-bb2e-380c088e4aa2"}, {"name": "Kansas City Foot and Ankle", "address": "1010 Carondelet Dr, Kansas City, MO 64114, United States", "specialty": "Pathology", "long": "-94.604822", "lat": "38.93594099999999", "days_avalible": "MTWRF", "times_avail": "c396ba7e-1ef1-35ae-9e64-a4828c3c4d8b"}, {"name": "Primary Care North", "address": "5861 NW 72nd St, Kansas City, MO 64151, United States", "specialty": "Pathology", "long": "-94.6484436", "lat": "39.2239919", "days_avalible": "MTWRF", "times_avail": "ec6202cf-fac8-3025-8a8a-20536b2f4c61"}, {"name": "Kansas City CARE Clinic", "address": "3515 Broadway, Kansas City, MO 64111, United States", "specialty": "Pediatrics", "long": "-94.5899304", "lat": "39.0633194", "days_avalible": "MTWRF", "times_avail": "a66c1dd1-6ff6-3bf1-8f13-7347c2951f09"}, {"name": "Midwest Heart and Vascular Specialists - Kansas City", "address": "2330 E Meyer Blvd #509, Kansas City, MO 64132, United States", "specialty": "Pathology", "long": "-94.55802229999999", "lat": "39.0086632", "days_avalible": "MTWRF", "times_avail": "8151cf5b-e862-32d5-96aa-d246e961e668"}, {"name": "Encompass Medical Group - Midtown Office", "address": "2340 E Meyer Blvd, Kansas City, MO 64132, United States", "specialty": "Allergy", "long": "-94.55791049999999", "lat": "39.0089514", "days_avalible": "MTWRF", "times_avail": "14396e8c-0e37-3275-aa66-062d95da0d29"}, {"name": "Neighorhood Walk-in and Family Care", "address": "5151 Troost Ave #200, Kansas City, MO 64110, United States", "specialty": "Emergency Medicine", "long": "-94.57307519999999", "lat": "39.0332361", "days_avalible": "MTWRF", "times_avail": "545610fd-f37a-3e06-8a18-c9760305ab07"}, {"name": "ENT Associates of Greater Kansas City, PC", "address": "1004 Carondelet Dr, Kansas City, MO 64114, United States", "specialty": "Pathology", "long": "-94.6040488", "lat": "38.9355437", "days_avalible": "MTWRF", "times_avail": "d432b6d9-71aa-3f74-8fc9-df4871665a98"}, {"name": "Mosaic Life Care at Shoal Creek", "address": "8880 NE 82nd Terrace, Kansas City, MO 64158, United States", "specialty": "Pediatrics", "long": "-94.4717735", "lat": "39.243818", "days_avalible": "MTWRF", "times_avail": "4fc9455c-1893-3f3b-bf51-18c62a99f9db"}, {"name": "Midwest Reproductive Center, PA", "address": "2750 Clay Edwards Dr Ste. 604, North Kansas City, MO 64116, United States", "specialty": "Pediatrics", "long": "-94.5525136", "lat": "39.15088650000001", "days_avalible": "MTWRF", "times_avail": "7629b08f-9db4-300e-bde4-68f474d4c643"}, {"name": "Briarcliff Medical Association: Stanley John O MD", "address": "5400 N Oak Trafficway # 200, Kansas City, MO 64118, United States", "specialty": "Family", "long": "-94.57708439999999", "lat": "39.1925653", "days_avalible": "MTWRF", "times_avail": "556e62ad-1efd-38d2-8877-7e3e7b3a9ba4"}]

	for doc in clean:
		D = Doctor(address=doc["address"], name=doc["name"], specialty=doc["specialty"], times_available=doc["times_avail"], days_available=doc["days_avalible"], lat=doc["lat"], lon=doc["long"])
		D.save()
	return HttpResponse(json.dumps({"status":"Doctors populated."}), content_type="application/json")
