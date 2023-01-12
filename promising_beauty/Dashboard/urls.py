from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('dashboard_page',views.Dashboard,name="Dashboard"),
    path('dashboard_page_cart',views.Dashboard_cart,name="Dashboard_cart"),
    
    
   
]