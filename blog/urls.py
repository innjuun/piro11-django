# blog/urls.py
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    # path('index/', views.indexV),
    # path('index/posting', views.postV),
    # path('index/register', views.regV),
    # path('index/search', views.searchV)
]