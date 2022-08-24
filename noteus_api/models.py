from django.db import models
from django.db.models import Model

class Note(Model):
    # this is not working
    text_content = models.TextField()

    def __str__(self):
        return self.text_content