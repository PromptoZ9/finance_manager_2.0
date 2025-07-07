from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Transaction
from .forms import TransactionForm, TransactionFilterForm
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import RegisterForm
import csv
# Create your views here.


def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    form = TransactionFilterForm(request.GET)

    if form.is_valid():
        t_type = form.cleaned_data.get('transaction_type')
        start = form.cleaned_data.get('start_date')
        end = form.cleaned_data.get('end_date')
        search = form.cleaned_data.get('search')

        if t_type:
            transactions = transactions.filter(transaction_type=t_type)
        if start:
            transactions = transactions.filter(date__gte=start)
        if end:
            transactions = transactions.filter(date__lte=end)
        if search:
            transactions = transactions.filter(title__icontains=search)

    total_income = Transaction.objects.filter(category__iexact='Income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(category__iexact='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense
    
    return render(request, 'transaction_list.html', {
        'transactions': transactions,
        'form': form,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    })

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction added successfully.')
            return redirect ('transaction_list') 
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.delete()
    messages.success(request, 'Transaction deleted successfully.')
    return redirect('transaction_list')

def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Transaction updated successfully.')
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'edit_transaction.html', {'form': form})

def transaction_detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    return render(request, 'transaction_detail.html', {'transaction': transaction})

def export_transactions(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'
    writer = csv.writer(response)
    writer.writerow(['Date', 'Title', 'Category', 'Amount'])
    transactions = Transaction.objects.all().order_by('-date')
    for transaction in transactions:
        writer.writerow([transaction.date, transaction.title, transaction.category, transaction.amount])
    return response

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('transaction_list')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})