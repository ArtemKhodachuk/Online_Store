from django.urls import path

from . import views


#Testing urls
app_name = 'product_cart'
urlpatterns = [
    path('user/int:pk/cart', views.UserCartView.as_view()), # Return the cart of the user
    path('cart/int:cart_id/cartitem', views.CartView.as_view()),
    path('cart/int:cart_id/cartitem/int:pk', views.InCartProductView.as_view()) 
]