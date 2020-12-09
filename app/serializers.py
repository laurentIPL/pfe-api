from rest_framework import serializers 
from app.models import Connection, Doctor, Establishment, Qrcode_Doctor, Qrcode_Establishment, Phones, Entries_Scans

class ConnectionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Connection
        fields = (
            'user_id',
            'expire_date'
        )

class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = (
            'user_id',
            'name',
            'telephone',
            'street_name',
            'house_number',
            'postcode',
            'tva',
            'mail'
        )

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'user_id',
            'firstname',
            'lastname',
            'telephone',
            'street_name',
            'house_number',
            'postcode',
            'inami',
            'mail'
        )

class Qrcode_DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qrcode_Doctor
        fields = (
            'qrcode_id',
            'doctor',
            'used'         
        )

class Qrcode_EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qrcode_Establishment
        fields = (
            'qrcode_id',
            'establishment',
            'nb_scans'
        )

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = (
            'phone_id',
            'sickness_date'
        )
                    
class Entries_ScansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entries_Scans
        fields = (
            'qrcode_id',
            'phone',
            'date_time'
        )