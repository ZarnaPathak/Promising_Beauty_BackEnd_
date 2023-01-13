from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('dashboard_page',views.Dashboard,name="Dashboard"),
    path('dashboard_page_cart',views.Dashboard_cart,name="Dashboard_cart"),
    path('dashboard_profileset',views.Dashboard_profileset,name="Dashboard_profileset")
]