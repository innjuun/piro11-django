from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', {'post_list': qs, 'q': q, })

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
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

def post_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'new posting is saved')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form' : form,
    })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'new posting is edited')
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form' : form,
    })
