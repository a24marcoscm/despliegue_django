from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('', include('social.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
