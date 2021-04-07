from django.db import models

# Create your models here.

class Users(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    birthday = models.CharField(max_length=10)
    email= models.EmailField(max_length = 254,unique=True)
    phone = models.BigIntegerField(unique=True)
    passw = models.CharField(max_length=100)
    father_name = models.CharField(max_length=50,null=True)
    address1 = models.CharField(max_length=500,null=True)
    address2 = models.CharField(max_length=500,null=True)
    landmark = models.CharField(max_length=100,null=True)
    district = models.CharField(max_length=50,null=True)
    pincode = models.IntegerField(null=True)
    address_type = models.CharField(max_length=50,null=True)




