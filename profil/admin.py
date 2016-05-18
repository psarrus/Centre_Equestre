from django.contrib import admin
from profil.models import Profil, Periode


class PeriodeInlineAdmin(admin.TabularInline):
    model = Periode
    extra = 1


class ProfilAdmin(admin.ModelAdmin):
    list_display  = ['nom', 'prenom', 'cp', 'ville', 'adresse', 'email', 'tel_1']
    inlines = [PeriodeInlineAdmin]



admin.site.register(Profil, ProfilAdmin)
