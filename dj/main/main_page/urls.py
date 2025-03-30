from django.urls import path

from .views import *

urlpatterns = [
    path("", main_page, name="main_page"),
    path("add_cashflow/", add_cashflow, name="add_cashflow"),
    path("get_subcategories/", get_subcategories, name="get_subcategories"),
    path("edit_cashflow/<int:record_id>/", edit_cashflow, name="edit_cashflow"),
    path("delete_cashflow/<int:record_id>/", delete_cashflow, name="delete_cashflow"),
    path("add_status/", add_status, name="add_status"),
    path("add_type/", add_type, name="add_type"),
    path("add_category/", add_category, name="add_category"),
    path("add_subcategory/", add_subcategory, name="add_subcategory"),
]