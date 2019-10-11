from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'bloggers_adda/home.html')

def about(request):
    return HttpResponse('<h1>Bloggers Adda About Page</h1>')
