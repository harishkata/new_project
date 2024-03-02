from django.db import models

# Create your models here.
class tention(models.Model):
    study = models.CharField(max_length=20)
    score = models.IntegerField()