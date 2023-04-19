from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


@login_required
def get_receipt(request):
    item = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts": item,
    }
    return render(request, "receipts/home.html", context)


# Create your views here.
