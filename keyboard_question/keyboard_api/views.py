from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET'])
def metrics_extremes(request):
    """Finds best and worst metric values by all reports."""
    extremes = {}
 
    metric_fields = [
        'travel_distance',
        'travel_distance_finger_1',
        'travel_distance_finger_2',
        'travel_distance_finger_3',
        'travel_distance_finger_4',
        'travel_distance_finger_5',
        'travel_distance_finger_6',
        'travel_distance_finger_7',
        'travel_distance_finger_8', 
        'travel_distance_finger_9',
        'travel_distance_finger_10',
        'finger_usage_1',
        'finger_usage_2',
        'finger_usage_3',
        'finger_usage_4',
        'finger_usage_5',
        'finger_usage_6',
        'finger_usage_7',
        'finger_usage_8',
        'finger_usage_9',
        'finger_usage_10',
        'row_usage_a',
        'row_usage_b',
        'row_usage_c',
        'row_usage_d',
        'row_usage_e',
        'row_usage_k',
        'same_finger_bigram_frequency',
        'same_finger_bigram_mean_distance',
        'same_finger_skipgram_frequency',
        'same_finger_skipgram_mean_distance',
        'half_scissor_bigram_frequency',
        'full_scissor_bigram_frequency',
        'half_scissor_skipgram_frequency',
        'full_scissor_skipgram_frequency',
        'lateral_stretch_bigram_frequency',
        'lateral_stretch_skipgram_frequency',
        'roll_frequency',
        'alternate_frequency',
        'onehand_frequency',
        'redirect_frequency'
    ]

    for field in metric_fields:
        ordered_field = Metric.objects.order_by(field)
        min_metric = ordered_field.first()
        max_metric = ordered_field.last()

        extremes[field] = {
            'min_value': getattr(min_metric, field) if min_metric else None,
            'max_value': getattr(max_metric, field) if max_metric else None,
            'min_object_url': reverse('metric-detail', args=[min_metric.id]) if min_metric else None,
            'max_object_url': reverse('metric-detail', args=[max_metric.id]) if max_metric else None,
        }

    return Response(extremes)
