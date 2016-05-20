from django.conf.urls import url
from views import CreateProfil, ListProfil, ProfilUpdate, CreatePublic, ListPublic, PublicUpdate


urlpatterns = [
    url(r'^$', ListProfil.as_view(), name='list_profil'),
    url(r'^create$', CreateProfil.as_view(), name='create_profil'),
    url(r'^(?P<pk>[\w-]+)$', ProfilUpdate.as_view(), name='profil_update'),
    url(r'^public/edit$', CreatePublic.as_view(), name='create_public'),
    url(r'^public/list$', ListPublic.as_view(), name='list_public'),
    url(r'^public/(?P<pk>[\w-]+)$', PublicUpdate.as_view(), name='public_update'),
    # url(r'^vue_profil/(?P<id>[\w-]+)$', edit_profil),
]
