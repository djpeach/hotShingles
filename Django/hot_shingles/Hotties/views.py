from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth import mixins, models as auth_models
from . import models, forms
from Shingles import models as shingles_models


def user_registration(req):
    if req.method == 'POST':
        form = forms.UserRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "Thanks for registering, hottie. Go ahead and login to start browsing our gorgeous shingles!")
            return redirect('hotties:login')
    else:
        form = forms.UserRegistrationForm()

    return render(req, 'hotties/hottie_form.html', {'form': form})


class HottieListAll(generic.ListView):
    model = models.Hottie


class HottieDetail(generic.DetailView):
    model = models.Hottie


class ShinglesListByUser(mixins.LoginRequiredMixin, generic.ListView):
    model = shingles_models.Shingle

    def get_queryset(self):
        user = get_object_or_404(auth_models.User, id=self.kwargs.get('pk'))
        hottie = get_object_or_404(models.Hottie, user=user)
        return shingles_models.Shingle.objects.filter(owner=hottie)
