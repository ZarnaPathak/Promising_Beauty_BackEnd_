from django.db import models

# Create your models here.
class customizationhome(models.Model):
    custm_id=models.IntegerField(primary_key=True)
    custm_type=models.CharField(max_length=10)

class hoop(models.Model):
    custm_id=models.ForeignKey('customizationhome',default=0,on_delete=models.SET_DEFAULT)
    hoop_id=models.IntegerField(primary_key=True)
    hoop_layout=models.IntegerField()
    hoop_name1=models.CharField(max_length=100)
    hoop_name2=models.CharField(max_length=100)
    hoop_date=models.DateField()
    hoop_msg=models.TextField(max_length=30)

