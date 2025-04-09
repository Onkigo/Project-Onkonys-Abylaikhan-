from django.urls import path
from .views import home_view, article_detail, register_view, login_view, logout_view
from . import views
from .views import category_articles_view

from .views import (
    home_view, article_detail,
    register_view, login_view, logout_view,
    create_article, edit_article
)

urlpatterns = [
    path('', home_view, name='home'),
    path('article/<int:id>/', article_detail, name='article_detail'),
    

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    
    path('article/create/', create_article, name='create_article'),
    path('article/<int:id>/edit/', edit_article, name='edit_article'),
    

    path('category/<int:category_id>/', category_articles_view, name='category_articles'),

    

]
