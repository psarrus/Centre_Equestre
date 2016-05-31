from django.contrib import admin
from models import RegistreSoins

admin.site.site_header = 'Centre equestre'


class RegistreSoinsAdmin(admin.ModelAdmin):
    list_display    = ['date', 'cheval', 'pathologie', 'acte', 'soigneur']
    list_filter     = ['cheval', 'pathologie', 'acte', 'soigneur']
    ordering        = ['date', 'cheval', 'pathologie', 'acte', 'soigneur']
    search_fields   = ['date', 'cheval', 'pathologie', 'acte', 'soigneur']

admin.site.register(RegistreSoins, RegistreSoinsAdmin)
