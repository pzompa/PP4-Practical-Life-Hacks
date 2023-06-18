from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djrichtextfield.models import RichTextField


CATEGORY = ("choose your category", "Choose Your Category"),("beauty", "Beauty"), ("household", "Household"), ("health", "Health"), ("cleaning", "Cleaning"), ("others", "Others")

class Hack(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORY, default="Choose your category")
    ingredients = RichTextField(max_length=10000, default= 'unknown', null=False, blank=False)
    description = RichTextField(max_length=10000, null=False, blank=False)
    created_by = models.ForeignKey(User, related_name='hack_owner', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    # bookmarks = models.ManyToManyField(User, related_name='bookmarks')
    image = CloudinaryField('image', default='placeholder')

"""To sort hacks search"""
class Meta:
    ordering = ['-created_on']
    
def __str__(self):
    return f"{self.title}"


# class Comment(models.Model):
#     """Model for Comment"""
#     hack = models.ForeignKey(
#         Hack, on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=80)
    
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now=True)

#     class Meta:
#         """ To display the comments by created_on in ascending order """
#         ordering = ['created_on']

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"
