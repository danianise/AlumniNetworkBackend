from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

class Network(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name

# class SocialMedia(models.Model):
#     linkedin = models.URLField(blank=True, null=True)
#     github = models.URLField(blank=True, null=True)
#     facebook = models.URLField(blank=True, null=True)
#     twitter = models.URLField(blank=True, null=True)
#     instagram = models.URLField(blank=True, null=True)
# blank=True and null=True so these fields can be blank

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=100)
    # socialmedia = models.ForeignKey(SocialMedia, null=True, on_delete=models.SET_NULL, related_name='users')
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    network = models.ForeignKey(Network, on_delete=models.PROTECT, related_name='users')
    # can networks be plural? need option for more than one...
# on_delete=models.SET_NULL will set this to null if referenced object is deleted
# on_delete=models.PROTECT will not allow referenced object to be deleted
    def __str__(self):
        return self.name

class Post(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='posts', default='Invalid')
    topic = models.CharField(max_length=100, default='Life')
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.author
