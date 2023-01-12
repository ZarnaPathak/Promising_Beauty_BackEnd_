from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('cart_page',views.Addtocart,name="Addtocart")
]