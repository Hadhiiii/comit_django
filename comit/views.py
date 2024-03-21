from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'comit/index.html')

def temp(request):
    return render(request,'comit/index-temp.html')

def travel(request):
    return render(request,'comit/pages/travel.html')

def food(request):
    return render(request,'comit/pages/food.html')