from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_cart, name='add_cart'),
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<item_id>/', views.remove_cart, name='remove_cart'),
    path('add_coupon/', views.add_coupon, name='add_coupon'),

]
