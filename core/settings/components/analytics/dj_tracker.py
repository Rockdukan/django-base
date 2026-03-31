"""
Настройки dj-tracker для Django

Компонент отвечает за:
1. Отслеживание и анализ SQL-запросов
2. Выявление проблем производительности баз данных
3. Предоставление рекомендаций по оптимизации запросов
4. Мониторинг N+1 проблем и других неэффективных шаблонов запросов
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------
DJ_TRACKER = {
    # Приложения, запросы которых не отслеживаются
    "APPS_TO_EXCLUDE": {
        # "third-party-app",
        # "test-app",
    },
    # Пути URL, которые не будут отслеживаться
    "IGNORE_PATHS": {
        "/favicon.ico",
        "/static/",
        "/media/",
        "/admin/jsi18n/",
    },
    # Модули, которые будут игнорироваться в трассировках
    "IGNORE_MODULES": {
        "whitenoise/",
        "sentry_sdk/",
        "debug_toolbar/",
    },
    # Интервал сохранения собранных данных (в секундах)
    "COLLECTION_INTERVAL": 5,
    # Пользовательские дескрипторы полей (если используются)
    "FIELD_DESCRIPTORS": {
        # "Creator": "dj_tracker.field_descriptors.EditableFieldDescriptor"
    },
    # Отслеживание доступа к атрибутам модели
    # Отключите, если вы заметите значительное влияние на производительность
    "TRACK_ATTRIBUTES_ACCESSED": True,
}

# ------------------ ПРИМЕРЫ ОПТИМИЗАЦИИ -------------------

"""
# Пример 1: Оптимизация N+1 запросов с использованием select_related

# Неоптимизированный запрос - приводит к N+1 проблеме


def books_list_slow(request):
    books = Book.objects.all()  # Загружает только Book
    return render(request, "books.html", {"books": books})
    # В шаблоне: book.author.name вызовет дополнительный запрос для каждой книги

# Оптимизированный запрос - решает N+1 проблему


def books_list_optimized(request):
    books = Book.objects.select_related("author", "category")  # Загружает Book, Author и Category за один запрос
    return render(request, "books.html", {"books": books})


# Пример 2: Оптимизация с использованием .only() для загрузки только необходимых полей

# Неоптимизированный запрос - загружает все поля, даже если используются не все


def articles_list_slow(request):
    articles = Article.objects.select_related("author")
    return render(request, "articles.html", {"articles": articles})
    # Если в шаблоне используются только article.title и article.author.name,
    # загрузка всех полей (включая большие текстовые поля) - это неэффективно

# Оптимизированный запрос - загружает только необходимые поля


def articles_list_optimized(request):
    articles = Article.objects.select_related("author").only(
        "title", "author__name"
    )
    return render(request, "articles.html", {"articles": articles})


# Пример 3: Использование .values() вместо полных экземпляров модели

# Неоптимизированный запрос - создает полные экземпляры модели


def users_list_slow(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})

# Оптимизированный запрос - возвращает только словари с необходимыми полями


def users_list_optimized(request):
    users = User.objects.values("id", "username", "email")
    return render(request, "users.html", {"users": users})


# Пример 4: Использование .iterator() для больших наборов данных

# Неоптимизированный запрос - загружает все объекты в память


def large_dataset_slow(request):
    items = LargeModel.objects.all()
    return render(request, "items.html", {"items": items})

# Оптимизированный запрос - использует итератор для снижения использования памяти


def large_dataset_optimized(request):
    items = LargeModel.objects.values("id", "name").iterator()
    return render(request, "items.html", {"items": items})


# Пример 5: Использование .exists() вместо .count() или len() для проверки наличия

# Неоптимизированный запрос


def check_exists_slow(request):
    has_comments = Comment.objects.filter(post_id=post_id).count() > 0
    # или
    # has_comments = len(Comment.objects.filter(post_id=post_id)) > 0

# Оптимизированный запрос


def check_exists_optimized(request):
    has_comments = Comment.objects.filter(post_id=post_id).exists()
"""

# ------------------ ОТДЕЛЬНАЯ БАЗА ДАННЫХ ДЛЯ ТРЕКИНГА -------------------

"""
# В settings.py необходимо добавить отдельную базу данных для хранения трекинга:

DATABASES = {
    "default": {
        # ...
    },
    "trackings": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "trackings.db",
    },
}

# Добавить роутер базы данных:
DATABASE_ROUTERS = [
    "dj_tracker.db_router.DjTrackerRouter",
]

# Затем выполнить миграции:
# python manage.py migrate dj_tracker --database=trackings
"""
