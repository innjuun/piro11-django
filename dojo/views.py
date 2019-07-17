# dojo/views.py
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os


# Create your views here.

def mysum(request, numbers):
    # request : HttpRequest
    # numbers = "1/2/3/4/5/2/5/...
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬 장고 메이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))


def post_list2(request):
    name = "공유"
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
   return JsonResponse({
       'message': 'hi python django',
       'items' : ['python', 'django', 'spring']
   }, json_dumps_params={'ensure_ascii' : False})


def excel_download(request):
    # filepath = 'C:\dev\my-first-django/excel.xlsx'
    filepath = os.path.join(settings.BASE_DIR, 'excel.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
