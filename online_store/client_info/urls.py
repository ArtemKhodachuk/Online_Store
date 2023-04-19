from django.urls import path

from . import views


#Testing urls
app_name = 'client_info'
urlpatterns = [
    path('user/', views.UserView.as_view()), # Look at the user list
]