"""
Настройки Django Slick Reporting для Django

Компонент отвечает за:
1. Настройку и интеграцию системы отчетов и аналитики
2. Определение параметров для внешнего вида отчетов и графиков
3. Конфигурацию ресурсов JavaScript и CSS
4. Настройку экспорта данных
"""

# ------------------ ОСНОВНЫЕ НАСТРОЙКИ -------------------

# Словарь с основными настройками slick_reporting
SLICK_REPORTING_SETTINGS = {
    # URL для jQuery (False, если вы хотите управлять jQuery самостоятельно)
    "JQUERY_URL": "https://code.jquery.com/jquery-3.7.0.min.js",
    # Дата и время начала по умолчанию для фильтров отчетов
    "DEFAULT_START_DATE_TIME": "2023-01-01 00:00:00",  # 1 января текущего года
    # Дата и время окончания по умолчанию для фильтров отчетов
    "DEFAULT_END_DATE_TIME": "now",  # Текущая дата и время
    # Движок графиков по умолчанию ('highcharts' или 'chartjs')
    "DEFAULT_CHARTS_ENGINE": "chartjs",
    # Настройки медиа-файлов
    "MEDIA": {
        # Если True, переопределяет медиа-файлы, если False - добавляет к существующим
        "override": False,
        # JavaScript-файлы
        "js": (
            "https://cdn.jsdelivr.net/momentjs/latest/moment.min.js",
            "https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js",
            "https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js",
            "https://cdn.datatables.net/1.13.4/js/dataTables.bootstrap5.min.js",
            "slick_reporting/slick_reporting.js",
            "slick_reporting/slick_reporting.report_loader.js",
            "slick_reporting/slick_reporting.datatable.js",
        ),
        # CSS-файлы
        "css": {
            "all": (
                "https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css",
                "https://cdn.datatables.net/1.13.4/css/dataTables.bootstrap5.min.css",
            )
        },
    },
    # Настройки для Font Awesome
    "FONT_AWESOME": {
        "CSS_URL": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        "ICONS": {
            "pie": "fas fa-chart-pie",
            "bar": "fas fa-chart-bar",
            "line": "fas fa-chart-line",
            "area": "fas fa-chart-area",
            "column": "fas fa-chart-column",
        },
    },
    # Настройки для графиков
    "CHARTS": {
        "highcharts": "$.slick_reporting.highcharts.displayChart",
        "chartjs": "$.slick_reporting.chartjs.displayChart",
    },
    # Сообщения, используемые во фронтенде
    "MESSAGES": {
        "total": "Итого",
    },
}

# ------------------ CRISPY FORMS НАСТРОЙКИ -------------------

# Пакет для шаблонов Crispy Forms
CRISPY_TEMPLATE_PACK = "bootstrap4"

# ------------------ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ -------------------
# Пример 1: Простой отчет по группам (продажи по продуктам)

from django.db.models import Sum
from slick_reporting.fields import ComputationField
from slick_reporting.views import Chart, ReportView

from .models import Sales


class ProductSalesReport(ReportView):
    # Основная модель для отчета
    report_model = Sales

    # Поле даты для фильтрации
    date_field = "date"

    # Группировка по продукту
    group_by = "product"

    # Колонки отчета
    columns = [
        "name",  # Имя продукта
        ComputationField.create(method=Sum, field="value", name="value_sum", verbose_name="Сумма продаж"),
        ComputationField.create(method=Sum, field="quantity", name="quantity_sum", verbose_name="Количество продаж"),
    ]

    # Настройки графиков
    chart_settings = [
        Chart(
            "Сумма продаж по продуктам",
            Chart.BAR,
            data_source=["value_sum"],
            title_source=["name"],
        ),
        Chart(
            "Объем продаж по продуктам",
            Chart.PIE,
            data_source=["quantity_sum"],
            title_source=["name"],
        ),
    ]


# Пример 2: Отчет по временным рядам (продажи по месяцам)


class MonthlySalesReport(ReportView):
    report_model = Sales
    date_field = "date"
    group_by = "product"

    # Определение временного ряда (месяцы)
    time_series_pattern = "monthly"

    # Колонки для временного ряда
    time_series_columns = [
        ComputationField.create(method=Sum, field="value", name="value_sum", verbose_name="Сумма продаж"),
    ]

    columns = [
        "name",
        "__time_series__",  # Маркер для вставки колонок временного ряда
        ComputationField.create(method=Sum, field="value", name="total_value", verbose_name="Общая сумма"),
    ]

    chart_settings = [
        Chart(
            "Продажи по месяцам",
            Chart.LINE,
            data_source=["value_sum"],
            title_source=["name"],
        ),
    ]


# Пример 3: Перекрестный отчет (продажи по продуктам и странам)


class ProductCountrySalesReport(ReportView):
    report_model = Sales
    date_field = "date"
    group_by = "product"

    # Поле для перекрестной таблицы
    crosstab_field = "client__country"

    # Колонки для перекрестной таблицы
    crosstab_columns = [
        ComputationField.create(method=Sum, field="value", name="value_sum", verbose_name="Сумма продаж"),
    ]

    # ID для перекрестной таблицы (страны)
    crosstab_ids = ["US", "UK", "DE", "FR"]

    # Включить остаток (прочие страны)
    crosstab_compute_remainder = True

    columns = [
        "name",
        "__crosstab__",  # Маркер для вставки колонок перекрестной таблицы
        ComputationField.create(method=Sum, field="value", name="total_value", verbose_name="Общая сумма"),
    ]

    chart_settings = [
        Chart(
            "Продажи по странам",
            Chart.BAR,
            data_source=["value_sum"],
            title_source=["name"],
        ),
    ]


# Пример 4: Список последних продаж

from slick_reporting.views import ListReportView


class LatestSalesList(ListReportView):
    report_model = Sales
    date_field = "date"

    # Колонки для отображения
    columns = [
        "date",
        "product__name",
        "client__name",
        "quantity",
        "price",
        "value",
    ]

    # Порядок сортировки
    default_order_by = "-date"

    # Ограничение количества записей
    limit_records = 10

    # Фильтры, доступные в форме
    filters = ["product", "client", "date"]


# Пример 5: Создание собственного вычисляемого поля

from django.db.models import Avg, Sum
from slick_reporting.decorators import report_field_register
from slick_reporting.fields import ComputationField


# Регистрация нового вычисляемого поля
@report_field_register
class AverageSalePrice(ComputationField):
    name = "avg_sale_price"
    verbose_name = "Средняя цена продажи"
    calculation_field = "price"
    calculation_method = Avg


# Использование в отчете


class ProductPriceReport(ReportView):
    report_model = Sales
    date_field = "date"
    group_by = "product"

    columns = [
        "name",
        "avg_sale_price",  # Использование по имени
        # Или можно использовать класс напрямую
        # AverageSalePrice,
    ]


# Пример 6: Добавление отчетов на дашборд

# В шаблоне dashboard.html:
DASHBOARD_TEMPLATE_EXAMPLE = """
{% extends "base.html" %}
{% load static slick_reporting_tags %}

{% block content %}
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <h2>Продажи по продуктам</h2>
                {% get_widget_from_url url_name="product-sales-report" %}
            </div>
            <div class="col-md-6">
                <h2>Продажи по месяцам</h2>
                {% get_widget_from_url url_name="monthly-sales-report" %}
            </div>
        </div>
        <div class="row mt-4">
            <div class="col-12">
                <h2>Последние продажи</h2>
                {% get_widget_from_url url_name="latest-sales-list" display_chart=False %}
            </div>
        </div>
    </div>
{% endblock %}

{% block extrajs %}
    {% include "slick_reporting/js_resources.html" %}
    {% get_charts_media "all" %}
{% endblock %}
"""


# Пример 7: Настройка формы фильтрации

from django import forms
from slick_reporting.forms import BaseReportForm


class CustomSalesFilterForm(BaseReportForm, forms.Form):
    start_date = forms.DateField(
        required=False, label="Начальная дата", widget=forms.DateInput(attrs={"type": "date"})
    )
    end_date = forms.DateField(required=False, label="Конечная дата", widget=forms.DateInput(attrs={"type": "date"}))
    price_range = forms.ChoiceField(
        choices=[("all", "Все"), ("low", "До 1000"), ("medium", "1000-5000"), ("high", "Свыше 5000")],
        required=False,
        label="Ценовой диапазон",
    )

    def get_filters(self):
        kw_filters = {}
        q_filters = []

        if self.cleaned_data["price_range"] == "low":
            kw_filters["price__lt"] = 1000
        elif self.cleaned_data["price_range"] == "medium":
            kw_filters["price__gte"] = 1000
            kw_filters["price__lt"] = 5000
        elif self.cleaned_data["price_range"] == "high":
            kw_filters["price__gte"] = 5000

        return q_filters, kw_filters

    def get_start_date(self):
        return self.cleaned_data["start_date"]

    def get_end_date(self):
        return self.cleaned_data["end_date"]


# Использование кастомной формы в отчете


class SalesWithCustomFilterReport(ReportView):
    report_model = Sales
    date_field = "date"
    group_by = "product"
    form_class = CustomSalesFilterForm

    columns = [
        "name",
        ComputationField.create(method=Sum, field="value", name="value_sum", verbose_name="Сумма продаж"),
    ]
