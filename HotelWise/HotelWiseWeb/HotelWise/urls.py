from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home import views as home_views
from reviews import views as reviews_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('reviews/', include('reviews.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
