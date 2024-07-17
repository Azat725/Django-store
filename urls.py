from django.contrib import admin
from django.urls import path
from . import views

from products.views import index, products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
]