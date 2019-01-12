from django.shortcuts import render
from django.views import generic
from . import models


class HottieListAll(generic.ListView):
    model = models.Hottie


class HottieDetail(generic.DetailView):
    model = models.Hottie
