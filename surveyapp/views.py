from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import logout as lo

from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    form=UserCreationForm
    main_cat=main_category.objects.all()



    return render(request,'index.html',{'main_cat':main_cat})

def signup(request):
    form=UserCreationForm
    if request.method=='POST':
        f=form(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/index')
        else:
            m="Invalid data !!"
            return HttpResponse("Not valid Data")


    return render(request,'signup.html',{'form':form})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                return redirect('/index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html')
@login_required
def logout(request):
            lo(request)
            return redirect("/index")

def subcat(request):
    if request.method=='POST':
        mcat = request.POST.get('one')
        sub_cat = sub_category.objects.filter(sub_cat_name__icontains=mcat)

        return render(request,'index2.html',{'sub_cat':sub_cat})

def question(request):
    #if request.method=='POST':
        #c = request.POST.get('one')
        #ques = question.objects.filter(question__icontains=c)
        ques=question.objetcs.all()

        return render(request,'question.html',{'ques':ques})


