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
	if request.GET.get('doctor_id', '') == '':
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
				"times_available": doc.times_available
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
			"times_available": doc.times_available
		}
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	return HttpResponse("Unidentified API request method or input parameters.")

'''
Handles creating doctors.
Request Types:
	GET (address, name, specialty, days_available, times_available): Creates a doctor.
'''
@csrf_exempt
def create_doctor(request):
	if request.GET.get('name', '') == '' or request.GET.get('address', '') == '' or request.GET.get('specialty', '') == '' or request.GET.get('times_available', '') == '' or request.GET.get('days_available', '') == '':
		return HttpResponse(json.dumps({"error":"Missing params."}), content_type="application/json", status=400)
	
	D = Doctor(address=request.GET.get('address', ''), name=request.GET.get('name', ''), specialty=request.GET.get('specialty', ''), times_available=request.GET.get('times_available', ''), days_available=request.GET.get('days_available', ''))
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
	GET (pharm_event_id, user_id, name, pharmacy_id, date, start_time, end_time): Edits an event.
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