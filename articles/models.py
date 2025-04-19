from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    awards = models.PositiveIntegerField(default=0)
    followers = models.PositiveIntegerField(default=0)

    # добавляем:
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.author_name}'



