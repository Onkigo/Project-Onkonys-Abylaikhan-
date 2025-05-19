from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, Category

class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='12345',
            first_name='Test',
            last_name='User'
        )
        self.category = Category.objects.create(name='Technology')
        self.article = Article.objects.create(
            title='Sample Article',
            content='This is a test article.',
            author=self.user,
            category=self.category
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Article')

    def test_article_detail_view(self):
        response = self.client.get(reverse('article_detail', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test article.')

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'Testpass123',
            'password2': 'Testpass123'
        })
        self.assertEqual(response.status_code, 302)  # redirect after registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_article_filter_by_category(self):
        response = self.client.get(reverse('home'), {'category': str(self.category.id)})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample Article')

    def test_login(self):
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login)
