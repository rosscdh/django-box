# -*- coding: utf-8 -*-
from django.views.generic import View

from braces.views import JSONResponseMixin

from .services import BoxWebhookService

import logging
logger = logging.getLogger('django.request')


class BoxView(JSONResponseMixin, View):
    """
    Handle the box callback
    """
    http_method_names = [u'post']

    json_dumps_kwargs = {'indent': 3}

    service = None
    data = None

    def dispatch(self, request, *args, **kwargs):
        logger.info('Recieved box webhook')
        self.service = BoxWebhookService()

        if request.method.lower() in self.http_method_names:
            self.data = self.service.process(data=request.POST)

        return super(BoxView, self).dispatch(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.render_json_response({
            'detail': 'Box Callback recieved',
            'data': self.data,
        })
