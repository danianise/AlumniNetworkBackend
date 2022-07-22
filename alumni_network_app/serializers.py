from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Network, Post, Comment, Event, Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'photo', 'location', 'linkedin', 'github', 'facebook', 'twitter', 'instagram',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'body', 'timestamp')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'network', 'topic', 'author', 'body', 'imageURL', 'timestamp',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'id')

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('name', 'email', 'password', 'photo', 'location', 'linkedin', 'github', 'facebook', 'twitter', 'instagram', 'networks')



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'location', 'dateTime', 'description')

class NetworkSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        many = True
    )
    # users = UserSerializer(
    #     many = True
    # )
    events = EventSerializer(
        many = True
    )
    class Meta:
        model = Network
        fields = ('name', 'location', 'logo', 'users', 'posts', 'events')