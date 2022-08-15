import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()

from faker import Faker
import random
from first_app.models import AccessRecord,Webpage,Topic

fakegen = Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t



def populate(N=5):
    for entry in range(N):
        # get the topic fro the entry
        top = add_topic()

        # create the fake data that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

        # create a fake AccessRecord for webpage


def add_access(N=6):
    for _ in range(N):
        fake_name_record = fakegen.company()
        fake_date = fakegen.date()
        acc_rec = AccessRecord.objects.get_or_create(name_record=fake_name_record,date=fake_date)[0]
        print(acc_rec)
        print(fake_name_record)





populate(10)
add_access(10)
