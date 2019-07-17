from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    url(r'^sum/(?P<a>\d+)/$', views.mysum),
    path('sum/<int:a>/<int:b>/', views.mysum),
    path('sum/<int:a>/<int:b>/<int:c>/', views.mysum),
]