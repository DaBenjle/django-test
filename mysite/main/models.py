from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ToDoItem(models.Model):
    text = models.CharField(max_length=400)
    toDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
