from rest_framework import serializers
from .models import Corpus, Keyboard, Layout, LayoutPreview, Metric, Frequency, Bigramm

class CorpusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corpus
        fields = '__all__'

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__'

class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layout
        fields = '__all__'

class LayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = LayoutPreview
        fields = '__all__'

class MetricSerializer(serializers.ModelSerializer):
    corpus_name = serializers.CharField(source='corpus.name', read_only=True)
    keyboard_name = serializers.CharField(source='keyboard.name', read_only=True)
    layout_name = serializers.CharField(source='layout.name', read_only=True)
    
    class Meta:
        model = Metric
        fields = '__all__'

class FrequencySerializer(serializers.ModelSerializer):
    corpus_name = serializers.CharField(source='corpus.name', read_only=True)
    
    class Meta:
        model = Frequency
        fields = '__all__'

class BigrammSerializer(serializers.ModelSerializer):
    corpus_name = serializers.CharField(source='corpus.name', read_only=True)
    
    class Meta:
        model = Bigramm
        fields = '__all__'
