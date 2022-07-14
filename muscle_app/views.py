<<<<<<< HEAD
from email import contentmanager
=======
from audioop import add
from email import contentmanager
from multiprocessing import context
from operator import is_
from wsgiref.handlers import format_date_time
>>>>>>> feature
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
<<<<<<< HEAD

=======
#markdownの画面を呼び出す（新規）
>>>>>>> feature
def markView(request):
    form = ArticleForm()
    mkdown = {'form':form,}
    return render(request, "muscle_app/markdown.html",mkdown)
<<<<<<< HEAD

=======
#保存する時の処理（保存した結果は表示しない）
>>>>>>> feature
def mark_insertView(request):
    form = forms.ArticleForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data["title"]
        body = form.cleaned_data["content"]
<<<<<<< HEAD
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

=======
        user_name = form.cleaned_data["user_name"]
        category= form.cleaned_data["category"]
        Article.objects.create(title=title, body=body, user_name=user_name, category=category)
        # obj = Article(title=title, body=body)
        # obj.save()
    return render(request, "muscle_app/mark_insert.html",{'form':form})
#ID指定の表示
def mark_viewViews(request):
    db_views = get_object_or_404(Article,id = 13)
    content = {
        'title' : db_views.title,
        'body' : db_views.body,
        'user_name':db_views.user_name,
        'category':db_views.category,
    }
    return render(request,"muscle_app/mark_view.html",{'db_view':content})

#編集画面への処理
def mark_editViews(request):
    # print(request.POST)
    # return 
    article_id = request.POST.get('id')
    article = get_object_or_404(Article,id = article_id)
    update_form = forms.Update_ArticleForm(
        initial = {
           'title':article.title,
           'content':article.body,
        }
    )
    if request.method == 'POST':
        form = forms.Update_ArticleForm(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["content"]
            category= form.cleaned_data["category"]
            # obj = Article(title=title,body=body,category=category)
            # obj.save()
            obj = Article.objects.get(id=10)
            obj = Article(title=title,body=body,category=category)
            obj.save()

    return render(request,"muscle_app/mark_edit.html",{'update_form':update_form})

def mark_listViews(request):
    db_views = Article.objects.all()
    content = {
        'db_list' : db_views
    }
    return render(request,"muscle_app/mark_list.html",{'content_list':content})

def mark_detailViews(request,id):
    # print(id)
    db_views = get_object_or_404(Article,id = id)

    return render(request,"muscle_app/mark_detail.html",{'article':db_views})

    
>>>>>>> feature
