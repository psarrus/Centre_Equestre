from django.conf.urls import url
from views import SoinList, SoinCreate, SoinDetail, SoinUpdate


urlpatterns = [
    url(r'^$', SoinList.as_view(), name='soin_list'),
    url(r'^creer$', SoinCreate.as_view(), name='soin_create'),
    url(r'^(?P<pk>[\w-]+)$', SoinDetail.as_view(), name='soin_detail'),
    url(r'^(?P<pk>[\w-]+)/modifier$', SoinUpdate.as_view(), name='soin_update'),
]
