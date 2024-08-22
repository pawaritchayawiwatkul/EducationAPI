from django.db import models
import random
import string
# from exercise.models import SpeakingPractice, ListeningPractice
# Create your models here.

class ListeningPracticeCategory(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    image_url = models.FileField()
    # practices = models.ManyToManyField(ListeningPractice, related_name="category")

    def generate_unique_code(self, length):
        """Generate a unique random code."""
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(length))
        return code
    
    def _generate_unique_code(self, length):
        """Generate a unique code and ensure it's not already in the database."""
        code = self.generate_unique_code(length)
        while ListeningPracticeCategory.objects.filter(code=code).exists():
            code = self.generate_unique_code(length)
        return code
    
    def save(self, *args, **kwargs):
        if self.code is None or self.code == "":
            self.code = "LI" + self._generate_unique_code(10)
        super(ListeningPracticeCategory, self).save(*args, **kwargs)

class SpeakingPracticeCategory(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    image_url = models.FileField()
    # practices = models.ManyToManyField(SpeakingPractice, related_name="category")

    def generate_unique_code(self, length):
        """Generate a unique random code."""
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(length))
        return code
    
    def _generate_unique_code(self, length):
        """Generate a unique code and ensure it's not already in the database."""
        code = self.generate_unique_code(length)
        while SpeakingPracticeCategory.objects.filter(code=code).exists():
            code = self.generate_unique_code(length)
        return code
    
    def save(self, *args, **kwargs):
        if self.code is None or self.code == "":
            self.code = "SP" + self._generate_unique_code(10)
        super(SpeakingPracticeCategory, self).save(*args, **kwargs)