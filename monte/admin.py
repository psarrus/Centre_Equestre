from django.contrib import admin
from models import CreneauMontoir
from profil.models import Profil
from cheval.models import Cheval

# Register your models here.
admin.site.register(CreneauMontoir)
admin.site.register(Profil)
admin.site.register(Cheval)
