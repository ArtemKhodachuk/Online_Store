from django.urls import path

from . import views


#Testing urls
app_name = 'order'
urlpatterns = [
    path('order/int:pk', views.OrderView.as_view()), # look at the product list
    path('user/order/int:pk', views.UserOrderView.as_view)
]