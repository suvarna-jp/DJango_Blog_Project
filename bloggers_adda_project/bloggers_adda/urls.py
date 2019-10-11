from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bloggers_adda_home'),
    path('home/', views.home, name='bloggers_adda_home'),
    path('about/', views.about, name='bloggers_adda_about'),
]