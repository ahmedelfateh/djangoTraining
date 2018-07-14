from django.shortcuts import render
from django.http import HttpResponse
from frist_app.models import Topic, Webpage, AccessRecord, user
from frist_app import forms

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

def userFunc(userdata):
    users_list = user.objects.order_by('frist_Name')
    users_dict = {'users_key': users_list}
    return render(userdata, "userdata.html", context=users_dict)

def formName(nForm):
    form = forms.formName()
    if nForm.method == "POST":
        form = forms.formName(nForm.POST)

    if form.is_valid():
        print("validatin is good!")
        print("Name:" + form.cleaned_data['name'])
        print("Email:" + form.cleaned_data['email'])
        print("Verifaied Email:" + form.cleaned_data['verify_email'])
        print("Text:" + form.cleaned_data['text'])
    form_dict = {"form":form}
    return render (nForm, "forms.html", context=form_dict)
