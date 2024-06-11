from django.urls import path
from .views import getProducts,add_product,edit_product,delete_product


urlpatterns = [
  path('getProducts/', getProducts, name="getProducts"),
  path('add_product/', add_product, name="add_product"),
  path('edit_product/', edit_product, name="edit_product"),
  path('delete_product/', delete_product, name="delete_product")
]