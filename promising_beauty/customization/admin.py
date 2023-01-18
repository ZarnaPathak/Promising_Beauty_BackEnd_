from django.contrib import admin
from customization.models import customizationhome,hoop
from django.contrib.admin.sites import site

# Register your models here.
class admin_customizationhome(admin.ModelAdmin):
    list_display=('custm_id','custm_type')

class admin_custmhoop(admin.ModelAdmin):
    list_display=('custm_id','hoop_id','hoop_layout','hoop_name1','hoop_name2','hoop_date','hoop_msg')

admin.site.register(customizationhome,admin_customizationhome)
admin.site.register(hoop,admin_custmhoop)