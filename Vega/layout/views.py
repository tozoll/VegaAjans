from django.shortcuts import render
from home.models import HomePage
from about.models import About

def home(request):
    homePage    = HomePage.objects.all()
    about       = About.objects.all()

    context = {
        'homePage' : homePage[0],
        'about'    : about[0],

    }
    
    

    return render(request,'index.html',context)
