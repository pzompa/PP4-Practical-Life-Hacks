from django.urls.base import reverse
from django.views.generic import CreateView
from .models import Hack
from .models import Comment
from django import forms
from .forms import HackForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateHack(LoginRequiredMixin, CreateView):
    model = Hack
    template_name = 'hacks/create_hack.html'
    fields = ['title', 'description', 'category', 'ingredients','image']
    success_url = '/hacks/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class Comment(LoginRequiredMixin, CreateView):
    
    model = Comment
    template_name = 'hacks/comment.html'
    fields = ['comment_text', 'author']
    success_url = '/hacks/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


