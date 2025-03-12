"""
Signals are used to perform some action after a particular event is triggered.
In this case, we want to perform some action after a new post is created.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def my_model_post_save(sender, **kwargs):
    print("Request finished!")
