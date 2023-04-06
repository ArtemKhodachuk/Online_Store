from django.urls import path

from . import views

#Testing urls
app_name = 'product_cart'
urlpatterns = [
    path('user/int:pk/cart', views.UserCartView.as_view()), # Return the cart of the user
]