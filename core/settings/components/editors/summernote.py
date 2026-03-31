SUMMERNOTE_CONFIG = {
    "summernote": {
        "width": "100%",  # Ширина редактора
        "height": "400",  # Высота редактора
        "iframe": True,  # Включает отображение редактора в iframe
        "attachment_upload_to": "media/summernote/",  # Папка для хранения загружаемых файлов
        "codemirror": {
            "mode": "htmlmixed",
            "lineNumbers": "true",
            "theme": "monokai",
        },
        "fontSizes": ["8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30", "32", "36", "48"],
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "italic", "underline", "clear"]],
            ["fontname", ["fontname"]],
            ["fontsize", ["fontsize"]],
            ["color", ["color"]],
            ["para", ["ul", "ol", "paragraph"]],
            ["alignment", ["ul", "ol", "paragraph", "alignleft", "aligncenter", "alignright", "justify"]],
            ["height", ["height"]],
            ["insert", ["link", "picture", "video"]],
            ["view", ["fullscreen", "codeview", "help"]],
        ],
        "fontNames": [
            "Arial",
            "Arial Black",
            "Comic Sans MS",
            "Courier New",
            "Good Vibes Pro",
            "Helvetica",
            "Impact",
            "Roboto",
            "Times New Roman",
            "Verdana",
        ],
        # Игнорируем проверку на стандартные шрифты
        "fontNamesIgnoreCheck": ["Good Vibes Pro", "Roboto"],
    }
}
