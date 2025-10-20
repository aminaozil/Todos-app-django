from django.conf import settings
from django.db import models
from django.utils import timezone

class Todos(models.Model):
    name = models.CharField(max_length=250, null=False)
    created_at = models.DateField(default=timezone.now)

    

    def __str__(self):
        return self.name
