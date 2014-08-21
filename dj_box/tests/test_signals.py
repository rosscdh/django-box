# -*- coding: utf-8 -*-
from django.core.cache import cache
from django.dispatch import receiver
from django.test import TestCase, Client
from django.core.urlresolvers import reverse_lazy

from dj_box.signals import box_event

from . import (TRANSLATED_WEBHOOK_DATA,
               WEBHOOK_POSTED_DATA,
               VALID_VIEW_RESPONSE)

import json
import httpretty


EXPECTED_SIGNAL_KEYS = ['signal', u'data', 'sender']


@receiver(box_event)
def test_box_webhook_event_recieved_and_signal_sent(**kwargs):
    """
    Test signal listner to handle the signal fired event
    """
    cache.set('test_box_webhook_event_recieved_and_signal_sent', kwargs.keys())


class BoxSignalTest(TestCase):
    """
    Test that the webhook on POST issues the event
    """
    def setUp(self):
        self.client = Client()
        self.url = reverse_lazy('dj_box:box_webhook_callback')
        self.valid_webhook_data = WEBHOOK_POSTED_DATA

    @httpretty.activate
    def test_signal_issued(self, *args, **kwargs):
        httpretty.register_uri(httpretty.POST, "http://beta.box.com/api/v2/stamp",
                       body=json.dumps(TRANSLATED_WEBHOOK_DATA),
                       status=200)

        resp = self.client.post(self.url, self.valid_webhook_data)
        self.assertEqual(resp.status_code, 200)

        self.assertEqual(cache.get('test_box_webhook_event_recieved_and_signal_sent'), EXPECTED_SIGNAL_KEYS)
