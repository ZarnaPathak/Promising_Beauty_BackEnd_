from django.db import models
from Orders.models import order
# Create your models here.
class Payment(models.Model):
    pay_id=models.IntegerField(primary_key=True)
    o_id=models.ForeignKey('orders',default=0,on_delete=models.SET_DEFAULT)
    pay_type=models.CharField(max_length=50)
    pay_upiid=models.CharField(max_length=50)
    pay_cardname=models.CharField(max_length=50)
    pay_cardnum=models.IntegerField()