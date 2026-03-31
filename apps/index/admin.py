from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import Index


@admin.register(Index)
class IndexAdmin(SingletonModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": ("content",),
            },
        ),
        (
            "SEO-настройки",
            {
                "fields": ("meta_title", "meta_description", "meta_keywords"),
                "classes": ("collapse",),
            },
        ),
    )
