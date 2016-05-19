from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', homepage),
    url(r'^create/montoir$', CreneauMontoirCreate.as_view(), name='creneau_montoir_create'),
    url(r'^update/montoir/(?P<pk>[\w-]+)$', CreneauMontoirUpdate.as_view(), name='creneau_montoir_update'),
    url(r'^delete/montoir/(?P<pk>[\w-]+)$', CreneauMontoirDelete.as_view(), name='creneau_montoir_delete'),
    url(r'^list/montoir$', CreneauMontoirList.as_view(), name='creneau_montoir_list'),
    url(r'^piquet/montoir/(?P<pk>[\w-]+)$', PiquetMontoirStaffDetail.as_view(), name='piquet_montoir'),
    # url(r'^piquet/montoir/(?P<id>[\w-]+)$', creneau_montoir, name='piquet_montoir'),

    # url(r'^create/piquet/staff$', PiquetMontoirStaff.as_view(), name='piquet_enseignant_create'),
    #
    # url(r'^create/piquet/enseignant$', PiquetMontoirEnseignant.as_view(), name='piquet_staff_create'),
]
