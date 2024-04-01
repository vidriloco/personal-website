from django.urls import path
from world.views import *

urlpatterns = [
    path('', index, name='index')
]