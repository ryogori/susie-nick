from django import forms
from .models import Article

from mdeditor.fields import MDTextFormField

tagu = (
    ("all","all"),
    ("chest","胸"),
    ("back","背中"),
    ("abs","腹"),
    ("arm","腕"),
    ("leg","脚"),
)

class ArticleForm (forms.Form):
    user_name = forms.CharField()
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tagu)
    
class Update_ArticleForm (forms.Form):
    title = forms.CharField ()
    content = MDTextFormField()
    category = forms.ChoiceField(choices=tagu)
    