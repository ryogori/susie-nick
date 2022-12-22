from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from django.contrib.auth import views as auth_views


app_name= 'muscle_app'

urlpatterns = [
    path('', views.index_view, name='index'),

    # ユーザー関連
    # 新規登録
    path('sign_up', views.SignUp.as_view(), name='sign_up'),
    # ログイン
    path('login', views.Login.as_view(), name='login'),
    # ログアウト
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # マイページ
    path('mypage', views.mypage_view, name='mypage'),
    # ユーザー情報詳細
    path('user_detail/<str:user_id>', views.user_detail, name='user_detail'),
    # ユーザー情報の変更
    # path('user_update', views.UserUpdate.as_view(), name='user_update'),
    # path('user_update', views.user_update, name='user_update'),
    # パスワードの変更
    path('password_change', views.PasswordChange.as_view(), name='password_change'),
    # パスワードの変更に成功した場合に表示表示
    path('password_change/done', views.PasswordChangeDone.as_view(), name='password_done'),

    # 記事関連
    # markはマークダウンでの登録画面の呼び出し
    path('mark', views.mark_view, name='mark'),
    # mark_insertは登録したことを通知
    path('mark_insert', views.mark_insert_view, name='mark_insert'),
    # mark_listはタイトルとユーザー名を表示した一覧画面
    path('mark_list', views.mark_list_views, name='mark_list'),
    # 部位ごとに記事を絞り込んで表示
    path('parts/<str:category>', views.parts_view, name='parts'),
    # 検索ボックスで検索した内容を絞り込んで表示
    path('mark_find', views.mark_find_views, name='mark_find'),
    # mark_detailは記事の詳細画面を表示
    path('mark_detail/<int:id>', views.mark_detail_view, name='mark_detail'),
    # mark_htmlは投稿した記事をHTMLで表示できる。
    path('mark_html/<int:id>', views.mark_html_view, name='mark_html'),
    # mark_editはマークダウンでの編集画面の呼び出し
    path('mark_edit/<int:id>', views.mark_edit_views, name='mark_edit'),
    # 7/20 追加 mark_checkはeditの変更内容結果を表示する画面
    # path('mark_check/<int:id>', views.check_views, name='mark_check'),
    # 8/30 追加 mark_saveは変更を保存を行う画面
    # path('mark_save/<int:id>', views.mark_save_view, name='mark_save'),
    # 7/15 追加 my_articelは自分の記事の画面表示
    path('my_articles', views.my_articles, name='my_articles'),
    # 7/26 変更 mark_deleteViewは記事の削除を行う
    path('mark_delete/<int:id>', views.mark_delete_view, name='mark_delete'),
    # 12/21追加
    path('mark_guide', views.mark_guide_view, name='mark_guide'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)