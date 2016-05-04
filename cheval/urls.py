from django.conf.urls import url
from views import cheval

urlpatterns = [
    url(r'^$', cheval),
]
