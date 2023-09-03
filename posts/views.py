from django.db.models import Q
from django.shortcuts import  render, redirect

from posts.models import Post, Hashtag
from posts.forms import PostCreateForm

from posts.constants import PAGINATION_LIMIT

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')




def posts_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        print(page)

        max_page = posts.__len__() / PAGINATION_LIMIT

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        if search:
            """startswith, endswith, icontains"""
            posts = posts.filter(Q(title__icontains=search) | Q(description__icontains=search))
            # posts = posts.filter(title__icontains=search, description__icontains=search)

        posts = posts[PAGINATION_LIMIT * (page-1): PAGINATION_LIMIT * page]

        context_data = {
            'posts' : posts,
            'user' : request.user,
            'pages' : range(1, max_page+1)
        }

        return render(request, 'posts/posts.html', context=context_data)

def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()

        context_hashtags = {
            'hashtags': hashtags
        }

        return render(request, 'posts/hashtagse.html', context=context_hashtags )

def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)

        context_data = {
            'post' : post
        }
        return render(request, 'posts/detail.html', context=context_data)

def posts_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': PostCreateForm
        }
        return render(request, 'posts/create.html', context=context_data)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = PostCreateForm(data,files)

        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect('/posts/')

        context_data = {
            'form': form
        }

        return render(request, 'posts/create.html', context=context_data)