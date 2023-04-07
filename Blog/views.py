from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post , Topic
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def home(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''

    post = Post.objects.filter(Topic__Name__icontains=q)
    topic = Topic.objects.all()

    Updated = timezone.now()
    context = {'post':post,'time':Updated,'topic':topic}
    return render(request,'Blog/main.html',context)

def loginPage(request):
    page = 'login'
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'No Such User Exist')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Incorrect!')
    context = {'page':page}
    return render(request,'Blog/login_register.html',context)


def registerPage(request):
    form = UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user  = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Something went wrong')

    context = {'form':form}
    return render(request,'Blog/login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def newPost(request):
    form = PostForm()
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'Blog/createPost.html',context)

def userPost(request,pk):
    post = Post.objects.get(id=pk)

    context = {'post':post}
    return render(request,'Blog/userPost.html',context)


@login_required(login_url='login')
def updatePost(request,pk):

    old_post = Post.objects.get(id=pk)
    edited_post = PostForm(instance=old_post)
    if request.method=="POST":
        edited_post = PostForm(request.POST,instance=old_post)
        if edited_post.is_valid():
            edited_post.save()
            return redirect('home')

    context = {'post':edited_post}

    return render(request,'Blog/updatePost.html',context)



@login_required(login_url='login')
def deletePost(request,pk):
        postDelete = Post.objects.get(id=pk)
        if request.method == 'POST':
            postDelete.delete()
            return redirect('home')



        context = {'room':postDelete}
        return render(request,'Blog/deletePost.html',context)


def myPost(request,pk):
    user = User.objects.get(id=pk)
    post = Post.objects.filter(Host=user)

    context = {'post':post,'user':user}
    return render(request,'Blog/myPost.html',context)
