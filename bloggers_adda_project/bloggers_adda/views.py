from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'bloggers_adda/home.html', context)

def about(request):
    return render(request, 'bloggers_adda/about.html')
