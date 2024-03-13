from django.urls import path
from .views import UserAPIView, UserDetailAPIView, PostAPIView, PostDetailAPIView, CommentAPIView, CommentDetailAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user-list-create'),
    path('users/<int:user_id>/', UserDetailAPIView.as_view(), name='user-retrieve-update-destroy'),
    
    path('posts/', PostAPIView.as_view(), name='post-list-create'),
    path('posts/<int:user_id>/', PostDetailAPIView.as_view(), name='post-retrieve-update-destroy'),
    
    path('comments/', CommentAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:user_id>/', CommentDetailAPIView.as_view(), name='comment-retrieve-update-destroy'),
]
