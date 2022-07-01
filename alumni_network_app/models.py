from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

class Network(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

class SocialMedia(models.Model):
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
# blank=True and null=True so these fields can be blank

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=100)
    socialmedia = models.ForeignKey(SocialMedia, null=True, on_delete=models.SET_NULL)
    network = models.ForeignKey(Network, on_delete=models.PROTECT)
    # can networks be plural? need option for more than one...
# on_delete=models.SET_NULL will set this to null if referenced object is deleted
# on_delete=models.PROTECT will not allow referenced object to be deleted

class Conversation(models.Model):
    network = models.ForeignKey(Network, on_delete=models.PROTECT)
    topic = models.CharField(max_length = 100)

class Post(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    body = models.TextField()

