"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from django.shortcuts import redirect

def root(request):
    return redirect('blog:post_list')

urlpatterns = [
    path('', root, name="root"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name="accounts"),
    path('core/', include('core.urls'), name='core'),
    path('blog/', include('blog.urls'), name="blog"),
    path('shop/', include('shop.urls'), name="shop"),
    re_path(r'^dojo/', include('dojo.urls'), name="dojo"),
# namespace 지정하면 오류남.. 그래서 각 app의 url에 app_name을 지정하긴 했는데,
    #이럴 경우에 project urls의 각 path에서 name을 제거했을때 오류가 또 안뜸. 뭐지?

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
    ]
