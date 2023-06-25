from django.urls import path
from .views import (
    CreateHack, Hacks,
    HackDetail, Comment, 
    DeleteHack, EditHack, 
    CreateComment)

urlpatterns = [
    path("", CreateHack.as_view(), name="create_hack"),
    path("hacks/", Hacks.as_view(), name="hacks"),
    path("<slug:pk>/", HackDetail.as_view(), name="hack_detail"),
    path("delete/<slug:pk>/", DeleteHack.as_view(), name="delete_hack_confirm"),
    path("edit/<slug:pk>/", EditHack.as_view(), name="edit_hack"),
    path('create_comment/', CreateComment.as_view(), name='create_comment'),
    path('create_comment/<int:hack_id>/', CreateComment.as_view(), name='create_comment'),
]

