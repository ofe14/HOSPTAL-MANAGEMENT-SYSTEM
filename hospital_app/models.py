from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('reception','Reception'),
        ('vitals','Vitals'),
        ('laboratory','laboratory'),
        ('pharmacy','Pharmacy'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='user')

    def __str__(self):
        return self.username
    
class register(models.Model):
    profile_photo=models.FileField(upload_to='patient_id_files/',blank=True)
    id=models.CharField(max_length=10,primary_key=True)
    reg_date=models.DateField(max_length=100)
    firstname= models.CharField(max_length = 200)
    middlename=models.CharField(max_length=200)
    surname = models.CharField(max_length = 200)
    gender=models.CharField(max_length = 200)
    dateofbirth=models.DateField(max_length=100)
    marital_status=models.CharField(max_length = 200)
    occupation=models.CharField(max_length = 200)
    nationality=models.CharField(max_length = 200)
    email=models.CharField(max_length = 200)
    address=models.CharField(max_length = 200)
    phone=models.CharField(max_length = 200)
    state=models.CharField(max_length = 200)
    emg_name=models.CharField(max_length = 200)
    emg_relationship=models.CharField(max_length = 200,default="")
    emg_address=models.CharField(max_length = 200)
    emg_phone=models.CharField(max_length = 200)
    emg_state=models.CharField(max_length = 200)
    payment=models.CharField(max_length = 200)
    age=models.CharField(max_length=100)
    identification=models.FileField(upload_to='patient_id_files/',null=True,blank=True)
    allergies=models.CharField(max_length = 200,default="")
    past_surgeries=models.CharField(max_length = 200,default="")
    chronic_illness=models.CharField(max_length = 200,default="")
    
    
    
    class Meta:
        db_table ="registration"
    
class patientlog(models.Model):
    patient_id=models.CharField(max_length = 150, primary_key=True)
    patient_name=models.CharField(max_length=150)
    date = models.CharField(max_length = 150)
    activity = models.CharField(max_length = 150)
    additional_info = models.CharField(max_length = 150)
    
    class Meta:
        db_table ="patient_log"

class staffs(models.Model):
    name =models.CharField(max_length=100 , primary_key=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    job = models.CharField(max_length = 150)
    department = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    
    class  Meta:
        db_table = 'staff'

class appoinment(models.Model):
    patient_id=models.CharField(max_length=100)
    session=models.CharField( max_length=100)
    department=models.CharField(max_length=100)
    doctor=models.CharField(max_length=100)
    date=models.DateField(max_length=100,primary_key=True)
    time=models.TimeField(max_length=6)
    add_info=models.CharField(max_length=500)
    
    class Meta:
        db_table = 'appointments'
        
class vital(models.Model):
    date =models.CharField(max_length=100,primary_key=True)
    name= models.CharField(max_length=100)
    blood_pressure = models.CharField(max_length=100)
    sugar_level=models.CharField(max_length=100)
    height=models.CharField(max_length=100)
    heart_rate=models.CharField(max_length=100)
    temperature=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    respiration=models.CharField(max_length=100)
    
    class Meta:
        db_table = 'vitals'
    
    
class doc_sess(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name =models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    message =models.CharField(max_length=100)
    cheif_complaint=models.CharField(max_length=100)
    recipient=models.CharField(max_length=100)
        
    class Meta:
        db_table = 'doc_sess'

        
class lab_data(models.Model):
    id=models.CharField(max_length=100, primary_key=True)
    name=models.CharField(max_length=100)
    report=models.CharField(max_length=100)
    reciever= models.CharField(max_length=100)
    file=models.FileField(upload_to='files/')
    time=models.CharField(max_length=100)
    
    class Meta:
        db_table = 'lab'

        
class communication(models.Model):
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    subject=models.CharField(max_length=100 , default="no subject" ,primary_key=True)
    message=models.CharField(max_length=100)
    file=models.FileField(upload_to='messages_files/',null=True,blank=True)
    time=models.CharField(max_length=100)
    
    class Meta:
        db_table = 'messages'
