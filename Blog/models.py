from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    Name = models.CharField(max_length=200)
    def __str__(self):
        return self.Name
class Post(models.Model):
     Host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
     Topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
     Title = models.CharField(max_length=500)
     Content = models.TextField()
     Updated  = models.DateTimeField(auto_now=True)
     Created = models.DateTimeField(auto_now_add=True)
     class Meta:
         ordering = ['-Updated','-Created']
     def __str__(self):
         return self.Title

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    updated  = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[0:50]
