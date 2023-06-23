from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djrichtextfield.models import RichTextField


class Hack(models.Model):
    CATEGORY = (
        ("choose your category", "Choose Your Category"),
        ("Beauty", "Beauty"),
        ("Household", "Household"),
        ("Health", "Health"),
        ("Cleaning", "Cleaning"),
        ("Others", "Others"),
    )

    title = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(
        max_length=50, choices=CATEGORY, default="choose your category"
    )
    ingredients = RichTextField(max_length=10000, default="", null=True)
    description = RichTextField(max_length=10000, null=False, blank=False)
    created_by = models.ForeignKey(
        User, related_name="hack_owner", on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # bookmarks = models.ManyToManyField(User, related_name='bookmarks')
    image = CloudinaryField("image", default="placeholder")

    """To sort hacks search"""

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"


# model for Comment#
class Comment(models.Model):
    # comment text
    comment_text = RichTextField(max_length=10000, default="", null=False, blank=False)
    # comment date
    created_on = models.DateTimeField(auto_now_add=True)
    # comment author
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.CharField(max_length=255)
    # comment for what Hack
    hack = models.ForeignKey(Hack, on_delete=models.CASCADE)


# model for likes#


class LikeComment(models.Model):
    # like counter
    # created on
    # user id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_comment_on = models.DateTimeField(auto_now_add=True)
    liked_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class LikeHack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_hack_on = models.DateTimeField(auto_now_add=True)
    liked_hack = models.ForeignKey(Hack, on_delete=models.CASCADE)


class Bookmark(models.Model):
    # what did i bookmark
    # when did i bookmark
    # who did bookmark
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmarked_on = models.DateTimeField(auto_now_add=True)
    bookmarked_hack = models.ForeignKey(Hack, on_delete=models.CASCADE)
