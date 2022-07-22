from .serializers import EventSerializer, NetworkSerializer, PostSerializer, CommentSerializer, UserSerializer
from rest_framework import generics, permissions
from .models import Network, Post, Comment, Event
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class NetworkList(generics.ListCreateAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class NetworkDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    permission_classes = [permissions.IsAuthenticated]

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    permission_classes = [permissions.IsAuthenticated]