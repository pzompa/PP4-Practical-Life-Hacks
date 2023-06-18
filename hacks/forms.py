from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Hack


class HackForm(forms.ModelForm):
    """Form to create a recipe"""

    ingredients = forms.CharField(widget=RichTextWidget())
    instructions = forms.CharField(widget=RichTextWidget())

    class Meta:
        model = Hack
        fields = [
            "title",
            "description",
            "ingredients",
            "image",
            "category",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "ingredients": RichTextWidget(),
           
        }
        labels = {
            "title": "Hack Title",
            "description": "Description",
            "ingredients": "Hack Ingredients",
            "instructions": "Hack Instructions",
            "image": "Hack Image",
            "category": "Hack Category",
        }


# class CommentForm(forms.ModelForm):
#     """ Create Comment Form """
#     body = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

#     class Meta:
#         """Get comment model, choose fields to display"""
#         model = Comment
#         fields = ('body',)




