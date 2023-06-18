from django.urls import path
from .views import CreateHack

urlpatterns = [
    path('', CreateHack.as_view(), name='create_hack'),
]