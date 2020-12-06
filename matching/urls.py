from django.urls import path

from . import views

app_name = 'matching'   # このアプリケーションのルーティングに名前を付ける
urlpatterns = [         # IndexViewに処理を渡し、このルーティング処理を識別する名前を付ける
    path('', views.IndexView.as_view(), name='Index'),
    path('contact/', views.ContactView.as_view(), name="contact")
]
