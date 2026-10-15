from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from budgettracker.transactions.models import Transaction, Category
from django.db.models import Sum, Q

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
    transactions = Transaction.objects.select_related("category")

    context = {
        "title": "Мої транзакції",
        "transactions": transactions,
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
    income_transactions = [item for item in TRANSACTIONS if item.transaction_type == 'income']
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

def transactions_by_category(request, category):
    category_obj = get_object_or_404(Category, name=category)
    transactions = Transaction.objects.filter(category=category_obj)

    context = {
        "title": f"Транзакції: {category_obj.name}",
        "category": category_obj,
        "transactions": transactions,
    }
    return render(request, "transactions/transactions_by_category.html", context)

def monthly_report(request, month):
    if not 1 <= month <= 12:
        return render(
            request,
            "transactions/monthly_report.html",
            {
                "title": "Невірний місяць",
                "error": "Номер місяця має бути від 1 до 12.",
            },
            status=400,
        )

    transactions = Transaction.objects.filter(created_at__month=month)

    total_income = transactions.filter(
        transaction_type="income"
    ).aggregate(total=Sum("amount"))["total"] or 0

    total_expense = transactions.filter(
        transaction_type="expense"
    ).aggregate(total=Sum("amount"))["total"] or 0

    balance = total_income - total_expense

    context = {
        "title": f"Звіт за місяць {month}",
        "month": month,
        "transactions": transactions,
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
    }
    return render(
        request,
        "transactions/monthly_report.html",
        context
    )