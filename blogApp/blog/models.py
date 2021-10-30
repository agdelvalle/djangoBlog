from django.core.exceptions import DisallowedHost
from django.db import models
from datetime import datetime, date

# Create your models here.
class blogEntry(models.Model):
    blogTitle = models.CharField(verbose_name="Title", max_length=200)
    blogBody = models.TextField(verbose_name="Body Text", max_length=10000)
    publishDate = models.DateField(auto_now_add=True)

class comment(models.Model):
    commBody = models.CharField(verbose_name="Comment", max_length=10000)
    userCom = models.CharField(verbose_name="commenterName", max_length=500)
    commDate = models.DateField(auto_now_add=True)
    blog = models.ForeignKey(blogEntry, verbose_name="blogEntryID",on_delete = models.CASCADE)