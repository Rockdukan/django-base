from django.views.generic import TemplateView


class WelcomeView(TemplateView):
    """Приветственная страница шаблона проекта."""

    template_name = "index/index.html"
