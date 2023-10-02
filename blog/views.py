from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from .models import Article, Category, Comment, Message, Like
from django.core.paginator import Paginator
from .forms import ContactUSForm, MessageForm


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)

    return render(request, "blog/article_details.html", {'article': article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get("page")
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, "blog/articles_list.html", {'articles': object_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog/articles_list.html", {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get("page")
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, "blog/articles_list.html", {'articles': object_list})


def contactus(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    return render(request, "blog/contact_us.html", {'form': form})


def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
    return redirect('blog:article_detail', slug)


class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.like.filter(article__slug=self.object.slug, user_id=self.request.user.id):
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context

