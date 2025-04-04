from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm
def home_view(request):
    articles = Article.objects.all().order_by('-pub_date')  # ← сначала данные
    return render(request, 'home.html', {'articles': articles})  # ← потом отдаём в шаблон

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', id=article.id)
    else:
        form = CommentForm()

    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form
    })