from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', homepage),
    url(r'^create/montoir$', CreneauMontoirCreate.as_view(), name='creneau_montoir_create'),

    # url(r'^create/piquet/staff$', PiquetMontoirStaff.as_view(), name='piquet_enseignant_create'),
    #
    # url(r'^create/piquet/enseignant$', PiquetMontoirEnseignant.as_view(), name='piquet_staff_create'),
]
