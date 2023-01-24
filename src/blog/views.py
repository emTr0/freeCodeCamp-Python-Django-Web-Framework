from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import ArticleModelForm
from .models import Article


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() # <blog>/<modelname>_list.html
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
