from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import ActorSerializer, DirectorSerializer, MovieSerializer

# Create your views here.
class ActorAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActorDetailAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(Actor, id=user_id)
        serializer = ActorSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = get_object_or_404(Actor, id=user_id)
        serializer = ActorSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        actor = get_object_or_404(Actor, id=user_id)
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DirectorAPIView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DirectorDetailAPIView(APIView):
    def get(self, request, user_id):
        directors = get_object_or_404(Director, id=user_id)
        serializer = DirectorSerializer(directors)
        return Response(serializer.data)

    def put(self, request, user_id):
        directors = get_object_or_404(Director, id=user_id)
        serializer = DirectorSerializer(directors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        director = get_object_or_404(Director, id=user_id)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MovieAPIView(APIView):
    def get(self, request):
        movies = MovieName.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAPIView(APIView):
    def get(self, request, user_id):
        movie = get_object_or_404(MovieName, id=user_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, user_id):
        movie = get_object_or_404(MovieName, id=user_id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        movie = get_object_or_404(MovieName, id=user_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)