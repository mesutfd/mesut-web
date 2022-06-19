from django.urls import path
from .views import *

urlpatterns = [
    path('super-god-mode/', all_articles, name='super-admin-panel')
]