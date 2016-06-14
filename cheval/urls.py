from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from views import ChevalList, ChevalCreate, ChevalDetail, ChevalUpdate, ChevalEtat, AptitudeUpdate, Journal, JournalCreate, JournalUpdate, Emplacement, EmplacementCreate, EmplacementUpdate, EmplacementDelete


urlpatterns = [

    url(r'^$', ChevalList.as_view(), name='cheval_list'),
    url(r'^creer/$', ChevalCreate.as_view(), name='cheval_create'),
    url(r'^(?P<pk>[\w-]+)$', ChevalDetail.as_view(), name='cheval_detail'),
    url(r'^(?P<pk>[\w-]+)/modifier/$', ChevalUpdate.as_view(), name='cheval_update'),


    url(r'^etat/$', ChevalEtat.as_view(), name='cheval_etat'),
    url(r'^etat/(?P<pk>[\w-]+)/update$', AptitudeUpdate.as_view(), name='aptitude_update'),


    url(r'^journal/$', Journal.as_view(), name='journal'),
    url(r'^journal/creer/$', JournalCreate.as_view(), name='journal_create'),
    url(r'^journal/(?P<pk>[\w-]+)/modifier/$', JournalUpdate.as_view(), name='journal_update'),


    url(r'^emplacement/$', Emplacement.as_view(), name='emplacement'),
    url(r'^emplacement/creer/$', EmplacementCreate.as_view(), name='emplacement_create'),
    url(r'^emplacement/(?P<pk>[\w-]+)/modifier/$', EmplacementUpdate.as_view(), name='emplacement_update'),
    url(r'^emplacement/(?P<pk>[\w-]+)/supprimer/$', EmplacementDelete.as_view(), name='emplacement_delete'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
