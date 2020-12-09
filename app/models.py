from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

class Qrcode_Establishment(models.Model):
    qrcode_id = models.CharField(max_length=100, blank=False, default='', primary_key = True)
    establishment = models.ForeignKey(
        'Establishment',
        on_delete=models.CASCADE,
    )
    nb_scans = models.IntegerField()
    name = models.CharField(max_length=20, blank=False, default='')


class Qrcode_Doctor(models.Model):
    qrcode_id = models.CharField(max_length=100, blank=False, default='', primary_key = True)
    doctor = models.ForeignKey(
        'Doctor',
        on_delete=models.CASCADE,
    )
    used = models.BooleanField()

class Entries_Scans(models.Model):
    qrcode_id = models.CharField(max_length=100, blank=False, default='')
    phone = models.ForeignKey(
        'Phones',
        on_delete=models.CASCADE,
    )
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)

class Establishment(models.Model):
    user_id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length=50, blank=False, default='')
    telephone = models.CharField(max_length=13, blank=False, default='')
    street_name = models.CharField(max_length=100, blank=False, default='')
    house_number = models.IntegerField()
    postcode = models.CharField(max_length=10, blank=False, default='') 
    tva = models.CharField(max_length=20, blank=False, default='')
    mail = models.CharField(max_length=100, blank=False, default='')

class Doctor(models.Model):  
    user_id = models.IntegerField(primary_key= True)
    firstname = models.CharField(max_length=50, blank=False, default='')
    lastname = models.CharField(max_length=50, blank=False, default='')
    telephone = models.CharField(max_length=13, blank=False, default='')
    street_name = models.CharField(max_length=100, blank=False, default='')
    house_number = models.IntegerField()
    postcode = models.CharField(max_length=10, blank=False, default='') 
    inami = models.CharField(max_length=20, blank=False, default='')
    mail = models.CharField(max_length=100, blank=False, default='')

class Connection(models.Model):
    user_id = models.IntegerField()
    expire_date = models.DateTimeField(auto_now=False, auto_now_add=False)

class Phones(models.Model):
    phone_id = models.CharField(max_length=50, blank=False, primary_key = True)
    sickness_date =  models.DateTimeField(null=True, blank=True)
