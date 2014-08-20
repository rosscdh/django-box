# -*- coding: utf-8 -*-
from .signals import box_event

import logging
logger = logging.getLogger('django.request')


class BoxWebhookService(object):
    def process(self, data):
        """
        Method to process the callback data
        """
        # issue the signal
        box_event.send(sender=self, **data)

        return data