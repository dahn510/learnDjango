from django.shortcuts import render
from django.http import HttpResponse

posts = [
        {
            'author': 'Potato',
            'title': 'Potato chips',
            'content': 'Potato chips are acutally overrated.',
        },
        {
            'author': 'Gaming mouse',
            'title': 'Razer mouse finally breaks',
            'content': 'Over the heavy usage of two years, the Razer DeathAdder Elite mouse finally stops registering mouse clicks.'
        }
]

def home(request):
    context = {
            'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
