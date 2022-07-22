from django.urls import path
from . import views

urlpatterns = [
    path('networks/', views.NetworkList.as_view(), name = 'network_list'),
    path('networks/<int:pk>/', views.NetworkDetail.as_view, name = 'network_detail'),

    path('users/', views.UserList.as_view(), name = 'user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name = 'user_detail'),

    path('profile/', views.ProfileList.as_view(), name = 'profile_list'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name = 'profile_detail'),

    path('posts/', views.PostList.as_view(), name = 'post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name = 'post_detail'),
    # path('posts/<int:post_id>/', views.PostDetail.as_view(), name = 'post_detail'),
    # path('posts/<int:pk>/edit/', views.PostDetail.as_view(), name='post_edit'),
    # path('posts/<int:pk>/delete/', views.PostDetail.as_view(), name='post_delete'),

    path('comments/', views.CommentList.as_view(), name = 'comment_list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name = 'comment_detail'),
    # path('comments/<int:comment_id>/', views.CommentDetail.as_view(), name = 'comment_detail'),

    path('events/', views.EventList.as_view(), name = 'event_list'),
    path('events/<int:pk>/', views.EventDetail.as_view(), name = 'event_detail')
]
