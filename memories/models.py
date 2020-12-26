from django.contrib.auth.models import User
# from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.urls import reverse


class Place(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated_at']
        indexes = [models.Index(fields=['name'])]
        # indexes = [GinIndex(fields=['name'])]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('memories:memory', args=[self.id])
