from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('shop/', views.product_shop, name='product_shop'),
    path('<str:slug>/', views.product_detail, name='product_detail')

]