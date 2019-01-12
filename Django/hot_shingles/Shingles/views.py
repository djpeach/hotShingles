from django.shortcuts import render
from django.views import generic
from . import models


class ShingleListAll(generic.ListView):
    model = models.Shingle


class ShingleDetail(generic.DetailView):
    model = models.Shingle
