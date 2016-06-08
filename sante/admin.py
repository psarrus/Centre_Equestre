from django.contrib import admin
from models import Soin

admin.site.site_header = 'Centre equestre'


class SoinAdmin(admin.ModelAdmin):
    list_display    = ['date', 'cheval', 'pathologie', 'acte', 'soigneur']
    list_filter     = ['cheval', 'pathologie', 'acte', 'soigneur']
    ordering        = ['date', 'cheval', 'pathologie', 'acte', 'soigneur']
    search_fields   = ['date', 'cheval', 'pathologie', 'acte', 'soigneur']

admin.site.register(Soin, SoinAdmin)
