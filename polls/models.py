from django.db import models

# Create your models here.
from django.db import models


class ToDoList(models.Model):
    ToDoListText = models.CharField(max_length=200)
    ToDoListDeadLine = models.DateTimeField()
    ToDoListCheckedOut = models.BooleanField(default=False)

    def __str__(self):
        return self.ToDoListText

    def deadline(self):
        return self.ToDoListDeadLine

    def checked_out(self):
        return self.ToDoListCheckedOut
