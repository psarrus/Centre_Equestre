from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from views import ChevalListView, ChevalCreateView, ChevalDetailView, ChevalUpdateView, ChevalEtatView, AptitudeUpdateView, JournalListView, JournalCreateView, JournalUpdateView, EmplacementListView, EmplacementCreateView, EmplacementUpdateView, EmplacementDeleteView


urlpatterns = [

    url(r'^$', ChevalListView.as_view(), name='cheval_list'),
    url(r'^creer/$', ChevalCreateView.as_view(), name='cheval_create'),
    url(r'^(?P<pk>[\w-]+)$', ChevalDetailView.as_view(), name='cheval_detail'),
    url(r'^(?P<pk>[\w-]+)/modifier/$', ChevalUpdateView.as_view(), name='cheval_update'),


    url(r'^etat/$', ChevalEtatView.as_view(), name='cheval_etat'),
    url(r'^etat/(?P<pk>[\w-]+)/update$', AptitudeUpdateView.as_view(), name='aptitude_update'),


    url(r'^journal/$', JournalListView.as_view(), name='journal_list'),
    url(r'^journal/creer/$', JournalCreateView.as_view(), name='journal_create'),
    url(r'^journal/(?P<pk>[\w-]+)/modifier/$', JournalUpdateView.as_view(), name='journal_update'),


    url(r'^emplacement/$', EmplacementListView.as_view(), name='emplacement_list'),
    url(r'^emplacement/creer/$', EmplacementCreateView.as_view(), name='emplacement_create'),
    url(r'^emplacement/(?P<pk>[\w-]+)/modifier/$', EmplacementUpdateView.as_view(), name='emplacement_update'),
    url(r'^emplacement/(?P<pk>[\w-]+)/supprimer/$', EmplacementDeleteView.as_view(), name='emplacement_delete'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
