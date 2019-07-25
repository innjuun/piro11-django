from django.conf.urls import url
from django.urls import path
from . import views
from . import views_cbv
app_name ='dojo'
urlpatterns = [
    path('new/', views.post_new),
    path('<int:id>/edit/', views.post_edit, name="post_edit"),
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    path('hello/<str:name>/<int:age>/', views.hello),

    path('list1/', views.post_list1),
    path('list2/', views.post_list2),
    path('list3/', views.post_list3),
    path('excel/', views.excel_download),

    path('cbv/list1/', views_cbv.post_list1),
    path('cbv/list2/', views_cbv.post_list2),
    #path('cbv/list3/', views_cbv.post_list3),
    #path('cbv/excel/', views_cbv.excel_download)
]