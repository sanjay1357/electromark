from django.db import models

# Create your models here.



# Create your models here.

class Cart(models.Model):
    userid=models.IntegerField()
    tablename=models.CharField(max_length=30)
    category=models.CharField(max_length=30,null=True)
    productid=models.IntegerField()
    price=models.IntegerField(null=True)

STATUS_CHOICES = ( 
    ("ordered", "ordered"), 
    ("delivered", "delivered"),
    ("ontheway", "ontheway"),
     
) 

class Order(models.Model):
    userid=models.IntegerField()
    tablename=models.CharField(max_length=30)

    productid=models.IntegerField()
    tracking=models.BigIntegerField(unique=True)
    status=models.CharField(max_length=30,choices = STATUS_CHOICES,default = 'ordered')
    times=models.CharField(max_length=50,null=True)
    payment=models.CharField(max_length=50,null=True)
    name=models.CharField(max_length=50)



     