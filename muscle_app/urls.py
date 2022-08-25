from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from .views import Login


app_name= 'muscle_app'

urlpatterns = [
    path('', views.indexView, name='home'),
    path('leg', views.legView, name="leg"),
    path('abs', views.absView, name="abs"),
    path('chest', views.chestView, name="chest"),
    path('back', views.backView, name="back"),
    path('arm', views.armView, name="arm"),
<<<<<<< HEAD
    #markはマークダウンでの登録画面の呼び出し
    path('mark',views.markView,name="mark"),
    #mark_insertは登録したことを通知
    path('mark_insert',views.mark_insertView,name="mark_insert"),
    #mark_viewは登録したマークダウンを見ることができる
    path('mark_view',views.mark_viewViews,name="mark_view"),
    #mark_editはマークダウンでの編集画面の呼び出し
    path('mark_edit/<int:id>',views.mark_editViews,name="mark_edit"),
    # path('mark_edit',views.mark_editViews,name="mark_edit"),
    #mark_listはタイトルとユーザー名を表示した一覧画面
    path('mark_list',views.mark_listViews,name="mark_list"),
    #mark_detailは記事の詳細画面を表示
    path('mark_detail/<int:id>',views.mark_detailViews,name="mark_detail"),
    #7/15追加 my_articelは自分の記事の画面表示
    path('my_article',views.my_article,name="my_article"),
    #7/26変更　mark_deleteViewは記事の削除を行う
    path('mark_delete/<int:id>',views.mark_deleteView,name='mark_delete'),
    #7/20追加　mark_checkはeditの変更内容結果を表示する画面
    path('mark_check/<int:id>',views.checkViews,name="mark_check"),

    #7/26追加　session付きの変更内容確認画面？
    #path('user_data_confirm/', views.user_data_confirm, name='user_data_confirm'),
=======
    # markはマークダウンでの登録画面の呼び出し
    path('mark', views.markView, name="mark"),
    # mark_insertは登録したことを通知
    path('mark_insert', views.mark_insertView, name="mark_insert"),
    # mark_viewは登録したマークダウンを見ることができる
    path('mark_view', views.mark_viewViews, name="mark_view"),
    # mark_editはマークダウンでの編集画面の呼び出し
    path('mark_edit', views.mark_editViews, name="mark_edit"),
    # mark_listはタイトルとユーザー名を表示した一覧画面
    path('mark_list', views.mark_listViews, name="mark_list"),
    # mark_detailは記事の詳細画面を表示
    path('mark_detail/<int:id>', views.mark_detailViews, name="mark_detail"),
    # 新規登録
    path('sign_up', views.Sign_up.as_view(), name="sign_up"),
    # ログイン
    path('login', views.Login, name="login"),
    # ログアウト
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # マイページ
    path('mypage', views.mypageView, name="mypage")

>>>>>>> users
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)