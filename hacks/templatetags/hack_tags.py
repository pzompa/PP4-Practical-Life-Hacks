from django import template
from hacks.models import Like

register = template.Library()


@register.simple_tag
def is_favorited_by_user(hack, user):
    if user.is_authenticated:
        return hack.favorite_set.filter(user=user).exists()
    else:
        return False


@register.simple_tag
def get_favorite(hack, user):
    if user.is_authenticated:
        return Favorite.objects.filter(hack=hack, user=user).first()
    else:
        return False


@register.simple_tag
def is_liked_by_user(hack, user):
    if user.is_authenticated:
        return Like.objects.filter(hack=hack, user=user).exists()
    else:
        return False
