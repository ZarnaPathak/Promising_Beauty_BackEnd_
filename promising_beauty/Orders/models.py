from django.db import models
from Dashboard.models import customer
from Products.models import P_Details
# Create your models here.
class order(models.Model):
    o_id=models.IntegerField(primary_key=True)
    cus_id=models.ForeignKey('customer',default=0,on_delete=models.SET_DEFAULT)
    p_id=models.ForeignKey('P_Details',default=0,on_delete=models.SET_DEFAULT)
    o_qty=models.IntegerField()
    o_netamount=models.IntegerField()
    o_date=models.DateField()
    o_details=models.CharField(max_length=100)
    o_status=models.BooleanField()