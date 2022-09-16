from django import forms
from .models import Article, Users_list
from django.forms import ModelForm
from mdeditor.fields import MDTextFormField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()#Userモデルの柔軟な取得方法

class Sign_up_Form(UserCreationForm):#より短縮できたためコメントアウト
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
       
    class Meta:
       model = Users_list
       fields = ("user_id", "username", "email", "password1", "password2",)

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Users_list
        fields = ("email", "username","password")



tagu = (
    ("all","all"),
    ("chest","胸"),
    ("back","背中"),
    ("abs","腹"),
    ("arm","腕"),
    ("leg","脚"),
)

class ArticleForm(forms.Form):
    user_name = forms.CharField()
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tagu)
    #session用？の為に追加
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Article
        fields = ("user_name","title","content","category",)

class Update_ArticleForm(forms.Form):
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tagu)
    #session用？の為に追加
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
#=============↓動作確認用form
class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = (User.USERNAME_FIELD,)  # ユーザー名として扱っているフィールドだけ、作成時に入力する

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
#=============↑
