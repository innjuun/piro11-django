from django.urls import path
from . import views

app_name = 'core'

urlpatterns =[
    path('', views.home, name='home'),
    path('article_list/', views.article_list, name='article_list'),
    path('article_detail/<int:pk>', views.article_detail, name='article_detail'),
]