from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    my_dect = {"insert_django": "my frist django in HTML"}
    return render (response, "index.html", context=my_dect )

def help(helpapp):
    help_dect = {"help": "help page"}
    return render (helpapp, "help.html", context=help_dect)
