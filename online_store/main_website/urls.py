from django.urls import path

from . import views

#Testing urls
app_name = 'main_website'
urlpatterns = [
    path('user/', views.UserView.as_view()), # Look at the user list
    path('user/<int:pk>/', views.UsercartView.as_view()), # Look at the user cart
    path('product/', views.ProductView.as_view()), # look at the product list
]