from django.db import models
from django.contrib.auth.models import AbstractUser


class Newspaper(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='newspapers'
    )
    publishers = models.ManyToManyField(
        Redactor, related_name='newspapers'
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
