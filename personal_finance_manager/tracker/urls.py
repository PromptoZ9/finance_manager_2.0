from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('edit/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('transaction/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('export/', views.export_transactions, name='export_transactions'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
]