from django.urls import path, re_path, register_converter
from market import views, converters

register_converter(converters.FourDigitYearConverter,"year4")

urlpatterns = [
 path('', views.index, name = 'home'),
 path('cats/<int:cat_id>/', views.show_category, name = 'cat_id'),
 # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
 path('archive/<year4:year>/', views.archive, name = 'archive'),
 path('', views.index, name='home'),
 path('about/', views.about, name='about'),
 path('add/', views.add_product, name='add_product'),
 path('contact/', views.contact, name='contact'),
 path('login/', views.login, name='login'),
 path('product/<slug:product_slug>/', views.show_product, name='product'),
]
