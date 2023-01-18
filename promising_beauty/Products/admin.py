from django.contrib import admin
from Products.models import Cat,SubCat,P_Details
from django.contrib.admin.sites import site
# Register your models here.
class CatAdmin(admin.ModelAdmin):
    list_display=('cat_id','cat_name')

class SubCatAdmin(admin.ModelAdmin):
    list_display=('subcat_id','cat_id','subcat_name')

class PDetailsAdmin(admin.ModelAdmin):
    list_display=('p_id','subcat_id','p_name','p_price','p_qty','p_type','p_fabric','p_size','p_img','p_desc','p_color')


admin.site.register(Cat,CatAdmin)
admin.site.register(SubCat,SubCatAdmin)
admin.site.register(P_Details,PDetailsAdmin)