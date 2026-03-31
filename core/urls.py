from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import core.admin  # noqa: F401, E402

urlpatterns = [
    # ----------------- CABINET -------------------
    path("cabinet/logs/", include("log_viewer.urls")),
    path("cabinet/", admin.site.urls),
    # -------------- PROJECT URL"s ----------------
    path("", include("apps.index.urls")),
]


# --------------------------- SWAGGER (API docs) ------------------------
try:
    from core.settings.components.api.swagger import swagger_urlpatterns

    urlpatterns += swagger_urlpatterns
except Exception:
    pass

# --------------------------- URLS EXTENDED ----------------------------
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
