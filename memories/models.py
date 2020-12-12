from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
