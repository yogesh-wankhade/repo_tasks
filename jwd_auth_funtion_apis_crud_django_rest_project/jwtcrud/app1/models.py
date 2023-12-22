from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Person(models.Model):
    GENDER=[('Male','Male'),
            ('Female','Female'),
            ('Other','Other')
    ]
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=6,choices=GENDER)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    contact_no=PhoneNumberField(region="IN")
    aadhar_no=models.CharField(max_length=12)
    email=models.EmailField()
