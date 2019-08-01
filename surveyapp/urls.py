from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('index', home, name='index'),
    path('subcat', subcat, name='subcat'),
    path('question', question, name='question'),

]
