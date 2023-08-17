import datetime

from django.shortcuts import  render
from posts.models import Post, Hashtag

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')




def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context_data = {
            'posts' : posts
        }

        return render(request, 'posts/posts.html', context=context_data)

def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context_hashtags = {
            'hashtags': hashtags
        }

        return render(request, 'posts/hashtagse.html', context=context_hashtags )