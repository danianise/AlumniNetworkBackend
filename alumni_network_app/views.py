from .serializers import EventSerializer, NetworkSerializer, PostSerializer, CommentSerializer, UserSerializer
from rest_framework import generics, permissions
from .models import Network, User, Post, Comment, Event

# Create your views here.

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # permission_classes = [permissions.IsAuthenticated]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # permission_classes = [permissions.IsAuthenticated]

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # permission_classes = [permissions.IsAuthenticated]

# class PostListProtected(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     permission_classes = [permissions.IsAuthenticated]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # permission_classes = [permissions.IsAuthenticated]

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

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # permission_classes = [permissions.IsAuthenticated]

class CommentDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    # permission_classes = [permissions.IsAuthenticated]

class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    # permission_classes = [permissions.IsAuthenticated]

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    # permission_classes = [permissions.IsAuthenticated]