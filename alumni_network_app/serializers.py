from rest_framework import serializers
from .models import Network, User, Post, Comment, Event

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'body')

class PostSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(
    #     # view_name='CommentDetail',
    #     many = True,
    #     # read_only = True
    # )
    class Meta:
        model = Post
        fields = ('network', 'topic', 'author', 'body',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'password', 'photo', 'location', 'linkedin', 'github', 'facebook', 'twitter', 'instagram', 'networks')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'location', 'dateTime', 'description', 'network')

class NetworkSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        many = True
    )
    users = UserSerializer(
        many = True
    )
    events = EventSerializer(
        many = True
    )
    class Meta:
        model = Network
        fields = ('name', 'location', 'logo', 'users', 'posts', 'events')