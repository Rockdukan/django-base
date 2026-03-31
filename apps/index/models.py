from django.db import models
from solo.models import SingletonModel

from core.models.mixins import MetaMixin


class Index(SingletonModel, MetaMixin):
    """Модель для главной страницы."""

    content = models.TextField("Содержание", blank=True)

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

    def __str__(self):
        return "Настройки главной страницы"
