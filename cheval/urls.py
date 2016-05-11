from django.conf.urls import url
from views import ChevalList, ChevalCreate, ChevalUpdate

urlpatterns = [
    url(r'^$', ChevalList.as_view(), name='cheval_list'),
    url(r'^creer$', ChevalCreate.as_view(), name='cheval_create'),
    url(r'^(?P<pk>[\w-]+)$', ChevalUpdate.as_view(), name='cheval_update'),
]
