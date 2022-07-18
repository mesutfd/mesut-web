from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView

from article_module.models import Article
HttpResponse



def index(request: HttpRequest):
    return render(request, 'admin_panel/admin_panel.html', {})


class ArticlesListView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'admin_panel/articles/article_list_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query


class ArticleEditPage(UpdateView):
    model = Article
    template_name = 'admin_panel/articles/article_edit_page.html'
    fields = '__all__'
    success_url = reverse_lazy('super-admin-panel')
