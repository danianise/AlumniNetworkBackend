from re import S
from django.contrib import admin
from .models import Network, User, Post, Comment, Event, Profile

admin.site.register(Network)
# admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Profile)