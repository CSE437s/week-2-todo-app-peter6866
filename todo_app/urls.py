from django.urls import path
from .views import TodoListListView, ItemListView, ListCreate, ItemCreate, ItemUpdate

urlpatterns = [
    path("", TodoListListView.as_view(), name="index"),
    path("list/<int:list_id>/", ItemListView.as_view(), name="list"),
    path("list/add/", ListCreate.as_view(), name="list-add"),
    path("list/<int:list_id>/item/add/", ItemCreate.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/", ItemUpdate.as_view(), name="item-update"),
]
