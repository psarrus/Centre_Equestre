from django.conf.urls import url
from views import SoinListView, SoinCreateView, SoinUpdateView


urlpatterns = [
    url(r'^$', SoinListView.as_view(), name='soin_list'),
    url(r'^creer/$', SoinCreateView.as_view(), name='soin_create'),
    url(r'^(?P<pk>[\w-]+)/modifier/$', SoinUpdateView.as_view(), name='soin_update'),
]
