from django.db import models

# Create your models here.
class Reporter(models.Model):
    name=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE,related_name='reporter')
    
    def __str__(self):
        return self.headline