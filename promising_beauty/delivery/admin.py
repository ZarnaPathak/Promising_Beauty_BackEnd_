from django.contrib import admin
from django.contrib.admin.sites import site
from delivery.models import delivery


class admin_delivery(admin.ModelAdmin):
    list_display=('dbg_id','dbg_fname','dbg_lname','dbg_password','dbg_email','dbg_phoneno','dbg_gender','dbg_img',
    'dbg_adharcard','dbg_address')

admin.site.register(delivery,admin_delivery)
