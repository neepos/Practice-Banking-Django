from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm, ExpenseCategoryForm, AccountForm
from django.contrib.auth.decorators import login_required


@login_required
def get_receipt(request):
    item = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": item,
    }
    return render(request, "receipts/home.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

    context = {
        "form": form,
    }

    return render(request, "receipts/create.html", context)


@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "receipts/categories.html", context)


@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts,
    }
    return render(request, "receipts/accounts.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm()

    context = {
        "form": form,
    }

    return render(request, "receipts/categories/create.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("account_list")
    else:
        form = AccountForm()

    context = {
        "form": form,
    }

    return render(request, "receipts/accounts/create.html", context)
