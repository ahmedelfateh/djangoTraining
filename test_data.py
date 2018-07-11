import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","frist_project.settings")

import django
django.setup()

#FAKE DATA SCRIPT

import random
from frist_app.models import AccessRecord, Webpage, Topic, user
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        #Create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_user_frist = fakegen.first_name_male()
        fake_user_last = fakegen.last_name_male()
        fake_mail = fakegen.safe_email()

        #Create new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url= fake_url)[0]

        #Create new AccessRecord entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date= fake_date)[0]

        #creat new user DATA
        user_data = user.objects.get_or_create(frist_Name=fake_user_frist,
                                                   last_Name=fake_user_last,
                                                   email=fake_mail)[0]

if __name__ == "__main__":
    print("the data is here!")
    populate(20)
    print("completed!")
