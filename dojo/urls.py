from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    path('hello/<str:name>/<int:age>/', views.hello)
]