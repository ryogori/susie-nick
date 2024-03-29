from pickletools import TAKEN_FROM_ARGUMENT1
from django.db import models
from mdeditor.fields import MDTextField
# ユーザー認証に使用するモジュールをインポート
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator, RegexValidator, EmailValidator

class MyUserManager(BaseUserManager):
    def create_user(self, user_id, email, password=None):
        if not user_id:
            raise ValueError('ユーザーidを登録する必要があります。')
        if not email:
            raise ValueError('メールアドレスを登録する必要があります。')

        user = self.model(
            user_id=user_id,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, username, email, password):
        user = self.create_user(
            user_id=user_id,
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

# ユーザーアカウントのモデルクラス
class UsersList(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^[A-Za-z0-9_]*$', message='ユーザーIDには小文字英字、大文字英字、数字、アンダースコア(_)のみ入力可能です。')])
    username = models.CharField(max_length=16)
    email = models.EmailField(max_length=50, unique=True, validators=[EmailValidator])
    # password = models.CharField(max_length=128, validators=[MinLengthValidator(8), RegexValidator(r'^(?=.*[A-Z])(?=.*[1-9])(?=.*[&=-@#{}!\^\$\(\)\[\]\?\*])[a-zA-Z0-9&=-@#{}!\^\$\(\)\[\]\?\*]{8,16}$', message='パスワードには大文字英字、数字、記号(-@^#$(){}[]!?*&=)をそれぞれ1回以上使用し、8文字以上にしてください。')])
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])
    gender = models.CharField(max_length=3, validators=[MinLengthValidator(2)])
    
    objects = MyUserManager()
    
    EMAIL_FIELD = 'email'

    # 一意のフィールドを指定
    USERNAME_FIELD = 'user_id'

    REQUIRED_FIELDS = ['email', 'username']

    def __str__(self):
        return self.email


# 必要な機能　ID(デフォルトのプライマリキー)　ユーザー名 タイトル　本文　作成日　更新日　記事のカテゴライズ
class Article(models.Model):
    author = models.ForeignKey(UsersList, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = MDTextField(verbose_name = '記事', default='ここに記事を記入')
    create_data = models.DateTimeField(auto_now_add=True, help_text='作成日')
    update_data = models.DateTimeField(auto_now=True, help_text='更新日')
    category = models.CharField(max_length=7, default='all')    # タグを想定、内容は(abs,arm,back,base,chest,allを想定、デフォはall)
    # snsimage = models.ImageField(upload_to="")

    def __str__(self):
        return self.title