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
from .forms import HackForm, CommentForm
from .models import Hack, Comment
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic

"""Add a Hack"""

class CreateHack(LoginRequiredMixin, CreateView):
    model = Hack
    template_name = "hacks/create_hack.html"
    fields = ["category", "title", "ingredients", "description", "image"]
    success_url = "/hacks/hacks/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'You have successfully created a Hack.')
        return super().form_valid(form)

"""Create a comment"""

class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "hacks/create_comment.html"
    fields = ["comment_text"] 

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.name = self.request.user.username 
        form.instance.email = self.request.user.email 
        form.instance.hack = get_object_or_404(Hack, pk=self.kwargs['hack_id'])
        messages.success(self.request, 'Your comment has been added successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        hack_id = self.object.hack.id
        return reverse('hack_detail', args=[hack_id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['hack_id']
        return context


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

"""View a single hack"""

class HackDetail(DetailView):
    model = Hack
    template_name = "hacks/hack_detail.html"
    context_object_name = "hack"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(active=True)
        context['new_comment'] = None
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        hack = self.get_object()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.hack = hack
            new_comment.save()
        return self.get(request, *args, **kwargs)




"""Delete hack"""

class DeleteHack(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hack
    success_url = '/hacks/hacks/'

    """ display message after successful deletion """

    def form_valid(self, form):
     
        messages.success(self.request, 'Your hack has been deleted successfully.')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().created_by

    
"""Edit Hack"""

class EditHack(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name= 'hacks/edit_hack.html'
    model = Hack
    form_class = HackForm
    success_url = '/hacks/hacks/'

    """ display message after successful edit """

    def form_valid(self, form):
        messages.success(self.request, 'Your hack has been updated successfully.')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().created_by

    def get_success_url(self):
        hack_id = self.object.id
        return reverse('hack_detail', args=[hack_id])
