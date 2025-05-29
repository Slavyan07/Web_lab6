from django.http import  HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
 return HttpResponse("Страница приложения market.")

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