from django.shortcuts import render

# Create your views here.
def customization(request):
    return render(request,'customizationhome.html')

def customization_hoop(request):
    return render(request,'hoop.html')  

def customization_dress(request):
    return render(request,'product_customization.html')

