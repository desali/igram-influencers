from __future__ import absolute_import

import os
from celery import Celery

# set the default Django settings module for the 'igram-influencers' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'influencers.settings')
app = Celery('influencers')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
