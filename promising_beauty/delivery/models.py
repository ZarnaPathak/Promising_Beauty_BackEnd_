from django.db import models

# Create your models here.
class delivery(models.Model):
    dbg_id=models.IntegerField(primary_key=True)
    dbg_fname=models.CharField(max_length=50)
    dbg_lname=models.CharField(max_length=50)
    dbg_password=models.CharField(max_length=20)
    dbg_email=models.CharField(max_length=30)
    dbg_phoneno=models.IntegerField()
    dbg_gender=models.CharField(max_length=15)
    dbg_img=models.CharField(max_length=50)
    dbg_adharcard=models.IntegerField()
    dbg_address=models.CharField(max_length=100)
