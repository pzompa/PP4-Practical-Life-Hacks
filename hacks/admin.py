from django.contrib import admin
from .models import (
    Hack, Comment, Favorite, Like
)

@admin.register(Hack)
class HackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created_by", "description", "image")
    search_fields = ["title", "description", "category"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","comment_text", "name", "created_on", "active", "email")
    list_filter = ["active", "created_on", "updated_on"]
    search_fields = ("name", "email", "comment_text")


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "hack", "created_at")
    search_fields = ["id"]


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "hack", "category", "liked_at")
    search_fields = ["id"]