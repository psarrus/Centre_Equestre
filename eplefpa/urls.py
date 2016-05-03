from django.conf.urls import url
from views import encadrement, homepage, create_profil, edit_profil, ChevalCreate

urlpatterns = [
    url(r'^$', homepage),
    url(r'^profil$', create_profil),
    url(r'^cheval$', ChevalCreate.as_view(), name='cheval_create_form.html'),
    url(r'^encadrement$', encadrement),
    url(r'^vue_profil/(?P<id>[\w-]+)$', edit_profil),
]
