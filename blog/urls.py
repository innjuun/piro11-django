# blog/urls.py
from django.conf.urls import url
from django.urls import path
from . import views
from . import views_cbv


app_name='blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name ='post_new'),
    path('<int:id>/edit/', views.post_edit, name="post_edit"),
    path('cbv/new/', views_cbv.post_new),
    # path('index/', views.indexV),
    # path('index/posting', views.postV),
    # path('index/register', views.regV),
    # path('index/search', views.searchV)
]