from django.contrib import admin
from models import CreneauMontoir, PiquetMontoirStaff
from cheval.models import Cheval

# Register your models here.
admin.site.register(CreneauMontoir)
admin.site.register(PiquetMontoirStaff)

admin.site.register(Cheval)
