from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения market.")


def exp(request, material):
    return HttpResponse(f"Вы выбрали материал: {material}")
