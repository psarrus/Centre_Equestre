from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^create/montoir$', CreneauMontoirCreate.as_view(), name='creneau_montoir_create'),
    url(r'^update/montoir/(?P<pk>[\w-]+)$', CreneauMontoirUpdate.as_view(), name='creneau_montoir_update'),
    url(r'^delete/montoir/(?P<pk>[\w-]+)$', CreneauMontoirDelete.as_view(), name='creneau_montoir_delete'),

    url(r'^list/montoir/previsionnel$', CreneauMontoirPrevisionnelList.as_view(), name='creneau_montoir_previsonnel_list'),
    url(r'^list/montoir/reel$', CreneauMontoirReelList.as_view(), name='creneau_montoir_reel_list'),

    url(r'^detail/montoir/previsionnel(?P<pk>[\w-]+)$', CreneauMontoirPrevisionnelDetail.as_view(), name='piquet_montoir_previsionnel'),
    # url(r'^detail/montoir/reel/(?P<pk>[\w-]+)$', CreneauMontoirReelDetail.as_view(), name='piquet_montoir_reel'),

    url(r'^create/montoir/enseignant/(?P<pk_prev>[\w-]+)$', CreneauMontoirReelCreate.as_view(), name='creneau_montoir_ensignant_create'),

    url(r'^list/piquet/reel$', PiquetReelList.as_view(), name='piquet_reel_list'),




    url(r'^json$', PiquetMontoirJsonListView.as_view(), name='piquet_json_list'),
    url(r'^piquet/update/(?P<pk>[\w-]+)/json$', PiquetMontoirJsonUpdateView.as_view(), name='update_piquet_json'),




]
