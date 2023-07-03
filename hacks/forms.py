from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Hack, Comment

"""Form to create a recipe"""


class HackForm(forms.ModelForm):
    ingredients = forms.CharField(widget=RichTextWidget())
    description = forms.CharField(widget=RichTextWidget())

    class Meta:
        model = Hack
        fields = [
            "category",
            "title",
            "ingredients",
            "description",
            "image",
        ]
        widgets = {
            "ingredients": RichTextWidget(),
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "category": "Category",
            "title": "Title",
            "ingredients": "Ingredients",
            "description": "Description",
            "image": "Image",
        }


""" Create Comment Form """


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment_text')
