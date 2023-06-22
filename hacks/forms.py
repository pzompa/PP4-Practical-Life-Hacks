from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Hack

"""Form to create a recipe"""


class HackForm(forms.ModelForm):
    ingredients = forms.CharField(widget=RichTextWidget())
    instructions = forms.CharField(widget=RichTextWidget())

    class Meta:
        model = Hack
        fields = [
            "category",
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
        ]
        widgets = {
            "ingredients": RichTextWidget(),
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "title": "Title",
            "description": "Description",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "image": "Image",
            "category": "Category",
        }


# class CommentForm(forms.ModelForm):
#     """ Create Comment Form """
#     body = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

#     class Meta:
#         """Get comment model, choose fields to display"""
#         model = Comment
#         fields = ('description', 'title')
#       labels = {
#       'title' : 'Hach Title',
#       'comment' : 'Comment'}
