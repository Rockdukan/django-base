LUCUS_DASHBOARD = [
    {
        "column": 1,
        "title": "🧩 Содержимое сайта",
        "links": [
            {"label": "Главная", "admin_urlname": "admin:index_index_changelist"},
        ],
    },
    {
        "column": 3,
        "title": "👤 Аккаунты",
        "links": [
            {"label": "Пользователи", "admin_urlname": "admin:auth_user_changelist"},
            {"label": "Группы", "admin_urlname": "admin:auth_group_changelist"},
        ],
    },
    {
        "column": 4,
        "title": "⚙️ Системные настройки",
        "links": [
            {"label": "Перенаправления", "admin_urlname": "admin:redirects_redirect_changelist"},
            {"label": "Сессии", "admin_urlname": "admin:sessions_session_changelist"},
            {"label": "Сайты", "admin_urlname": "admin:sites_site_changelist"},
            {"label": "Константы", "admin_urlname": "admin:constance_config_changelist"},
        ],
    },
    {
        "column": 4,
        "title": "🧾 Логи",
        "links": [
            {"label": "Логи Django admin", "admin_urlname": "admin:admin_logentry_changelist"},
            {"label": "Логи auditlog", "admin_urlname": "admin:auditlog_auditlogentry_changelist"},
            {"label": "Log viewer", "url": "/cabinet/logs/"},
        ],
    },
]
