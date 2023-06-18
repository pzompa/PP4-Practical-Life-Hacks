from django.contrib import admin
from . models import Hack


@admin.register(Hack)
class HackAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_by', 'description','image',)
    search_fields = ['title', 'description', 'category']

