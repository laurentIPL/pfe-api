from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import uuid
import app.views
from django.contrib.auth.models import User
from app.models import Connection, Doctor, Establishment, Phones, Entries_Scans
from app.serializers import ConnectionSerializer, EstablishmentSerializer, DoctorSerializer, Qrcode_DoctorSerializer, Qrcode_EstablishmentSerializer, PhonesSerializer
from datetime import datetime, timedelta 
import pytz

utc=pytz.UTC


# codes renvoyés : 0 error, 1 welcome, 2 vous etes safe, 3 vous etes danger
@api_view(['POST'])
def handle_app_launched(request):
    request_data = JSONParser().parse(request)
    req_phone_id = request_data['id']
    print("THIS PHONE : " + str(req_phone_id))
    if(req_phone_id is not None): 
        try:
            expositions_count = 0
            for this_phone_scan in Entries_Scans.objects.filter(phone_id = req_phone_id):
                if (this_phone_scan.date_time > utc.localize(datetime.now() - timedelta(days=10))) & (this_phone_scan.date_time <= utc.localize(datetime.now())):
                    for same_qrcode_scan in Entries_Scans.objects.filter(qrcode_id = this_phone_scan.qrcode_id):
                        if (same_qrcode_scan.date_time > this_phone_scan.date_time - timedelta(hours=1)) & (same_qrcode_scan.date_time < this_phone_scan.date_time + timedelta(hours=1)) & (same_qrcode_scan.phone != this_phone_scan.phone):
                            nearby_phones = Phones.objects.filter(phone_id = same_qrcode_scan.phone.phone_id)
                            for nearby_phone in nearby_phones:
                                if (nearby_phone.sickness_date > this_phone_scan.date_time - timedelta(days=10)) & (nearby_phone.sickness_date <= this_phone_scan.date_time + timedelta(days=10)):
                                    print("NEARBY PHONE : " + str(nearby_phone.phone_id))
                                    expositions_count += 1
            if expositions_count != 0:
                return JsonResponse({'code': 3, 'expositions': expositions_count}, status=status.HTTP_201_CREATED)
            return JsonResponse({'code': 2}, status=status.HTTP_201_CREATED)
        except Phones.DoesNotExist:
            return JsonResponse({'code': 0, 'error': 'DB operation error'}, status=status.HTTP_400_BAD_REQUEST)
    newPhoneId = str(uuid.uuid4())
    newPhone = {'phone_id': newPhoneId, 'sickness_date': utc.localize(datetime.min)}
    phone_serializer = PhonesSerializer(data = newPhone)
    if phone_serializer.is_valid():
        try:
            phone_serializer.save()
        except Exception as e:
            return JsonResponse({'code': 0, 'error': 'Phone couldnt be added in DB'}, status=status.HTTP_400_BAD_REQUEST)
        print("NEW PHONE : " + str(newPhoneId))
        return JsonResponse({'code': 1, 'id': newPhoneId}, status=status.HTTP_201_CREATED)
    return JsonResponse({'code': 0, 'error': 'API error'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_users_for_dev(request):
    try:
        docteur = User.objects.create_user('doc@gmail.com', 'doc@gmail.com', '12345678')
        # docteur_id = User.objects.get(email = 'doc@gmail.com')
        pierre = User.objects.create_user('p@gmail.com', 'p@gmail.com', '12345678')
        laurent = User.objects.create_user('l@gmail.com', 'l@gmail.com', '12345678')
        simon = User.objects.create_user('s@gmail.com', 's@gmail.com', '12345678')
        marc = User.objects.create_user('m@gmail.com', 'm@gmail.com', '12345678')
        colin = User.objects.create_user('c@gmail.com', 'c@gmail.com', '12345678')
        doctor = { 
            'user_id' : 1,
            'firstname' : '1',
            'lastname' : '1',
            'telephone' : '1',
            'street_name' : '1',
            'house_number' : 1,
            'postcode' : '1',
            'inami' : '1',
            'mail' : '1'
        }
        establishmentP = {
            'user_id' : 2,
            'name' : '2',
            'telephone' : '2',
            'street_name' : '2',
            'house_number' : 2,
            'postcode' : '2',
            'tva' : '2',
            'mail' : '2'
        }
        establishmentL = {
            'user_id' : 3,
            'name' : '3',
            'telephone' : '3',
            'street_name' : '3',
            'house_number' : 3,
            'postcode' : '3',
            'tva' : '3',
            'mail' : '3'
        }
        establishmentS = {
            'user_id' : 4,
            'name' : '4',
            'telephone' : '4',
            'street_name' : '4',
            'house_number' : 4,
            'postcode' : '4',
            'tva' : '4',
            'mail' : '4'
        }
        establishmentM = {
            'user_id' : 5,
            'name' : '5',
            'telephone' : '5',
            'street_name' : '5',
            'house_number' : 5,
            'postcode' : '5',
            'tva' : '5',
            'mail' : '5'
        }
        establishmentC = {
            'user_id' : 6,
            'name' : '6',
            'telephone' : '6',
            'street_name' : '6',
            'house_number' : 6,
            'postcode' : '6',
            'tva' : '6',
            'mail' : '6'
        }
        if doctor is not None: 
            doctor_serializer = DoctorSerializer(data = doctor)
            if doctor_serializer.is_valid():
                doctor_serializer.save()
        if establishmentP is not None: 
            establishment_serializer = EstablishmentSerializer(data = establishmentP)
            if establishment_serializer.is_valid():
                establishment_serializer.save()
        if establishmentL is not None: 
            establishment_serializer = EstablishmentSerializer(data = establishmentL)
            if establishment_serializer.is_valid():
                establishment_serializer.save()
        if establishmentS is not None: 
            establishment_serializer = EstablishmentSerializer(data = establishmentS)
            if establishment_serializer.is_valid():
                establishment_serializer.save()
        if establishmentM is not None: 
            establishment_serializer = EstablishmentSerializer(data = establishmentM)
            if establishment_serializer.is_valid():
                establishment_serializer.save()
        if establishmentC is not None: 
            establishment_serializer = EstablishmentSerializer(data = establishmentC)
            if establishment_serializer.is_valid():
                establishment_serializer.save()
    except Exception as e:
        return JsonResponse({'response': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'response': 'ok'}, status=status.HTTP_201_CREATED)
    
