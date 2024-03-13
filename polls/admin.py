from django.contrib import admin
# from polls.models import Article, Reporter
from . import models

# Register your models here.
admin.site.register(models.Article)
admin.site.register(models.Reporter)