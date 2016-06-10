from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from views import ChevalList, ChevalCreate, ChevalDetail, ChevalUpdate, ChevalEtat, EmplacementList, EmplacementCreate, EmplacementDetail, EmplacementUpdate, EmplacementDelete, JournalList, JournalCreate, JournalUpdate


urlpatterns = [

    url(r'^$', ChevalList.as_view(), name='cheval_list'),
    url(r'^etat$', ChevalEtat.as_view(), name='cheval_etat'),
    url(r'^creer$', ChevalCreate.as_view(), name='cheval_create'),

    url(r'^list/journal$', JournalList.as_view(), name='journal-list'),
    url(r'^create/journal$', JournalCreate.as_view(), name='journal-create'),
    url(r'^update/(?P<pk>[\w-]+)/journal$', JournalUpdate.as_view(), name='journal-update'),

    url(r'^emplacement$', EmplacementList.as_view(), name='emplacement_list'),
    url(r'^emplacement/creer$', EmplacementCreate.as_view(), name='emplacement_create'),

    url(r'^(?P<pk>[\w-]+)$', ChevalDetail.as_view(), name='cheval_detail'),
    url(r'^(?P<pk>[\w-]+)/modifier$', ChevalUpdate.as_view(), name='cheval_update'),

    url(r'^emplacement/(?P<pk>[\w-]+)$', EmplacementDetail.as_view(), name='emplacement_detail'),
    url(r'^emplacement/(?P<pk>[\w-]+)/modifier$', EmplacementUpdate.as_view(), name='emplacement_update'),
    url(r'^emplacement/(?P<pk>[\w-]+)/supprimer$', EmplacementDelete.as_view(), name='emplacement_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
