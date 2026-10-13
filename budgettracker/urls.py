"""
URL configuration for budgettracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from budgettracker.transactions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('transactions/', views.transactions_list, name='transactions_list'),
    path('transactions/<int:transaction_id>/', views.transaction_detail, name='transaction_detail'),
    path('budgets/', views.budgets_list, name='budgets_list'),
    path('income/', views.income_list, name='income_list'),
    path('expenses/', views.expense_list, name='expense_list'),
]
