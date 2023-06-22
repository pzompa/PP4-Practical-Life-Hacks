from django.urls import path
from .views import CreateHack, Hacks

urlpatterns = [
    path('', CreateHack.as_view(), name='create_hack'),
    path('hacks/', Hacks.as_view(), name= 'hacks'),
   
]