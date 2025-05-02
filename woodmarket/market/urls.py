from django.urls import path
from market import views

urlpatterns = [
 path('', views.index),
 path('cats/', views.categories)
]
