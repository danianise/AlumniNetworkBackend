from .serializers import NetworkSerializer, PostSerializer, CommentSerializer, UserSerializer
from rest_framework import generics
from .models import Network, User, Post, Comment

# Create your views here.
class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class NetworkList(generics.ListCreateAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()

class NetworkDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()