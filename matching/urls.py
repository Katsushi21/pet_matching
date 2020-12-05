from django.urls import path

from . import views

app_name = 'matching'   # このアプリケーションのルーティングに名前を付ける
urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),      # IndexViewに処理を渡し、このルーティング処理を識別する名前を付ける
]