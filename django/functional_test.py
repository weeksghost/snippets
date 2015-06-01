import os
import unittest
import requests
from time import sleep

from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE']='XXXX.settings'

from XXXX.models import XXXX
from XXXX.tasks import XXXX
from XXXX.tasks import XXXX


class NewsletterTests(unittest.TestCase):
    offers_nl = XXXX.objects.get(id=1)
    line_nl = XXXX.objects.get(id=2)
    group_nl = XXXX.objects.get(id=3)

    admins = [emails[1] for emails in settings.XXXX]
    EMAIL = ''
    for email in xxxx:
        EMAIL = email

    profile_url = 'http://backend_manager/' \
                  'url_for/' \
                  'verification'.format(EMAIL)

    def _offers(self):

        offers = Celery_Task.delay(self.offers_nl, self.EMAIL)
        sleep(2)
        response = requests.get(self.profile_url)
        content = response.text
        assert 'SUCCESS' or 'PENDING' in offers.status
        assert 'DistId="15"' in content

        offers = Celery_Task.delay(self.offers_nl, self.EMAIL)
        sleep(2)
        response = requests.get(self.profile_url)
        content = response.text
        assert 'SUCCESS' or 'PENDING' in offers.status
        assert 'DistId="15"' not in content


    def _line(self):
        buzz = Celery_Task.delay(self.line_nl, self.EMAIL)
        sleep(2)
        response = requests.get(self.profile_url)
        content = response.text
        assert 'SUCCESS' or 'PENDING' in buzz.status
        assert 'DistId="14"' in content

        buzz = Celery_Task.delay(self.line_nl, self.EMAIL)
        sleep(2)
        response = requests.get(self.profile_url)
        content = response.text
        assert 'SUCCESS' or 'PENDING' in buzz.status
        assert 'DistId="14"' not in content


    def _group(self):
        groups = Celery_Task.delay(self.group_nl, self.EMAIL)
        sleep(2)
        response = requests.get(self.profile_url)
        content = response.text
        assert 'SUCCESS' or 'PENDING' in groups.status
        assert 'DistId="13"' in content

        groups = Celery_Task.delay(self.group_nl, self.EMAIL)
        sleep(2)
        response = requests.get(self.profile_url)
        content = response.text
        assert 'SUCCESS' or 'PENDING' in groups.status
        assert 'DistId="13"' not in content


    def test_newsletters(self):
        """Test email subscription backend"""
        self._offers()
        self._line()
        self._group()

