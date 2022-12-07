from django import forms
from .models import Article, Users_list
from django.forms import ModelForm
from mdeditor.fields import MDTextFormField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()#Userモデルの柔軟な取得方法

from django.forms import ModelForm


class Sign_up_Form(UserCreationForm):
    class Meta:
       model = Users_list
       fields = ("user_id", "username", "email", "password1", "password2",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        # self.fields['user_id'].widget.attrs['class'] = 'form-control'
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        # 説明:self .Metaに記載されているfields(...) .辞書型のキーとバリュー取得するvalues()をfieldに代入
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    class Meta:
       model = Users_list
       fields = ("email", "password")

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'
    
class UserChangeForm(ModelForm):
    class Meta:
        model = Users_list
        fields = ["user_id", "username",]

    def __init__(self, user_id=None, username=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        if user_id:
            self.fields['user_id'].widget.attrs['value'] = user_id
        if username:
            self.fields['username'].widget.attrs['value'] = username

    def update(self, user):
        user.user_id = self.cleaned_data['user_id']
        user.username = self.cleaned_data['username']
        user.save()

# class UserUpdateForm(forms.ModelForm):
#     # ユーザー情報更新フォーム

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         #htmlの表示を変更可能にします
#         self.fields['user_id'].widget.attrs['class'] = 'form-control'
#         self.fields['username'].widget.attrs['class'] = 'form-control'
#         self.fields['email'].widget.attrs['class'] = 'form-control'
#         self.fields['newpassword1'].widget.attrs['class'] = 'form-control'
#         self.fields['newpassword2'].widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = Users_list
#         firlds = ("user_id", "username", "email", "newpassword1", "newpassword2",)



tagu = (
    ("all","all"),
    ("chest","胸"),
    ("back","背中"),
    ("abs","腹"),
    ("arm","腕"),
    ("leg","脚"),
)

class ArticleForm(forms.ModelForm):

    user_name = forms.CharField()
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tagu)
    snsimage = forms.FileField(required=False)

    #session用？の為に追加
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Article
        fields = ("user_name","title","content","category","snsimage")


class Update_ArticleForm(forms.Form):
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tagu)
    #session用？の為に追加
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

