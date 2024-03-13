from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Actor(models.Model):
    name=models.CharField(max_length=20)
    DOB=models.DateField()
    nationality=models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class Director(models.Model):
    director = models.CharField(max_length=100)
    DOB=models.DateField()
    nationality=models.CharField(max_length=15)
    def __str__(self):
        return self.director


class MovieName(models.Model):
    mname= models.CharField(max_length=150)
    release_date = models.DateField(auto_now_add=True)
    director = models.ForeignKey('Director', on_delete=models.CASCADE,related_name='Movie_director')
    actor = models.ForeignKey('Actor', on_delete=models.CASCADE,related_name='Movie_actor')
    
