from django.shortcuts import render

# Create your views here.
def Order_detail(request):
    return render(request,'customer_order_detail.html')