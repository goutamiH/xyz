from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     # add any custom fields here
#     pass
#model to store user's data coming from contact us form
class contact_us_model(models.Model):
    name=models.CharField(max_length=200,blank=True)
    email=models.EmailField()
    subject=models.CharField(max_length=400,blank=False)
    message = models.TextField(blank=False)
    #date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.name

class Topic(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=300)
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    description=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.name

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    room=models.ForeignKey(Room,on_delete=models.SET_NULL,null=True)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.body[0:45]

class Diary_Writing(models.Model):
    text = models.TextField(null=True,blank=True)
    data_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-data_created',)
        verbose_name_plural = 'Diary'


class ShareStory(models.Model):
    name=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    story_title=models.TextField(max_length=200,null=True)
    story=models.TextField(max_length=2000)
    def __str__(self):
        return self.name
    