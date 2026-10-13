from django.shortcuts import render
from django.http import HttpResponse

TRANSACTIONS = [
    {"id": 1, "amount": 10000, "type": "income", "category": "Salary", "date": "2026-10-01", "description": "Monthly salary"},
    {"id": 2, "amount": 500, "type": "expense", "category": "Groceries", "date": "2026-10-02", "description": "Weekly groceries"},
    {"id": 3, "amount": 1000, "type": "expense", "category": "Transport", "date": "2026-10-03", "description": "Bus fare"},
    {"id": 4, "amount": 20000, "type": "income", "category": "Freelance", "date": "2026-10-04", "description": "Freelance project payment"},
    {"id": 5, "amount": 1500, "type": "expense", "category": "Food", "date": "2026-10-05", "description": "Grocery products"},
]

BUDGETS = [
    {"category": "Groceries", "monthly_limit": 1500},
    {"category": "Transport", "monthly_limit": 2000},
    {"category": "Food", "monthly_limit": 3000},
]

def home(request):
    """Головна"""
    total_income = sum(item["amount"] for item in TRANSACTIONS if item["type"] == 'income')
    total_expense = sum(item["amount"] for item in TRANSACTIONS if item["type"] == 'expense')
    balance = total_income - total_expense

    context = {
        "title": "Expense Tracker",
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
    }
    return render(request, 'transactions/home.html', context)

def transactions_list(request):
    """Список всіх транзакцій"""
    context = {
        "title": "Мої транзакції",
        "transactions": TRANSACTIONS,
    }
    return render(request, "transactions/transactions_list.html", context)

def transaction_detail(request, transaction_id):
    """Деталі транзакції"""
    transaction = next((item for item in TRANSACTIONS if item["id"] == transaction_id), None)
    if transaction is None:
        return HttpResponse("Транзакція не знайдена", status=404)

    context = {
        "title": f"Деталі транзакції {transaction_id}",
        "transaction": transaction,
    }
    return render(request, "transactions/transaction_detail.html", context)

def budgets_list(request):
    """Список бюджетів"""
    context = {
        "title": "Бюджети",
        "budgets": BUDGETS,
    }
    return render(request, "transactions/budgets_list.html", context)

def income_list(request):
    """Тільки доходи"""
    income_transactions = [item for item in TRANSACTIONS if item.type == 'income']
    total = sum(item.amount for item in income_transactions)
    context = {
        "title": "Доходи",
        "transactions": income_transactions,
        "total": total,
    }
    return render(request, "transactions/income_list.html", context)

def expense_list(request):
    """Тільки витрати"""
    expense_transactions = [item for item in TRANSACTIONS if item.type == 'expense']
    total = sum(item.amount for item in expense_transactions)
    context = {
        "title": "Витрати",
        "transactions": expense_transactions,
        "total": total,
    }
    return render(request, "transactions/expense_list.html", context)