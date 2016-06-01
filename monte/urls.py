from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^create/montoir$', CreneauMontoirCreate.as_view(), name='creneau_montoir_create'),
    url(r'^update/montoir/(?P<pk>[\w-]+)$', CreneauMontoirUpdate.as_view(), name='creneau_montoir_update'),
    url(r'^delete/montoir/(?P<pk>[\w-]+)$', CreneauMontoirDelete.as_view(), name='creneau_montoir_delete'),
    url(r'^list/montoir$', CreneauMontoirList.as_view(), name='creneau_montoir_list'),
    url(r'^detail/montoir/(?P<pk>[\w-]+)$', CreneauMontoirDetail.as_view(), name='piquet_montoir'),
    # url(r'^update/montoir_staff/(?P<pk>[\w-]+)$', PiquetMontoirStaffUpdate.as_view(), name='montoir_staff'),
    url(r'^detail/montoir/(?P<pk>[\w-]+)/json$', PiquetDetailJsonView.as_view(), name='piquet_json_detail'),




]
