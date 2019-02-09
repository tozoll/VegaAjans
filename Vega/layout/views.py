from django.shortcuts import render
from home.models import HomePage

def home(request):
    homePage = HomePage.objects.all()

    context = {
        'homePage' : homePage[0],

    }
    
    

    return render(request,'index.html',context)
