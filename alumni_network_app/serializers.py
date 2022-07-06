from rest_framework import serializers
from .models import Network, User, Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'author', 'body',)

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(
        # view_name='CommentDetail',
        many = True,
        # read_only = True
    )
    class Meta:
        model = Post
        fields = ('network', 'topic', 'author', 'title', 'body', 'comments',)
