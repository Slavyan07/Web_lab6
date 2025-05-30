from django.http import  HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить товар", 'url_name': 'add_product'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]

products = [
    {
        'id': 1,
        'title': 'Стол из дуба',
        'description': """
Прочный и надёжный обеденный стол, выполненный из натурального дуба.  
Идеально подходит для кухни или столовой в классическом и современном стиле.  
Каждая деталь тщательно обработана вручную для сохранения текстуры древесины.  
Покрытие на основе натурального масла защищает поверхность от влаги и повреждений.  
Этот стол станет центром внимания в любом интерьере и прослужит десятилетия.""",
        'is_published': True
    },
    {'id': 2, 'title': 'Шкаф из сосны', 'description': 'Экологично', 'is_published': False},
    {'id': 3, 'title': 'Кровать из ясеня', 'description': 'Крепкая конструкция', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Столы'},
    {'id': 2, 'name': 'Шкафы'},
    {'id': 3, 'name': 'Кровати'},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'products': products,
        'cat_selected': 0,
    }
    return render(request, 'woodmarket/index.html', data)


def show_product(request, product_id):
    product = next((p for p in products if p['id'] == product_id), None)

    if product is None:
        raise Http404("Товар не найден")

    context = {
        'title': product['title'],
        'menu': menu,
        'product': product,
    }
    return render(request, 'woodmarket/index.html', context=context)


def about(request):
    return render(request, 'woodmarket/about.html', {'title': 'О сайте', 'menu': menu})

def add_product(request):
    return HttpResponse("Добавить товар")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Войти")

def categories(request):
 return HttpResponse("<h1>Статьи по категориям</h1>")
def categories_by_slug(request, cat_slug):
 if request.GET:
     print(request.GET)
 return HttpResponse("<h1>Статьи по категориям</h1>")

def page_not_found(request, exception):
 return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def archive(request, year):
 if year > 2025:
     return redirect('home', permanent=True)
 return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")