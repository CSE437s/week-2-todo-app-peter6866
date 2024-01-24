from enum import unique
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Model for a todo list
class TodoList(models.Model):
    title = models.CharField(max_length=255, unique=True)
    
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    def __str__(self):
        return self.title
    

# Model for a todo item (can be multiple per list)
class TodoItem(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    due = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["due"]
    
    
