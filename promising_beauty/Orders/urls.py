from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('dashboard_order_detail',views.Order_detail,name="Order_detail")
]
