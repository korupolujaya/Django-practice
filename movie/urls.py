from django.urls import path
from .views import ActorAPIView, ActorDetailAPIView, DirectorAPIView, DirectorDetailAPIView,MovieAPIView, MovieDetailAPIView

urlpatterns = [
    path('actors/', ActorAPIView.as_view(), name='user-list-create'),
    path('actors/<int:user_id>/', ActorDetailAPIView.as_view(), name='user-retrieve-update-destroy'),
    
    path('directors/', DirectorAPIView.as_view(), name='post-list-create'),
    path('directors/<int:user_id>/', DirectorDetailAPIView.as_view(), name='post-retrieve-update-destroy'),
    
    path('movies/', MovieAPIView.as_view(), name='comment-list-create'),
    path('movies/<int:user_id>/', MovieDetailAPIView.as_view(), name='comment-retrieve-update-destroy'),
]
