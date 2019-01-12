from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from . import models, forms


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
