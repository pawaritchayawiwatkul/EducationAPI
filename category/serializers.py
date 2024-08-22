from rest_framework import serializers
from core.models import User
from category.models import SpeakingPracticeCategory, ListeningPracticeCategory

class SpeakingPracticeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingPracticeCategory
        fields = ("title", "code", "image_url")

class ListeningPracticeCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningPracticeCategory
        fields = ("title", "code", "image_url")
