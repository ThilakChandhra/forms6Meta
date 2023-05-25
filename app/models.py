from django.db import models
from django.core import validators

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(10)])

    def __str__(self) -> str:
        return self.topic_name