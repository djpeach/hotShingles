from django.shortcuts import render
from django.urls import reverse_lazy
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


class ShingleEdit(generic.UpdateView):
    model = models.Shingle
    fields = '__all__'


class ShingleDelete(generic.DeleteView):
    model = models.Shingle
    success_url = reverse_lazy('shingles:list_all_shingles')
