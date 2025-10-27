from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import Bigramm, Corpus, Frequency, Keyboard, Layout, Metric
from .serializers import (BigrammSerializer, CorpusSerializer,
                          FrequencySerializer, KeyboardSerializer,
                          LayoutSerializer, MetricSerializer)


class CorpusViewSet(viewsets.ModelViewSet):
    queryset = Corpus.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = CorpusSerializer

class KeyboardViewSet(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = KeyboardSerializer

class LayoutViewSet(viewsets.ModelViewSet):
    queryset = Layout.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = LayoutSerializer

class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = MetricSerializer

class FrequencyViewSet(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = FrequencySerializer

class BigrammViewSet(viewsets.ModelViewSet):
    queryset = Bigramm.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    serializer_class = BigrammSerializer
