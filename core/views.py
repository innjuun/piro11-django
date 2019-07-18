from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Article


# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def article_list(request):
    articles = Article.objects.all().order_by('-id')

    return render(request, 'core/article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    # article = Article.objects.get.filter(id=1)
    # article = get_object_or_404(Article, id=1)

    return render(request, 'core/article_detail.html', {'article': article})


def article_create(request):
    if request.method == 'POST':
        print(request.POST)
        article = Article()
        article.title = request.POST['title']
        article.contents = request.POST['contents']
        article.author = request.POST['author']
        article.save()
        return redirect(reverse('core:article_detail', kwargs={'pk': article.pk}))

    elif request.method == 'GET':
        return render(request, 'core/article_create.html')


def article_update(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk) #Article.objects.get(pk=pk)
        article.title = request.POST['title']
        article.contents = request.POST['contents']
        article.author = request.POST['author']
        article.save()
        return redirect(reverse('core:article_detail', kwargs={'pk': article.pk}))
    elif request.method == 'GET':
        article = get_object_or_404(Article, pk=pk)
        return render(request, 'core/article_create.html', {"article" : article})

def article_delete(request, pk):        #안전하게 할거면 post, 아니면 get
    #articles = Article.objects.all()

    article = get_object_or_404(Article, pk=pk)
    # if article.unactivate:
    #     print('삭제된 게시글입니다.')
    article.delete()
    return redirect(reverse('core:article_list'))
