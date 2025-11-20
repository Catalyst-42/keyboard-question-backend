from django.contrib import admin
from .models import Corpus, Keyboard, Layout, LayoutPreview, Metric

@admin.register(Corpus)
class CorpusAdmin(admin.ModelAdmin):
    list_display = ['name', 'unique_symbols', 'size', 'language']
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
