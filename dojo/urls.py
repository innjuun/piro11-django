from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    path('hello/<str:name>/<int:age>/', views.hello),
    path('list1/', views.post_list1),
    path('list2/', views.post_list2),
    path('list3/', views.post_list3),
    path('excel/', views.excel_download)
]