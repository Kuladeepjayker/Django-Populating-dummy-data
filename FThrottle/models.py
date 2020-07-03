from django.db import models
from datetime import datetime

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name
