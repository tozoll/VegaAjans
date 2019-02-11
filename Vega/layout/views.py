
from django.shortcuts import render
from about.models import About
from history.models import HistoryHeader, HistoryYears
from home.models import HomePage


def home(request):
    homePage       = HomePage.objects.all()
    about          = About.objects.all()
    historyHeader  = HistoryHeader.objects.all()
    historyYears   = HistoryYears.objects.all()

    context = {
        'homePage'          : homePage[0],
        'about'             : about[0],
        'historyHeader'     : historyHeader[0],
        'historyYears'      : historyYears,

    }
    
    

    return render(request,'index.html',context)
