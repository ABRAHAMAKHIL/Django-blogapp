from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),
    path('createPost/', views.newPost,name='createPost'),
    path('userPost/<str:pk>/',views.userPost,name='userPost'),
    path('updatePost/<str:pk>/',views.updatePost,name='updatePost'),
    path('deletePost/<str:pk>/',views.deletePost,name='deletePost'),
    path('myPost/<str:pk>/',views.myPost,name='myPost'),
    path('register',views.registerPage,name='register')
]
