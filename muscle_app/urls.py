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
   #markはマークダウン編集画面の呼び出し
    path('mark',views.markView,name="mark"),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)