from django.db import models

# Create your models here.
class Note(models.Model):
    text_content = models.TextField