from rest_framework import serializers
from core.models import User
from exercise.models import ListeningPractice, ListeningQuestion, SpeakingPractice, SpeakingTargets

class ListeningQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestion
        fields = ("answer", "choice1", "choice2", "choice3", "choice4", "image")

class ListeningPracticeDetailSerializers(serializers.ModelSerializer):
    questions = ListeningQuestionSerializers(many=True, read_only=True)

    class Meta:
        model = ListeningPractice
        fields = ("image_url",  "questions")

class ListListeningPracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListeningPractice
        fields = ("title", "code", "released_date", "number_of_plays", "question_amount", "image_url")

class SpeakingTargetSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingTargets
        fields = ("text", "image")

class SpeakingPracticeDetailSerializers(serializers.ModelSerializer):
    targets = SpeakingTargetSerializers(many=True, read_only=True)

    class Meta:
        model = SpeakingPractice
        fields = ("targets", "image_url")

class ListSpeakingPracticeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpeakingPractice
        fields = ("title", "practice_type", "code", "released_date", "number_of_plays", "question_amount", "image_url")