from pickletools import TAKEN_FROM_ARGUMENT1
from django.db import models
from mdeditor.fields import MDTextField

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = MDTextField(verbose_name = '記事',  default='ここに記事を記入')
   
    def __str__(self):
        return self.title

