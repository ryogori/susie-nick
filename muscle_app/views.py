from django import views
#リダイレクト先
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

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

# markdownの画面を呼び出す（新規）

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
    return render(request, "muscle_app/mark_insert.html",{'form':form})#form使われてない？

#ID指定の表示
def mark_viewViews(request):
    db_views = get_object_or_404(Article,id = 13)
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
    #modelのデータを持ってくるs
    article = get_object_or_404(Article,id = id)
    update_form = {"title": article.title, "body":article.body}
    form = forms.Update_ArticleForm(request.POST or update_form)
    #ctxに辞書型を挿入することでrenderの見た目と拡張性が上がるはず
    ctx = {"update_form": form}
    ctx["object"] = article
    if form.is_valid():
        #.cleaned_dataは.is_valid()がtrueだった場合に,正しかったデータが入る
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        # obj = Article(title=title, body=content)
        # obj.save()
        article.title = title 
        article.body = content
        article.save()
    return render(request, "muscle_app/mark_edit.html", ctx)
# #=============================================↑

# def mark_checkView(request):7/20まだ作成していない　確認画面予定
#         if request.method == 'POST':

#         form = forms.Update_ArticleForm(request.POST or None,)
#         if form.is_valid():
#             title = form.cleaned_data["title"]
#             body = form.cleaned_data["content"]
#             category= form.cleaned_data["category"]
#             # obj = Article(title=title,body=body,category=category)
#             # obj.save()
#             obj = Article.objects.get(id=1)#7/19ここがうまく動いていないと見ている
#             # obj = Article(title=title,body=body,category=category)
#             #なぜかstr()を追加すると成功した
#             obj.title = str(Article(title=title))
#             obj.body = str(Article(body=body))
#             obj.category = str(Article(category=category))
#             obj.save()#既にプライマリーキーがあるものは更新する特性があるのに追加ということはしっかりとプリマリが指定されてない？

def checkViews(request,id):
    db_views = get_object_or_404(Article,id = id)

    return render(request,"muscle_app/mark_check.html",{'article':db_views})


#ログインしたユーザーの記事だけ表示処理
def my_article(request):
    db_views = Article.objects.all()
    content = {
        'db_list' : db_views
    }
    #下の処理はモデルからのDBの一行目のデータ取得。pk1のユーザー名を取得する
    #pkの数値は現在一番小さい値 1,2は削除した為参照できない
    user_name = Article.objects.get(pk=3)
    return render(request,"muscle_app/my_article.html",{'content_list':content,'user_name':user_name.user_name})
    
#7/26ブログ参考　mark_listの削除処理 
def mark_deleteView(request, id):
    obj = get_object_or_404(Article, id=id)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
    return render(request, "muscle_app/mark_delete.html", ctx)