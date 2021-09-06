from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from App_Post.models import Post, Like
from accounts.models import Follow


@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post=Like.objects.filter(user=request.user)
    liked_list=liked_post.values_list('post', flat=True)
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__contains=search)
        context = {
            'search': search,
            'result': result,
            'following_list': following_list,
            'posts':posts,
            'liked_list':liked_list
        }
    return render(request, 'app_post/index.html', context)

@login_required
def liked(request, pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post, user=request.user)
    if not already_liked:
        liked_post=Like(post=post, user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('home'))

@login_required
def unliked(request, pk):
    post=Post.objects.get(pk=pk)
    already_liked=Like.objects.filter(post=post, user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))