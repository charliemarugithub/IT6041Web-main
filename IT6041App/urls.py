from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name="checkout"),
    path('staff/', views.staff, name='staff'),
    path('update_item/', views.updateItem, name='update_item'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('clothing/', views.clothing, name='clothing'),
    path('gardening/', views.gardening, name='gardening'),
    path('accessories/', views.accessories, name='accessories'),
    path('furniture/', views.furniture, name='furniture'),
    path('cleaning/', views.cleaning, name='cleaning'),
    path('allproducts/', views.allproducts, name='allproducts'),
    path('<int:id>', views.product_details, name='product_details'),
    path('coupons/apply/cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
]