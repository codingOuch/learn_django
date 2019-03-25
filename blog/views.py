from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'OuchMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 24, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 25, 2019'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

