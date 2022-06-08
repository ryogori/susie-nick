from django.urls import path
from . import views

app_name= 'muscle_app'

urlpatterns = [
    path('', views.indexView, name='home'),
    path('leg', views.legView, name="leg"),
    path('abs', views.absView, name="abs"),
    path('chest', views.chestView, name="chest"),
    path('back', views.backView, name="back"),
    path('arm', views.armView, name="arm"),
]
