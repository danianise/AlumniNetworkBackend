from django.urls import path
from . import views

urlpatterns = [
    path('networks/', views.NetworkList.as_view(), name = 'network_list'),
    path('networks/<int:pk>/', views.NetworkDetail.as_view, name = 'network_detail'),

    path('users/', views.UserList.as_view(), name = 'user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user_detail'),

    path('posts/', views.PostList.as_view(), name = 'post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name = 'post_detail'),
    # path('posts/<int:post_id>/', views.PostDetail.as_view(), name = 'post_detail'),
    # path('posts_protected/', views.PostListProtected.as_view(), name='post_list_protected'),
    # path('posts2/', views.posts2),

    path('comments/', views.CommentList.as_view(), name = 'comment_list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name = 'comment_detail'),
    # path('comments/<int:comment_id>/', views.CommentDetail.as_view(), name = 'comment_detail'),

    path('events/', views.EventList.as_view(), name = 'event_list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name = 'event_detail')
]
