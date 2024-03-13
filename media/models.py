from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    post_title = models.CharField(unique=True, max_length=100)
    description= models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_posts')
    def __str__(self):
        return self.post_title


class Comment(models.Model):
    comment= models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='commented_post')
    
