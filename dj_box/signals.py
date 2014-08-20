# -*- coding: utf-8 -*-
"""
Webhook signals
"""
from django.dispatch import Signal

#
# Outgoing Events
#
box_event = Signal(providing_args=[])
