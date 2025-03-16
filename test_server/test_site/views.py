from django.shortcuts import render
from django.templatetags.static import static

def index_page(request):
    context = {
        "page_name": "Тренеры",
        "goods": [
            {"label": "Ольга", "img": static("images/1.png")},
            {"label": "Иван", "img": static("images/ivan.jpg")},
            {"label": "Елена", "img": static("images/elena.jpg")},
            {"label": "Евгений", "img": static("images/evgeniy.png")}
        ]
    }
    return render(request, 'index.html', context)
