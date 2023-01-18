from django.db import models

# Create your models here.
class customer(models.Model):
   cus_id=models.IntegerField(primary_key=True)
   first_name=models.CharField(max_length=50) 
   last_name=models.CharField(max_length=50) 
   phone_no=models.CharField(max_length=11)
   email=models.EmailField(max_length=30)
   address=models.CharField(max_length=50)
   city=models.CharField(max_length=15)
   state=models.CharField(max_length=15)
   zipcode=models.IntegerField()
   