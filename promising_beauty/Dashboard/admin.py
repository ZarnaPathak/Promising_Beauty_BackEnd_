from django.contrib import admin
from Dashboard.models import customer
from django.contrib.admin.sites import site

# Register your models here.
class admin_customer(admin.ModelAdmin):
    list_display=('cus_id','first_name','last_name','phone_no','email','address','city','state','zipcode')

admin.site.register(customer,admin_customer)
