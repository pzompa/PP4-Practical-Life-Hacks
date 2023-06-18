from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djrichtextfield.models import RichTextField
import django.utils.timezone as tz

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
    ordering = ['created_on']
    
def __str__(self):
    return f"{self.title}"

