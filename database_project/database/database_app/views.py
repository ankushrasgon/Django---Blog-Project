from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,"database_app/index.html",{'posts': posts})


def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request, 'database_app/post_detail.html', {'post': post})


@login_required
def post_new(request):
    form = PostForm()
    return render(request, 'database_app/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'database_app/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'database_app/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
     posts=Post.objects.filter(published_date__isnull=True).order_by('created_date')
     return render(request,'database_app/post_draft_list.html',{posts:posts})


@login_required
def post_publish(request, pk):
     post = get_object_or_404(Post, pk=pk)
     post.publish()
     return redirect('post_detail', pk=pk)

@login_required
def post_remove(request,pk):
    post= get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('homepage')

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'database_app/add_comment_to_post.html', {'form': form})