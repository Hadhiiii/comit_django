from django.shortcuts import render, redirect
from comit.models import apps
from django.contrib import messages

# Create your views here.
def add_data(request):
    if request.method == 'GET':
        return render(request, "dbms/index.html", {"alert":None})
    
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            icon_link = request.POST.get('icon_link')
            link = request.POST.get('link')
            my_model = apps(
                name=name,
                icon_link=icon_link,
                link=link
            )
            my_model.save()

            message='Data saved successfully!'
            messages.success(request, str(message))
            return redirect("/dbms")
        
    except Exception as e:
        messages.error(request, str(e))
        return redirect("/dbms")
