# -*- coding: utf-8 -*-
from .signals import box_event

import logging
logger = logging.getLogger('django.request')


class BoxWebhookService(object):
    def process(self, data):
        """
        Method to process the callback data
        """
        logger.debug('Recieved webhook data from Box: %s' % data)
        # issue the signal
        box_event.send(sender=self, **data)
        logger.debug('Issued box_event signal')

        return data