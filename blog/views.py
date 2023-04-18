from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'J. K. Rowling',
        'title': "Harry Potter and the Philosopher's Stone",
        'content': 'First book',
        'data_posted': '1997'
    },
    {
        'author': 'J. K. Rowling',
        'title': 'Harry Potter and the Chamber of Secrets ',
        'content': 'Second book',
        'data_posted': '1998'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
