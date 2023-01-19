from django.contrib import admin
from Addtocart.models import addtocart
from django.contrib.admin.sites import site

# Register your models here.
class admin_cart(admin.ModelAdmin):
    list_display=('cus_id','cart_id','p_id')

admin.site.register(addtocart,admin_cart)
