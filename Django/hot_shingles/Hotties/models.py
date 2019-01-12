from django.db import models
from django.urls import reverse


class Hottie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('hotties:hottie-detail', kwargs={'pk': self.id})
