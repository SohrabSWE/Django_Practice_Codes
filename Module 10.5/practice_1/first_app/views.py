from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    value = {
        "list" : ['a', 'b', 'c', 'd'],
        "str" : ['python', 'is', 'fun'],
        "birthday" : datetime.datetime.now(),
        "word" : 'jai',
        "sentence" : 'String with spaces',
    }
    return render(request,"first_app/home.html", value)