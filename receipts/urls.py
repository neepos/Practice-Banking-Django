from django.urls import path
from receipts.views import get_receipt, create_receipt

urlpatterns = [
    path("", get_receipt, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]
