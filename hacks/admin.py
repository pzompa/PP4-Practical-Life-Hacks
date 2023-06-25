from django.contrib import admin
from .models import (
    Hack, Comment, Bookmark, LikeHack, LikeComment,
    Favorite
)



@admin.register(Hack)
class HackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created_by", "description", "image")
    search_fields = ["title", "description", "category"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "name", "created_on", "active", "email")
    list_filter = ["active", "created_on", "updated_on"]
    search_fields = ("name", "email", "comment_text")

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "bookmarked_hack", "bookmarked_on")
    search_fields = ["bookmarked_hack"]


@admin.register(LikeHack)
class LikeHackAdmin(admin.ModelAdmin):
    list_display = ("user", "liked_hack_on", "liked_hack")
    search_fields = ["liked_hack"]


@admin.register(LikeComment)
class LikeCommentAdmin(admin.ModelAdmin):
    list_display = ("user", "liked_comment_on", "liked_comment")
    search_fields = ["liked_comment"]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "hack", "created_at")
    search_fields = ["id"]
