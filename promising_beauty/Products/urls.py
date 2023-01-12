from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('product_page',views.Products,name="Products")
]