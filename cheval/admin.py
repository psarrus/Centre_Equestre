from django.contrib import admin
from models import Cheval, Emplacement, Journal

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


class JournalAdmin(admin.ModelAdmin):
    list_display    = ['cheval', 'date', 'motif', 'lieu']
    list_filter     = ['cheval', 'motif', 'lieu']
    ordering        = ['cheval', 'date', 'motif', 'lieu']
    search_fields   = ['cheval', 'date', 'motif', 'lieu']

admin.site.register(Journal, JournalAdmin)
