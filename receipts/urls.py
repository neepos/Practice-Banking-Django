from django.urls import path
from receipts.views import get_receipt

urlpatterns = [
    path("", get_receipt, name="get_receipt_home"),
]
