from django.contrib import admin
from .models import Corpus, Keyboard, Layout, LayoutPreview, Metric, Frequency, Bigramm

@admin.register(Corpus)
class CorpusAdmin(admin.ModelAdmin):
    list_display = ['name', 'unique_symbols', 'size']
    search_fields = ['name']

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ['name', 'form_factor', 'keys', 'rows']
    list_filter = ['form_factor']
    search_fields = ['name']

@admin.register(Layout)
class LayoutAdmin(admin.ModelAdmin):
    list_display = ['name', 'language']
    list_filter = ['language']
    search_fields = ['name', 'language']

@admin.register(LayoutPreview)
class LayoutPreviewAdmin(admin.ModelAdmin):
    list_display = ['keyboard', 'layout']
    list_filter = ['keyboard', 'layout']
    search_fields = ['keyboard', 'layout']

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ['corpus', 'keyboard', 'layout', 'travel_distance']
    list_filter = ['corpus', 'keyboard', 'layout']
    search_fields = ['corpus__name', 'keyboard__name', 'layout__name']

@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ['corpus', 'key', 'entrances']
    list_filter = ['corpus']
    search_fields = ['key', 'corpus__name']

@admin.register(Bigramm)
class BigrammAdmin(admin.ModelAdmin):
    list_display = ['corpus', 'pair', 'entrances']
    list_filter = ['corpus']
    search_fields = ['pair', 'corpus__name']
