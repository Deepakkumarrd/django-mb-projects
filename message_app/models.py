from django.db import models

# message_app/models.py
class Post(models.Model):
    text=models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.text[:50]