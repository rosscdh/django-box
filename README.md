django-box
==========

A Django app for integrating with box webhook callbacks


Installation
------------

1. python setup.py
2. pip install requirements.txt
3. add dj_box to INSTALLED_APPS
4. add dj_box.urls to your apps urls.py


__Example Implementation__

1. Setup your urls.py to use the view below as the callback reciever or just use the default sss reciever
2. Register the url "https://yourhost.com/sss/webhook/" as the webhook callback at box
3. and that is it, you can now hook up the signal listener and get a signal event whenever a webhook event happens

```
url(r'^box/', include('dj_box.urls', namespace='dj_box')),
```

__Or__

You can write a custom view, by extending our View and doing somethign more specific with the data, and hook the view up to a url and register that url with box.

```views.py
from dj_box.views import BoxView


class MyCustomBoxWebhookRecieverView(BoxView):
    def post(self, request, *args, **kwargs):
        # do something amazing

        return self.render_json_response({
            'detail': 'Box Callback recieved',
        })
```


__Please Note__

If you use the BoxView then a signal will be issued when recieving callbacks from dj_box, which you can then listen for and do other things.


__Signal Example Implementation__


```signals.py
from django.dispatch import receiver
from dj_box.signals import box_event


@receiver(box_event)
def on_box_callback(sender, **kwargs):
    # do something amazing with the data in the kwargs dict
    pass
```


__TODO__

1. improve setup.py to install from requirements
