from django import views
from django.shortcuts import render

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

