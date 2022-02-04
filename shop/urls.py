from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    # path('a/', views.home, name="home"),
    path('', views.allProdCat, name="allProdCat"),
    path('<slug:c_slug>/', views.allProdCat, name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',
         views.proDetail, name="prodCatDetail")
]
