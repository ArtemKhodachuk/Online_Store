from django.urls import path

from . import views

#Testing urls
app_name = 'warehouse_product_info'
urlpatterns = [
    path('product/', views.ProductView.as_view()), # look at the product list
]