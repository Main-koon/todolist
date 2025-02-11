from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.CharField(max_length=10)

