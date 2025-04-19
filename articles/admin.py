from django.contrib import admin
from .models import Article, Comment,Category
from .models import Profile

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)