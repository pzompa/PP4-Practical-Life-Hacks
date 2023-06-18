from django.urls.base import reverse
from django.views.generic import CreateView
from .models import Hack
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


# class CommentForm(forms.ModelForm):
#     """ Create Comment Form """
#     def __init__(self, *args, **kwargs):
#         super(CommentForm, self).__init__(*args, **kwargs)
#         self.fields['body'].widget = forms.Textarea(attrs={'rows': 3})

#     class Meta:
#         """Get comment model, choose fields to display"""
#         model = Comment
#         fields = ('body',)

  
