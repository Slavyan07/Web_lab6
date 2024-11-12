from django.urls import path

from .views import index, exp


urlpatterns = [
    path('', index),
    path('<str:material>', exp)
]
