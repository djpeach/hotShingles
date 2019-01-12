from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models


class ShingleCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Shingle
    fields = '__all__'


class ShingleListAll(generic.ListView):
    model = models.Shingle


class ShingleDetail(generic.DetailView):
    model = models.Shingle
