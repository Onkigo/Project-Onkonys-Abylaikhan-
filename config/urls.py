
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from articles import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('', views.home_view, name='home'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



