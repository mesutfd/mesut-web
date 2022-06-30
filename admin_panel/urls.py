from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='super-admin-panel'),
    path('articles/', ArticlesListView.as_view(), name='article-edit-list'),
    path('articles/edit/<pk>', ArticleEditPage.as_view(), name='article-edit-page'),
]