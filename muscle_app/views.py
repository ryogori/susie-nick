from .models import UsersList, Article
from . forms import *
from .Exceptions import ValueNoneError

from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import DataError

from audioop import add
from email import contentmanager
from multiprocessing import context
from operator import is_
from turtle import back
from wsgiref.handlers import format_date_time


# Create your views here.
def index_view(request):
    return render(request, "muscle_app/index.html")

# ユーザーの新規登録処理
class SignUp(CreateView):
    def post(self, request, *args, **kwargs):
        form = Sign_up_Form(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get("user_id")
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = UsersList.objects.create(user_id=user_id, username=username, email=email)
            user.set_password(password)
            user.save()
            login(request, user, backend="muscle_app.backends.EmailAuthenticationBackend")
            return redirect('/')
        return render(request, 'muscle_app/sign_up.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = Sign_up_Form(request.POST or None)
        form.initialized = False
        return  render(request, 'muscle_app/sign_up.html', {'form': form})


# ログイン処理
class Login(View):
    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        if username.find("@") == 0:
            username = username[1:]
        form = LoginForm(data={"username": username, "password": request.POST["password"]})
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if username.find("@") == -1:
                login(request, user, "muscle_app.backends.UseridAuthenticationBackend")
                # print("ユーザーIDでログインしたよ。")
            else:
                login(request, user, "muscle_app.backends.EmailAuthenticationBackend")
                # print("Emailでログインしたよ。")
            return redirect('/')

        form = LoginForm(data=request.POST)
        return render(request, 'muscle_app/login.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'muscle_app/login.html', {'form': form})

# ログアウト処理
class Logout(LogoutView):
    template_name = 'logout.html'

# マイページの表示
@login_required
def mypage_view(request):
    return render(request, "muscle_app/mypage.html")

# ユーザー情報を表示
@login_required
def user_detail(request, user_id):
    # get_object_or_404の引数は、(データベース名, カラム名=変数名)で書く。pkはプライマリーキーのこと。
    user = get_object_or_404(UsersList, user_id=user_id)
    return render(request, 'muscle_app/users_detail.html', {'user': user})

# ユーザー情報の更新処理
# @login_required
# class UserUpdate(UpdateView):
#     def post(self, request, *args, **kwargs):
#         user = get_object_or_404(UsersList, user_id=request.user.user_id)
#         form = UserChangeForm(data=request.POST, instance=user)
#         print(form.is_valid())
#         if form.is_valid():
#             form.save()
#             return redirect("/user_detail/" + str(user.user_id))
#         else:
#             form = UserChangeForm(data=request.POST)
#             return render(request, 'muscle_app/change.html', {'form': form})

#     def get(self, request, *args, **kwargs):
#         kwargs = dict(user_id=request.user.user_id, username=request.user.username, email=request.user.email)    
#         form = UserChangeForm(request.POST, initial=kwargs)
#         return  render(request, 'muscle_app/change.html', {'form': form})

# ログインしてるかどうかの関数を作成したほうがよき。
class UserUpdate(View):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(UsersList, user_id=request.user.user_id)
        form = UserChangeForm(data=request.POST, instance=user)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect("/user_detail/" + str(user.user_id))
        else:
            form = UserChangeForm(data=request.POST)
            return render(request, 'muscle_app/change.html', {'form': form})

    def get(self, request, *args, **kwargs):
        kwargs = dict(user_id=request.user.user_id, username=request.user.username, email=request.user.email)    
        form = UserChangeForm(request.POST, initial=kwargs)
        return  render(request, 'muscle_app/change.html', {'form': form})

# パスワード変更処理
class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('muscle_app:password_done')
    template_name = 'muscle_app/password_change.html'

# パスワード変更完了画面を表示
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'muscle_app/password_change_done.html'

#markdownの画面を呼び出す（新規）
@login_required
def mark_view(request):
    form = ArticleForm()
    mkdown = {'form': form}
    return render(request, "muscle_app/markdown.html", mkdown)

#保存する時の処理（保存した結果は表示しない）
@login_required
def mark_insert_view(request):
    form = ArticleForm(request.POST or None)
    user = get_object_or_404(UsersList, user_id=request.user.user_id)
    if form.is_valid():
        title = form.cleaned_data["title"]
        body = form.cleaned_data["content"]
        category= form.cleaned_data["category"]
        Article.objects.create(author=user, title=title, body=body, category=category)
    return render(request, "muscle_app/mark_insert.html", {'form': form})

#記事一覧
def mark_list_views(request):
    obj = Article.objects.all()
    content = {
        'db_list' : obj
    }
    return render(request, "muscle_app/mark_list.html", {'content_list': content})

# タグごとに記事を絞り込んで表示
def parts_view(request, category):
    partsname = {"leg": "脚", "abs": "腹部", "chest": "胸部", "back": "背中", "arm": "腕"}
    parts = Article.objects.filter(category=category)
    return render(request, "muscle_app/parts.html", {'category_list': parts, 'category': partsname[category]})

# 検索ボックスに入力されたキーワードをもとに記事を検索
def mark_find_views(request):
    word = request.POST['word']
    if word.find("@") == 0:
        obj = Article.objects.filter(author_id__user_id__icontains=word[1:])
    else:
        obj = Article.objects.filter(title__icontains=word)
    content = {
        'db_list' : obj
    }
    return render(request, "muscle_app/mark_list.html", {'content_list': content})
    
#記事の詳細
def mark_detail_view(request, id):
    # print(id)
    obj = get_object_or_404(Article, id=id)
    return render(request, "muscle_app/mark_detail.html", {'article': obj})


# デザインについてゴリラと要相談
# HTML表示の際に、どのようなデザインにするか。また、user_idや、usernameなどを表示するかなど。
# ID指定の表示
def mark_html_view(request, id):
    obj = get_object_or_404(Article, id=id)
    content = {
        'author': obj.author_id,
        'title' : obj.title,
        'body' : obj.body,
        'category': obj.category,
    }
    return render(request, "muscle_app/mark_view.html", {'db_view':content, 'article':obj})

# 記事の編集
def mark_edit_views(request, id):
    #modelのデータを持ってくる
    article = get_object_or_404(Article, id=id)
    update_form = {"title": article.title, "content":article.body, "category":article.category}
    form = Update_ArticleForm(request.POST or update_form)
    if request.POST:
        try:
            if form.is_valid():
                #.cleaned_dataは.is_valid()がtrueだった場合に,正しかったデータが入る
                article.title = form.cleaned_data["title"]
                article.body = form.cleaned_data["content"]
                article.category = form.cleaned_data["category"]
                article.save()
                obj = Article.objects.all()
                content = {
                    'db_list' : obj
                }
                return render(request, "muscle_app/mark_list.html", {'content_list':content})

            else:
                if request.POST["title"].isspace or request.POST["content"].isspace:
                    raise ValueNoneError("タイトル、またはコンテンツが入力されていません。")
                else :
                    redirect('muscle_app:mark_list')

        except DataError:
            ctx = { "update_form": form }
            ctx["object"] = article
            ctx["error"] = '入力内容が不正です。'
            return render(request, "muscle_app/mark_edit.html", ctx)

        except ValueNoneError as e:
            ctx = { "update_form": form }
            ctx["object"] = article
            ctx["error"] = e
            return render(request, "muscle_app/mark_edit.html", ctx)

    else:
        #ctxに辞書型を挿入することでrenderの見た目と拡張性が上がるはず
        ctx = { "update_form": form }
        ctx["object"] = article
       
    return render(request, "muscle_app/mark_edit.html", ctx)

# ログインしたユーザーの記事だけ表示処理
def my_articles(request):
    obj = Article.objects.filter(author_id__user_id=request.user.user_id)
    content = {
        'db_list' : obj
    }
    return render(request, "muscle_app/my_article.html", {'content_list': content})
    
# 記事の削除処理 
def mark_delete_view(request, id):
    obj = get_object_or_404(Article, id=id)
    if request.user.user_id == obj.author_id:
        ctx = {"object": obj}
        if request.POST:
            obj.delete()
            return redirect("muscle_app:mark_insert")
        return render(request, "muscle_app/mark_delete.html", ctx)

    else:
        obj = Article.objects.all()
        content = {
            'db_list' : obj
        }
        return render(request, "muscle_app/mark_list.html", {'content_list': content, 'error': "投稿者以外消せねーよばーか"})

