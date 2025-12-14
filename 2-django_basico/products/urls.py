from django.urls import path
from . import views
urlpatterns = [
    path("", views.get_products, name="get_products"),
    path("insert", views.insert_product, name="insert_product"),
    path("", views.post_product, name="post_product")
]