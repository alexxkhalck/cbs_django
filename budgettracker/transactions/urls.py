from django.urls import path, include
from budgettracker.transactions import views

urlpatterns = [
    path('', views.transactions_list, name='transactions_list'),
    path('<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('category/<str:category>/', views.transactions_by_category, name='transactions-by-category'),
]