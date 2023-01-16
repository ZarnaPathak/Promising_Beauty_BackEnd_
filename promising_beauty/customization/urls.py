from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('custom_page',views.customization,name="customization"),
    path('custom_hoop',views.customization_hoop,name="customization_hoop"),
    path('custom_dress',views.customization_dress,name="customization_dress")
]
