from django.urls import path
from . import views

app_name = 'core'

urlpatterns =[
    path('', views.home, name='home'),
    path('article_list/', views.article_list, name='article_list'),
    path('article_detail/<int:pk>', views.article_detail, name='article_detail'),
    path('article_create/', views.article_create, name='article_create'),
    path('article_update/<int:pk>', views.article_update, name='article_update'),
    path('article_delete/<int:pk>', views.article_delete, name='article_delete'),
]