from django.urls import path
from receipts.views import (
    get_receipt,
    create_receipt,
    category_list,
    account_list,
)

urlpatterns = [
    path("", get_receipt, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", category_list, name="category_list"),
    path("accounts/", account_list, name="account_list"),
]
