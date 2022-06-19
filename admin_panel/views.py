from django.http import HttpRequest
from django.shortcuts import render


def all_articles(request: HttpRequest):
    return render(request, 'admin_panel/articles/articles_list.html', {})
