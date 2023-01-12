from django.urls import path,URLPattern
from . import views

urlpatterns = [
    path('reg',views.auth,name='auth')
]
