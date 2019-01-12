from django.db import models
from django.urls import reverse


class Shingle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('shingles:shingle-detail', kwargs={'pk': self.id})
