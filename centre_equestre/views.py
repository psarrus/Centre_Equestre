from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect

def homepage(request):
    return render(request,"homepage.html")

class UserListView(ListView):
    model = User
    template_name = 'registration/registration_form.html'
    context_object_name = 'users'
    queryset = User.objects.all()
