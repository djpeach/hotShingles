from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Shingle(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    rooms_availabe = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('shingles:list_all_shingles')
