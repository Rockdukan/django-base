CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",  # Заголовки
            "|",  # Разделитель
            "bold",
            "italic",
            "underline",
            "strikethrough",  # Форматирование текста
            "fontSize",
            "fontFamily",  # Размер и шрифт
            "fontColor",
            "fontBackgroundColor",  # Цвет текста и фона
            "|",
            "link",
            "bulletedList",
            "numberedList",  # Ссылки и списки
            "|",
            "alignment",  # Выравнивание
            "outdent",
            "indent",  # Отступы
            "|",
            "blockQuote",
            "insertTable",  # Цитаты и таблицы
            "horizontalLine",  # Горизонтальная линия
            "|",
            "imageUpload",
            "mediaEmbed",  # Загрузка изображений и медиа
            "|",
            "undo",
            "redo",  # Отмена и повтор
        ],
        "fontSize": {
            "options": [
                "tiny",
                "small",
                "default",
                "big",
                "huge",
                "12px",
                "14px",
                "16px",
                "18px",
                "20px",
                "24px",
                "30px",
                "36px",
                "48px",
                "60px",
                "72px",
            ],
        },
        "fontFamily": {
            "options": [
                "default",
                "Arial, Helvetica, sans-serif",
                "Courier New, Courier, monospace",
                "Georgia, serif",
                "Lucida Sans Unicode, Lucida Grande, sans-serif",
                "Tahoma, Geneva, sans-serif",
                "Times New Roman, Times, serif",
                "Trebuchet MS, Helvetica, sans-serif",
                "Verdana, Geneva, sans-serif",
            ],
        },
        "alignment": {
            "options": ["left", "center", "right", "justify"],
        },
        "image": {
            "toolbar": [
                "imageStyle:alignLeft",
                "imageStyle:alignCenter",
                "imageStyle:alignRight",
                "|",
                "imageTextAlternative",
            ],
            "styles": [
                "alignLeft",
                "alignCenter",
                "alignRight",
            ],
        },
        "table": {
            "contentToolbar": ["tableColumn", "tableRow", "mergeTableCells"],
        },
        "height": 500,  # Высота редактора
        "width": "100%",  # Ширина редактора
    },
}
