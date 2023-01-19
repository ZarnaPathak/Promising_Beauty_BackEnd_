from django.db import models

# Create your models here.
class addtocart(models.Model):
    cart_id=models.IntegerField(primary_key=True)
    cus_id=models.ForeignKey('customer',default=0,on_delete=models.SET_DEFAULT )
    p_id=models.ForeignKey('P_Details',default=0,on_delete=models.SET_DEFAULT )