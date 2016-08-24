from django.shortcuts import get_object_or_404, render
from django import forms


from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from .models import Article, Comment
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

# представление в виде списка статей
class ArticlesView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/article_list.html'

    def get_queryset(self):
        articles = Article.objects.annotate(Count('comments')).order_by('-id')
        
        # разбивка на страницы по 5 статей
        paginator = Paginator(articles, 5)
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        #articles.object_list.annotate(Count('comments'))
        return articles


# отображение одной статьи
class ArticleDetailView(DetailView):
    model = Article


# форма комментария
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('caption', 'commentText',)


# загрузка / добавление комментария
def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":  # добавление нового
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    # вывод комментариев к статье
    return render(request, 'blog/comment_list.html',
                  {'article': article})


# фильтрация по тегу
def tags(request, tag):
    articles_with_tag = (Article.objects.filter(tags__name__in=[tag]).annotate(Count('comments'))
                                        .order_by('-id'))
    return render(request, 'blog/article_list.html',
                  {'object_list': articles_with_tag})
