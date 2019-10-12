# DJango_Blog_Project
Creating an application for blogging using DJango

Steps followed :

1) pip install django

>> Collecting django ......etc.....
>> Successfully installed django-2.2.6 sqlparse-0.3.0

2) python -m django --version

>> 2.2.6    => This shows django was installed properly and shows the version

3) django-admin startproject bloggers_adda_project

>> => This creates a folder by name bloggers_adda_project along with contents needed for the project. This folder would contain manage.py file and another folder inside by the same name as the project folder name i.e. "bloggers_adda_project".

4) code .

>> => To open the project in VS Code editor.

5) cd bloggers_adda_project

>> => To move one level/directory/folder inside the created project folder to execute the runserver command.

6) python manage.py runserver

>> .......etc...
>> Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

=> This code runs the server using the manage.py file. Usually the port would be http://127.0.0.1:8000/ for Django projects.

7) Open web browser window and go to http://127.0.0.1:8000/ - we should be able to see django default web page which says "The install worked successfully! Congratulations!"

[You may need to stop server with <ctrl + c> before the next step]
8) python manage.py startapp bloggers_adda

>> => This creates a new App inside the project that we just created. A project can have multiple Apps running. Hence this step. 


# Steps to modify files created by django

1) views.py ==>>

Add code : 
```
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Bloggers Adda Home Page</h1>')
```
2) Create urls.py file in bloggers_adda (app folder) and add code : 
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bloggers_adda_home'),
]
```
3) bloggers_adda_project/urls.py ==>> 

Modify line :
```
from django.urls import path
```
to 
```
from django.urls import path, include
```

and to the urlpatterns list, add another line :
```
path('bloggers_adda/', include('bloggers_adda.urls')),
```

4) python manage.py runserver

>> => To run the server again after all the file modifications.

5) Browsing http://127.0.0.1:8000/ would now give a 404 page not found error since it does not match any url pattern that we created. Hence, we may have to try :

http://127.0.0.1:8000/admin/

or

http://127.0.0.1:8000/bloggers_adda/


# Adding another route (About page for example)

1) Modify views.py file in bloggers_adda ==>>

Add code :
```
def about(request):
    return HttpResponse('<h1>Bloggers Adda About Page</h1>')
```

2) Modify urls.py file in bloggers_adda ==>>

Add line to urlpatterns list :
```
path('about/', views.about, name='bloggers_adda_about'),
```

# Creating templates

1) Inside the bloggers_adda (app folder), create a folder by name 'templates'.

2) Create home.html, about.html, layout.html etc... and add the requied html codes.

3) bloggers_adda/apps.py ==>>

Copy class name : 'BloggersAddaConfig'

4) bloggers_adda_project/settings.py ==>>

Add line on top of the INSTALLED_APPS list 
```
INSTALLED_APPS = [
    'bloggers_adda.apps.BloggersAddaConfig',
```
5) bloggers_adda/views.py ==>>

Instead of return HttpRequest line, code :
```
return render(request, 'bloggers_adda/home.html')
```

# Added Bootstrap code

# Created 'static/bloggers_adda/' folder & Added main.css file

# Modified templates by adding more code

# Added base.html to contain all the common html code that would have otherwise been on all templates

# used code snippets for urls instead of hard coding them... for example :
```
{% load static %} 
```
=> has been used on base.html even before <!DOCTYPE html> which is to be noted in Django

Also used :

```
{% static 'bloggers_adda/main.css' %}  # => for stylesheet href

{% url 'bloggers_adda_home' %} # => for href link to home page instead of hardcoding /home/
{% url 'bloggers_adda_home' %} # => for href link to about page instead of hardcoding /about/
```