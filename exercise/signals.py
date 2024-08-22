from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ListeningQuestion

@receiver(post_save, sender=ListeningQuestion)
def update_child_count_on_save(sender, instance, **kwargs):
    parent = instance.exercise
    parent.question_amount = parent.children.count()
    parent.save()