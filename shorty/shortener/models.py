from django.db import models
# import uuid

# Create your models here.


class URL(models.Model):
    key = models.CharField(primary_key=True, max_length=100, unique=True)
    url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

