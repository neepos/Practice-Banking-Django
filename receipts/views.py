from django.shortcuts import render
from receipts.models import Receipt


def get_receipt(request):
    item = Receipt.objects.all()
    context = {
        "receipts": item,
    }
    return render(request, "receipts/home.html", context)


# Create your views here.
