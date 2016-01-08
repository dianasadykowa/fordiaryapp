from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=70)
    age = models.CharField(max_length=30)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Day(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    generaite_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Create your models here.
