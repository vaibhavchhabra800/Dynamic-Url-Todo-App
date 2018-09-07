from django.db import models

# Create your models here.
class Comment(models.Model):
    title=models.TextField()
    description=models.TextField()
