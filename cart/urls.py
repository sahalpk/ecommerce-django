from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name="add_cart"),
    path('remove/<int:product_id>/', views.remove, name='remove'),
    path('delete/<int:product_id>/', views.delete, name='delete'),
]
