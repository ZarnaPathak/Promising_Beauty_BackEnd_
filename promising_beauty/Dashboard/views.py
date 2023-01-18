from django.shortcuts import render

# Create your views here.
def Dashboard(request):
    return render(request,'customer_dashboard.html')

def Dashboard_cart(request):
    return render(request,'customer_cart.html')

def Dashboard_profileset(request):
    return render(request,'customer_profileset.html')

