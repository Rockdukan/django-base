"""
Настройки django-extensions

Компонент отвечает за:
1. Расширенные команды Django (shell_plus, graph_models и др.)
2. Настройки shell и генерации схемы моделей
"""

# ------------------ НАСТРОЙКИ SHELL -------------------

# Использовать IPython или bpython вместо стандартного shell
SHELL_PLUS = "ipython"

# Автоматически импортировать все модели при запуске shell_plus
SHELL_PLUS_IMPORTS = [
    ("django.contrib.auth.models", "User"),
]

# ------------------ НАСТРОЙКИ ГЕНЕРАЦИИ UML -------------------

# Путь к Graphviz для генерации схем
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}
