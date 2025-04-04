from django.urls import path
from .views import home_view, article_detail

urlpatterns = [
    path('', home_view, name='home'),
    path('article/<int:id>/', article_detail, name='article_detail'),
]
