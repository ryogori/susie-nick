from audioop import add
from email import contentmanager
from multiprocessing import context
from operator import is_
from turtle import back
from wsgiref.handlers import format_date_time
from django import views
#リダイレクト先
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ArticleForm,UserCreateForm
from .models import Article
from . import forms

# アカウント操作関連
from .models import Users_list
from . forms import Sign_up_Form, LoginForm
from django.views import generic
from django.views.generic import CreateView, View
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import LogoutView

from django.views.decorators.http import require_POST
User = get_user_model()

# Create your views here.
def indexView(request):
    return render(request, "muscle_app/index.html")

def legView(request):
    leg = Article.objects.filter(category = 'leg')
    return render(request, "muscle_app/leg.html",{'category_list':leg})

def absView(request):
    abs = Article.objects.filter(category = 'abs')
    return render(request, "muscle_app/abs.html",{'category_list':abs})

def chestView(request):
    chest = Article.objects.filter(category = 'chest')
    return render(request, "muscle_app/chest.html",{'category_list':chest})

def backView(request):
    back= Article.objects.filter(category = 'back')
    return render(request, "muscle_app/back.html",{'category_list':back})

def armView(request):
    arm = Article.objects.filter(category = 'arm')
    return render(request, "muscle_app/arm.html",{'category_list':arm})

class Sign_up(CreateView):
    def post(self, request, *args, **kwargs):
        form = Sign_up_Form(data=request.POST)
        # form = Sign_up_Form(request.POST)
        if form.is_valid():
            form.save()
            user_id = "@" + form.cleaned_data.get('user_id')
            username = form.cleaned_data.get('username')
            email= form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            # Users_list.objects.create(user_id=user_id, username=username, email=email, password=password)
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'muscle_app/sign_up.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = Sign_up_Form(request.POST)
        return  render(request, 'muscle_app/sign_up.html', {'form': form,})
    
sign_up = Sign_up.as_view()

class Login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # user = User.objects.get(email=email)
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'muscle_app/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'muscle_app/login.html', {'form': form,})

Login = Login.as_view()

class Logout(LogoutView):
    template_name = 'logout.html'

def mypageView(request):
    return render(request, "muscle_app/mypage.html")


#markdownの画面を呼び出す（新規）
def markView(request):
    form = ArticleForm()
    mkdown = {'form':form,}
    return render(request, "muscle_app/markdown.html",mkdown)

#記事一覧
def mark_listViews(request):
    db_views = Article.objects.all()
    content = {
        'db_list' : db_views
    }
    return render(request,"muscle_app/mark_list.html",{'content_list':content})

#記事の詳細
def mark_detailViews(request,id):
    # print(id)
    db_views = get_object_or_404(Article,id = id)
    return render(request,"muscle_app/mark_detail.html",{'article':db_views})

#保存する時の処理（保存した結果は表示しない）
def mark_insertView(request):
    form = forms.ArticleForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data["title"]
        body = form.cleaned_data["content"]
        user_name = form.cleaned_data["user_name"]
        category= form.cleaned_data["category"]
        Article.objects.create(title=title, body=body, user_name=user_name, category=category)
        # obj = Article(title=title, body=body)
        # obj.save()
    return render(request, "muscle_app/mark_insert.html",{'form':form})

#ID指定の表示
def mark_viewViews(request,id):
    db_views = get_object_or_404(Article,id = id)
    content = {
        'title' : db_views.title,
        'body' : db_views.body,
        'user_name':db_views.user_name,
        'category':db_views.category,
    }
    return render(request,"muscle_app/mark_view.html",{'db_view':content,'article':db_views})


#編集画面への処理
# def mark_editViews(request,id):
#     article = get_object_or_404(Article,id = id)
#     update_form = forms.ArticleForm(#forms.Update_ArticleFormをforms.ArticleFormに変更7/26
#         initial = {
#            'title':article.title,
#            'content':article.body,
#         }
#     )
#     return render(request,"muscle_app/mark_edit.html",{'update_form':update_form,'article':article.id,})
#=============================================比較↓ こっちがうまく起動するのでこの処理を本番で使用する
# 【アップデートビュー】nippoUpdateFormView
def mark_editViews(request, id):
    #modelのデータを持ってくる
    article = get_object_or_404(Article,id = id)
    update_form = {"title": article.title, "content":article.body,"category":article.category}
    form = forms.Update_ArticleForm(request.POST or update_form)
    #ctxに辞書型を挿入することでrenderの見た目と拡張性が上がるはず
    ctx = {"update_form": form}
    ctx["object"] = article
    if form.is_valid():
        #.cleaned_dataは.is_valid()がtrueだった場合に,正しかったデータが入る
        # user_name = form.cleaned_data["user_name"]
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        category = form.cleaned_data["category"]
        # obj = Article(title=title, content=content, category=category)
        # obj.save()
        # article.user_name = user_name
        article.title = title 
        article.body = content
        article.category = category
        article.save()
        #db_views = get_object_or_404(Article,id = id)...{'article':db_views}) 
       
    return render(request, "muscle_app/mark_edit.html", ctx)

def checkViews(request,id):
    """入力データの確認画面。"""
    # user_data_inputで入力したユーザー情報をセッションから取り出す。
    session_form_data = request.session.get('form_data')
    if session_form_data is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('muscle_app:mark_edit')

    context = {
        'form': forms.Update_ArticleForm(session_form_data)
    }
    return render(request, 'muscle_app/mark_check.html', context)

#======================================sessionユーザ変更保存関数↓
# @require_POST
def mark_saveView(request):
    """記事変更を保存。"""
    # user_data_inputで入力したユーザー情報をセッションから取り出す。
    # ユーザー作成後は、セッションを空にしたいのでpopメソッドで取り出す。
    session_form_data = request.session.pop('form_data', None)
    if session_form_data is None:
        # ここにはPOSTメソッドで、かつセッションに入力データがなかった場合だけ。
        # セッション切れや、不正なアクセス対策。
        return redirect('muscle_app:mark_edit')

    form = forms.Update_ArticleForm(session_form_data)
    if form.is_valid():
        form.save()
        return redirect('muscle_app:mark_list')

    # is_validに通過したデータだけセッションに格納しているので、ここ以降の処理は基本的には通らない。
    context = {
        'form': form
    }
    return render(request, 'muscle_app/mark_edit', context)
#==================================================↑


#ログインしたユーザーの記事だけ表示処理
def my_article(request):
    db_views = Article.objects.all()
    content = {
        'db_list' : db_views
    }
    #下の処理はモデルからのDBの一行目のデータ取得。pk1のユーザー名を取得する
    #pkの数値は現在一番小さい値 1,2は削除した為参照できない
    # user_name = Article.objects.get(pk=3)
    form = LoginForm(data=request.POST)
    user_name = form.cleaned_data.get('username')#ユーザ名で判別　現在固定
    return render(request,"muscle_app/my_article.html",{'content_list':content,'user_name':user_name.user_name})
    
#記事の削除処理 
def mark_deleteView(request, id):
    obj = get_object_or_404(Article, id=id)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("muscle_app:mark_insert")
    return render(request, "muscle_app/mark_delete.html", ctx)
