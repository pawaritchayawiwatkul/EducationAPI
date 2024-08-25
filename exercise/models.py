from django.db import models
from category.models import ListeningPracticeCategory, SpeakingPracticeCategory
import string
import random

class ListeningPractice(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=12)
    image_url = models.FileField(upload_to="images/practice")
    released_date = models.DateField(auto_now_add=True)
    number_of_plays = models.IntegerField(default=0)
    category = models.ManyToManyField(ListeningPracticeCategory, related_name="practices")
    question_amount = models.IntegerField(default=0)

    def generate_unique_code(self, length):
        """Generate a unique random code."""
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(length))
        return code
    
    def _generate_unique_code(self, length):
        """Generate a unique code and ensure it's not already in the database."""
        code = self.generate_unique_code(length)
        while ListeningPractice.objects.filter(code=code).exists():
            code = self.generate_unique_code(length)
        return code
    
    def save(self, *args, **kwargs):
        if self.code is None or self.code == "":
            self.code = "LI" + self._generate_unique_code(10)
        super(ListeningPractice, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title

class ListeningQuestion(models.Model):
    ANSWER_CHOICE = [
        ("1", "CHOICE 1"),
        ("2", "CHOICE 2"),
        ("3", "CHOICE 3"),
        ("4", "CHOICE 4"),
    ]
    answer = models.CharField(choices=ANSWER_CHOICE, default="1", max_length=1)
    choice1 = models.CharField(max_length=255)
    choice2 = models.CharField(max_length=255)
    choice3 = models.CharField(max_length=255)
    choice4 = models.CharField(max_length=255)
    image = models.FileField(upload_to="images/question")
    exercise = models.ForeignKey(ListeningPractice, on_delete=models.CASCADE, related_name="questions")

class SpeakingPractice(models.Model):
    PRACTICE_TYPE_CHOICE = [
        ("SW", "Speaking Word Practice"),
        ("SS", "Speaking Sentence Practice"),
        ("SP", "Speaking Paragraph Practice")
    ]
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    practice_type = models.CharField(choices=PRACTICE_TYPE_CHOICE, default="SW", max_length=2)
    category = models.ManyToManyField(SpeakingPracticeCategory,related_name="practices")
    image_url = models.FileField(upload_to="images/practice")
    released_date = models.DateField(auto_now_add=True)
    number_of_plays = models.IntegerField(default=0)
    question_amount = models.IntegerField(default=0)

    def generate_unique_code(self, length):
        """Generate a unique random code."""
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(length))
        return code
    
    def _generate_unique_code(self, length):
        """Generate a unique code and ensure it's not already in the database."""
        code = self.generate_unique_code(length)
        while SpeakingPractice.objects.filter(code=code).exists():
            code = self.generate_unique_code(length)
        return code
    
    def save(self, *args, **kwargs):
        if self.code is None or self.code == "":
            self.code = self.practice_type + self._generate_unique_code(10)
        super(SpeakingPractice, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
class SpeakingTargets(models.Model):
    text = models.TextField()
    targets = models.ForeignKey(SpeakingPractice, models.CASCADE, related_name="targets")
    image = models.FileField(upload_to="images/question")
