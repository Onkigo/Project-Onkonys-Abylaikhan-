Описание

"Project Onkonys Abylaikhan" — это Django-веб-приложение для публикации статей, редактирования профиля автора, комментариев к статьям и фильтрации содержимого.

Функционал

Главная страница сайта с поиском и фильтрацией статей

Авторизация, регистрация и выход из аккаунта

Личный кабинет автора:

Отображение аватара, имени, соц.сетей, био

Редактирование профиля (avatar, bio, social links)

Отображение собственных статей c возможностью редактирования

Страница статьи с выводом профиля автора статьи

Возможность добавить комментарии

Структура проекта

articles/

models.py — Модели: Article, Comment, Profile, Category

forms.py — Формы для регистрации, статей, комментариев, редактирования профиля

views.py — Вюхи для сайта

urls.py — Роуты

templates/ — шаблоны HTML (home.html, article_detail.html, edit_profile.html, author_profile.html)

static/ — статические файлы (CSS, JS, изображения)

config/

settings.py — Настройки Django

urls.py — общий URLconf


Установка

1)Склонируйте репозиторий:
git clone https://github.com/Onkigo/Project-Onkonys-Abylaikhan-.git
cd Project-Onkonys-Abylaikhan-

2)Активируйте виртуальное окружение (по необходимости) и установите зависимости:

pip install -r requirements.txt

3)Создайте superuser:
Создайте базу и примените миграции:
python manage.py makemigrations
python manage.py migrate

4)Создайте superuser:
python manage.py createsuperuser

5)Запустите сервер:
python manage.py runserver
6)Зайдите на http://127.0.0.1:8000/

Технологии

Django 5.1

HTML5, CSS3, Bootstrap5

SQLite3


Created by Onkigo.