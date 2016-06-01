from django.contrib import admin
from models import Cheval, Emplacement

admin.site.site_header = 'Centre equestre'


class ChevalAdmin(admin.ModelAdmin):
    list_display    = ['sire', 'nom', 'race', 'pedigree', 'annee_naissance', 'photo', 'date_entree', 'date_sortie', 'activite', 'remarques', 'statut', 'aptitude', 'emplacement']
    list_filter     = ['race', 'pedigree', 'annee_naissance', 'activite', 'statut', 'aptitude']
    ordering        = ['sire', 'nom', 'race', 'pedigree', 'annee_naissance', 'photo', 'date_entree', 'date_sortie', 'activite', 'remarques', 'statut', 'aptitude', 'emplacement']
    search_fields   = ['sire', 'nom', 'race', 'pedigree', 'annee_naissance', 'photo', 'date_entree', 'date_sortie', 'activite', 'remarques', 'statut', 'aptitude', 'emplacement']

admin.site.register(Cheval, ChevalAdmin)


class EmplacementAdmin(admin.ModelAdmin):
    list_display    = ['zone', 'box']
    list_filter     = ['zone']
    ordering        = ['zone', 'box']
    search_fields   = ['zone', 'box']

admin.site.register(Emplacement, EmplacementAdmin)
