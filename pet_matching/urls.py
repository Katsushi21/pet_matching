from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import static
from . import settings_dev, settings_common

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('matching.urls')),     # matching/urlsへのルーティング
    path('accounts/', include('allauth.urls')),
]
# 開発サーバーでメディア配信を可能にする記述
urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)