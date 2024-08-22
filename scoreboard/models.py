from django.db import models
from exercise.models import ListeningPractice, SpeakingPractice
from core.models import User

# Create your models here.

class ListeningScoreboard(models.Model):
    exercise = models.OneToOneField(ListeningPractice, models.CASCADE)
    
    def __str__(self) -> str:
        return self.exercise.title

class ListeningUserRanking(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    score = models.IntegerField()
    scoreboard = models.ForeignKey(ListeningScoreboard, models.CASCADE, "rankings")

    def __str__(self) -> str:
        return self.user.full_name
    
class SpeakingScoreboard(models.Model):
    exercise = models.OneToOneField(SpeakingPractice, models.CASCADE)

    def __str__(self) -> str:
        return self.exercise.title

class SpeakingUserRanking(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    score = models.IntegerField()
    scoreboard = models.ForeignKey(SpeakingScoreboard, models.CASCADE, "rankings")

    def __str__(self) -> str:
        return self.user.full_name
    