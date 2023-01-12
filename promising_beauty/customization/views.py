from django.shortcuts import render

# Create your views here.
def customization(request):
    return render(request,'customizationhome.html')