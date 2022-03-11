from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('yamm/', include('yamm.urls')),
    path('boards/', include('board.urls')),
    path('user/', include('user.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)