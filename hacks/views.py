from django.urls.base import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView, ListView, 
    DetailView, DeleteView,
    UpdateView)
from django import forms
from django.shortcuts import render
from .models import Hack, Comment
from django.views import View
from .forms import HackForm




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





