from django.db import models


class Corpus(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    unique_symbols = models.IntegerField()
    size = models.IntegerField()

    class Meta:
        verbose_name = 'корпус'
        verbose_name_plural = 'корпуса'

    def __str__(self):
        return self.name

class Keyboard(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    form_factor = models.CharField(max_length=32)
    keys = models.IntegerField()
    rows = models.IntegerField()
    keyboard_model = models.FileField(upload_to='keyboard_models/')  # YAML
    keyboard_preview = models.ImageField(upload_to='keyboard_previews/')

    class Meta:
        verbose_name = 'клавиатура'
        verbose_name_plural = 'клавиатуры'

    def __str__(self):
        return self.name

class Layout(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=128)
    layout_model = models.FileField(upload_to='layout_models/')  # YAML

    class Meta:
        verbose_name = 'раскладка'
        verbose_name_plural = 'раскладки'

    def __str__(self):
        return f"{self.name} ({self.language})"

class LayoutPreview(models.Model):
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)

    layout_preview = models.ImageField(upload_to='layout_previews/')

    class Meta:
        verbose_name = 'превью раскладки'
        verbose_name_plural = 'превью раскладок'
        unique_together = ['layout', 'keyboard']

    def __str__(self):
        return f"{self.layout.name} on {self.keyboard.name}"

class Metric(models.Model):
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)
    layout = models.ForeignKey(Layout, on_delete=models.CASCADE)

    frequency_heatmap = models.ImageField(upload_to='frequency_heatmaps/')

    # Travel distance
    travel_distance = models.FloatField()
    travel_distance_finger_1 = models.FloatField()
    travel_distance_finger_2 = models.FloatField()
    travel_distance_finger_3 = models.FloatField()
    travel_distance_finger_4 = models.FloatField()
    travel_distance_finger_5 = models.FloatField()
    travel_distance_finger_6 = models.FloatField()
    travel_distance_finger_7 = models.FloatField()
    travel_distance_finger_8 = models.FloatField()
    travel_distance_finger_9 = models.FloatField()
    travel_distance_finger_10 = models.FloatField()
    
    # Hand usage (%)
    hand_usage_left_hand = models.FloatField()
    hand_usage_right_hand = models.FloatField()
    
    # Finger usage (%)
    finger_usage_1 = models.FloatField()
    finger_usage_2 = models.FloatField()
    finger_usage_3 = models.FloatField()
    finger_usage_4 = models.FloatField()
    finger_usage_5 = models.FloatField()
    finger_usage_6 = models.FloatField()
    finger_usage_7 = models.FloatField()
    finger_usage_8 = models.FloatField()
    finger_usage_9 = models.FloatField()
    finger_usage_10 = models.FloatField()

    # Row usage (%)
    row_usage_top = models.FloatField()
    row_usage_home = models.FloatField()
    row_usage_bottom = models.FloatField()

    # Scissors (%)
    scissor_bigrams_left_hand = models.FloatField()
    scissor_bigrams_right_hand = models.FloatField()

    # Same finger bigrams (%)
    same_finger_bigrams_left_hand = models.FloatField()
    same_finger_bigrams_right_hand = models.FloatField()

    # Alternating finger bigrams (%)
    alternating_finger_bigrams_left_hand = models.FloatField()
    alternating_finger_bigrams_right_hand = models.FloatField()

    # Rolling (%)
    inrolls = models.FloatField()
    outrolls = models.FloatField()

    class Meta:
        verbose_name = 'метрика'
        verbose_name_plural = 'метрики'

    def __str__(self):
        return f"Metric: {self.corpus.name} - {self.keyboard.name} - {self.layout.name}"

class Frequency(models.Model):
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)
    key = models.CharField(max_length=1)
    entrances = models.IntegerField()

    class Meta:
        verbose_name = 'частота'
        verbose_name_plural = 'частоты'

    def __str__(self):
        return f"{self.key}: {self.entrances} ({self.corpus.name})"

class Bigramm(models.Model):
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)
    pair = models.CharField(max_length=2)
    entrances = models.IntegerField()

    class Meta:
        verbose_name = 'биграмма'
        verbose_name_plural = 'биграммы'

    def __str__(self):
        return f"{self.pair}: {self.entrances} ({self.corpus.name})"
