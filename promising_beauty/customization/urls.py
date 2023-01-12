from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('custom_page',views.customization,name="customization")
]
