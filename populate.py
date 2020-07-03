import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fullthrottle.settings')

import django
# Import settings
django.setup()

import random
from FThrottle.models import Members
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fak_name = fake_name[0]
        fak_alias = fake_name[1]

        # Create new User Entry
        user = Members.objects.get_or_create(name=fak_name,
                                         alias=fak_alias)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
