from django.conf.urls import url
from views import ChevalList, ChevalCreate, ChevalUpdate, EmplacementList, EmplacementCreate, EmplacementUpdate

urlpatterns = [
    url(r'^$', ChevalList.as_view(), name='cheval_list'),
    url(r'^creer$', ChevalCreate.as_view(), name='cheval_create'),

    url(r'^emplacement$', EmplacementList.as_view(), name='emplacement_list'),
    url(r'^emplacement/creer$', EmplacementCreate.as_view(), name='emplacement_create'),

    url(r'^(?P<pk>[\w-]+)$', ChevalUpdate.as_view(), name='cheval_update'),

    url(r'^emplacement/(?P<pk>[\w-]+)$', EmplacementUpdate.as_view(), name='emplacement_update'),
]
