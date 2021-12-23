from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text