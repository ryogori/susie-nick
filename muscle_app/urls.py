from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name= 'muscle_app'

urlpatterns = [
    path('', views.indexView, name='home'),
    path('leg', views.legView, name="leg"),
    path('abs', views.absView, name="abs"),
    path('chest', views.chestView, name="chest"),
    path('back', views.backView, name="back"),
    path('arm', views.armView, name="arm"),
    #markはマークダウンでの登録画面の呼び出し
    path('mark',views.markView,name="mark"),
    #mark_insertは登録したことを通知
    path('mark_insert',views.mark_insertView,name="mark_insert"),
    #mark_viewは登録したマークダウンを見ることができる
    path('mark_view',views.mark_viewViews,name="mark_view"),
    #mark_editはマークダウンでの編集画面の呼び出し
    path('mark_edit',views.mark_editViews,name="mark_edit"),
    #mark_listはタイトルとユーザー名を表示した一覧画面
    path('mark_list',views.mark_listViews,name="mark_list"),
    #mark_detailは記事の詳細画面を表示
    path('mark_detail/<int:id>',views.mark_detailViews,name="mark_detail"),
    path('sign_up', views.Sign_up.as_view(), name="sign_up"),
    path('login', views.Login, name="login"),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)