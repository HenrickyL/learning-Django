from django.urls import path
from . import views
urlpatterns = [
    path("", views.get_products, name="products"),
    path("", views.insert_product, name="insert")
    
]