from django.urls import path

from . import views

#Testing urls
app_name = 'transaction_info'
urlpatterns = [
    path('transactions/', views.TransactionView.as_view()), # look at the transaction list
]