from django.contrib import admin
from django.contrib.admin.sites import site
from Authentication.models import user_registration


class admin_user(admin.ModelAdmin):
    list_display=('first_name','last_name','phone_no','email','address','city','state','zipcode','password')
   
    
admin.site.register(user_registration,admin_user)
