from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


@receiver(post_save, sender=Post)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('Testing signals, post created!')