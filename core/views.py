from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.



def home(request):
    return render(request, 'core/home.html')

def article_list(request):
    articles = Article.objects.all()

    return render(request, 'core/article_list.html', {'articles':articles})

def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    #article = Article.objects.get.filter(id=1)
    #article = get_object_or_404(Article, id=1)

    return render(request, 'core/article_detail.html', {'article':article})