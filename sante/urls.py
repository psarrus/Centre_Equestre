from django.conf.urls import url
from views import Soin, SoinCreate, SoinUpdate


urlpatterns = [
    url(r'^$', Soin.as_view(), name='soin'),
    url(r'^creer/$', SoinCreate.as_view(), name='soin_create'),
    url(r'^(?P<pk>[\w-]+)/modifier/$', SoinUpdate.as_view(), name='soin_update'),
]
