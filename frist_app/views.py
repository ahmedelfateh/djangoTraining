from django.shortcuts import render
from django.http import HttpResponse
from frist_app.models import Topic, Webpage, AccessRecord

# Create your views here.

def index(response):
    my_dect = {"insert_django": "my frist django in HTML"}
    return render (response, "index.html", context=my_dect )

def help(helpapp):
    help_dect = {"help": "help page"}
    return render (helpapp, "help.html", context=help_dect)

# def modtest(modapp):
#     mod_dect={"mod":"mod page"}
#     return render (modapp, "modret.html", context=mod_dect)
    # webpages_list = AccessRecord.objects.order_by('date')
    # date_dict = {"access_records": webpages_list}
    # return render (modapp, "modret.html", context=date_dict)

def modnew(modret):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": webpages_list}
    return render (modret, "modret.html", context=date_dict)
