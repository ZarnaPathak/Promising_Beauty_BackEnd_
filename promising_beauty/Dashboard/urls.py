from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('dashboard_page',views.Dashboard,name="Dashboard")
]