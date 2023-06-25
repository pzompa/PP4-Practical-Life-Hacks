from django.urls.base import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, ListView, 
    DetailView, DeleteView,
    UpdateView)
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import HackForm
from .models import Hack, Comment, Favorite



class CreateHack(LoginRequiredMixin, CreateView):
    model = Hack
    template_name = "hacks/create_hack.html"
    fields = ["category", "title", "ingredients", "description", "image"]
    success_url = "/hacks/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class Comment(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "hacks/comment.html"
    fields = ["comment_text", "author"]
    success_url = "/hacks/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""View all hacks"""


class Hacks(ListView):
    model = Hack
    template_name = "hacks/hacks.html"
    context_object_name = "hacks"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            hacks = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(category__icontains=query) |
                Q(description__icontains=query)
            )
        else: 
            hacks = self.model.objects.all()
        return hacks

class HackDetail(DetailView):
    model = Hack
    template_name = "hacks/hack_detail.html"
    context_object_name = "hack"

 
"""Delete hack"""

class DeleteHack(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hack
    success_url = '/hacks/'

    def test_func(self):
        return self.request.user == self.get_object().created_by
    
"""Edit Hack"""

class EditHack(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name= 'hacks/edit_hack.html'
    model = Hack
    form_class = HackForm
    success_url = '/hacks/'

    def test_func(self):
        return self.request.user == self.get_object().created_by




