from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('staff/', views.staff, name="staff"),
    path('update_item/', views.updateItem, name="update_item"),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
]