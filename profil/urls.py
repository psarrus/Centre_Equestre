from django.conf.urls import url
from views import create_profil, edit_profil


urlpatterns = [
    url(r'^$', create_profil),
    url(r'^vue_profil/(?P<id>[\w-]+)$', edit_profil),
]
