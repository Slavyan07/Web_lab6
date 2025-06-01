from django.http import  HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
# Create your views here.
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить товар", 'url_name': 'add_product'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]

Product.objects.filter(is_published=1)

cats_db = [
    {'id': 1, 'name': 'Столы'},
    {'id': 2, 'name': 'Шкафы'},
    {'id': 3, 'name': 'Кровати'},
]

def index(request):
    products = Product.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'products': products,
        'cat_selected': 0,
    }
    return render(request, 'woodmarket/index.html', data)
def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'woodmarket/product.html', {
        'title': product.title,
        'menu': menu,
        'product': product,
    })

def about(request):
    return render(request, 'woodmarket/about.html', {'title': 'О сайте', 'menu': menu})

def add_product(request):
    return HttpResponse("Добавить товар")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Войти")

def show_category(request, cat_id):
    # Получаем название категории по id
    cat = next((c for c in cats_db if c['id'] == cat_id), None)
    if cat is None:
        raise Http404("Категория не найдена")

    # Фильтруем опубликованные товары по категории
    filtered = [p for p in products if p['cat_id'] == cat_id and p['is_published']]

    # Получаем описание первого продукта (если есть)
    first_description = filtered[0]['description'] if filtered else 'Нет доступных товаров в этой категории.'

    data = {
        'title': f"Товары по категории {cat['name']}",
        'menu': menu,
        'products': filtered,
        'cat_selected': cat_id,
        'first_description': first_description,  # передаём в шаблон
    }
    return render(request, 'woodmarket/index.html', data)

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
