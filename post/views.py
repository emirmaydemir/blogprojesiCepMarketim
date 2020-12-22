from django.shortcuts import render,get_object_or_404,HttpResponsePermanentRedirect,redirect,Http404
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.utils.text import slugify
from django.db.models import Q
# Create your views here.
def home_view(request):
    return render(request,'home.html',{})
def post_index(request):
    post_list = Post.objects.all()
    query=request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'index.html',{'posts':posts})


def post_detail(request,slug):
    post=get_object_or_404(Post,slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponsePermanentRedirect(post.get_absolute_url())
    context={
        'post':post,
        'form':form,
    }
    return render(request,'detail.html',context)


def post_create(request):
    if not request.user.is_authenticated:
        return Http404

    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post=form.save(commit=False)
        post.user=request.user
        post.save()
        messages.success(request,'Başarılı bir şekilde oluşturdunuz. ')
        return HttpResponsePermanentRedirect(post.get_absolute_url())
    context={
        'form':form,
    }
    return render(request,'form.html',context)


def post_update(request,slug):
    if not request.user.is_authenticated:
        return Http404

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,request.FILES or None,instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde güncellediniz. ')
        return HttpResponsePermanentRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)

def post_delete(request,slug):
    if not request.user.is_authenticated:
        return Http404

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')
