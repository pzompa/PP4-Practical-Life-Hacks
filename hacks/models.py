from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djrichtextfield.models import RichTextField
from django.utils.timezone import now


class Hack(models.Model):
    CATEGORY = (
        ("Beauty", "Beauty"),
        ("Household", "Household"),
        ("Health", "Health"),
        ("Cleaning", "Cleaning"),
        ("Others", "Others"),
    )

    title = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(
        max_length=50, choices=CATEGORY, default="Others"
    )
    ingredients = RichTextField(max_length=10000, default="", null=True)
    description = RichTextField(max_length=10000, null=False, blank=False)
    created_by = models.ForeignKey(
        User, related_name="hack_owner", on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField("image", default="placeholder")

    """To sort hacks search"""

    class Meta:
        ordering = ["-created_on"]

    def is_favorited_by_user(self, user):
        return self.favorite_set.filter(user=user).exists()

    def count_favorites(self):
        return self.favorite_set.count()

    def count_likes(self):
        return self.like_set.filter(category="hack").count()

    def count_comments(self):
        return self.comments.filter(active=True).count()

    def __str__(self):
        return f"{self.title}"


"""Model for Comment"""


class Comment(models.Model):
    hack = models.ForeignKey(Hack, on_delete=models.CASCADE,
                             related_name='comments')
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='comments')
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    comment_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return f'Comment by {self.name} on {self.hack}'


""" Model for Favorite """


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hack = models.ForeignKey(Hack, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


""" model for likes """


class Like(models.Model):
    CATEGORY = (
        ("hack", "Hack"),
        ("comment", "Comment"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hack = models.ForeignKey(Hack, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=50, choices=CATEGORY, default="hack"
    )
    liked_at = models.DateTimeField(auto_now_add=True)
