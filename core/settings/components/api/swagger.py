from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

"""
Настройки Swagger/OpenAPI для Django

Компонент отвечает за:
1. Настройку интерактивной документации API
2. Конфигурацию Swagger и ReDoc
3. Настройки генерации схемы OpenAPI
4. Разрешения для доступа к документации
"""

# ------------------ НАСТРОЙКИ МАРШРУТОВ SWAGGER -------------------

swagger_urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
