"""
Настройки Django Insights для Django

Компонент отвечает за:
1. Сбор и хранение метрик из приложений Django
2. Настройку дашборда для визуализации метрик
3. Конфигурацию базы данных SQLite для хранения инсайтов
4. Настройку внешнего вида и поведения графиков
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------

# Название приложения для отображения в дашборде
INSIGHTS_APP_NAME = "Мое приложение"

# Качество изображений графиков (DPI)
INSIGHTS_CHART_DPI = 180

# Тема дашборда (light или dark)
INSIGHTS_THEME = "dark"

# ------------------ НАСТРОЙКИ ЦВЕТОВ -------------------

# Основной цвет для светлой темы
INSIGHTS_CHART_LIGHT_PRIMARY_COLOR = "#2563EB"

# Основной цвет для темной темы
INSIGHTS_CHART_DARK_PRIMARY_COLOR = "#BFDBFE"

# ------------------ НАСТРОЙКИ БАЗЫ ДАННЫХ -------------------

# База данных insights уже должна быть определена в DATABASES в settings.py:
# DATABASES = {
#     ...
#     "insights": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db/insights.db",
#     },
# }

# Роутер базы данных insights уже должен быть определен в settings.py:
# DATABASE_ROUTERS = ['django_insights.database.Router']

# ------------------ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ -------------------

"""
# Пример файла insights.py в вашем приложении:

from django_insights.metrics import metrics
from myapp.models import User, Post

# Метка для группировки метрик этого приложения
label = "Метрики пользователей"

# Пример счетчика
@metrics.counter(question="Сколько активных пользователей?")


def count_active_users() -> int:
    return User.objects.filter(is_active=True).count()

# Пример счетчика со средним значением
@metrics.gauge(question="Среднее количество постов на пользователя")


def avg_posts_per_user() -> float:
    total_users = User.objects.count()

    if total_users == 0:
        return 0
    return Post.objects.count() / total_users

# Пример временного ряда
from django.db.models import Count
from django.db.models.functions import TruncMonth

@metrics.timeseries(
    question="Количество регистраций по месяцам",
    desc="Сколько пользователей регистрируется каждый месяц",
    xlabel="Месяц",
    xformat='%m-%Y',
    ylabel="Количество пользователей",
)


def registrations_per_month():
    return (
        User.objects.all()
        .annotate(month=TruncMonth('date_joined'))
        .values('month')
        .filter(month__isnull=False)
        .annotate(total=Count('id'))
        .values_list('month', 'total')
        .order_by('month')
    )

# Пример точечной диаграммы
@metrics.scatterplot(
    question="Активность пользователей по возрасту",
    xlabel="Возраст",
    ylabel="Количество действий",
)


def user_activity_by_age():
    return (
        User.objects.annotate(actions_count=Count('actions'))
        .values_list('actions_count', 'age', 'username')
    )

# Пример столбчатой диаграммы
from django.db.models import Case, When, Value

@metrics.barchart(
    question="Посты по типам контента",
    xlabel="Тип контента",
    ylabel="Количество постов",
)


def posts_by_content_type():
    return (
        Post.objects.values('content_type')
        .annotate(
            count=Count('id'),
            type_name=Case(
                When(content_type=1, then=Value('Текст')),
                When(content_type=2, then=Value('Изображение')),
                When(content_type=3, then=Value('Видео')),
            ),
        )
        .values_list('count', 'content_type', 'type_name')
    )
"""
