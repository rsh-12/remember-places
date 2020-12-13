from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Place(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False, max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('memories:memory', args=[self.id])
