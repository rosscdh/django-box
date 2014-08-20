# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt

from .views import BoxView


urlpatterns = patterns('',
    url(r'^webhook/$', csrf_exempt(BoxView.as_view()), name='box_webhook_callback'),
)
