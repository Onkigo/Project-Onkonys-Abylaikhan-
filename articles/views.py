
from django.shortcuts import render, get_object_or_404, redirect,render
from .models import Article, Comment,Category
from .forms import CommentForm,ArticleForm,CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.db.models.functions import TruncMonth
from django.db.models import Count
from datetime import datetime



def home_view(request):
    # Получаем все статьи
    articles = Article.objects.all()
    
    # Получаем параметры из GET-запроса
    query = request.GET.get('q')
    category = request.GET.get('category')
    date = request.GET.get('date')

    # Фильтрация по запросу (по заголовку или контенту)
    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    # Фильтрация по категории
    if category:
        articles = articles.filter(category__name=category)

    # Фильтрация по дате (по месяцу и году)
    if date:
        year, month = date.split('-')
        articles = articles.filter(pub_date__year=year, pub_date__month=month)

    # Для отображения всех категорий в форме фильтрации
    categories = Category.objects.all()

    context = {
        'articles': articles,
        'query': query,
        'selected_category': category,
        'selected_date': date,
        'categories': categories,
        
    }

    return render(request, 'home.html', context)

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})

def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_form.html', {'form': form})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    form = CommentForm(request.POST or None)
    comments = article.comments.all().order_by('-created_at')
    if request.method == "POST" and form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('article_detail', id=article.id)

    

    return render(request, 'article_detail.html', {
        'article': article,
        'form': form,
        'comments': comments  # ← передаём комментарии в шаблон
    })

    
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})







def category_articles_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'articles': articles})


