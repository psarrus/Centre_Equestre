from django.conf.urls import url
from views import SoinList, SoinCreate, SoinDetail, SoinUpdate, SoinDelete

urlpatterns = [
    url(r'^$', SoinList.as_view(), name='soins'),
    url(r'^creer$', SoinCreate.as_view(), name='soin_create'),
    url(r'^(?P<pk>[\w-]+)$', SoinDetail.as_view(), name='soin_detail'),
    url(r'^(?P<pk>[\w-]+)/modifier$', SoinUpdate.as_view(), name='soin_update'),
    url(r'^(?P<pk>[\w-]+)/supprimer$', SoinDelete.as_view(), name='soin_delete'),
]
