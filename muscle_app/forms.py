from django import forms
from .models import Article, UsersList
from mdeditor.fields import MDTextFormField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


# ユーザー関連
# 新規登録のフォーム
class Sign_up_Form(UserCreationForm):
    class Meta:
       model = UsersList
       fields = ("user_id", "username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['user_id'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# ログイン画面のフォーム
class LoginForm(AuthenticationForm):
    class Meta:
       model = UsersList
       fields = ("email", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
    
# ユーザー情報の変更画面のフォーム
# class UserChangeForm(forms.ModelForm):
#     class Meta:
#         model = UsersList
#         fields = ("user_id", "username", "email")



class UserChangeForm(forms.ModelForm):
    class Meta:
        model = UsersList
        fields = ("user_id", "username", "email")

    def __init__(self, user_id=None, username=None, email=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        if user_id:
            self.fields['user_id'].widget.attrs['value'] = user_id
        if username:
            self.fields['username'].widget.attrs['value'] = username
        if email:
            self.fields['email'].widget.attrs['value'] = email
            
    # def update(self, user):
    #     user.user_id = self.cleaned_data['user_id']
    #     user.username = self.cleaned_data['username']
    #     user.email = self.cleaned_data['email']
    #     user.save()

# パスワード変更画面のフォーム
class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# 記事関連
# 記事につけるカテゴリのリスト
tag = (
    ("all","all"),
    ("chest","胸"),
    ("back","背中"),
    ("abs","腹"),
    ("arm","腕"),
    ("leg","脚"),
)

# 記事の新規登録画面のフォーム
class ArticleForm(forms.Form):
    # username = forms.CharField()
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tag)
    #session用？の為に追加
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Article
        fields = ("user_id", "username", "title", "content", "category")

# 記事の更新画面のフォーム
class Update_ArticleForm(forms.Form):
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tag)
    #session用？の為に追加
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
