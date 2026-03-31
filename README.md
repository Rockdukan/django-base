## Структура проекта:
```bash
django-base/
├── core/                          # Ядро проекта
│   ├── settings/                  # Модульные настройки
│   │   ├── base.py                # Базовые настройки
│   │   ├── development.py         # Настройки для разработки
│   │   ├── production.py          # Продакшн настройки
│   │   └── components/            # Компоненты настроек
│   │       ├── database/          # Настройки БД
│   │       ├── security/          # Безопасность
│   │       ├── performance/       # Производительность
│   │       ├── authentication/    # Аутентификация
│   │       └── ...                # Другие компоненты
│   ├── models/                    # Базовые модели и миксины
│   │   └── mixins/                # Миксины для моделей
│   ├── middlewares/               # Кастомные middleware
│   ├── utils/                     # Утилиты
│   └── dashboard.py               # Настройка дашборда админки
├── apps/                          # Приложения проекта
└── manage.py
```

## Установка и запуск:
#### Быстрый старт (на основе uv):
```bash
cp env_example .env  # Настройте переменные окружения
make install          # Установка зависимостей
make migrate          # Применение миграций
make superuser        # Создание суперпользователя
make run              # Запуск сервера разработки
```

#### Makefile команды:
```bash
make install          # Установка зависимостей
make migrate          # Применение миграций
make makemigrations   # Создание миграций
make superuser        # Создание суперпользователя
make run              # Запуск development сервера
make shell            # Django shell
make test             # Запуск тестов
make collectstatic    # Сборка статических файлов
make celery           # Запуск Celery worker
make beat             # Запуск Celery beat
make requirements     # Обновление requirements.txt
```

#### Ручная установка:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


## Доступ к приложению:
Админ-панель: http://127.0.0.1:8000/cabinet/

## Middleware и Mixins: что и зачем

### Middleware

- `core.middlewares.healthcheck.HealthcheckMiddleware`
  - **Для чего:** быстрые liveness/readiness пробы для инфраструктуры.
  - **Как работает:** перехватывает `GET /healthz` и `GET /readyz`, возвращает JSON и не гоняет остальной стек.
  - **Как пользоваться:** готово из коробки; пути можно переопределить через `HEALTHCHECK_PATH` и `READINESS_PATH` в settings.

- `core.middlewares.request_id.RequestIdMiddleware`
  - **Для чего:** корреляция логов и трассировка запросов.
  - **Как работает:** берет `X-Request-ID` из входящего запроса (если есть) или генерирует новый, кладет в `request.request_id` и в заголовок ответа.
  - **Как пользоваться:** включен в `MIDDLEWARE`; в логах используйте `request.request_id`.

- `core.middlewares.request_log_middleware.RequestLogMiddleware`
  - **Для чего:** диагностическое логирование запросов/ответов.
  - **Как работает:** пишет метод, путь, статус, время, IP и `request_id`; умеет маскировать чувствительные поля (`authorization`, `token`, `password` и т.д.).
  - **Как пользоваться:** настройте:
    - `REQUEST_LOG_BODY=True|False`
    - `REQUEST_LOG_HEADERS=True|False`
    - `REQUEST_LOG_RESPONSE=True|False`
    - `REQUEST_LOG_MAX_BODY_SIZE=10240`
    - `REQUEST_LOG_EXCLUDE_PATHS=[...]`

- `RemoveServerHeader/RemoveVia/RemoveXPoweredBy`
  - **Статус:** удалены из проекта.
  - **Почему:** эти заголовки корректнее и надежнее контролировать на reverse-proxy (Nginx/Traefik), а не в Django.

### Mixins и QuerySet

- `SoftDeleteMixin` + `SoftDeleteQuerySet`
  - **Для чего:** безопасное удаление без потери данных.
  - **Как работает:**
    - `objects` -> только живые записи;
    - `all_objects` -> все записи;
    - `deleted_objects` -> только удаленные;
    - `delete()` -> мягкое удаление;
    - `hard_delete()` -> физическое удаление;
    - `restore()` -> восстановление.
  - **Как пользоваться:**
    - унаследовать модель от `SoftDeleteMixin`;
    - для массовых операций: `Model.all_objects.filter(...).soft_delete()` / `.restore()`.

- `AuditMixin`
  - **Для чего:** базовый аудит (`created_at`, `updated_at`, `created_by`, `updated_by`).
  - **Как работает:** при `save(actor=user)` автоматически проставляет пользователя в audit-поля.
  - **Как пользоваться:** `instance.save(actor=request.user)`.

- `OwnershipMixin` / `TenantMixin`
  - **Для чего:** контроль доступа и мультиарендность.
  - **Как работает:** `OwnershipMixin` добавляет поле `owner`, `TenantMixin` — `tenant_id`.
  - **Как пользоваться:** в запросах фильтровать через QuerySet миксины: `.for_owner(user)`, `.for_tenant(tenant_id)`.

- `PublishWindowMixin`
  - **Для чего:** ограничение видимости записи по времени.
  - **Как работает:** поля `published_from`/`published_to` и метод `is_in_publication_window()`.
  - **Как пользоваться:** проверка на объекте или фильтрация через `VisibilityQuerySet.in_publication_window()`.

- `VisibilityQuerySet`
  - **Для чего:** единые фильтры видимости.
  - **Методы:** `active()`, `inactive()`, `published()`, `in_publication_window()`, `for_owner()`, `for_tenant()`.
  - **Как подключить к модели:**
    - `objects = models.Manager.from_queryset(VisibilityQuerySet)()`
    - затем использовать цепочки: `Model.objects.active().published().in_publication_window()`.

### Пример модели

```python
from django.db import models

from core.models.mixins import AuditMixin, OwnershipMixin, PublishWindowMixin, SoftDeleteMixin, TenantMixin
from core.models.querysets import ContentManager


class Article(SoftDeleteMixin, AuditMixin, OwnershipMixin, TenantMixin, PublishWindowMixin):
    title = models.CharField(max_length=255)
    objects = ContentManager()

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
```
