from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from magtrailer import settings
from pages.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # отдельно добавляет маршруты приложения
]

# Для отображение при включенном DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound  # Обработчик 404 ошибки
