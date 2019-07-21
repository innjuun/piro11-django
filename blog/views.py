from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', {'post_list': qs, 'q': q, })

# def indexV(request):
#
#     return render(request, 'blog/index.html')
#
#
# def postV(request):
#     rqst = request.POST
#
#     context = {
#         'ctx': rqst
#     }
#     return render(request, 'blog/posting.html', context)
#

# def regV(request):
#     if request.method == 'POST':
#         rqst = request.POST
#         user = User()
#         user.idd = request.POST['firstInp']
#         user.password = request.POST['longInp']
#         user.save()
#         context = {'ctx' : rqst}
#         return render(request, 'blog/register.html', context)
#
#     elif request.method == 'GET':
#         return render(request, 'blog/register.html')
#
#
#
#
# def searchV(request):
#     rqst = request.GET
#     print(rqst.get("firstInp"))
#     context = {
#         'ctx' : rqst
#     }
#     return render(request, 'blog/search.html', context)