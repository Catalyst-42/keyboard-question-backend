from django.http import JsonResponse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Corpus, Keyboard, Layout, LayoutPreview, Metric
from .serializers import (CorpusSerializer, KeyboardSerializer,
                          LayoutPreviewSerializer, LayoutSerializer,
                          MetricSerializer)


class HealthCheckView(View):
    def get(self, request):
        return JsonResponse({
            'status': 'ok', 
        }, status=200)

class CorpusViewSet(viewsets.ModelViewSet):
    queryset = Corpus.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    serializer_class = CorpusSerializer

class KeyboardViewSet(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    serializer_class = KeyboardSerializer

class LayoutViewSet(viewsets.ModelViewSet):
    queryset = Layout.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['name', 'language']
    serializer_class = LayoutSerializer

class LayoutPreviewViewSet(viewsets.ModelViewSet):
    queryset = LayoutPreview.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['keyboard__id', 'layout__id']
    search_fields = ['keyboard__name', 'layout__name']
    serializer_class = LayoutPreviewSerializer

class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['corpus__id', 'keyboard__id', 'layout__id']
    search_fields = ['corpus__name', 'keyboard__name', 'layout__name']
    serializer_class = MetricSerializer
