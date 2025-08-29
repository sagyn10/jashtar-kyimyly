CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading',  # форматирование (h1,h2,h3, p)
                '|',
                'fontFamily', 'fontSize',
                '|',
                'fontColor', 'fontBackgroundColor',
                '|',
                'bold', 'italic', 'underline', 'strikethrough',
                '|',
                'alignment',  # выравнивание
                '|',
                'numberedList', 'bulletedList',
                '|',
                'outdent', 'indent',
                '|',
                'link', 'blockQuote',
                '|',
                'removeFormat', 'sourceEditing'  # для просмотра кода, если включен плагин
            ]
        },
        'fontFamily': {
            'options': [
                'default',
                'Arial, Helvetica, sans-serif',
                'Times New Roman, Times, serif',
                'Verdana, Geneva, sans-serif',
            ],
        },
        'fontSize': {
            'options': ['12px', '14px', '16px', '18px', '24px', '36px'],
        },
        'height': 300,
        'width': '100%',
        'language': 'ru',
        'removePlugins': ['Styles', 'Title'],  # если надо удалить
    }
}
