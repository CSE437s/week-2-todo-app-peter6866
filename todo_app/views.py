from typing import Any
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TodoList, TodoItem


class TodoListListView(ListView):
    model = TodoList
    template_name = "todo_app/index.html"
    

class ItemListView(ListView):
    model = TodoItem
    template_name = "todo_app/todo_list.html"
    
    def get_queryset(self):
        return TodoItem.objects.filter(todo_list__id=self.kwargs["list_id"])
    
    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = TodoList.objects.get(id=self.kwargs["list_id"])
        return context


class ListCreate(CreateView):
    model = TodoList
    fields = ["title"]
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Create a new Todo List here"
        return context
    
    
class ItemCreate(CreateView):
    model = TodoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = TodoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = TodoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item here"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(UpdateView):
    model = TodoItem
    fields = [
        "todo_list",
        "name",
        "description",
        "due",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["name"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])