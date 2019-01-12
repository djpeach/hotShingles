from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Hottie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse('hotties:hottie-detail', kwargs={'pk': self.id})
