from django.urls import path
from . import views

app_name= 'muscle_app'

urlpatterns = [
    path('', views.indexView, name='home'),
    path('leg', views.legView, name="leg"),
    path('abs', views.legView, name="abs"),
    path('chest', views.legView, name="chest"),
    path('back', views.legView, name="back"),
    path('arm', views.legView, name="arm"),
]
