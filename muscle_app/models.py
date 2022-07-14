from pickletools import TAKEN_FROM_ARGUMENT1
from django.db import models
from mdeditor.fields import MDTextField


# 必要な機能　ID(デフォルトのプライマリキー)　ユーザー名 タイトル　本文　作成日　更新日　記事のカテゴライズ
class Article(models.Model):
    user_name = models.CharField(max_length=16,default='user')
    title = models.CharField(max_length=200)
    body = MDTextField(verbose_name = '記事',  default='ここに記事を記入')
    create_data = models.DateTimeField(auto_now_add=True,help_text='作成日')
    update_data = models.DateTimeField(auto_now=True,help_text='更新日')
    category = models.CharField(max_length=7,default='all')#タグを想定、内容は(abs,arm,back,base,chest,allを想定、デフォはall)
    def __str__(self):
        return self.title

