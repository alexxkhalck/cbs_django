from django.urls import path
from budgettracker.transactions import views

urlpatterns = [
    path("transactions/", views.transactions_list, name="transactions_list"),
    path("transactions/category/<str:category>/", views.transactions_by_category, name="transactions-by-category"),
    path("reports/<int:month>/", views.monthly_report, name="monthly_report"),
    path("budgets/", views.budgets_list, name="budgets_list"),
    path("income/", views.income_list, name="income_list"),
    path("expenses/", views.expense_list, name="expense_list"),]