from django.contrib import admin
from . models import Hack
from . models import Comment
from . models import Bookmark
from . models import LikeHack
from . models import LikeComment


@admin.register(Hack)
class HackAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category','created_by', 'description','image')
    search_fields = ['title', 'description', 'category']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'hack_id')
    search_fields = ['comment_text']

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'bookmarked_hack','bookmarked_on')
    search_fields = ['bookmarked_hack']

@admin.register(LikeHack)
class LikeHackAdmin(admin.ModelAdmin):
    list_display = ('user', 'liked_hack_on','liked_hack')
    search_fields = ['liked_hack']

@admin.register(LikeComment)
class LikeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'liked_comment_on','liked_comment')
    search_fields = ['liked_comment']