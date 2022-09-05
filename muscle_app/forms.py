from django import forms
from .models import Article, Users_list

from mdeditor.fields import MDTextFormField

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class Sign_up_Form(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['user_id'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
       model = Users_list
       fields = ("user_id", "username", "email", "password1", "password2",)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'
    
    class Meta:
       model = Users_list
       fields = ("email", "password")

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

class ArticleForm(forms.Form):
    user_name = forms.CharField()
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tagu)
    
class Update_ArticleForm(forms.Form):
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tagu)
    