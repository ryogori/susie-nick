from email import contentmanager
from django import views
from django.shortcuts import render,get_object_or_404

# from muscle_app.models import Article
from .forms import ArticleForm
from .models import Article
from . import forms

# Create your views here.
def indexView(request):
    return render(request, "muscle_app/index.html")

def legView(request):
    return render(request, "muscle_app/leg.html")

def absView(request):
    return render(request, "muscle_app/abs.html")

def chestView(request):
    return render(request, "muscle_app/chest.html")

def backView(request):
    return render(request, "muscle_app/back.html")

def armView(request):
    return render(request, "muscle_app/arm.html")

def markView(request):
    form = ArticleForm()
    mkdown = {'form':form,}
    return render(request, "muscle_app/markdown.html",mkdown)

def mark_insertView(request):
    form = forms.ArticleForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data["title"]
        body = form.cleaned_data["content"]
        Article.objects.create(title=title, body=body)
        # obj = Article(title=title, body=body)
        # obj.save()
    return render(request, "muscle_app/mark_insert.html",{'form':form})

def mark_viewViews(request):
    db_views = get_object_or_404(Article,id = 8)
    content = {
        'title' : db_views.title,
        'body' : db_views.body
    }
    return render(request,"muscle_app/mark_view.html",{'db_view':content})

